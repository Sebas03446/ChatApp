import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import declarative_base

sqlite_file_name = "../../db.sqlite"
base_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

database_url = f"sqlite:///{base_dir}/{sqlite_file_name}"


engine = create_engine(database_url, echo=True)

test_engine = create_engine(f"sqlite:///{base_dir}/test_{sqlite_file_name}", echo=True)

Test_session = sessionmaker(bind=test_engine)

Session = sessionmaker(bind=engine)

Base = declarative_base()