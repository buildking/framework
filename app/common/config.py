from dataclasses import dataclass, asdict
from os import path, environ

base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))


@dataclass
class Config:
    """
    기본 Configuration
    """
    BASE_DIR = base_dir

    DB_POOL_RECYCLE: int = 900
    DB_ECHO: bool = True


@dataclass
class LocalConfig(Config):
    PROJ_RELOAD: bool = True
    DB_URL: str = "mysql+pymysql://auth_test@localhost:3306/notification_api?charset=utf8mb4"
    #mysql+pymysql://[계정ID]:[패스워드]@[DB접속 IP]:[포트]/[DB명(schema)]]?charset=utf8mb4


@dataclass
class ProdConfig(Config):
    PROJ_RELOAD: bool = False


#####수업진행
def abc(DB_ECHO=None, DB_POOL_RECYCLE=None, **kwargs):
    print(DB_ECHO, DB_POOL_RECYCLE)
arg = asdict(LocalConfig())
abc(**arg)
# abc(DB_POOL_RECYCLE=900, DB_ECHO=True)
# print(LocalConfig().DB_ECHO)
#####


def conf():
    """
    환경 불러오기
    :return:
    """
    config = dict(prod=ProdConfig(), local=LocalConfig())
    return config.get(environ.get("API_ENV", "local"))
