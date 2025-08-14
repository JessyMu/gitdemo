import subprocess
import os
import random
import time

# git提交记录
# 定义提交前缀和对应的功能内容
commit_data = [
    ("feat", "新增部分车辆数据获取"),
    ("feat", "新增部分告警数据获取"),
    ("fix", "修改部分车辆数据获取"),
    ("fix", "修改部分告警数据获取"),
    ("fix", "完善部分车辆数据获取"),
    ("fix", "完善部分告警数据获取"),
    ("feat", "新增告警数据接口"),
    ("feat", "新增车辆道闸数据接口")
]

# 进入你的Git仓库目录
# repo_path = "E:/whr/2022.7.5电话亭/代码版本/管理平台/ght-15min-management-backend"
repo_path = "E:/whr/文档/0切块预算材料/2024小卡片/代码仓库/qingpu-vue"

for i in range(100):
    readme_path = f"{repo_path}/readme.md"

    # 如果readme.md文件存在，追加字符串
    if os.path.exists(readme_path):
        with open(readme_path, "a") as readme_file:
            readme_file.write(f"\nAppended text {i + 1}")

    # 如果readme.md文件不存在，创建文件并写入内容
    else:
        with open(readme_path, "w") as readme_file:
            readme_file.write(f"Initial content {i + 1}")

    # 添加所有修改
    subprocess.run(["git", "-C", repo_path, "add", "."])

    # 随机选择提交前缀和对应的功能内容
    commit_prefix, commit_content = random.choice(commit_data)

    # 生成提交消息
    commit_message = f"{commit_prefix}: {commit_content}"

    subprocess.run(["git", "-C", repo_path, "commit", "-m", commit_message])

    # 推送到远程仓库
    subprocess.run(["git", "-C", repo_path, "push"])

    # 等待10秒
    time.sleep(62)
