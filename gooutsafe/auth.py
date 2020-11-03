import functools

from flask_login import current_user, LoginManager

from gooutsafe.models.user import User


def init_login_manager(app):
    login_manager = LoginManager(app)
    login_manager.login_view = 'auth.login'
    login_manager.refresh_view = 'auth.relogin'

    @login_manager.user_loader
    def load_user(user_id):
        user = User.query.get(user_id)
        if user is not None:
            user._authenticated = True
        return user

    return login_manager


def admin_required(func):
    @functools.wraps(func)
    def _admin_required(*args, **kw):
        admin = current_user.is_authenticated and current_user.is_admin
        if not admin:
            return login.unauthorized()
        return func(*args, **kw)

    return _admin_required
