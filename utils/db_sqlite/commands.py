from xmlrpc.client import Boolean
from utils.db_sqlite.schemas.client import Client
from utils.db_sqlite.schemas.user import User
from utils.db_sqlite.schemas.boat import Boat
from utils.db_sqlite.base import session



def add_user(telegram_id:int) -> Boolean:
    try:
        sess = session()
        user = User(telegram_id = telegram_id)
        sess.add(user)
        sess.commit()
        sess.close()
        return True
    except Exception as inst:
        print(inst)
        print('Errore add user')
        return False

def add_client(data: dict) -> True | False:
    try:
        sess = session()
        try:
            client = Client()
            client.add_data(data)
            sess.add(client)
            sess.commit()
            sess.close()
            return True
        except Exception as inst:
            print(inst)
            sess.close()
            return False
    except Exception as inst:
        print(inst)
        sess.close()
        print('Errore add client')
        return False

def add_boat(data:dict) -> True | False:
    try:
        sess = session()
        try:
            boat = Boat()
            boat.add_data(data)
            sess.add(boat)
            sess.commit()
            sess.close()
            return True
        except Exception as inst:
            print(inst)
            sess.close()
            return False
    except Exception as inst:
        print(inst)
        sess.close()
        print('Errore add boat')
        return False

def select_all_users() -> list:
    sess = session()
    users = sess.query(User).all()
    sess.close()
    return users

def select_all_clients()  -> list[Client]:
    sess = session()
    clients = sess.query(Client).all()
    sess.close()
    return clients


def select_all_boats()  -> list:
    sess = session()
    boats = sess.query(Boat).all()
    sess.close()
    return boats

def select_user(telegram_id: User.id) -> User:
    sess = session()
    user = sess.query(User).filter(User.telegram_id==telegram_id).first()
    sess.close()
    return user

def select_client(id: Client.id) -> tuple:
    sess = session()
    client = sess.query(Client).filter(Client.id==id).first()
    if client.boat:
        boat_id = client.boat.id
    else:
        boat_id = None
    sess.close()
    return client, boat_id

def select_boat(id: Boat.id) -> tuple:
    sess = session()
    boat = sess.query(Boat).filter(Boat.id==id).first()
    print(boat)
    
    if boat.owner:
        client_id = boat.owner.id
    else:
        client_id = None
    sess.close()
    return boat, client_id


def count_users():
    return len(select_all_users())

def count_client():
    return len(select_all_clients())

def count_boats():
    return len(select_all_boats())
