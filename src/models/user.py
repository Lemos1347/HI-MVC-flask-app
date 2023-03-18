import bcrypt


def create_user(user_name, email, password) -> bool:
    from src import db, app
    from src.migrations.user import User

    with app.app_context():
        response = db.session.scalars(
            db.select(User).filter_by(email=email)).all()
        if response != []:
            raise NameError(f"The email {email} is already in use")

        password = str(password)
        password = password.encode('UTF_8')
        password_crypt = bcrypt.hashpw(password, bcrypt.gensalt(10))
        user = User(name=user_name, email=email, password=password_crypt)
        db.session.add(user)
        db.session.commit()
        return True


def login(email, password) -> int:
    from src import db, app
    from src.migrations.user import User

    with app.app_context():
        user = db.first_or_404(db.select(User).filter_by(email=email))
        if bcrypt.checkpw(str(password).encode('UTF_8'), str(user.password).encode('UTF_8')):
            return user.id
        raise NameError("Incorrect password!")


def get_user_by_id(id) -> dict:
    from src import db, app
    from src.migrations.user import User

    with app.app_context():
        response = db.first_or_404(db.select(User).filter_by(id=id))
        return response
        return {'id': response.id, 'name': response.name, 'email': response.email}


def change_user_email(id, email) -> str:
    from src import db, app
    from src.migrations.user import User

    with app.app_context():

        check = db.session.scalars(db.select(User).filter_by(email=email)).all()
        if check != []:
            raise NameError('Email already in use')

        user = db.session.scalars(db.select(User).filter_by(id=id)).one()

        if user.email == email:
            raise NameError('Trying to change for the same email')

        user.email = email
        db.session.commit()
        return f"The email was updated for {email}"

def get_admin_status_by_id(id) -> dict:
    from src import db, app
    from src.migrations.user import User

    with app.app_context():
        response = db.first_or_404(db.select(User).filter_by(id=id))
        return {'is_admin': response.is_admin}

def delete_user_by_id(id) -> str:
    from src import db, app
    from src.migrations.user import User

    with app.app_context():
        user = db.first_or_404(db.select(User).filter_by(id=id))
        # name = user.name.copy()
        print('chegou')
        db.session.delete(user)
        db.session.commit()
        return f'The user was deleted'