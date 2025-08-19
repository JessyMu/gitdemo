import time
import requests
import json

# 测试用例

def solve_test_commit():
    url = "https://www.srdcloud.cn/api/cibackend/cicenter/pipeline/v2/job"
    dd = f'job{int(time.time())}'
    payload = json.dumps({"syncModifyFlag":1,"cloneDepth":1,"configDeploy":0,"artifactModels":[],"artifactConfigModels":[],"branchName":"master","branchPattern":-1,"buildTool":1,"buildType":0,"codeQualityServiceModels":[],"codeUpdateTriggerType":0,"commitId":"","compileContainer":"","compileServiceModels":[],"description":"","dockerImageTag":{"enableCommitId":1,"enableLatest":0,"enableCodeTag":0,"enableCustom":0,"customPattern":""},"dynamicBranchConfig":0,"downloadFiles":[],"eventTriggerModules":[],"fortifyScanConfig":{"srcPath":"","scanType":0,"fortifyParam":"","pythonInstallPath":"","scalaVersion":"","gccVersion":"","cBuildTool":0,"usePrivateImage":0,"rubyPath":"","rubyGemPath":"","useQualityGate":False,"pythonVersion":""},"fortifyScanModules":[],"gradleVersion":"","initShell":"","isSampleProject":0,"jobAddressRelation":{"codeClusterId":5,"codeClusterUrl":"https://code.srdcloud.cn/","artifactClusterId":"","artifactClusterUrl":"https://gz01-srdart.srdcloud.cn","artifactClusterType":"sr","artifactProjectIdentifier":"codefree2025","appRootUrl":"","appRootInnerUrl":"","gitType":2},"jobEnvGroups":[],"jobName":f"{dd}","jobTags":[],"jobType":1,"langVersion":"","libCache":0,"dockerSave":0,"language":1,"merge":-1,"manualModuleTrigger":0,"node":{"id":"626218377f2e874b78517cb9","nodeDisplayName":"非信创X86节点","nodeName":"非信创X86节点","type":"cloud","createTime":"2022-04-22 10:51:35","creator":"devmonlogqg","updateTime":"2025-08-18 11:52:28","updator":"opsadminmohs","status":1,"operationSystem":0,"operationSystemName":"Linux","architecture":"x86"},"npmOrYarn":1,"notification":{"enableNotification":1,"notifyFailed":1,"notifyTimeout":1,"notifyAbort":0,"notifySuccess":0,"notifyExecutor":1,"notifyManager":0,"notifyMember":0,"notifyDingdingRobot":0,"notifyWechatRobot":0,"dingdingRobotAccounts":[],"wechatRobotAccounts":[]},"nodeType":"cloud","operationSystem":0,"pipelineTemplateId":547074,"projName":"codefree2025/firstgroup","projId":"75945","projDisplayName":"第一组","parentProjId":75944,"registryModels":[],"repoName":"kk","repoFullName":"codefree2025/firstgroup/kk","requirementsPath":"","scanTool":1,"srcPath":"","steps":[{"stepIndex":0,"stageGroups":[{"stageGroupId":200,"stageGroupType":15,"stageGroupParallelIndex":0,"stageGroupName":"代码下载","stageGroupDisplayName":"代码下载","langClass":1,"requiredShow":0,"requiredChoice":0,"artifactType":0,"buildTool":0,"guideUrl":"https://www.srdcloud.cn/helpcenter/content?id=1222550295844679680","stageGroupConfig":{"codeCheckout":{"id":44495,"jobId":547074,"repoType":1,"clusterUrl":"https://code.srdcloud.cn/","repoFullName":"codefree2025/firstgroup/kk","checkoutType":1,"checkoutParam":"master","checkoutPath":"/kk","projId":75945}},"artifactRelatedConfig":0,"subJobIndex":0,"allowDelSteps":1,"async":False}]}],"scanPath":"","sonarExclusions":"","sonarScanConfig":{"gccVersion":"","cBuildTool":0,"useQualityGate":False,"usePrivateImage":0,"scanPrivateImage":0},"taasTestModels":[],"tag":"","triggerType":1,"triggerDate":"","triggerMode":1,"triggerTime":"","triggerTimeFrame":"","triggerInterval":60,"timeoutMinute":1440,"unitTestServiceModels":[],"usePrivateImage":0,"verify":1})
    # 需要变动 sessionid   userid(后续不变）    x-dup-id  Cookie'
    headers = {
        'Host': 'www.srdcloud.cn',
        'pragma': 'no-cache',
        'projectid': '75945',##
        'sessionid': '1083acfb-b22f-4e6e-8b9b-8aae08af81a1',
        'userid': '428801',##
        'x-dup-id': '1755495453-utdlw2usx',
        # 'Cookie': '_pk_id.8.136f=3489c818118ee943.1725241416.; _pk_id.5.136f=1b3e3f31a58e0037.1725241417.; _pk_id.4.136f=0b49a46a7a943210.1725325196.; fp=c94054e345de06e2421e1b1f4942c649; _pk_id.3.136f=923e2f550de8dde0.1734319653.; _pk_ref..136f=%5B%22%22%2C%22%22%2C1747962219%2C%22https%3A%2F%2Fopen.e.189.cn%2F%22%5D; _pk_id.11.136f=c670d85a08784856.1742785487.; prodtoken=0741a5e8-1024-483c-99b8-fb75011bcaed; produserId=264841; CTWIMAPPDPGSSOCookie=0741a5e8-1024-483c-99b8-fb75011bcaed; CTWIMAPPDPGSSOUser=wanghr3; sidebar_status=closed',
        'content-type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    return response



a = solve_test_commit()


def run_job(jobid):
    url = f"https://www.srdcloud.cn/api/cibackend/cicenter/pipeline/v2/job/build?jobId={jobid}"
    dd = f'job{int(time.time())}'
    payload = json.dumps({"branch":"","envGroupName":"","envVariables":[]})
    # 需要变动 sessionid   userid(后续不变）    x-dup-id  Cookie'
    headers = {
        'Host': 'www.srdcloud.cn',
        'pragma': 'no-cache',
        'projectid': '75945',##
        'sessionid': '1083acfb-b22f-4e6e-8b9b-8aae08af81a1',
        'userid': '428801',##
        'x-dup-id': '1755495453-utdlw2usx',
        # 'Cookie': '_pk_id.8.136f=3489c818118ee943.1725241416.; _pk_id.5.136f=1b3e3f31a58e0037.1725241417.; _pk_id.4.136f=0b49a46a7a943210.1725325196.; fp=c94054e345de06e2421e1b1f4942c649; _pk_id.3.136f=923e2f550de8dde0.1734319653.; _pk_ref..136f=%5B%22%22%2C%22%22%2C1747962219%2C%22https%3A%2F%2Fopen.e.189.cn%2F%22%5D; _pk_id.11.136f=c670d85a08784856.1742785487.; prodtoken=0741a5e8-1024-483c-99b8-fb75011bcaed; produserId=264841; CTWIMAPPDPGSSOCookie=0741a5e8-1024-483c-99b8-fb75011bcaed; CTWIMAPPDPGSSOUser=wanghr3; sidebar_status=closed',
        'content-type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    return response


b = run_job(a.json()['data']['jobId'])