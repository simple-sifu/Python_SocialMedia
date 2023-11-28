from fastapi import FastAPI
from storeapi.routers.post import router as post_router
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()

app.include_router(post_router)

conn_string = (
    f"mysql+pymysql://{'root'}:{'adomoleole'}"
    f"@{'dev-ngtommyhan.own-backup-dev.com'}:{'3306'}/{'ownbackup'}"
)

# Create an SQLAlchemy engine
engine = create_engine(conn_string, pool_pre_ping=True, pool_recycle=300)

# Create a session factory
Session = sessionmaker(bind=engine)

# Create a declarative base
Base = declarative_base()


# Define a sample model
class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    default_subtitle = Column(String(length=50), unique=True, index=True)
    displayed_name = Column(String(length=100), unique=True, index=True)


# Create tables
Base.metadata.create_all(bind=engine)

# Create a session
session = Session()

# Example of adding a user
# new_user = User(username="john_doe", email="john@example.com")
# session.add(new_user)
# session.commit()

# Example of querying all users
services = session.query(Service).all()
for service in services:
    print(
        f"Service ID: {service.id}, SubTitle: {service.default_subtitle}, Name: {service.displayed_name}"
    )

# Close the session
session.close()
