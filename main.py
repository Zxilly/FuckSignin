import requests

cookies = {
    "loginName": "",
    "loginType": "0",
    "yzxx": ""
}
signdata = {
    "province": "江西省",
    "city": "南昌市",
    "district": "",
    "street": "",
    "xszt": "0",
    "jkzk": "0",
    "jkzkxq": "",
    "sfgl": "1",
    "gldd": "",
    "mqtw": "0",
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
    "lng": "28.764745",
    "lat": "115.83801",
    "sfby": "1",
}

formdata = {
    "dcwj": '{"name":"%E5%91%A8%E6%98%95%E9%9B%A8","xb":"0","gtjzrysfyyshqzbl":"N","xzzdsfyyqfbqy":"N",'
            '"jqsfqwzdyq":"N","sfzyblbbdsq":"N","sfyhqzbljcs":"N","sfszsqjfjcxqz":"N","jrtw":"37","xcwz":"3",'
            '"sf":"0","stype":"0","xy":"'
            '","nj":"2019","bj":"","age":"18","lxdh":"17572693170","jjdh":"","sfz":"",'
            '"szd":"1","address":"","hbc":"K232","hjtgj":"0",'
            '"sffx":"1","jkzk":"0"}'
}


def get_auth():
    main_session = requests.session()
    main_session.get(
        "https://fxgl.jx.edu.cn/4136010419/third/alipayLogin?cardId="
        "&sfzMd5=") # 请自行抓包补上
    return main_session


def sign(session):
    sign_object = session.post("https://fxgl.jx.edu.cn/4136010419/studentQd/saveStu", cookies=cookies, data=signdata)
    print(sign_object.content.decode('utf-8'))


def form(session):
    form_object = session.post("https://fxgl.jx.edu.cn/4136010419/dcwjEditNew/dcwjSubmit2", cookies=cookies,
                               data=formdata)
    print(form_object.content.decode('utf-8'))


if __name__ == '__main__':
    session = get_auth()
    sign(session)
    form(session)
