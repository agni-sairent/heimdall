import sys
from datetime import datetime
import uuid

from argon2 import PasswordHasher

from models.Subscriber import Subscriber
from models.User import User
from services.DatabaseService import DatabaseService

db = DatabaseService().get_db()


def prepare_db():
    db.create_tables([User, Subscriber])
    return True


def load_subscriber():
    return Subscriber.create(name="DefaultSubscriber", description="Master subscriber account not actual subscriber",
                             subscriber_key="Ds4GlQNozwQHaHBVFHXhlrZABuLHE2CXOl81HUyf2RqMH08j8mbcYofJfQWDT3If",
                             can_authenticate=True, can_register=True, active=True, created=datetime.now())


def create_default_user():
    ph = PasswordHasher()
    default_subscriber = Subscriber.get(subscriber_key='Ds4GlQNozwQHaHBVFHXhlrZABuLHE2CXOl81HUyf2RqMH08j8mbcYofJfQWDT3If')
    return User.create(id=uuid.uuid4(), username='tester', password=ph.hash('WsQ4562+'), email='email@example.com',
                       registered_by=default_subscriber, active=True, created=datetime.now())


print(prepare_db())
print(load_subscriber())
print(create_default_user())
sys.exit(0)

