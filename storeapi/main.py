from fastapi import FastAPI
from storeapi.routers.post import router as post_router
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, BigInteger, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from faker import Faker
from datetime import datetime


app = FastAPI()

app.include_router(post_router)

# Replace these values with your MariaDB connection details
db_config = {
    'host': 'your_host',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'your_database',
}

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
class Section(Base):
    __tablename__ = "sections"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    service_id = Column(Integer)
    name = Column(String(255, collation='utf8_unicode_ci'))
    num_items = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    displayed_name = Column(String(255, collation='utf8_unicode_ci'))
    backup_id = Column(Integer, default=0)
    position = Column(Integer, default=0)
    num_api_calls = Column(Integer)
    status = Column(String(255, collation='utf8_unicode_ci'))
    message = Column(Text(collation='utf8_unicode_ci'))
    size = Column(BigInteger, default=0)
    num_updated_items = Column(Integer)
    updated_size = Column(BigInteger, default=0)
    num_deleted_items = Column(Integer)
    backup_method = Column(String(1, collation='utf8_unicode_ci'), default='F')
    num_inserted_items = Column(Integer)
    inserted_size = Column(BigInteger, default=0)
    deleted_size = Column(BigInteger, default=0)
    items_filename = Column(String(255, collation='utf8_unicode_ci'))
    inserted_items_filename = Column(String(255, collation='utf8_unicode_ci'))
    deleted_items_filename = Column(String(255, collation='utf8_unicode_ci'))
    updated_items_filename = Column(String(255, collation='utf8_unicode_ci'))
    overwritten_items_filename = Column(String(255, collation='utf8_unicode_ci'))
    num_second_api_calls = Column(Integer)
    num_third_api_calls = Column(Integer)
    binaries_size = Column(BigInteger)
    items_size = Column(BigInteger)
    started_at = Column(DateTime)
    completed_at = Column(DateTime)
    parent_section_id = Column(Integer)
    display_group_id = Column(String(255, collation='utf8_unicode_ci'))


    # Ensure uniqueness of column1 and column2
    __table_args__ = (UniqueConstraint('id', 'service_id'),)

# Create tables
Base.metadata.create_all(bind=engine)

# Create a session
session = Session()

# Example of adding a user
# new_user = User(username="john_doe", email="john@example.com")
# session.add(new_user)
# session.commit()

# Use Faker to generate fake data
fake = Faker()

# Generate and insert fake data into the table
num_fake_records = 5  # Change this value based on your needs
fake_records = []

for _ in range(num_fake_records):
    fake_data = {
        'id': fake.random_int(min=1000000, max=9000000),
        'service_id': fake.random_int(min=1000000, max=9000000),
        'name': fake.word(),
        'num_items': fake.random_int(min=1, max=100),
        'created_at': datetime.now(),
        'updated_at': fake.date_time_this_year(),
        'displayed_name': fake.word(),
        'status': fake.word(),
        'message': fake.text(),
        'num_api_calls': fake.random_int(min=1, max=100),
        'size': fake.random_int(min=1, max=1000),
        'num_updated_items': fake.random_int(min=1, max=100),
        'updated_size': fake.random_int(min=1, max=1000),
        'num_deleted_items': fake.random_int(min=1, max=100),
        'num_inserted_items': fake.random_int(min=1, max=100),
        'inserted_size': fake.random_int(min=1, max=1000),
        'deleted_size': fake.random_int(min=1, max=1000),
        'items_filename': fake.word(),
        'inserted_items_filename': fake.word(),
        'deleted_items_filename': fake.word(),
        'updated_items_filename': fake.word(),
        'overwritten_items_filename': fake.word(),
        'num_second_api_calls': fake.random_int(min=1, max=100),
        'num_third_api_calls': fake.random_int(min=1, max=100),
        'binaries_size': fake.random_int(min=1, max=1000),
        'items_size': fake.random_int(min=1, max=1000),
        'started_at': fake.date_time_this_month(),
        'completed_at': fake.date_time_this_month(),
        'parent_section_id': fake.random_int(min=1, max=100),
        'display_group_id': fake.word(),
    }
    fake_records.append(fake_data)

num = 0
for record in fake_records:
    num += 1
    print(" ****** record ", num, " ******")
    print(record)
    print(" ******************************")



# Example of querying all users
# sections = session.query(Section).all()
# Select the first 5 rows
sections = session.query(Section).limit(5).all()

for section in sections:
    print(
        f"id: {section.id}, service_id: {section.service_id}, name: {section.name}"
    )

try:
    for fake_record in fake_records:
        data = Section(**fake_record)
        session.add(data)
        session.commit()
except Exception as e:
    session.rollback()
    print(f"Error inserting fake data: {e}")

# Close the session
session.close()
