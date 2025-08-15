import time
import requests
import json

# 测试用例

def solve_test_commit():
    url = "https://www.srdcloud.cn/api/tsback/casemanager/v1/add-case"
     
    payload = json.dumps({"productId":"32687","name":"123","category":"function","level":"P1","demandId":"-1","descType":"step","demandName":"","groupId":"127935","status":"draft","description":{"preCond":"","steps":"","expects":"","steplist":[]},"annexIds":[],"testPhase":[],"externalId":"","tagIds":[]})
    # 需要变动 sessionid   userid(后续不变）    x-dup-id  Cookie'
    headers = {
        'authority': 'www.srdcloud.cn',
        'pragma': 'no-cache',
        'projectid': '75945',##
        'sessionid': 'fc74fd8d-639b-4941-878f-d3d97efabe03',
        'userid': '428801',##
        'x-dup-id': '1755160340-qazhxmaiy',
        'Cookie': '_pk_id.8.136f=3489c818118ee943.1725241416.; _pk_id.5.136f=1b3e3f31a58e0037.1725241417.; _pk_id.4.136f=0b49a46a7a943210.1725325196.; fp=c94054e345de06e2421e1b1f4942c649; _pk_id.3.136f=923e2f550de8dde0.1734319653.; _pk_ref..136f=%5B%22%22%2C%22%22%2C1747962219%2C%22https%3A%2F%2Fopen.e.189.cn%2F%22%5D; _pk_id.11.136f=c670d85a08784856.1742785487.; prodtoken=0741a5e8-1024-483c-99b8-fb75011bcaed; produserId=264841; CTWIMAPPDPGSSOCookie=0741a5e8-1024-483c-99b8-fb75011bcaed; CTWIMAPPDPGSSOUser=wanghr3; sidebar_status=closed',
        'content-type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

solve_test_commit()
# if __name__ == "__main__":
#     while(1==1):
#         time.sleep(2.5)
#         solve_test_commit()