# from faker import Faker
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from app import app, Member, Admin, User

# # Initialize Faker
# faker = Faker()

# DB_CONFIG={
#     "dbname":"postgres",
#     "user": "postgres.bmkjhzotrhchferoexsh",
#     "password":"TsHtijPlPGN04e6t",
#     "host":"aws-0-eu-central-1.pooler.supabase.com",
#     "port":5432
# }

# DATABASE_URL= f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}"
# engine = create_engine(DATABASE_URL)
# Session = sessionmaker(bind=engine)
# session = Session()

# NUM_USERS = 15
# NUM_ADMIN = 2
# NUM_MEMBERS = 13

# # Assuming you have an initialized session
# # session = sessionmaker(bind=engine)()

# # Generate fake data for User table
# for _ in range(NUM_USERS):
#     user = User(
#         name=faker.name(),
#         email=faker.email(),
#         phonenumber=faker.phone_number()[:10],  # Generates a valid 10-digit phone number
#         role=faker.random_element(elements=("member", "pastor")),  # Assigns either "member" or "pastor"
#         password_hash=faker.sha256(raw_output=False)  # Fake SHA256 password hash
#     )
#     session.add(user)

# session.commit()  # Commit users first to generate their IDs

# # Generate fake data for Member table
# member_user_ids = [
#     user.id for user in session.query(User).filter_by(role="member").limit(NUM_MEMBERS).all()
# ]
# for user_id in member_user_ids:
#     member = Member(
#         user_id=user_id,
#         name=faker.company(),  # Example: Church name or other related data
#         residence=faker.address()  # Example: Member's address
#     )
#     session.add(member)

# session.commit()  # Commit members

# # Generate fake data for Pastor table (Admin)
# admin_user_ids = [
#     user.id for user in session.query(User).filter_by(role="pastor").limit(NUM_ADMIN).all()
# ]
# for user_id in admin_user_ids:
#     pastor = Admin(
#         user_id=user_id,
#         name=faker.name(),  # Pastor's name
#         phonenumber=faker.msisdn()[:10]  # Valid 10-digit phone number
#     )
#     session.add(pastor)

# session.commit()  # Commit pastors

# from faker import Faker
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from app import app, Member, Admin, User

# # Initialize Faker
# faker = Faker()

# # Database configuration
# DB_CONFIG = {
#     "dbname": "postgres",
#     "user": "postgres.bmkjhzotrhchferoexsh",
#     "password": "TsHtijPlPGN04e6t",
#     "host": "aws-0-eu-central-1.pooler.supabase.com",
#     "port": 5432
# }

# # Construct database URL
# DATABASE_URL = f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}"

# # Create engine and session
# engine = create_engine(DATABASE_URL)
# Session = sessionmaker(bind=engine)
# session = Session()

# # Number of users to generate
# NUM_USERS = 15
# NUM_ADMIN = 2
# NUM_MEMBERS = 13

# def generate_fake_users(session):
#     """Generate fake users."""
#     for _ in range(NUM_USERS):
#         user = User(
#             name=faker.name(),
#             email=faker.email(),
#             phonenumber=faker.phone_number()[:10],  
#             role=faker.random_element(elements=("member", "pastor")),  
#             password_hash=faker.sha256(raw_output=False)  
#         )
#         session.add(user)
#     session.commit()  # Commit users first to generate their IDs

# def generate_fake_members(session):
#     """Generate fake members."""
#     member_user_ids = [
#         user.id for user in session.query(User).filter_by(role="member").limit(NUM_MEMBERS).all()
#     ]
#     for user_id in member_user_ids:
#         member = Member(
#             user_id=user_id,
#             name=faker.company(),  
#             residence=faker.address()  
#         )
#         session.add(member)
#     session.commit()  # Commit members

# def generate_fake_admins(session):
#     """Generate fake admins (pastors)."""
#     admin_user_ids = [
#         user.id for user in session.query(User).filter_by(role="pastor").limit(NUM_ADMIN).all()
#     ]
#     for user_id in admin_user_ids:
#         pastor = Admin(
#             user_id=user_id,
#             name=faker.name(),  
#             phonenumber=faker.msisdn()[:10]  
#         )
#         session.add(pastor)
#     session.commit()  # Commit pastors

# def main():
#     try:
#         generate_fake_users(session)
#         generate_fake_members(session)
#         generate_fake_admins(session)
#         print("Fake data generated successfully.")
#     except Exception as e:
#         session.rollback()
#         print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     main()



# from faker import Faker
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from app import app, Member, Admin, User

# # Initialize Faker
# faker = Faker()

# # Database configuration
# DB_CONFIG = {
#     "dbname": "postgres",
#     "user": "postgres.bmkjhzotrhchferoexsh",
#     "password": "TsHtijPlPGN04e6t",
#     "host": "aws-0-eu-central-1.pooler.supabase.com",
#     "port": 5432
# }

# # Construct database URL
# DATABASE_URL = f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}"

# # Create engine and session
# engine = create_engine(DATABASE_URL)
# Session = sessionmaker(bind=engine)
# session = Session()

# # Number of users to generate
# NUM_USERS = 15
# NUM_ADMIN = 2
# NUM_MEMBERS = 13

# def generate_fake_users(session):
#     """Generate fake users."""
#     for _ in range(NUM_USERS):
#         user = User(
#             name=faker.name(),
#             email=faker.email(),
#             phonenumber=faker.random_number(digits=10, fix_len=True),  # Generate 10-digit phone number
#             role=faker.random_element(elements=("member", "pastor")),  # Assign random role
#             password_hash=faker.sha256(raw_output=False)  # Generate fake password hash
#         )
#         session.add(user)
#     session.commit()  # Commit users first to generate their IDs

# def generate_fake_members(session):
#     """Generate fake members."""
#     member_user_ids = [
#         user.id for user in session.query(User).filter_by(role="member").limit(NUM_MEMBERS).all()
#     ]
#     for user_id in member_user_ids:
#         member = Member(
#             user_id=user_id,
#             name=faker.name(),  # Use a person's name instead of a company name
#             phonenumber=faker.random_number(digits=10, fix_len=True),  # Generate valid phone number
#             email=faker.email(),
#             role="member",  # Ensure the role matches the table's definition
#             residence=faker.address()  # Generate fake address
#         )
#         session.add(member)
#     session.commit()  # Commit members

# def generate_fake_admins(session):
#     """Generate fake admins (pastors)."""
#     admin_user_ids = [
#         user.id for user in session.query(User).filter_by(role="pastor").limit(NUM_ADMIN).all()
#     ]
#     for user_id in admin_user_ids:
#         pastor = Admin(
#             user_id=user_id,
#             name=faker.name(),  # Use a person's name
#             phonenumber=faker.random_number(digits=10, fix_len=True),  # Generate valid phone number
#             email=faker.email(),
#             role="pastor"  # Ensure the role matches the table's definition
#         )
#         session.add(pastor)
#     session.commit()  # Commit pastors

# def main():
#     try:
#         generate_fake_users(session)
#         generate_fake_members(session)
#         generate_fake_admins(session)
#         print("Fake data generated successfully.")
#     except Exception as e:
#         session.rollback()
#         print(f"An error occurred: {e}")
#     finally:
#         session.close()

# if __name__ == "__main__":
#     main()

from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import app, Member, Admin, User

# Initialize Faker
faker = Faker()

# Database configuration
DB_CONFIG = {
    "dbname": "postgres",
    "user": "postgres.bmkjhzotrhchferoexsh",
    "password": "TsHtijPlPGN04e6t",
    "host": "aws-0-eu-central-1.pooler.supabase.com",
    "port": 5432
}

# Construct database URL
DATABASE_URL = f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}"

# Create engine and session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Number of users to generate
NUM_USERS = 15
NUM_ADMIN = 2
NUM_MEMBERS = 13

def generate_fake_users(session):
    """Generate fake users."""
    for _ in range(NUM_USERS):
        user = User(
            name=faker.name(),
            email=faker.email(),
            phonenumber=int(faker.msisdn()[:10]),  # Ensuring a valid integer
            role=faker.random_element(elements=("member", "pastor")),  
            password_hash=faker.sha256(raw_output=False)  
        )
        session.add(user)
    session.commit()  # Commit users first to generate their IDs

def generate_fake_admins(session):
    """Generate fake admins (pastors)."""
    admin_user_ids = [
        user.id for user in session.query(User).filter_by(role="pastor").limit(NUM_ADMIN).all()
    ]
    for user_id in admin_user_ids:
        pastor = Admin(
            user_id=user_id,
            name=faker.name(),
            phonenumber=int(faker.msisdn()[:10]),  # Ensuring a valid integer
            email=faker.email(),
            role="pastor"
        )
        session.add(pastor)
    session.commit()  # Commit pastors

def generate_fake_members(session):
    """Generate fake members."""
    member_user_ids = [
        user.id for user in session.query(User).filter_by(role="member").limit(NUM_MEMBERS).all()
    ]
    admin_ids = [admin.id for admin in session.query(Admin).all()]  # Get all admin IDs

    for user_id in member_user_ids:
        admin_id = faker.random_element(elements=admin_ids)  # Assign a random admin ID
        member = Member(
            user_id=user_id,
            name=faker.name(),
            phonenumber=int(faker.msisdn()[:10]),  # Ensuring a valid integer
            email=faker.email(),
            role="member",
            residence=faker.address(),
            Admin_id=admin_id  # Assign a valid admin_id
        )
        session.add(member)
    session.commit()  # Commit members

def main():
    try:
        generate_fake_users(session)
        generate_fake_admins(session)  # Generate admins before members
        generate_fake_members(session)
        print("Fake data generated successfully.")
    except Exception as e:
        session.rollback()
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()



