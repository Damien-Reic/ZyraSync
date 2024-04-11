from ZyraSync.App import App

__app = App()


app,bcrypt,db,login_manager = __app.app, __app.bcrypt, __app.db, __app.login_manager

### Creation du package

import ZyraSync.views
import ZyraSync.Models
import ZyraSync.AppConfig
import ZyraSync.App

### Creations de la base de donnée

with app.app_context():
    db.create_all()