from playwright.sync_api import sync_playwright
import json
import time

# 目标 URL（你已知的 POST 接口）
TARGET_URL = "https://www.srdcloud.cn/"

# 存储捕获的请求信息
captured_request = None

def on_request(request):
    global captured_request
    if request.method == "POST" and TARGET_URL in request.url:
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
def get_post(web_page):
    with sync_playwright() as p:
        # 🔥 启动持久化上下文（使用本地用户数据，保留登录状态）
        context = p.chromium.launch_persistent_context(
                    user_data_dir='./edge_user_data',  # 独立的用户数据目录
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

        page = context.pages[0]
        page.goto(web_page)  # 替换为你的登录页

        print("📌 请在浏览器中完成登录操作（扫码/输入账号）...")
        print("监听页面请求中...")

        # 🔔 设置监听器
        context.on("request", on_request)

        # 给你 3 分钟时间登录（可调整）
        input("登录成功点击任意键输出请求...")

        # 关闭
        context.close()

get_post(TARGET_URL)
# 最后可以打印或使用 captured_request
if captured_request:
    print("\n🎉 已成功捕获请求，headers 可用于 requests:")
    print(json.dumps(captured_request["headers"], indent=2, ensure_ascii=False))
else:
    print(f"\n❌ 未捕获到 POST 请求: {TARGET_URL}")
    print("可能原因：URL 不匹配、未触发请求、网络问题")



