import json
import os

import requests

def get_auth(
        url="https://fxgl.jx.edu.cn/4136010419/third/alipayLogin?cardId=&sfzMd5="):  # 请自行抓包补上支付宝cardid，后面那个诡异变量不会变的，我猜是身份证MD5
    main_session = requests.session()
    main_session.get(url)
    return main_session


def sign(session):
    sign_object = session.post("https://fxgl.jx.edu.cn/4136010419/studentQd/saveStu", cookies=cookies, data=signdata)
    print(sign_object.content.decode('utf-8'))


def form(session):
    form_object = session.post("https://fxgl.jx.edu.cn/4136010419/dcwjEditNew/dcwjSubmit2", cookies=cookies,
                               data=formdata)
    print(form_object.content.decode('utf-8'))


if __name__ == '__main__':
    if not os.getenv('CI'):
        cookies = {
            "loginName": "",
            "loginType": "0",
            "yzxx": ""
        }  # name学号，密码疑似统一111111
        signdata = {
            "province": "",
            "city": "",
            "district": "",
            "street": "",
            "xszt": "",
            "jkzk": "",
            "jkzkxq": "",
            "sfgl": "",
            "gldd": "",
            "mqtw": "",
            "mqtwxq": "",
            "zddlwz": "",
            "sddlwz": "",
            "bprovince": "",
            "bcity": "",
            "bdistrict": "",
            "bstreet": "",
            "sprovince": "",
            "scity": "",
            "sdistrict": "",
            "lng": "",
            "lat": "",
            "sfby": "",
        }  # 随便填，估计提交上去也没人看
        formdata = {
            "dcwj": ''
        }  # 随便填，估计提交上去也没人看
        session = get_auth()
        sign(session)
        form(session)
    else:
        url = os.getenv('URL')
        cookies = json.loads(os.getenv('COOKIES'))
        signdata = json.loads(os.getenv('SIGNDATA'))
        formdata = {"dcwj": os.getenv('FORMDATA')}

        session = get_auth(url)
        sign(session)
        form(session)
