import yaml
import json
import argparse
import random
import time
import asyncio
import traceback
from playwright.sync_api import sync_playwright


captured_request = None

def main():
    from util import gitCommit,doc_edit,writeFile,postData,checkStatus,get_post,pipe_wrap,get_info,click_submit,remove_item_all,new_gitRepo

    parser = argparse.ArgumentParser(description="一个示例程序")
    parser.add_argument('--config',default='data/config.yaml', help='config file path')
    parser.add_argument('--mode',default=['work'],nargs='+', help='auto mode from [git, doc, pipe, sample, work, all]')
    parser.add_argument('--browser',default='edge',help='edge,chrome,firefox')
    parser.add_argument('--projId',type=int,default=57670)
    parser.add_argument('--isRepoCreate', action='store_true', default=False, help='是否创建仓库 (默认: True)')
    args = parser.parse_args()
    
    assert len(args.mode), 'Error! 必须选择至少一种指标!'
    # 读取 YAML 配置文件
    with open(args.config, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)

    requests_list = get_post(config)
        
    assert requests_list, f"Error! \n❌ 未捕获到 POST 请求: {config['web_page']}!"
    for request in requests_list:
        sessionid = request['headers']['sessionid']
        x_dup_id = request['headers']['x-dup-id']
        user_id = request['headers']['userid']
        if sessionid != 'undefined' and user_id != 'undefined' and x_dup_id != 'undefined':
            break
    assert sessionid != 'undefined' and user_id != 'undefined' and x_dup_id != 'undefined', "Error! 未检测到登录用户信息!"

    config['headers']['sessionid'] = sessionid
    config['headers']['x-dup-id'] = x_dup_id 
    config['headers']['userId'] = user_id
    config['headers']['projectid'] = str(args.projId)
    
    
    proj_info = get_info(config['projectInfo']['url']+str(args.projId),config['headers'])
    assert checkStatus(proj_info), "Error! 项目 Id 错误！"
    print("✅ 已获取项目概览信息")
    config['pipeline']['newPipe']['data']['projName'] = proj_info.json()['baseInfo']['name']
    config['pipeline']['newPipe']['data']['projId'] = proj_info.json()['baseInfo']['projectId']
    config['pipeline']['newPipe']['data']['projDisplayName'] = proj_info.json()['baseInfo']['displayName']
    config['pipeline']['newPipe']['data']['parentProjId'] = proj_info.json()['baseInfo']['parentProjectId']
    
    # config['pipeline']['newPipe']['data']['steps']['parentProjId']
    
    # modify all the variable attributes in the config file
    
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
        if args.isRepoCreate:
            config['pipeline']['repoName'] = new_gitRepo(config['user_dir'],config['browser_path'],config['addRepo']['web_url'].format(config['headers']['projectid']),config['addRepo'],context)
            print("✅ 新建代码仓库成功！")
        context.close()

    # get the git repo info
    time.sleep(config['addRepo']['wait_time'])
    repo_info = get_info(config['projectInfo']['repo']['repolist_url']+str(args.projId),config['headers'])
    assert checkStatus(repo_info) and len(repo_info.json()['data']['dataList']), "Error! 无法获取repo信息或项目代码仓库为空！"
    repo_flag = False
    for repo in repo_info.json()['data']['dataList']:
        if repo['repositoryName'] == config['pipeline']['repoName']:
            repo_flag = True
            # config['pipeline']['newPipe']['data']['gitType'] = repo['gitType']
            config['pipeline']['newPipe']['data']['repoName'] = repo['repositoryName']
            config['pipeline']['newPipe']['data']['repoFullName'] = repo['repoFullName']
            # config['pipeline']['newPipe']['data']['jobName'] += str(int(time.time()))

            config['pipeline']['newPipe']['data']['steps'][0]['stageGroups'][0]['stageGroupConfig']['codeCheckout']['repoFullName'] = repo['repoFullName']
            config['pipeline']['newPipe']['data']['steps'][0]['stageGroups'][0]['stageGroupConfig']['codeCheckout']['checkoutPath'] = f"/{repo['repositoryName']}"
            config['pipeline']['newPipe']['data']['steps'][0]['stageGroups'][0]['stageGroupConfig']['codeCheckout']['projId'] = proj_info.json()['baseInfo']['projectId']
            break
    assert repo_flag, f"不存在名为{config['pipeline']['repoName']}的代码仓库"
    print(f"✅ Load Git Repo: {config['pipeline']['repoName']}")
    flag = True
    while flag:
        flag = False
        assert len(args.mode), 'Error! 当前没有可以提升使用率的指标!'
        current_mode = random.choice(args.mode)
        try:
            if current_mode == 'git':
                gitCommit(config['gitCommit'])
            elif current_mode == 'doc':
                doc_edit(config['user_dir'],config['browser_path'],config['docEdit'])
            elif current_mode == 'pipe':
                pipe_wrap(config['pipeline'])
            elif current_mode == 'sample':
                click_submit(config['user_dir'],config['browser_path'],config['testSample']['web_url'].format(config['headers']['projectid']),config['testSample'],'sample')
            elif current_mode == 'work':
                click_submit(config['user_dir'],config['browser_path'],config['workItem']['web_url'].format(config['headers']['projectid']),config['workItem'],'work')
            else:
                print(f'Warning! {current_mode}指标不存在!')
                raise(Exception('指标不存在'))
        except Exception as e:
            args.mode = remove_item_all(args.mode,current_mode)
            print(f'Error! {traceback.print_exc()}')
            print(f'删除{current_mode}，继续执行')

if __name__ == "__main__":
    # asyncio.run(main())
    main()