import  pymysql


class database:
# 实现python链接MySQL服务器
    def __init__(self):
           self.con = pymysql.connect(host='localhost',
                              port=3306,
                              user='root',
                              password='123456',
                              database='test',
                              charset="utf8",
                              # 游标类型，默认是元组，当前语句是指定为字典游标，控制查询结果的显示数据类型
                               cursorclass=pymysql.cursors.DictCursor
                             )
           #通过上一步创建的数据库连接的对象来创建游标
           self.cur = self.con.cursor()
    #通过游标来执行MYsql命令
    def select_sql_excute(self,sql,query_key):
            self.info =  self.cur.execute(sql)
            self.result = self.info.get(query_key)
            #断开连接
            self.con.close()
            return self.result
            # cur.fetchall()
            # cur.fetchmany()
# 提交数据的修改
# self.con.commit()