
DBUG = True

DIALECT ='mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = 'gx123456' # 此处填写你的数据库密码
HOST = 'localhost' # 部署到服务器不能用127.0.0.1 得用localhost
PORT = '3306'
DATABSE = 'gcat' # 此处为你建的数据库的名称
SQLALCHEMY_DATABASE_URI ="{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABSE)

SQLALCHEMY_TRACK_MODIFICATIONS = False