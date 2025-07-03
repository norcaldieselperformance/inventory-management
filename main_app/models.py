from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, username, password, role):
        self.id = id
        self.username = username
        self.password = password
        self.role = role

# users stored in a dictionary for testing
users = {
    "admin": User("1", "admin", "adminpassword", "admin"),
    "manager": User("2", "manager", "managerpassword", "manager")
}