import requests
import json
def getWeiBoInfo():
    url="https://weibo.com/ajax/statuses/show?id=N1MZXBoWx"
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        # "Cookie": "XSRF-TOKEN=ZwIwpdYCpWjVfIXxv3geuN2A; SUB=_2A25JbpXODeRhGeFM6lYV-CrEzj6IHXVqHYAGrDV8PUNbmtAGLVTEkW9NQPKfaRaoFng4EWmPQBlzUHwrFhM1mdLU; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWEH9fOKyadefAgnbxf9DX-5JpX5KzhUgL.FoMEeKBX1hBRSKz2dJLoI7UNIsyrdJUX; WBPSESS=m9ZQ_rIYXHCLmRBLonq-nSjeZw6R6XjlINnjVw16D7N72h2Tze1a8JdRUw2ad9CR6G4dAR1iA1S-00gwpoFUabEEEyfO5n7vV0_4cl6DULJnuQRJn37jvPchn8kxw1EbZ43nDht9zjXmpMvZOX7FrQ==; ALF=1716263197; SSOLoginState=1684727198",
        "Cookie":"SINAGLOBAL=3515970433579.552.1634092726310; UOR=,,www.baidu.com; wb_view_log=1536*8641.25; ULV=1684734482214:10:1:1:9103076245110.465.1684734482211:1654498708230; XSRF-TOKEN=6oyuKgD8zK80EgY1iZjS2Fwd; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFfQFXznYpU.ANoI2iLqsdz5JpX5KMhUgL.FoqcSK2c1hqR1hz2dJLoIXBLxK-L12BL1KqLxK-LBK-LBoeLxK-LB-BLBK.LxKML1-2L1hBLxK-LBo5L12qLxKML1h2LB-zLxKqL1-qLBoBES0n7eBtt; ALF=1687334897; SSOLoginState=1684742898; SCF=AtcSR7K2wDtNNsFCrPbUq5j7pzPhDfhroRd9HHaDUwUGYUYnJRwzDlVQQDrrQlge0lGRH1Z4z28Rpv4cGYu3i6w.; SUB=_2A25Jb1KiDeRhGeBI7lMX-CjEwz6IHXVqHcNqrDV8PUNbmtAGLVnVkW9NRpD6Gn8B30zL__HYTP9Ua4uZkcv1tEmQ; WBPSESS=RZFsVNJpYlz-VyF3Q7-hYrkvwWGZkPFgBfRw1xZjgU5-dNFRU157h8TCcbPYa142-6SDA1pajGMTWTktLgWPM06Hm-qq4HjYNPIb5DkjBzuhvSpCW35_6-fxijcmzV77DCx7_BWwzefogEiLVRWt_Q=="

    }

    res=requests.get(url,headers)
    html=res.content.decode()
    # print(res)
    # print(html)

    js=json.loads(html)
    # print(js["pic_focus_point"])
    llist=["https://wx4.sinaimg.cn/orj360/"+i["pic_id"]+".jpg" for i in js["pic_focus_point"]]
    # print(llist)
    # llist=["https://wx4.sinaimg.cn/orj360/008xIZODgy1he7cd46lbsj31400u0qbm.jpg"]
    weiboContent={
        "publishName":js["user"]["screen_name"],
        "publishId":js["user"]["id"],
        "content":js["text_raw"],
        "imageList":llist,
        "commentsNum":js["comments_count"]
    }
    # print(weiboContent)
    return weiboContent

'''
weiboContent={
    "publishName":"发布者昵称",
    "publishId":"发布者id",
    "content":"微博文字内容",
    "imageList":["图片链接1","图片链接2","图片链接3"],
    "commentsNum":"评论数"
}

'''