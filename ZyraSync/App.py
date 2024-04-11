from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from ZyraSync.Models.Utilities.Logs import Logs
from ZyraSync.AppConfig import Config
import logging

class App():
    def __init__(self):
        self.app, self.bcrypt,self.db,self.login_manager = App.create_app()


    ### Creation de l'application
    @staticmethod
    def create_app(config_class=Config):
        app = Flask(__name__)
        app.config.from_object(config_class)

        ### Ajout du module de hashage des mots de passes

        bcrypt = Bcrypt(app)

        ### Ajout du module de base de donnée

        db = SQLAlchemy(app)

        ### Ajout du gestionnaire de connection

        login_manager = LoginManager()
        login_manager.init_app(app)
        login_manager.login_view = "login"

        ### Configuration du logger web

        logs_conf_path = "conf/web_logs.conf"

        Logs.setup_logging(logs_conf_path, logging_level=logging.DEBUG)

        logfile = logging.getLogger('file')
        logconsole = logging.getLogger('console')
        logfile.debug("Debug FILE")
        logconsole.debug("Debug CONSOLE")

        return app, bcrypt, db, login_manager