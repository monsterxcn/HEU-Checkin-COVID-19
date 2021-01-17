<h1 align="center">HEU 平安行动自动打卡</h1>

<div align="center">HEU-Checkin-COVID-19</div></br>


> **近期校园网络调整引起的打卡失败已经修复，多谢 [@liulu1998](https://github.com/liulu1998) 和 [@amberOoO](https://github.com/amberOoO) 的修改。Python 和 Ruby 版本均已测试可用，保险起见建议您执行多次定时任务防止遗漏**

利用 GitHub Actions 为 HEU 宅家人士每日平安行动打卡提供便利的小项目，使用前请确认自己健康状况。

请参考 [Wiki](https://github.com/monsterxcn/HEU-Checkin-COVID-19/wiki) 自行选择部署位置和代码版本，并修改配置。


**快速开始**

 1. Fork 此仓库
 2. 启用仓库 Actions
 3. 添加 Secrets
 4. 手动执行一次 Action
 5. 起飞


**慢速开始**

你可以选择在本地机器或自己的服务器上部署，也可以白嫖 GitHub Actions 免费提供的机器。

首先需要做的是获取打卡数据 → [部署前的准备](https://github.com/monsterxcn/HEU-Checkin-COVID-19/wiki/%E9%83%A8%E7%BD%B2%E5%89%8D%E7%9A%84%E5%87%86%E5%A4%87)

接下来，

 - 如果你希望白嫖 GitHub Actions → [部署到 Actions](https://github.com/monsterxcn/HEU-Checkin-COVID-19/wiki/%E9%83%A8%E7%BD%B2%E5%88%B0-Actions)
 - 如果你希望在自己的计算机上部署 → [部署到自有机器](https://github.com/monsterxcn/HEU-Checkin-COVID-19/wiki/%E9%83%A8%E7%BD%B2%E5%88%B0%E8%87%AA%E6%9C%89%E6%9C%BA%E5%99%A8)

最后为了安心的睡眠，你可能还需要 [启用 SMTP 邮件提醒](https://github.com/monsterxcn/HEU-Checkin-COVID-19/wiki/%E5%90%AF%E7%94%A8-SMTP-%E9%82%AE%E4%BB%B6%E6%8F%90%E9%86%92) 或者 [启用 Server 酱微信提醒](https://github.com/monsterxcn/HEU-Checkin-COVID-19/wiki/%E5%90%AF%E7%94%A8-Server-%E9%85%B1%E5%BE%AE%E4%BF%A1%E6%8F%90%E9%86%92)（默认均未启用）来通知你打卡的结果。


**文件结构**

 - `/Server` 目录下是服务器或本地部署的文件
 - `/Actions` 目录下是 GitHub Actions 部署的文件
 - `/Self` 目录下是 Monst.x 自用的文件
 - `/.github/workflows` 目录下是 Actions 自动打卡的工作流文件

   其中 `delete-this-*.yml` 文件是 Monst.x 自用的工作流文件

> 可以参考 Monst.x 自用部署启用 Server 酱微信提醒哦～


**一些说明**

 - 建议您使用 Python 版本 GitHub Actions 部署
 - 建议您至少启用邮件提醒和 Server 酱微信提醒之一
 - 如果一次打卡不能安心的话那就多打几次
 - 本项目使用的 Python 版本为 3.7+。3.7 以下版本需要修改几处代码。已知 Python 2.x 会出现错误
 - Ruby 版本打卡由于网络连接质量、校园服务器响应等某种问题可能出现失败，建议在 Linux 自有机器部署
 - 如需停止 GitHub Action，请删除仓库或删除 `.github/workerflows` 文件夹下 `.yml` 文件
 - 使用本项目因操作不当导致的平安行动打卡错误责任自负
 - 代码来自 [ZJW](https://zjw1.top) | [XYenon](https://xyenon.bid) | [@liulu1998](https://github.com/liulu1998) | [@amberOoO](https://github.com/amberOoO) | [Monst.x](https://monsterx.cn)