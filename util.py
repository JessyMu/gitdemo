import requests
import json
import subprocess
import os
import random
import time
from playwright.sync_api import sync_playwright
from functools import partial
from playwright._impl._errors import TimeoutError

def postData(url, data, headers):
    payload = json.dumps(data)
    response = requests.request("POST", url, headers=headers, data=payload)
    return response

def checkStatus(response):
    if response.status_code == 200:
        # try:
        #     result = response.json()
        #     print("响应成功！结果：", result)
        # except requests.exceptions.JSONDecodeError:
        #     print("响应成功！字符串内容：", response.text)
        return True
    else:
        # print("请求失败，状态码：", response.status_code)
        # print("错误信息：", response.text)
        return False

def writeFile(filepath,content):
    if os.path.exists(filepath):
        with open(filepath, "a") as readme_file:
            readme_file.write(f"Appended {content} at {time.time()}\n")
    else:
        with open(filepath, "w") as readme_file:
            readme_file.write(f"Initial {content} at {time.time()}\n")

def gitCommit(config):
    assert os.path.isdir(config['repo_path']),'Error! [Git提交]: Git路径不存在or非目录!'
    for i in range(config['iterations']):
        try:
            readme_path = f"{config['repo_path']}/readme.md"
            writeFile(readme_path,config['contents'][i] if len(config['contents'])>1 and config['iterations']==len(config['contents']) else config['contents'][0])

            # 添加所有修改
            subprocess.run(["git", "-C", config['repo_path'], "add", "."])
            # 随机选择提交前缀和对应的功能内容
            commit_prefix, commit_content = random.choice(config['commit_msg'])
            # 生成提交消息
            commit_message = f"{commit_prefix}: {commit_content}"
            subprocess.run(["git", "-C", config['repo_path'], "commit", "-m", commit_message])
            # 推送到远程仓库
            subprocess.run(["git", "-C", config['repo_path'], "push"])

            time.sleep(config['sleep_time'])
        except Exception as e:
            print("Error! [Git提交]: 异常!")
            raise e

def doc_edit(user_dir,browser_path,config):
    assert config['contents'],'Error! [文档编辑]: 编辑内容不能为空!'
    try:
        with sync_playwright() as p:
            
            context = p.chromium.launch_persistent_context(
                user_data_dir=user_dir,  # 独立的用户数据目录
                headless=False,
                executable_path=browser_path,  # 关键：使用 Edge 浏览器程序
                args=[
                    "--disable-blink-features=AutomationControlled",
                    "--no-sandbox",
                    "--disable-infobars",
                    "--disable-extensions",
                    "--disable-web-security",
                    "--allow-running-insecure-content",
                ],
            )

            page = context.new_page()
            # 注入防检测脚本（非常重要）
            page.add_init_script("""
                Object.defineProperty(navigator, 'webdriver', {
                    get: () => false,
                });
                window.chrome = {
                    runtime: {},
                    loadTimes: () => {},
                    csi: () => {}
                };
                Object.defineProperty(navigator, 'plugins', {
                    get: () => [1, 2, 3, 4, 5],
                });
                Object.defineProperty(navigator, 'languages', {
                    get: () => ['zh-CN', 'zh', 'en'],
                });
            """)

            # page.goto(web_page)
            # input("Press Enter to start...")

            # 开始循环刷编辑次数
            for i in range(config['iterations']):
                print(f"===>第 {i+1} 次编辑")
                page.goto(config['doc_url'])

                editor = page.locator(config['location_item'])
                
                editor.click()
                editor.press("Control+End")   # 移动到文末
                editor.type(config['contents'][i] if config['iterations']==len(config['contents']) else config['contents'][0])     # 输入一个空格
                page.wait_for_timeout(config['save_time'])  # 等待自动保存
                page.go_back()       # 返回上一页（或关闭标签页）
                time.sleep(config['sleep_time'])        # 避免被检测为机器人

            context.close()
    except TimeoutError as e:
        print('Error! [文档编辑]: 捕获元素超时，url或location input/button错误!')
        raise e
    except Exception as e:
        print('Error! [文档编辑]: 其他异常!')
        raise e


def click_submit(user_dir,browser_path,web_url,config,mode):
    assert config['title'],'Error! 工作项/测试用例标题不能为空'
    try:
        with sync_playwright() as p:
            
            context = p.chromium.launch_persistent_context(
                user_data_dir=user_dir,  # 独立的用户数据目录
                headless=False,
                executable_path=browser_path,  # 关键：使用 Edge 浏览器程序
                args=[
                    "--disable-blink-features=AutomationControlled",
                    "--no-sandbox",
                    "--disable-infobars",
                    "--disable-extensions",
                    "--disable-web-security",
                    "--allow-running-insecure-content",
                ],
            )

            page = context.new_page()
            # 注入防检测脚本（非常重要）
            page.add_init_script("""
                Object.defineProperty(navigator, 'webdriver', {
                    get: () => false,
                });
                window.chrome = {
                    runtime: {},
                    loadTimes: () => {},
                    csi: () => {}
                };
                Object.defineProperty(navigator, 'plugins', {
                    get: () => [1, 2, 3, 4, 5],
                });
                Object.defineProperty(navigator, 'languages', {
                    get: () => ['zh-CN', 'zh', 'en'],
                });
            """)
            page.goto(web_url)
            time.sleep(config['wait_time'])
            # 开始循环刷编辑次数
            for i in range(config['iterations']):
                print(f"===>第 {i+1} 次新增")

                # 定位并输入文本到指定的文本框
                time.sleep(config['sleep_time'])
                page.fill(config['location_input'], config['title'][i] if len(config['title'])==config['iterations'] else config['title'][0])
                time.sleep(config['sleep_time'])
                page.click(config['location_button'])

                page.wait_for_timeout(config['save_time'])  # 等待自动保存
                page.go_back()       # 返回上一页（或关闭标签页）
                time.sleep(config['sleep_time'])        # 避免被检测为机器人
                # page.goto(web_url)
            context.close()
    except TimeoutError as e:
        if mode == 'work':
            print('Error! [工作项]: 捕获元素超时，location input/button错误!')
        elif mode == 'sample':
            print('Error! [测试用例]: 捕获元素超时，当前无测试产品或location input/button错误!')
        raise e
    except Exception as e:
        print(f'Error! 其他异常 from {mode}')
        raise e


requests_list = []
import main
def on_request(request,target_url):
    global captured_request
    if request.method == "POST" and target_url in request.url:
        print("✅ 捕获到目标 POST 请求:")
        print(f"   URL: {request.url}")
        print(f"   Method: {request.method}")
        
        # 获取 headers
        headers = request.headers
        print("📎 Request Headers:")
        for k, v in headers.items():
            print(f"  {k}: {v}")
        
        # 获取请求体
        try:
            post_data = request.post_data
            if post_data:
                print("📝 Request Body:")
                print(post_data.decode('utf-8') if isinstance(post_data, bytes) else post_data)
        except:
            pass
        
        # 保存
        captured_request = {
            "url": request.url,
            "method": request.method,
            "headers": headers,
            "post_data": post_data if 'post_data' in locals() else None
        }
        requests_list.append(captured_request)
def get_post(config):
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
                user_data_dir=config['user_dir'],  # 独立的用户数据目录
                headless=False,
                executable_path=config['browser_path'],  # 关键：使用 Edge 浏览器程序
                args=[
                    "--disable-blink-features=AutomationControlled",
                    "--no-sandbox",
                    "--disable-infobars",
                    "--disable-extensions",
                    "--disable-web-security",
                    "--allow-running-insecure-content",
                ],
            )

        page = context.pages[0]
        page.goto(config['web_page'])  # 替换为你的登录页

        print("📌 请在浏览器中完成登录操作（扫码/输入账号）...")
        # print("监听页面请求中...")

        # 设置监听器
        handler = partial(on_request, target_url=config['web_page'])
        context.on("request", handler)

        input("Success! [登录成功]: 点击任意键继续!")

        # 关闭
        context.close()

        return requests_list
    
def pipe_wrap(config):
    pipe_name = f'job{int(time.time())}'
    config['newPipe']['data']['jobName'] = pipe_name
    res = postData(config['newPipe'])

    if checkStatus(res):
        pipe_id = res.json()['data']['jobId']
        config['runPipe']['url'] += str(pipe_id)
        res = postData(config['runPipe'])
        if not checkStatus(res):
            print(f"Error! [流水线]: 执行流水线请求失败, 状态码: {res.status_code}")
            raise Exception(f"Error! [流水线]: 执行流水线请求失败, 状态码: {res.status_code}")
    else:
        print(f"Error! [流水线]: 新建流水线请求失败, 状态码: {res.status_code}")
        raise Exception(f"Error! [流水线]: 新建流水线请求失败, 状态码: {res.status_code}")

def get_info(url,headers):
    response = requests.request("GET", url, headers=headers, data=None)
    return response

def remove_item_all(lst, value):
    """从列表中删除所有等于 value 的元素"""
    return [item for item in lst if item != value]


def new_gitRepo(user_dir,browser_path,web_url,config,context):
    # assert config['repo_name'],'Error! [新建代码仓库]: 代码仓库名字不能为空'
    try:
        # with sync_playwright() as p:
            
        #     context = p.chromium.launch_persistent_context(
        #         user_data_dir=user_dir,  # 独立的用户数据目录
        #         headless=False,
        #         executable_path=browser_path,  # 关键：使用 Edge 浏览器程序
        #         args=[
        #             "--disable-blink-features=AutomationControlled",
        #             "--no-sandbox",
        #             "--disable-infobars",
        #             "--disable-extensions",
        #             "--disable-web-security",
        #             "--allow-running-insecure-content",
        #         ],
        #     )

            page = context.new_page()
            # 注入防检测脚本（非常重要）
            page.add_init_script("""
                Object.defineProperty(navigator, 'webdriver', {
                    get: () => false,
                });
                window.chrome = {
                    runtime: {},
                    loadTimes: () => {},
                    csi: () => {}
                };
                Object.defineProperty(navigator, 'plugins', {
                    get: () => [1, 2, 3, 4, 5],
                });
                Object.defineProperty(navigator, 'languages', {
                    get: () => ['zh-CN', 'zh', 'en'],
                });
            """)

            page.goto(web_url)

            # 定位并输入文本到指定的文本框
            time.sleep(config['sleep_time'])
            page.click(config['location_new'])
            time.sleep(config['sleep_time'])
            page.click(config['location_empty'])
            time.sleep(config['sleep_time'])
            page.click(config['location_next'])
            time.sleep(config['sleep_time'])
            repoName = f"{config['repo_name']}{int(time.time())}"
            page.fill(config['location_name'], repoName)
            time.sleep(config['sleep_time'])
            page.click(config['location_submit'])

            page.wait_for_timeout(config['save_time'])  # 等待自动保存
            page.go_back()       # 返回上一页（或关闭标签页）
            time.sleep(config['sleep_time'])        # 避免被检测为机器人

            # context.close()
            return repoName
    except TimeoutError as e:
        print('Error! [代码仓库]: 捕获元素超时，当前无创建代码仓库权限!')
        raise e
    except Exception as e:
        print(f'Error! [代码仓库]: 其他异常')
        raise e