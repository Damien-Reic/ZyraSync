from ZyraSync.Models.Users.User import User



class BasicUser(User):
    def __repr__(self):
        return '<BasicUser %r>' % self.username
