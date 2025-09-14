from typing import Optional #this is like Generics in Java, this is type hint, makes code cleaner, Mapped[int] = type hint
import sqlalchemy as sa #importing Core
import sqlalchemy.orm as so #importing ORM, we can combine ORM and Core together
from app import db #importing the object of Sqlalchemy defined in init

#Optional and typing are python features, Mapped is or sqlalchemy feature
#typing = module which helps with type hints and specifying type sof variables, args, functions and return types
#Optional = It is a type hint from typing module, can be either a specified type or None, Optional[int] = int or None


class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    
    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    