import getCommentList
import getWeiBoInfo
import storage
import time

'''
weiboContent={
    "publishName":"发布者昵称",
    "publishId":"发布者id",
    "content":"微博文字内容",
    "imageList":["图片链接1","图片链接2","图片链接3"],
    "commentsNum":"评论数",
    "commentInfoList":commentList
}
commentList=[{
    "publishName":"评论者昵称",
    "publishId":"评论者Id",
    "content":"评论内容",
    "commentId":"评论id"
}]

'''

def run():
    commentList=getCommentList.getComment()
    weiboInfo=getWeiBoInfo.getWeiBoInfo()
    print(commentList)
    print(weiboInfo)
    weiboInfo["commentInfoList"]=commentList
    storage.save(weiboInfo,commentList)
    tmpNum=weiboInfo["commentsNum"]
    while True:
        time.sleep(5)
        weiboInfo = getWeiBoInfo.getWeiBoInfo()
        if weiboInfo["commentsNum"]!=tmpNum:
            commentList = getCommentList.getComment()
            weiboInfo["commentInfoList"] = commentList
            storage.save(weiboInfo,commentList)
            tmpNum=weiboInfo["commentsNum"]
        else:
            continue


if __name__ == '__main__':
    run()
