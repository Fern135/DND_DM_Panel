from dotenv import load_dotenv
import os

# Load variables from the .env file into os.environ
load_dotenv()

HTTP_CODES = {
    100: "Continue",
    101: "Switching Protocols",
    102: "Processing",
    103: "Early Hints",
    200: "OK",
    201: "Created",
    202: "Accepted",
    203: "Non-Authoritative Information",
    204: "No Content",
    205: "Reset Content",
    206: "Partial Content",
    207: "Multi-Status",
    208: "Already Reported",
    226: "IM Used",
    300: "Multiple Choices",
    301: "Moved Permanently",
    302: "Found",
    303: "See Other",
    304: "Not Modified",
    305: "Use Proxy",
    307: "Temporary Redirect",
    308: "Permanent Redirect",
    400: "Bad Request",
    401: "Unauthorized",
    402: "Payment Required",
    403: "Forbidden",
    404: "Not Found",
    405: "Method Not Allowed",
    406: "Not Acceptable",
    407: "Proxy Authentication Required",
    408: "Request Timeout",
    409: "Conflict",
    410: "Gone",
    411: "Length Required",
    412: "Precondition Failed",
    413: "Payload Too Large",
    414: "URI Too Long",
    415: "Unsupported Media Type",
    416: "Range Not Satisfiable",
    417: "Expectation Failed",
    418: "I'm a teapot",
    421: "Misdirected Request",
    422: "Unprocessable Entity",
    423: "Locked",
    424: "Failed Dependency",
    425: "Too Early",
    426: "Upgrade Required",
    428: "Precondition Required",
    429: "Too Many Requests",
    431: "Request Header Fields Too Large",
    451: "Unavailable For Legal Reasons",
    500: "Internal Server Error",
    501: "Not Implemented",
    502: "Bad Gateway",
    503: "Service Unavailable",
    504: "Gateway Timeout",
    505: "HTTP Version Not Supported",
    506: "Variant Also Negotiates",
    507: "Insufficient Storage",
    508: "Loop Detected",
    510: "Not Extended",
    511: "Network Authentication Required",
}

def get_codes(code):
    return HTTP_CODES.get(code, "Unknown")

class Config:
    # General Configurations
    DEBUG           = True
    host            = '127.0.0.1'
    API_PORT        = 8000
    WEB_SOCKET_PORT = 9000 # for handling communication between server and client
    secret_key      = os.getenv("SECRET_KEY")

    # name of db. 
    DB_NAME = "DND_PANEL"

    # default db_return
    db_return_title = "Server"

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