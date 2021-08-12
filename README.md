<h1 align="center">HEU 平安行动自动打卡</h1>

<div align="center">HEU-Checkin-COVID-19</div></br>


利用 GitHub Actions 为 HEU 宅家人士每日平安行动打卡提供便利的小项目，使用前请确认自己健康状况。

此分支使用了开源项目 [@easychen/wecomchan](https://github.com/easychen/wecomchan) 从自行部署的企业微信接口推送消息提醒，改用单独文本配置，可进行多账号打卡。仅提供 Python 自有机器部署文件，理论上也可以使用 GitHub Actions 白嫖，思路是将配置文件内容写入仓库 Secrets，再修改代码以读取环境变量。欢迎体验~


## config.txt

配置文件被 Python 按行读取并赋值给变量，请 **严格** 按照仓库中的文件编写，文件结尾需要 **保留一个空行**。

```
ww205a0XXXXXX9487c                          # 企业微信的企业 ID（企业微信 - 我的企业 - 企业信息
loPX-WKdsc4_fEjtolvh7aXXXXXXXXXXXXXfeel4    # 企业微信自建应用的 Secret（企业微信 - 应用管理 - 自建
100000X                                     # 企业微信自建应用的 AgentId（企业微信 - 应用管理 - 自建


20XX0XXXXX               # 用户 1 学号
01011234                 # 用户 1 密码
fieldCXXXdqszdjtx,fieldCXXXjtgjbc,fieldGLJL,...  BOUNDFIELDS HERE  ...,fieldJBXXdw,fieldCFDD,fieldCXXXsftjhbjtdz,fieldMQJCRlxfs
{"_VAR_EXECUTE_INDEP_ORGANIZE_Name":"XXXX学院",...  FORMDATA HERE  ...,"_VAR_ENTRY_NAME":"平安行动_","_VAR_ENTRY_TAGS":"生活服务"}
@all                     # 企业微信接收提醒的用户 UID

20XX0YYYYY               # 用户 2 学号
01015678                 # 用户 2 密码
fieldCXXXdqszdjtx,fieldCXXXjtgjbc,fieldGLJL,...  BOUNDFIELDS HERE  ...,fieldJBXXdw,fieldCFDD,fieldCXXXsftjhbjtdz,fieldMQJCRlxfs
{"_VAR_EXECUTE_INDEP_ORGANIZE_Name":"XXXX学院",...  FORMDATA HERE  ...,"_VAR_ENTRY_NAME":"平安行动_","_VAR_ENTRY_TAGS":"生活服务"}
@all                     # 企业微信接收提醒的用户 UID

```

鉴于这样自己部署起来就方便很多（逃...