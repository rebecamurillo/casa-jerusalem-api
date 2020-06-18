#postgresql init
# coding=utf-8
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Engine = create_engine('postgresql://postgresdev:postgresdev@localhost:5433/casajerusalem')
Session = sessionmaker(bind=Engine)
Base = declarative_base()
