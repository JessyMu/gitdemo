import time
import requests
import json
# 测试用例

def solve_work_item():
    url = "https://www.srdcloud.cn/api/agilebackend/mission/react_task"
     
    payload = json.dumps({"dialog_id":"3fc894d4-9f87-a097-0a87-678d55f3f872","msg":"1. Background and Requirements\nTo meet the self-service monitoring needs of IDC users, it is necessary to build a self-service large-screen monitoring platform tailored for IDC data center users. The platform will integrate the capabilities of the i-Park SmartLink application to achieve data collection, cleaning, storage, and comprehensive management of scenarios, dashboards, data, users, and roles, providing users with efficient and intuitive large-screen monitoring services.\n\n2. Functional Requirements\nIntegrate the scenario repository capability of the i-Park SmartLink application to provide reference scenarios for common data center monitoring use cases. Support reuse of scenario components to accelerate the realization of users' dashboard requirements.","retry_last_round":False,"previous_work_items":[]})
    # 需要变动 sessionid   userid(后续不变）    x-dup-id  Cookie'
    headers = {
        'Host': 'www.srdcloud.cn',
        'pragma': 'no-cache',
        'projectId': '75945',##
        'sessionid': '1eb23433-b618-4515-ac07-6c809a4465c9',
        'userId': '428801',##
        'x-dup-id': '1755162319-llvop94h',
        'Cookie': '_pk_id.5.136f=389e611a3363ca0d.1754545408.; _pk_id.8.136f=5b71364bf6f7490d.1754547001.; _pk_id.9.136f=71d62570514ea50f.1754553005.; fp=84b4a8b0b8038ed001d1a0154a318f93; _pk_id.3.136f=ab31da71dbd49a90.1755140267.; _pk_id.6.136f=686a64ee4f53aa95.1755150471.; uvId=4b001f62-4530-4338-9c7d-a6be338ed83f; sidebar_status=closed; srdcloud.cn=HttpOnly; _pk_ref..136f=%5B%22%22%2C%22%22%2C1755161584%2C%22https%3A%2F%2Fopen.e.189.cn%2F%22%5D; _pk_ses.9.136f=1; prodtoken=b12ecfb2-643e-45e4-a891-b7f71fd9a8fc; produserId=428801; CTWIMAPPDPGSSOCookie=b12ecfb2-643e-45e4-a891-b7f71fd9a8fc; CTWIMAPPDPGSSOUser=srd18964600668',
        'content-type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

solve_work_item()