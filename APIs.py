# -*- coding: utf-8 -*-

import requests
import json
import re
from bs4 import BeautifulSoup as bs


class Spiders(object):
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                                      ' (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        self.headers_m = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 '
                                        '(KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'}


    # 形成富文本，参数是文本内容和字体颜色
    def getmsg(self,themsg,thecolor):
        msg = '<html><head/><body><p><span style=" font-family:Microsoft YaHei;font-size:9pt; color:{};">{}</span></p></body></html>'.format(thecolor,themsg)
        return msg

    # 从文件读取信息，返回一个列表
    def get_Infos(self, filename):
        Infos = []
        with open(filename, 'r') as f:
            data = f.readlines()
        for each in data:
            if len(each.strip()) > 0:
                Infos.append(each.strip())
        return Infos

    # 获取单个天猫商品DSR
    def get_TM(self, id, outfile):
        url = 'https://dsr-rate.tmall.com/list_dsr_info.htm?itemId=%s' % id
        res = requests.get(url, headers=self.headers)
        html = res.text
        date = re.findall('json.*?\((.*)\)', html)[0]
        dsr = json.loads(date)['dsr']  # 转换成字典格式
        DSR = id + ',' + str(dsr['gradeAvg']).strip() + ',' + str(dsr['rateTotal']).strip()
        with open(outfile, 'a') as f:
            f.write(DSR + '\n')
        return

    # 获取单个京东商品DSR
    def get_JD(self, id, outfile):
        url = 'https://club.jd.com/comment/productCommentSummaries.action?referenceIds=%s' % id
        res = requests.get(url, headers=self.headers)
        html = res.text
        dic = json.loads(html)['CommentsCount'][0]
        SkuId = str(dic['SkuId']).strip()  # 商品ID
        GoodRate = str(dic['GoodRate']).strip()  # 好评率
        GoodCount = str(dic['GoodCount']).strip()  # 好评数
        GeneralCount = str(dic['GeneralCount']).strip()  # 中评数
        PoorCount = str(dic['PoorCount']).strip()  # 差评数
        DSR = SkuId + ',' + GoodRate + ',' + GoodCount + ',' + GeneralCount + ',' + PoorCount
        with open(outfile, 'a') as f:
            f.write(DSR + '\n')
        return

    # 获取天猫主图链接和价格
    def getimglink(self, ID, outfile):
        # 打开手机端网页
        url = "https://detail.m.tmall.com/item.htm?id={}".format(ID)
        html = requests.get(url, headers=self.headers_m).text
        try:
            soup = bs(html, "lxml")
            imglink = "https:" + soup.select("div.itbox > a > img")[0].get("src")
        except:
            imglink = "miss"
        infos = re.findall('"price":"(\d+?\.\d\d)"', html)
        try:
            maxprice = max(list(map(float, infos)))
            minprice = min(list(map(float, infos)))
        except ValueError:
            maxprice = max(infos)
            minprice = min(infos)
        except:
            maxprice = "miss"
            minprice = "miss"
        thestr = ",".join([str(ID), imglink, str(maxprice), str(minprice)])
        with open(outfile, "a") as f:
            f.write(thestr + "\n")

    # 下载图片
    def downimg(self, savefile, savename, url):
        item = requests.get(url, headers=self.headers).content
        Imgname = savefile + '\\' + savename + '.jpg'
        with open(Imgname, 'wb') as f:
            f.write(item)
        return