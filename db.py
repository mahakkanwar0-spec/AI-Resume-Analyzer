from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

DATABASE_URL="mysql+pymysql://2aB6tBZCH7kTuw3.root:Bhel4fhL60vBzsUa@gateway01.ap-southeast-1.prod.aws.tidbcloud.com:4000/test?ssl_ca=C:\\tidb\\isrgrootx1.pem&ssl_verify_cert=true&ssl_verify_identity=true"

engine=create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    connect_args={
        "ssl":{
            "ssl":True
        }
    }
)

SessionLocal=sessionmaker(bind=engine)
Base=declarative_base()
