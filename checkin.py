#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import json,lxml.html,re,random,requests,time,traceback

def getCfg(filename):
    # Try to read a txt file and return a list.
    # Return [] if there was a mistake.
    # https://www.cnblogs.com/givemelove/p/9892100.html
    try:
        file = open(filename,'r')
    except IOError:
        error = []
        return error
    content = file.readlines()
    for i in range(len(content)):
        content[i] = content[i][:len(content[i])-1]
    file.close()
    return content

def getHito():
    # https://github.com/easychen/wecomchan/blob/main/README.md
    get_hitokoto_url = "https://v1.hitokoto.cn/?c=a&c=b&c=c&encode=text&charset=utf-8"
    response = requests.get(get_hitokoto_url).content.decode('UTF-8','strict')
    return response

def sendNtf(text,wecom_aid,wecom_secret,wecom_cid,wecom_touid):
    # https://github.com/easychen/wecomchan/blob/main/README.md
    get_token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={wecom_cid}&corpsecret={wecom_secret}"
    response = requests.get(get_token_url).content
    access_token = json.loads(response).get('access_token')
    if access_token and len(access_token) > 0:
        send_msg_url = f'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}'
        data = {
            "touser":wecom_touid,
            "agentid":wecom_aid,
            "msgtype":"textcard",
            "textcard":{
                "title": '平安行动 通知',
                "description": text,
                "url": 'https://github.com/monsterxcn/HEU-Checkin-COVID-19',
                "btntxt": '更多',
            },
            "duplicate_check_interval":600
        }
        response = requests.post(send_msg_url,data=json.dumps(data)).content
        return response
    else:
        return False

def checkin(studentid,password,bound,data,log):
    # Run checkin
    proxies = {"http": None, "https": None}
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "",
        "Host": "cas.hrbeu.edu.cn",
        "Origin": "https://cas.hrbeu.edu.cn",
        "Referer": "https://cas.hrbeu.edu.cn/cas/login",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362"
    }
    try:
        ## 登陆校园网络认证界面
        url_login = 'https://cas.hrbeu.edu.cn/cas/login'
        log += f'[{time.strftime("%H:%M:%S", time.localtime())}] 开始登录 CAS 认证界面\n'
        sesh = requests.session()
        req = sesh.get(url_login, proxies=proxies)
        html_content = req.text
        login_html = lxml.html.fromstring(html_content)
        hidden_inputs = login_html.xpath(r'//input[@type="hidden" and @class="for-form"]')
        user_form = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}
        if user_form['pid'] == '':
            user_form.pop('pid')
        user_form["username"] = studentid
        user_form["password"] = password
        user_form["_eventId"] = 'submit'
        headers['Cookie'] = headers['Cookie'] + req.headers['Set-cookie'].split(' ')[0] + req.headers['Set-cookie'].split(' ')[3]
        req.url = f'https://cas.hrbeu.edu.cn/cas/login'
        response302 = sesh.post(req.url, data=user_form, headers=headers, proxies=proxies)
        log += f'[{time.strftime("%H:%M:%S", time.localtime())}] CAS 认证登陆成功，等待跳转\n'
        time.sleep(5)
        ## 进入平安行动界面
        jkgc_response = sesh.get( "http://jkgc.hrbeu.edu.cn/infoplus/form/JSXNYQSBtest/start", proxies=proxies)
        headers['Accept'] = '*/*'
        headers['Cookie'] = jkgc_response.request.headers['Cookie']
        headers['Host'] = 'jkgc.hrbeu.edu.cn'
        headers['Referer'] = jkgc_response.url
        jkgc_html = lxml.html.fromstring(jkgc_response.text)
        log += f'[{time.strftime("%H:%M:%S", time.localtime())}] 平安行动界面解析完成\n'
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
        log += f'[{time.strftime("%H:%M:%S", time.localtime())}] 开始提交平安行动表单数据\n'
        time.sleep(5)
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
            'boundFields': bound,                    # boundFields 修改位置
            'csrfToken': csrfToken2,
            'formData': data,                        # formData 修改位置
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
        log += f'[{time.strftime("%H:%M:%S", time.localtime())}] 平安行动表单提交结束\n\n'
        if (resJson['errno'] == 0):
            log += f'**今日打卡成功！**\n'
            log += f'表单状态：<{submit_form["stepId"]}> {str(resJson["ecode"])}\n'
            log += f'表单地址：{form_response.url}\n'
            print('\t表单地址: ' + form_response.url + '\n\n\t表单状态: \n\t\terrno：' + str(resJson['errno']) + '\n\t\tecode：' + str(
                resJson['ecode']) + '\n\t\tentities：' + str(resJson['entities']) + '\n\n\n\t完整返回：' + response_end.text)
        else:
            log += f'**今日打卡失败！**\n'
            log += f'错误编号：{str(resJson["ecode"])}\n'
            log += f'错误信息：{str(resJson["entities"])}\n'
            print('\t表单地址: ' + form_response.url + '\n\n\t错误信息: \n\t\terrno：' + str(resJson['errno']) + '\n\t\tecode：' + str(
                resJson['ecode']) + '\n\t\tentities：' + str(resJson['entities']) + '\n\n\n\t完整返回：' + response_end.text)
        ## 获取一言 Hitokoto
        htkt = getHito()
    except:
        log += f'{time.strftime("%H:%M:%S", time.localtime())} 运行出错！\n'
        err = traceback.format_exc()
        log += f'\t错误信息：{err}\n'
        print('\t脚本报错: \n\n\t' + err)
    finally:
        log += f'\n悄悄告诉你：{htkt}'
    return log

if __name__ == "__main__":
    config = getCfg("config.txt")  ## if you got `IndexError: list index out of range` check this path
    corpId = config[0]
    corpSecret = config[1]
    agentId = config[2]
    for i in range(int((len(config) - 4) / 6)):
        ckID = config[i*6+5]
        ckPass = config[i*6+6]
        ckBound = config[i*6+7]
        ckData = config[i*6+8]
        toUid = '@all' if (config[i*6+9] == '') else config[i*6+9]
        log = f'{time.strftime("%m 月 %d 日", time.localtime())}用户 {ckID} 平安行动运行日志\n\n'
        notification = checkin(ckID,ckPass,ckBound,ckData,log)
        sendNtf(notification,agentId,corpSecret,corpId,toUid)
        time.sleep(30)