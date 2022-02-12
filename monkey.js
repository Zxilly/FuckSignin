// ==UserScript==
// @name         JGSU 补签到
// @version      0.0.1
// @description  井冈山大学疫情签到补签到
// @namespace    Zxneric
// @author       Zxneric
// @match        *://ehall.jgsu.edu.cn/*
// @grant        none
// @license      MIT
// ==/UserScript==

(function () {
    'use strict';
    window.sign = function () {
        const days_need_submit = []

        const stu_name = 'QaQ' // 替换为姓名
        const stu_code = '1234' // 替换为学号

        if (stu_name === 'QaQ' || stu_code === '1234') {
            alert('请先替换姓名和学号')
            return
        }

        let data_fill_flag = false
        const sub_data = {
            "SFHBRYJCS_DISPLAY": "否",
            "SZD": "",
            "SFHBRYJCS": "0",
            "SZD_DISPLAY": "",
            "SFYSQZJCS": "0",
            "SFYSQZ_DISPLAY": "否",
            "TXRQ": "",
            "XSBH": "",
            "CZZ": "",
            "DDYMT": "3",
            "DDYMT_DISPLAY": "绿码",
            "CZRQ": "Feb 12, 2022 10:44:15 PM",
            "TW": "36",
            "SFYSQZ": "0",
            "WID": "",
            "SFSTBS": "0",
            "CZZXM": "",
            "DKDW": "",
            "SFYSQZJCS_DISPLAY": "否",
            "SFSTBS_DISPLAY": "否",
            "SFSTBSQKSM": "",
            "SFHBRYJCSQKSM": "",
            "SFYSQZJCSQKSM": "",
            "SFYSQZQKSM": ""
        }

        fetch("https://ehall.jgsu.edu.cn/xsfw/sys/swmlsfxyqtbjgsu/modules/xssq/getMrtbxx.do", {
            "headers": {
                "accept": "application/json, text/plain, */*",
                "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                "cache-control": "no-cache",
                "content-type": "application/x-www-form-urlencoded",
                "pragma": "no-cache",
                "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"98\", \"Microsoft Edge\";v=\"98\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin"
            },
            "referrer": "https://ehall.jgsu.edu.cn/xsfw/sys/swmlsfxyqtbjgsu/*default/index.do",
            "referrerPolicy": "strict-origin-when-cross-origin",
            "body": "data=%7B%7D",
            "method": "POST",
            "mode": "cors",
            "credentials": "include"
        }).then((resp) => {
            return resp.json()
        }).then((data) => {
            const cus = data.data;
            for (let i = 0; i < cus.length; i++) {
                if (!("WID" in cus[i])) {
                    const rq = cus[i]['RQ']
                    days_need_submit.push(rq)
                } else {
                    if (!data_fill_flag) {
                        data_fill_flag = true

                        const loc_str = cus[i]['SZD_DISPLAY']
                        const loc_code = cus[i]['SZD']
                        sub_data['SZD_DISPLAY'] = loc_str
                        sub_data['SZD'] = loc_code

                        sub_data['CZZ'] = stu_code
                        sub_data['XSBH'] = stu_code
                        sub_data['CZZXM'] = stu_name
                    }
                }
            }
            for (const day of days_need_submit) {
                sub_data['TXRQ'] = day
                fetch("https://ehall.jgsu.edu.cn/xsfw/sys/swmlsfxyqtbjgsu/modules/xssq/savaStuMrqk.do", {
                    "headers": {
                        "accept": "application/json, text/plain, */*",
                        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                        "cache-control": "no-cache",
                        "content-type": "application/x-www-form-urlencoded",
                        "pragma": "no-cache",
                        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"98\", \"Microsoft Edge\";v=\"98\"",
                        "sec-ch-ua-mobile": "?0",
                        "sec-ch-ua-platform": "\"Windows\"",
                        "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "same-origin"
                    },
                    "referrer": "https://ehall.jgsu.edu.cn/xsfw/sys/swmlsfxyqtbjgsu/*default/index.do",
                    "referrerPolicy": "strict-origin-when-cross-origin",
                    "body": "data=" + encodeURIComponent(JSON.stringify(sub_data)),
                    "method": "POST",
                    "mode": "cors",
                    "credentials": "include"
                });
            }
        })
    }
})();