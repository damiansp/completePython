from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

from create_tables import User


engine = create_engine('sqlite:///ecommerce.db', echo=True)
# Create a session factory bound to the engine
Session = sessionmaker(bind=engine)


def add_user(name: str, email: str):
    '''Adds a new user to the database. Returns the user ID if successful,
    else None.'''
    session = Session()
    new_user = User(name=name, email=email)
    try:
        session.add(new_user)
        session.commit()
        print(f"User '{name}' added with ID {new_user.id}")
        return new_user.id
    except IntegrityError:
        session.rollback()
        print(f"Error: A user with the email '{email}' already exists.")
        return None
    finally:
        session.close()


def get_users_by_name(name: str, return_type='user'):
    '''Fetches and returns all user records that match the given name.'''
    session = Session()
    try:
        users = session.query(User).filter(User.name == name).all()
        for user in users:
            print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")
        if return_type == 'dict':
            users = [
                {'id': u.id, 'name': u.name, 'email': u.email} for u in users]
        return users
    finally:
        session.close()


def update_user_email(user_id: int, new_email: str):
    '''Updates the email of the user with the given ID. Returns True if
    successful, False otherwise.'''
    session = Session()
    try:
        user = session.query(User).filter(User.id == user_id).first()
        if user is None:
            print(f'No user found with ID {user_id}.')
            return False
        user.email = new_email
        session.commit()
        print(f"Email updated for user ID {user_id} to '{new_email}'")
        return True
    except IntegrityError:
        session.rollback()
        print(f"Error: The email '{new_email}' is already in use.")
        return False
    finally:
        session.close()


def delete_user(user_id: int):
    '''Deletes the user with the given ID. Returns True if successful, False if
    user not found.'''
    session = Session()
    try:
        user = session.query(User).filter(User.id == user_id).first()
        if user is None:
            print(f'No user found with ID {user_id}.')
            return False
        session.delete(user)
        session.commit()
        print(f'User with ID {user_id} has been deleted.')
        return True
    finally:
        session.close()

# Test
#user_id = add_user('Alice Smith', 'alice@example.com')
alice_smiths = get_users_by_name('Alice Smith', 'dict')
for alice in alice_smiths:
    print(alice)
update_user_email(1, 'alice@wonderland.com')
alice_smiths = get_users_by_name('Alice Smith', 'dict')
for alice in alice_smiths:
    print(alice)
delete_user(1)
