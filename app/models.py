from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()


class Employee(db.Model, UserMixin):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    employee_number = Integer()
    hashed_password = String(255)


    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
