from sqlalchemy import select

from fast_zero.models import User


def teste_create_user(session):
    new_user = User(username='alice', password='secrete', email='teste@teste')
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'alice'))

    assert user.username == 'alice'
