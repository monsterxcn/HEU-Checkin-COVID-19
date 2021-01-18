<h1 align="center">HEU 平安行动自动打卡</h1>

<div align="center">HEU-Checkin-COVID-19</div></br>


利用 GitHub Actions 为 HEU 宅家人士每日平安行动打卡提供便利的小项目，使用前请确认自己健康状况。


## 快速开始

 1. Fork 此仓库
 2. 添加 Secrets
 3. 启用 Actions
 4. 手动执行一次 Action
 5. 起飞


## 慢速开始

你可以选择在本地机器或自己的服务器上部署，也可以白嫖 GitHub Actions 免费提供的机器。

首先需要做的是获取打卡数据 → [部署前的准备](https://github.com/monsterxcn/HEU-Checkin-COVID-19/wiki/%E9%83%A8%E7%BD%B2%E5%89%8D%E7%9A%84%E5%87%86%E5%A4%87)

接下来，

 - 如果你希望白嫖 GitHub Actions → [部署到 Actions](https://github.com/monsterxcn/HEU-Checkin-COVID-19/wiki/%E9%83%A8%E7%BD%B2%E5%88%B0-Actions)
 - 如果你希望在自己的计算机上部署 → [部署到自有机器](https://github.com/monsterxcn/HEU-Checkin-COVID-19/wiki/%E9%83%A8%E7%BD%B2%E5%88%B0%E8%87%AA%E6%9C%89%E6%9C%BA%E5%99%A8)

最后为了安心的睡眠，你可能还需要 [启用 SMTP 邮件提醒](https://github.com/monsterxcn/HEU-Checkin-COVID-19/wiki/%E5%90%AF%E7%94%A8-SMTP-%E9%82%AE%E4%BB%B6%E6%8F%90%E9%86%92) 或者 [启用 Server 酱微信提醒](https://github.com/monsterxcn/HEU-Checkin-COVID-19/wiki/%E5%90%AF%E7%94%A8-Server-%E9%85%B1%E5%BE%AE%E4%BF%A1%E6%8F%90%E9%86%92)（默认启用）来通知你打卡的结果。


## 文件结构

 - `/.github/workflows` 目录下是 Actions 自动打卡的工作流文件

   其中 `delete-this-*.yml` 文件是 Monst.x 自用的工作流文件

 - `/Actions` 目录下是 **GitHub Actions 部署的文件**
 - `/Logs` 目录下是打卡生成的日志文件
 - `/Self` 目录下是 Monst.x 自用的文件
 - `/Server` 目录下是 **自有机器部署的文件**


&nbsp;

**戳 [Wiki](https://github.com/monsterxcn/HEU-Checkin-COVID-19/wiki) 开始部署吧**