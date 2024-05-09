from functools import wraps
from flask import request
from flask_login import current_user


class Logs:
    access_log_file = "./ZyraSync/logs/web_access.log"
    login_log_file = "./ZyraSync/logs/login.log"

    @staticmethod
    def log_access(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Call the function being decorated
            result = func(*args, **kwargs)

            # Log the access to the file
            with open(Logs.access_log_file, 'a') as f:
                f.write(f'{request.remote_addr} - {request.method} {request.path}\n')

            return result

        return wrapper

    @staticmethod
    def log_login(username=current_user, success=True):
        with open(Logs.login_log_file, 'a') as f:
            f.write(f'{request.remote_addr} - {username} {"loggin success" if success else "login failed"}\n')

    @staticmethod
    def log_logout():
        with open(Logs.login_log_file, 'a') as f:
            f.write(f'{request.remote_addr} - {current_user} {"lougout"}\n')



