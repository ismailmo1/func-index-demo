from os import getenv

from flask import Flask
from flask_security import (
    RoleMixin,
    Security,
    SQLAlchemyUserDatastore,
    UserMixin,
    login_required,
)
from flask_sqlalchemy import SQLAlchemy

# Create app
app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "super-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("SQLALCHEMY_DATABASE_URI")
app.config["SECURITY_PASSWORD_SALT"] = "salty"
app.config["WTF_CSRF_ENABLED"] = False
# Create database connection object
db = SQLAlchemy(app)

# Define models
roles_users = db.Table(
    "roles_users",
    db.Column("user_id", db.Integer(), db.ForeignKey("user.id")),
    db.Column("role_id", db.Integer(), db.ForeignKey("role.id")),
)


class Role(db.Model, RoleMixin):  # type: ignore
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):  # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship(
        "Role",
        secondary=roles_users,
        backref=db.backref("users", lazy="dynamic"),
    )


# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


@app.route("/")
@login_required
def home():
    return "success"


if __name__ == "__main__":
    app.run()
