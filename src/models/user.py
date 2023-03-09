
def create_user(userName, email, password):
    from src import db, app
    from src.migrations.user import User

    user = User(userName=userName, email=email, password=password)
    with app.app_context():
        db.session.add(user)
        db.session.commit()