from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    context = p.chromium.launch_persistent_context(
        user_data_dir="./edge_user_data",  # 独立的用户数据目录
        headless=False,
        executable_path="/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",  # 关键：使用 Edge 浏览器程序
        args=[
            "--disable-blink-features=AutomationControlled",
            "--no-sandbox",
            "--disable-infobars",
            "--disable-extensions",
            "--disable-web-security",
            "--allow-running-insecure-content",
        ],
    )

    # 打开目标页面
    page = context.new_page()
    page.goto("https://www.srdcloud.cn/code/57670/repo")  # 替换为你的目标页面
    input('按键登录完毕')
    import time
    page.click('.code-srd-button.code-srd-button_primary:has-text("新建代码仓库")')
    input('1')
    page.click('div.select-card-main:has-text("创建空白仓库")')
    input('2')
    page.click('[data-test="editBranch"]:has-text("下一步")')
    input('3')
    # 定位并输入文本到指定的文本框
    page.fill('input[data-test="create-repository"].code-el-input__inner', 't2')
    input('4')
    page.click('[data-test="editBranch"]:has-text("确定")')
    
    # 保持浏览器打开以便查看结果
    input("按回车键关闭浏览器...")
    
    # 关闭浏览器上下文
    context.close()