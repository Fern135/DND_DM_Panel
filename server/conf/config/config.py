from dotenv import load_dotenv
import os

# Load variables from the .env file into os.environ
load_dotenv()

class Config:
    # General Configurations
    DEBUG           = True
    host            = '127.0.0.1'
    API_PORT        = 8000
    WEB_SOCKET_PORT = 9000 # for handling communication between server and client
    secret_key      = os.getenv("SECRET_KEY")

    # database
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{passwd}@{url}/

    db_sql = {
        "host"      : os.getenv("db_host"),
        "user"      : os.getenv("db_user_name"),
        "password"  : os.getenv("db_password"),
        "name"      : os.getenv("db_name")
    }