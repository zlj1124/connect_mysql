import MySQLdb

class MysqlSerch(object):

    def __init__(self):
        self.get_conn()
    def get_conn(self):
        try:
            self.conn=MySQLdb.connect(
                host='127.0.0.1',
                user ='root',
                passwd='123456',
                db='school',
                port=3306,
                charset='utf8'
            )
        except MySQLdb.Error as e:
            print('Error:%s'%e)    
          
             
            
    def close_conn(self):
        try:
            if self.conn:
                #  关闭连接
                self.conn.close()

        except MySQLdb.Error as e:
            print('Error:%s'%e)

    def add_one(self):
        #    准备sql
        sql=(
            "INSERT INTO `studants` (`name`,`nickname`,`sex`) VALUE"
            " (%s,%s,%s);"
        )
        #    获取连接和cursor
        cursor=self.conn.cursor()
        #    提交数据到数据库
        cursor.execute(sql,('张扬','bf','男'))
        #    提交事务
        self.conn.commit()
        #    关闭cursor和连接
        cursor.close()
        self.close_conn()


    def get_noe(self):
        # 准备sql
        sql= 'SELECT * FROM `studants` WHERE `sex`=%s;'       
        # 找到cursor
        cursor=self.conn.cursor()
        # 执行sql
        cursor.execute(sql,('女',))
        # 拿到结果
        rest=cursor.fetchone()
        # 处理数据
        r=dict(zip([k[0] for k in cursor.description],rest))
      
        # 关闭cursor/连接
        cursor.close()
        self.close_conn()
        return r

    def get_more(self):
        # 准备sql
        sql= 'SELECT * FROM `studants` ;'       
        # 找到cursor
        cursor=self.conn.cursor()
        # 执行sql
        cursor.execute(sql)
        # 拿到结果
        rest=cursor.fetchall()
        # 处理数据
        r=[dict(zip([k[0] for k in cursor.description],row))
        for row in rest]
      
        # 关闭cursor/连接
        cursor.close()
        self.close_conn()
        return r

           
if __name__ == "__main__":
    obj=MysqlSerch()
    # rest=obj.get_noe()
    # print(rest['name'])

    # rest1=obj.get_more()
    # for item in rest1:
    #     print(item)
    #     print("*"*20)
    
    obj.add_one()