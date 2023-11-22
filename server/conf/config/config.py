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

    DB_NAME = "DND_PANEL"

    # database
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{passwd}@{url}/

    databases = {
        "mysql": 
            {
                "host"     : os.getenv("db_host"),
                "user"     : os.getenv("db_user_name"),
                "password" : os.getenv("db_password"),
                "name"     : os.getenv("db_name")
        },
        "sqlite3" : f"../../database/{DB_NAME}.sqlite3",
        "mongoDB" : {
            "host"      : os.getenv("mongoDB_HOST"),
            "port"      : os.getenv("mongoDB_PORT"),
            "db_name"   : os.getenv("mongoDB_DB_NAME"),
        }
        
    }