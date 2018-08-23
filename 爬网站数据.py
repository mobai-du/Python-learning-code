#!/usr/bin/env python
# @-_-@ coding:utf-8 @-_-@
# Author:warm sun
import xlsxwriter
import requests,json
import re
from pyquery import PyQuery as pq

rowl = 0
workbook = xlsxwriter.Workbook('用户信息''.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(rowl,0,'电话号码')
worksheet.write(rowl,1,'姓名')

login_url = 'https://mis.mo9.com/a/login'
headers = {
    "Accept":"5.0 (Windows NT 6.1; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Cache-Control":"max-age=0",
    "Connection":"keep-alive",
    "Host":"mis.mo9.com",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"5.0 (Windows NT 6.1; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0",
}
headers2 = {
    "Accept":"5.0 (Windows NT 6.1; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2"	,
    "Connection":"keep-alive",
    "Content-Length":"404",
    "Content-Type":"application/x-www-form-urlencoded",
    "Host":"mis.mo9.com",
    "Referer":"https://mis.mo9.com/a/dunning/tMisDunningTask/findOrderPageList?tabPageId=jerichotabiframe_0",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"5.0 (Windows NT 6.1; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0",
}
paseSize = int(input("请输入你查询的总数量:"))
data={
    "pageNo":1,
    "pageSize":paseSize,
    "realname":"",
    "mobile":"",
    "dealcode":"",
    "platformExt":"",
    "telremark":"",
    "status":"payment",
    "beginOverduedays":"",
    "endOverduedays":"",
    "beginPayofftime":"",
    "endPayofftime":"",
    "beginRepaymenttime":"",
    "endRepaymenttime":"",
    "beginpromisepaydate":"",
    "endpromisepaydate":"",
    "beginnextfollowdate":"",
    "endnextfollowdate":"",
    "groupType":"",
    "groupIds":"",
    "dunningPeople.queryIds":"",
    "beginDunningtime":"",
    "endDunningtime":"",
    "beginlatestlogintime":"",
    "endlatestlogintime":"",
    "actionCode":"",
}
session = requests.session()
r1 = session.get(login_url,headers=headers)
r2 = session.post(login_url,data={'username':'juce1','password':'123$%^'})
cookies1=r1.cookies.get_dict()
r3 = session.post('https://mis.mo9.com/a/dunning/tMisDunningTask/findOrderPageList',
                  headers=headers2,
                  cookies=cookies1,data=data)
html = pq(r3.text)
f1 = html.find("a[target=_blank]")
f2 = html.find("input[name=orders]")
user = f1.text()
f2 = str(f2)
user=str(user)
pattern = re.compile('<input.*?value="\d+#.*?#(\d+)"/',re.S)
items = re.findall(pattern,f2)

pattern2 = re.compile("\S+")
user = re.findall(pattern2,user)
print(items,user)
for i in items:
    rowl+=1
    worksheet.write(rowl, 0, i)

rowl=0
for i in user:
    rowl+=1
    worksheet.write(rowl, 1, i)

workbook.close()

