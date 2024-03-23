import pymysql
import json
def save(weiboContent,commentList):
    # 连接数据库
    conn = pymysql.connect(host="localhost", user="guiying", password="Pw84489695", database="weibo2", charset="utf8mb4")
    # 创建游标
    cursor = conn.cursor()
    # 查询微博数据是否存在
    weibo_sql = "SELECT id FROM weibo WHERE publish_id=%s AND content=%s"
    weibo_params = (weiboContent['publishId'], weiboContent['content'])
    cursor.execute(weibo_sql, weibo_params)
    result = cursor.fetchone()

    if result:
        # 如果微博数据已存在，则执行更新操作
        weibo_id = result[0]
        try:
            # 将图片列表转换为JSON格式
            weiboContent['imageList'] = json.dumps(weiboContent['imageList'])
            # 构建更新微博表的SQL语句和参数
            weibo_update_sql = "UPDATE weibo SET image_list=%s, comments_num=%s WHERE id=%s"
            weibo_update_params = (weiboContent['imageList'], weiboContent['commentsNum'], weibo_id)
            # 执行SQL语句
            cursor.execute(weibo_update_sql, weibo_update_params)
            # 删除原有评论数据
            comment_delete_sql = "DELETE FROM comment WHERE weibo_id=%s"
            comment_delete_params = (weibo_id,)
            cursor.execute(comment_delete_sql, comment_delete_params)
            # 插入新的评论数据
            for comment in commentList:
                # 构建插入评论表的SQL语句和参数
                comment_sql = "INSERT INTO comment (weibo_id, publish_name, publish_id, content, created_at) VALUES (%s, %s, %s, %s, NOW())"
                comment_params = (weibo_id, comment['publishName'], comment['publishId'], comment['content'])
                # 执行SQL语句
                cursor.execute(comment_sql, comment_params)
            # 提交事务
            conn.commit()
            print("Update data successfully!")
        except Exception as e:
            # 发生异常时回滚事务
            conn.rollback()
            print("Update data failed:", e)
    else:
        # 如果微博数据不存在，则执行插入操作
        try:
            # 将图片列表转换为JSON格式
            weiboContent['imageList'] = json.dumps(weiboContent['imageList'])
            # 构建插入微博表的SQL语句和参数
            weibo_insert_sql = "INSERT INTO weibo (publish_name, publish_id, content, image_list, comments_num, created_at) VALUES (%s, %s, %s, %s, %s, NOW())"
            weibo_insert_params = (
            weiboContent['publishName'], weiboContent['publishId'], weiboContent['content'], weiboContent['imageList'],
            weiboContent['commentsNum'])
            # 执行SQL语句
            cursor.execute(weibo_insert_sql, weibo_insert_params)
            # 获取插入的微博id
            weibo_id = cursor.lastrowid
            # 插入评论数据
            for comment in commentList:
                # 构建插入评论表的SQL语句和参数
                comment_sql = "INSERT INTO comment (weibo_id, publish_name, publish_id, content, created_at) VALUES (%s, %s, %s, %s, NOW())"
                comment_params = (weibo_id, comment['publishName'], comment['publishId'], comment['content'])
                # 执行SQL语句
                cursor.execute(comment_sql, comment_params)
            # 提交事务
            conn.commit()
            print("Insert data successfully!")
        except Exception as e:
            # 发生异常时回滚事务
            conn.rollback()
            print("Insert data failed:", e)

    # 关闭数据库连接
    cursor.close()
    conn.close()
