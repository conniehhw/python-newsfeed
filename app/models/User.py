import email
import bcrypt
from app.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates

salt = bcrypt.gensalt()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    
    def verify_password(self, password):
        return bcrypt.checkpw(
            password.encode('utf-8'),
            self.password.encode('utf-8')
        )

    @validates('email')
    def validate_email(self, key, email):
        # make sure email address contains @ character
        assert '@' in email
        return email

    @validates('password')
    def validate_password(self, key, password):
        assert len(password) > 4

        # encrypt password
        return bcrypt.hashpw(password.encode('utf-8'), salt)

# import email
# import bcrypt
# from app.db import Base
# from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import validates
# # We want to directly use the bcrypt module, so this time, the import syntax differs a bit. 

# salt = bcrypt.gensalt() # create a salt to hash passwords against

# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     username = Column(String(50), nullable=False)
#     email = Column(String(50), nullable=False, unique=True)
#     password = Column(String(100), nullable=False)

#     @validates('email')
#     def validate_email(self, key, email):
#     # make sure email address contains @ character  
#     assert '@' in email

#     return email

#   @validates('password')
#   def validate_password(self, key, password):
#     assert len(password) > 4

#   # encrypt password
#     return bcrypt.hashpw(password.encode('utf-8'), salt)

#   # @validates('email')
#   # def validate_email(self, key, email):                 # added new validate_email() method to the class that a @validate('email') decorator wraps.
#   #   # make sure email address contains @ character      # this method returns what the value of teh 'email' column should be and the @validates() decorator internally handles the rest.
#   #   assert '@' in email                                 # use 'assert' keyword to check if email has '@'. Auto throws error if condition is false, preventing return statement from happening
    
#   #   return email

#   # @validates('password')
#   # def validate_password(self, key, password):
#   #   assert len(password) > 4            # use assert to check length of password

#   #   # encrypt password
#   #   return bcrypt.hashpw(password.encode('utf-8'), salt)  # now returns an encrypted version of the password, if the assert doesn't throw an error.

#   #   return password  