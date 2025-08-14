from playwright.sync_api import sync_playwright
import time

# 文档链接
DOC_URL = "https://docs.srdcloud.cn/docs/NJkbEl9MyKh0OoqR"


with sync_playwright() as p:
    # 指定 Microsoft Edge 的可执行文件路径
    edge_path = "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"
    # Linux 示例: "/usr/bin/microsoft-edge"

    context = p.chromium.launch_persistent_context(
        user_data_dir="./edge_user_data",  # 独立的用户数据目录
        headless=False,
        executable_path=edge_path,  # 关键：使用 Edge 浏览器程序
        args=[
            "--disable-blink-features=AutomationControlled",
            "--no-sandbox",
            "--disable-infobars",
            "--disable-extensions",
            "--disable-web-security",
            "--allow-running-insecure-content",
        ],
    )

    # page = context.pages[0]
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

    page.goto("https://www.srdcloud.cn/")
    input("Press Enter to close...")

    # 开始循环刷编辑次数
    for i in range(100):
        print(f"第 {i+1} 次编辑")
        page.goto(DOC_URL)

        editor = page.locator("div.ql-editor.notranslate")
        
        editor.click()
        editor.press("Control+End")   # 移动到文末
        editor.type("测试")     # 输入一个空格
        page.wait_for_timeout(3000)  # 等待自动保存
        page.go_back()       # 返回上一页（或关闭标签页）
        time.sleep(2)        # 避免被检测为机器人


    context.close()