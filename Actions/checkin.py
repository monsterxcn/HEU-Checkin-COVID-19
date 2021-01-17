#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
平安行动自动打卡

Created on 2020-04-13 20:20
@author: ZhangJiawei & Liu Chongpeng & Liu Lu
"""

import os
import requests
import lxml.html
import re
import json
import random
import time
import smtplib
import traceback

myid = os.environ ['SECRET_ID']
mypass = os.environ ['SECRET_PASS']
mybound = os.environ ['SECRET_BOUND']
mydata = os.environ ['SECRET_DATA']
# mysckey = os.environ ['SECRET_SCKEY']


title = ""
msg = ""

proxies = {"http": None, "https": None}

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "MESSAGE_TICKET=%7B%22times%22%3A0%7D; ",
    "Host": "cas.hrbeu.edu.cn",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362"
}


def findStr(source, target):
    return source.find(target) != -1


if __name__ == '__main__':
    try:
        ## 登陆校园网络认证界面
        url_login = 'https://cas.hrbeu.edu.cn/cas/login?'
        print("============================\n[debug] Begin to login ...")
        sesh = requests.session()
        req = sesh.get(url_login, proxies=proxies)
        html_content = req.text
        login_html = lxml.html.fromstring(html_content)
        hidden_inputs = login_html.xpath( r'//div[@id="main"]//input[@type="hidden"]')
        user_form = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}
        user_form["username"] = myid
        user_form["password"] = mypass
        user_form["captcha"] = ''
        user_form["submit"] = '登 录'
        headers['Cookie'] = headers['Cookie'] + req.headers['Set-cookie']
        req.url = f'https://cas.hrbeu.edu.cn/cas/login'
        response302 = sesh.post(req.url, data=user_form, headers=headers, proxies=proxies)

        ## 进入平安行动界面
        jkgc_response = sesh.get( "http://jkgc.hrbeu.edu.cn/infoplus/form/JSXNYQSBtest/start", proxies=proxies)
        headers['Accept'] = '*/*'
        headers['Cookie'] = jkgc_response.request.headers['Cookie']
        headers['Host'] = 'jkgc.hrbeu.edu.cn'
        headers['Referer'] = jkgc_response.url
        jkgc_html = lxml.html.fromstring(jkgc_response.text)
        csrfToken = jkgc_html.xpath(r'//meta[@itemscope="csrfToken"]')
        csrfToken = csrfToken.pop().attrib["content"]
        jkgc_form = {
            'idc': 'JSXNYQSBtest',
            'release': '',
            'csrfToken': csrfToken,
            'formData': {
                '_VAR_URL': jkgc_response.url,
                '_VAR_URL_Attr': {}
            }
        }
        jkgc_form['formData'] = json.dumps(jkgc_form['formData'])
        jkgc_url = 'http://jkgc.hrbeu.edu.cn/infoplus/interface/start'
        response3 = sesh.post(jkgc_url, data=jkgc_form, headers=headers, proxies=proxies)

        ## 提交平安行动表单
        form_url = json.loads(response3.text)['entities'][0]
        form_response = sesh.get(form_url)
        headers['Accept'] = 'application/json, text/javascript, */*; q=0.01'
        headers['Referer'] = form_url
        headers['X-Requested-With'] = 'XMLHttpRequest'
        submit_url = 'http://jkgc.hrbeu.edu.cn/infoplus/interface/doAction'
        submit_html = lxml.html.fromstring(form_response.text)
        csrfToken2 = submit_html.xpath(r'//meta[@itemscope="csrfToken"]')
        csrfToken2 = csrfToken2.pop().attrib["content"]
        submit_form = {
            'actionId': '1',
            'boundFields': mybound,                    # boundFields 修改位置
            'csrfToken': csrfToken2,
            'formData': mydata,                        # formData 修改位置
            'lang': 'zh',
            'nextUsers': '{}',
            'rand': str(random.random() * 999),
            'remark': '',
            'stepId': re.match(r'.*form/(\d*?)/', form_response.url).group(1),
            'timestamp': str(int(time.time()+0.5))
        }
        response_end = sesh.post(submit_url, data=submit_form, headers=headers, proxies=proxies)
        resJson = json.loads(response_end.text)

        ## 表单填写完成，返回结果
        print('[debug] Form url: ', form_response.url)
        print('[debug] Form Status: ', resJson['ecode'])
        print('[debug] Form stJson: ', resJson)

        ## 生成提醒返回的标题和信息
        if (resJson['errno'] == 0):
            print('[info] Checkin succeed with jsoncode', resJson['ecode'])
            title = f'打卡成功 <{submit_form["stepId"]}>'
            msg = '\t表单地址: ' + form_response.url + '\n\n\t表单状态: \n\t\terrno：' + str(resJson['errno']) + '\n\t\tecode：' + str(
                resJson['ecode']) + '\n\t\tentities：' + str(resJson['entities']) + '\n\n\n\t完整返回：' + response_end.text
        else:
            print('[error] Checkin error with jsoncode', resJson['ecode'])
            title = f'打卡失败！校网出错'
            msg = '\t表单地址: ' + form_response.url + '\n\n\t错误信息: \n\t\terrno：' + str(resJson['errno']) + '\n\t\tecode：' + str(
                resJson['ecode']) + '\n\t\tentities：' + str(resJson['entities']) + '\n\n\n\t完整返回：' + response_end.text
    except:
        print('\n[error] :.:.:.:.: Except return :.:.:.:.:')
        err = traceback.format_exc()
        print('[error] Python Error: \n', err)
        title = '打卡失败！脚本出错'
        msg = '\t脚本报错: \n\n\t' + err + '============================\n'
    finally:
        print(':.:.:.:.: Finally :.:.:.:.:')

        ## 发送邮件
        # from email.mime.text import MIMEText
        # from email.header import Header
        # mail_host = "smtp.qq.com"                      # SMTP 服务器地址
        # mail_user = "sender@example.com"               # SMTP 发信邮箱用户名
        # mail_pass = "emailpassword"                    # SMTP 发信邮箱密码
        # sender = 'sender@example.com'                  # 发信人邮箱，即 SMTP 发信邮箱用户名
        # receivers = ['receiver@example.com']           # 收信人邮箱，多邮箱以数组形式写
        # message = MIMEText(msg, 'plain', 'utf-8')
        # message['From'] = Header("1@example.com", 'utf-8')        # 发信人邮箱，仅用于显示
        # message['To'] =  Header("2@example.com", 'utf-8')         # 收信人邮箱，仅用于显示
        # subject = title
        # message['Subject'] = Header(subject, 'utf-8')
        # try:
        #     ##  smtpObj.connect(mail_host, 25)                    # Python 3.7 以下版本 一般发信 SMTP 端口号 25
        #     ##  smtpObj = smtplib.SMTP()                          # Python 3.7 以下版本 一般发信
        #     ##  smtpObj = smtplib.SMTP_SSL()                      # Python 3.7 以下版本 SSL 加密发信
        #     smtpObj = smtplib.SMTP_SSL(mail_host)        # Python 3.7 及以上版本 SSL 加密发信
        #     smtpObj.connect(mail_host, 465)              # Python 3.7 及以上版本 加密发信 SMTP 端口号 465
        #     smtpObj.login(mail_user,mail_pass)
        #     smtpObj.sendmail(sender, receivers, message.as_string())
        #     print ("[info] Success: The email was sent successfully")    # 日志输出
        # except smtplib.SMTPException:
        #     print ("[error] Error: Can not send mail")                   # 日志输出

        ## 或者发送 Server 酱的微信提醒
        # wcurl = 'https://sc.ftqq.com/' + mysckey + '.send'
        # wcdata = {'text': title, 'desp': msg}
        # wcresult = requests.post(wcurl, wcdata)
        # print('[info] Notification sended at', time.strftime("%Y-%m-%d %H:%M:%S %A", time.localtime()))

        print('[info] Task Finished at', time.strftime("%Y-%m-%d %H:%M:%S %A", time.localtime()))
        print('============================\n')
