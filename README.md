<h1 align="center">HEU 平安行动自动打卡</h1>

<div align="center">HEU-Checkin-COVID-19</div></br>


这是一个用来方便宅家 HEU 人士搞定每日平安行动的助手，使用本项目前你需要确认自己不会到处瞎跑，不会危害社会。然后你需要会一点点使用浏览器的技巧，实际这个项目部署起来并没有你想的那么麻烦。可选用的部署方式有两种：Server 用于有服务器人士，GitHub Actions 用于无服务器人士。

部署本项目需要四项数据：教务处学生账号、教务处密码、平安行动表单 `BoundFields` 、平安行动表单 `FormData` 。

后两项的获取需要电脑端浏览器 + 一点点使用浏览器的技巧，具体操作：

1. 在进入平安行动打卡界面后按下 `F12` 调出审查工具，选中 Network / 网络 项
2. **确认表单数据正确** 后提交表单，之后会弹出“办理成功！”的字样
3. 不要关闭页面，这时审查工具中最下方会多出一个 `doAction` 的项目，点击它
4. 在它的 `Header` 中查看 `Form Data` 即可找到本项目需要的 `BoundFields` 和 `FormData`

如果需要，请参考《[Mark 一个 HEU 自动打卡代码 - MonsterX 小怪兽](https://monsterx.cn/tech/Auto-Checkin-COVID19.html)》中的图片。

获取了这些数据后即可开始部署自己的自动打卡任务，无论你选择下面的哪一种方式，**请在运行前务必修改并核实自己的登录用户、表单数据（、SMTP 发信邮箱）！**

## Server 版

经过我简单的测试和修改之后，该项目用于服务器部署的完整代码已存放于 Server 目录下。使用前确保使用 `pip install` 安装了 `lxml` `requests` 库。

1. 按照自己需要修改文件内容
   - Server/checkin.py 修改 Line35-36 Line110 Line113 Line156-163 为自己的登录用户、表单数据、SMTP 发信邮箱
   - Server/checkin.sh 修改其中的路径为实际路径，它用于 Linux 服务器设置定时任务，仅供参考
   - Server/checkin.log 若使用 checkin.sh 则该文件将记录打卡日志，无需修改
2. SMTP 发信邮箱设置并不是必须的，仅用于服务器打卡完成后发送邮件提醒
   如果不需要这个功能，直接删除 Server/checkin.py Line152-176 即可
3. 安装 pip 依赖项 `lxml` `requests`
   命令行执行 `python -m pip install lxml requests`
4. **运行前务必修改并核实自己的登录用户、表单数据、SMTP 发信邮箱！**
5. 配置打卡定时任务
   这个版本的自动打卡通过服务器或本地主机的定时任务实现自动打卡。请参考《[Mark 一个 HEU 自动打卡代码 - MonsterX 小怪兽](https://monsterx.cn/tech/Auto-Checkin-COVID19.html#toc_7)》设置定时任务。

## GitHub Actions 版

为提升广大 HEU 无服务器玩家的体验，本仓库着手实现基于 GitHub Actions 的自动打卡。灵感源自《[wangziyingwen/AutoApiSecret](https://github.com/wangziyingwen/AutoApiSecret)》这个用于 Microsoft 365 E5 刷 API 调用次数帮助订阅自动续期的仓库。

部署 GitHub Actions 说明：

1. Fork 本仓库
2. 在仓库的 Settings 中添加 4 个 Secrets（[点这里](/settings/secrets)）
   | Name | Value |
   |:----:|:------|
   | SECRET_ID | myid="2018XXXXXX" |
   | SECRET_PASS | mypass="PASSWORD" |
   | SECRET_BOUND | mybound='fieldCXXXdqszdjtx,......,fieldMQJCRlxfs' |
   | SECRET_DATA | mydata=r'{"_VAR_EXECUTE_INDEP_ORGANIZE_Name":"XXX学院",......,"_VAR_ENTRY_TAGS":"生活服务"}' |
3. **务必核实自己的登录用户、表单数据！**
4. 给自己的仓库点个 Star 等待几分钟
5. 查看 GitHub Actions 状态（[点这里](/actions)）

状态正常后，打卡任务将在每天指定时刻运行，本项目设定时间为 8:00。你也可以根据自己需要在 .github/workerflows/auto.yml Line12 修改打卡执行时间，请注意时区为。

## 注意

 - 本项目使用的 Python 版本为 3.x。已知 Python 2.x 会出现错误，不予修复
 - 本项目的主体功能完全不是我写的，出处是这篇《[疫情期间自动健康打卡暨 CAS 单点登录认证实践 - SiteForZJW](https://zjw1.top/2020/03/10/auto_checkin_during_covid19_and_cas_sso_learning/)》
 - 使用本项目因操作不当导致的平安行动打卡错误责任自负（比如你不检查表单数据提交了别的同学的数据到自己的平安行动中）
 - 如果你确实啥也不会，那么我推荐你使用 [腐败街](https://www.fubaijie.cn) 提供的定时打卡功能
 - Licence & Author: MIT @ [ZJW](https://zjw1.top) & [Monst.x](https://monsterx.cn)