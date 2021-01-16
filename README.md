<h1 align="center">HEU 平安行动自动打卡</h1>

<div align="center">HEU-Checkin-COVID-19</div></br>


**由于近期校园网络调整，此项目尚未跟进修改，建议手动打卡，而不是依赖此项目**

利用 GitHub Actions 为 HEU 宅家人士每日平安行动打卡提供便利的小项目，使用前请确认自己健康状况。

请参考 [Wiki](https://github.com/monsterxcn/HEU-Checkin-COVID-19/wiki) 自行选择部署位置和代码版本，并修改配置。


**结构**

 - `/Server` 目录下是服务器或本地部署的文件
 - `/Actions` 目录下是 GitHub Actions 部署的文件


**部署**

 1. Fork 此仓库
 2. 启用仓库 Actions
 3. 添加 Secrets
 4. 手动执行一次 Action
 5. 起飞


**叨叨**

 - Python by [ZJW](https://zjw1.top/2020/03/10/auto_checkin_during_covid19_and_cas_sso_learning/) / Ruby by [XYenon](https://gist.github.com/XYenon/79317d63e7f769e5bdff5b595d709b65)
 - 建议您使用 Python 版本 GitHub Actions 部署
 - 建议您至少启用邮件提醒和 Server 酱微信提醒之一
 - 如果一次打卡不能安心的话那就多打几次
 - 本项目使用的 Python 版本为 3.x。已知 Python 2.x 会出现错误，不予修复
 - Ruby 版本打卡由于网络连接质量、校园服务器响应等某种问题可能出现失败
 - 如需停止 GitHub Action，请删除仓库或删除 `.github/workerflows` 文件夹下 `.yml` 文件
 - 使用本项目因操作不当导致的平安行动打卡错误责任自负
 - Author: [ZJW](https://zjw1.top) | [XYenon](https://xyenon.bid) | [Monst.x](https://monsterx.cn)