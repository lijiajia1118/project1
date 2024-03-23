import requests
import json

def getComment():
    url="https://weibo.com/ajax/statuses/buildComments?is_reload=1&id=4904266818914021&is_show_bulletin=2&is_mix=0&count=10&uid=7827405799&fetch_level=0"
    # url="https://weibo.com/ajax/statuses/buildComments?is_reload=1&id=4903775716771532&is_show_bulletin=2&is_mix=0&count=10&uid=5044281310&fetch_level=0"
    '''
    headers={
        'Authority':'weibo.com',
        'Method':'GET',
        # 'Path':'/ajax/statuses/buildComments?is_reload=1&id=4904266818914021&is_show_bulletin=2&is_mix=0&count=10&uid=7827405799&fetch_level=0',
        'Scheme':'https',
        'Accept':'application/json, text/plain, */*',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Client-Version':'v2.40.54',
        # 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        # "Cookie": "XSRF-TOKEN=ZwIwpdYCpWjVfIXxv3geuN2A; SUB=_2A25JbpXODeRhGeFM6lYV-CrEzj6IHXVqHYAGrDV8PUNbmtAGLVTEkW9NQPKfaRaoFng4EWmPQBlzUHwrFhM1mdLU; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWEH9fOKyadefAgnbxf9DX-5JpX5KzhUgL.FoMEeKBX1hBRSKz2dJLoI7UNIsyrdJUX; WBPSESS=m9ZQ_rIYXHCLmRBLonq-nSjeZw6R6XjlINnjVw16D7N72h2Tze1a8JdRUw2ad9CR6G4dAR1iA1S-00gwpoFUabEEEyfO5n7vV0_4cl6DULJnuQRJn37jvPchn8kxw1EbZ43nDht9zjXmpMvZOX7FrQ==; ALF=1716263197; SSOLoginState=1684727198",
        "Cookie":"SINAGLOBAL=3515970433579.552.1634092726310; UOR=,,www.baidu.com; wb_view_log=1536*8641.25; XSRF-TOKEN=6oyuKgD8zK80EgY1iZjS2Fwd; PC_TOKEN=dd1bc2589c; login_sid_t=31af0fd0f113cd503db94154bbb4c38a; cross_origin_proto=SSL; WBStorage=4d96c54e|undefined; _s_tentry=weibo.com; Apache=4732756149889.814.1684761567591; ULV=1684761567594:11:2:2:4732756149889.814.1684761567591:1684734482214; SSOLoginState=1684761586; SCF=AtcSR7K2wDtNNsFCrPbUq5j7pzPhDfhroRd9HHaDUwUGrcJEVqSoBOBr0WTi2Iw3oj7a0Q-eUdQSR8dOEyrqBug.; SUB=_2A25JbxuiDeRhGeBI7lMX-CjEwz6IHXVqHQpqrDV8PUNbmtAGLRPlkW9NRpD6GhzbztNwRiUQJGgQ5xtOtyT_FoiT; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFfQFXznYpU.ANoI2iLqsdz5JpX5KzhUgL.FoqcSK2c1hqR1hz2dJLoIXBLxK-L12BL1KqLxK-LBK-LBoeLxK-LB-BLBK.LxKML1-2L1hBLxK-LBo5L12qLxKML1h2LB-zLxKqL1-qLBoBES0n7eBtt; ALF=1716297585; WBPSESS=Dt2hbAUaXfkVprjyrAZT_OWkDu22w5KOE1ehUIO1Kq9TmxnEGEsez3IqXtvSoFP7FNQPsgYLeuzs9WIDhgPeCcm1elH74ccGEn1LdUHIraSyuzTjHLSTFe126djAYsd-4tlxgTW3s0IFgrbkmXXYFoJ3o0WFmbHkVaiuZr90McphayUySvRj2_jzNhplG73iDev-t36cfbZ4sdGrF4KmzQ==",
        # 'Referer':'https://weibo.com/7827405799/N1MZXBoWx',
        'Sec-Ch-Ua':'"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'Sec-Ch-Ua-Mobile':'?0',
        "Sec-Ch-Ua-Platform":'Windows',
        "Sec-Fetch-Dest":'empty',
        "Sec-Fetch-Mode":'cors',
        "Sec-Fetch-Site":'same-origin',
        "Server-Version":'v2023.05.17.1',
        "Traceparent":'00-5444eb559fab0d92796c24af81a9270e-a671efc49a9f9809-00',
        "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        "X-Requested-With":"XMLHttpRequest",
        "X-Xsrf-Token":"6oyuKgD8zK80EgY1iZjS2Fwd"
    }
    '''
    # res=requests.get(url,headers)
    res=requests.get(url)
    # print(res)
    html=res.content.decode()
    # print(html)


    js=json.loads(html)
    # print(js)

    commentList=[]
    for i in js["data"]:
        commentList.append({
            "publishName": i["user"]["screen_name"],
            "publishId": i["user"]["id"],
            "content": i["text_raw"],
            "commentId": i["id"]
        })

    # for comment in commentList:
    #     print(comment)
    # print(commentList)
    return commentList


'''
commentList=[{
    "publishName":"评论者昵称",
    "publishId":"评论者Id",
    "content":"评论内容",
    "commentId":"评论id"
}]


'''