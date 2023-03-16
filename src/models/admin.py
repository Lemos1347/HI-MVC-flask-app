def turn_indo_admin_by_id(id) -> str:
    from src import db, app
    from src.migrations.user import User

    with app.app_context():

        user = db.first_or_404(db.select(User).filter_by(id=id))
        if user.is_admin == True:
            raise Exception('User is already admin')

        user.is_admin = True
        db.session.commit()
        return f"The user {user.name} just became an admin"