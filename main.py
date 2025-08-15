# # url = 'https://www.srdcloud.cn/api/agilebackend/workitem/batchWorkitems'
# # data = {"workitems":[{"title":"集成i-Park智联应用场景仓库能力","description":"背景：<br/>- IDC机房用户需要自服务监控大屏平台<br/>- 需要集成现有i-Park智联应用的场景仓库能力<br/><br/>目标：<br/>- 提供机房监控常见场景参考模板<br/>- 实现场景组件的复用功能<br/><br/>功能描述：<br/>1. 对接i-Park智联应用API获取场景数据<br/>2. 建立机房监控场景分类体系<br/>3. 实现场景模板的预览功能<br/>4. 开发场景组件复用机制","project":75945,"workItemType":2,"status":1,"createType":1,"priority":2,"customFieldValues":{}},{"title":"构建监控大屏基础框架","description":"背景：<br/>- 需要为IDC机房用户提供自服务监控大屏平台<br/><br/>目标：<br/>- 搭建可扩展的监控大屏基础框架<br/><br/>功能描述：<br/>1. 设计并实现大屏布局系统<br/>2. 开发基础组件库（图表、表格等）<br/>3. 实现响应式布局适配不同屏幕尺寸","project":75945,"workItemType":2,"status":1,"createType":1,"priority":2,"customFieldValues":{}}]}
# headers = {
#         'Host': 'www.srdcloud.cn',
#         'pragma': 'no-cache',
#         'projectId': '75945',##
#         'sessionid': '1eb23433-b618-4515-ac07-6c809a4465c9',
#         'userId': '428801',##
#         'x-dup-id': '1755162319-llvop94h',
#         # 'Cookie': '_pk_id.5.136f=389e611a3363ca0d.1754545408.; _pk_id.8.136f=5b71364bf6f7490d.1754547001.; _pk_id.9.136f=71d62570514ea50f.1754553005.; fp=84b4a8b0b8038ed001d1a0154a318f93; _pk_id.3.136f=ab31da71dbd49a90.1755140267.; _pk_id.6.136f=686a64ee4f53aa95.1755150471.; uvId=4b001f62-4530-4338-9c7d-a6be338ed83f; sidebar_status=closed; srdcloud.cn=HttpOnly; _pk_ref..136f=%5B%22%22%2C%22%22%2C1755161584%2C%22https%3A%2F%2Fopen.e.189.cn%2F%22%5D; _pk_ses.9.136f=1; prodtoken=b12ecfb2-643e-45e4-a891-b7f71fd9a8fc; produserId=428801; CTWIMAPPDPGSSOCookie=b12ecfb2-643e-45e4-a891-b7f71fd9a8fc; CTWIMAPPDPGSSOUser=srd18964600668',
#         'content-type': 'application/json'
#     }

# # check(postData(url,data,headers))




# # git提交记录
# # 定义提交前缀和对应的功能内容
# commit_data = [
#     ("feat", "新增部分车辆数据获取"),
#     ("feat", "新增部分告警数据获取"),
#     ("fix", "修改部分车辆数据获取"),
#     ("fix", "修改部分告警数据获取"),
#     ("fix", "完善部分车辆数据获取"),
#     ("fix", "完善部分告警数据获取"),
#     ("feat", "新增告警数据接口"),
#     ("feat", "新增车辆道闸数据接口")
# ]

# # 进入你的Git仓库目录
# # repo_path = "E:/whr/2022.7.5电话亭/代码版本/管理平台/ght-15min-management-backend"
# repo_path = "/Users/jesse/Project/srdcloud"


# # 文档链接
# DOC_URL = "https://docs.srdcloud.cn/docs/NJkbEl9MyKh0OoqR"

# # 指定 Microsoft Edge 的可执行文件路径
#         # edge_path = "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"




import yaml
import argparse
from util import gitCommit,doc_edit,writeFile,postData,checkStatus


parser = argparse.ArgumentParser(description="一个示例程序")
parser.add_argument('--config',default='data/config.yaml', help='config file path')
parser.add_argument('--mode',default='all', help='auto mode')
args = parser.parse_args()

# 读取 YAML 配置文件
with open(args.config, 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

if args.mode == 'git':
    gitCommit(config['gitCommit'])
elif args.mode == 'doc':
    doc_edit(config['docEdit'])
elif args.mode == 'pipe':
    pass
elif args.mode == 'sample':
    checkStatus(postData(config['testSample']))
elif args.mode == 'work':
    checkStatus(postData(config['workItem']))
elif args.mode == 'all':
    print('---文档编辑---')
    doc_edit(config['docEdit'])
    print('---Git提交---')
    gitCommit(config['gitCommit'])
    print('---测试样例---')
    checkStatus(postData(config['testSample']))
    print('---工作项---')
    checkStatus(postData(config['workItem']))