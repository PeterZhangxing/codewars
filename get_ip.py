#!/usr/bin/python3.5

import sys,os,urllib.request,json,re

def ip_check(ip_addr):
    ip_exp = re.compile(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
    if ip_exp.match(ip_addr):
        return True
    else:
        return False

def get_ip_location(ip_addr):
    try:
        apiurl = "http://ip.taobao.com/service/getIpInfo.php?ip=%s" %ip_addr
        content = urllib.request.urlopen(apiurl).read().decode("utf-8")
        """
        {"code":0,"data":{"ip":"39.130.109.212","country":"中国","area":"","region":"云南",
        "city":"昆明","county":"XX","isp":"移动","country_id":"CN","area_id":"",
        "region_id":"530000","city_id":"530100","county_id":"xx","isp_id":"100025"}}
        """
        # print(content)

        data = json.loads(content)['data']
        code = json.loads(content)['code']

        if code == 0:
            print("Ip_address : ",data["ip"])
            print("Country : ",data["country"])
            print("Region : ",data["region"])
            print("City : ",data["city"])
            print("ISP : ",data["isp"])
            print("Country_id : ",data["country_id"])
        else:
            print(data)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    while True:
        ip_addr = input("Please input valid ipv4 address>>>:")

        if ip_addr == "exit" or ip_addr == "quit" or ip_addr == "Q":
            exit("Already quited from this programme!")

        if ip_check(ip_addr):
            get_ip_location(ip_addr)
        else:
            print("Invalid ipput,try again!")
