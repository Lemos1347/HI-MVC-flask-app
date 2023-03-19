import bcrypt

def create_user(user_name, email, password) -> bool:
    from src import db, app
    from src.migrations.user import User

    with app.app_context():
        user = User(name=user_name, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return True

def already_exists_by_email(email) -> bool:
    from src import db, app
    from src.migrations.user import User

    with app.app_context():
        db.first_or_404(db.select(User).filter_by(email=email))
        return True

def get_user_by_id(id) -> dict:
    from src import db, app
    from src.migrations.user import User

    with app.app_context():
        response = db.first_or_404(db.select(User).filter_by(id=id))
        return response

def get_user_by_email(email) -> dict:
    from src import db, app
    from src.migrations.user import User

    with app.app_context():
        response = db.first_or_404(db.select(User).filter_by(email=email))
        return response

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