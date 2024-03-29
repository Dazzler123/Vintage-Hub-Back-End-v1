from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.entity.user_mst import UserMst, Base
from app.models.login_user_dto import LoginUserDTO
from app.models.user_mst_dto import UserMstDTO


# from app.util.encryptor import encrypt_password


class UserService:

    # ===== This function is used to create new user =====
    def create_user(self: UserMstDTO):
        engine = create_engine("mysql+mysqlconnector://root:1234@localhost:3306/vintage_hub_db", echo=True)
        Base.metadata.create_all(bind=engine)

        Session = sessionmaker(bind=engine)
        session = Session()

        # TODO perform password encryption and save keys safely
        # encrypt password
        # encrypted_password, enc_key = encrypt_password(self.password)

        user = UserMst(self.name, self.address, self.nic, self.email, self.contactNo, self.drivingLicenseNo,
                       self.gender, self.username, self.password, self.password)

        session.add(user)

        try:
            session.commit()
            return True
        except Exception as e:
            print(f"Error committing the transaction: {e}")
            session.rollback()  # Rollback the transaction in case of an error
            return False
        finally:
            session.close()

    # ===== This function is used to authenticate user =====
    def verify_user(credentials: LoginUserDTO):
        engine = create_engine("mysql+mysqlconnector://root:1234@localhost:3306/vintage_hub_db", echo=True)
        Base.metadata.create_all(bind=engine)

        Session = sessionmaker(bind=engine)
        session = Session()

        user = session.query(UserMst).filter_by(username=credentials.username, password=credentials.password).first()

        session.close()

        if user:
            return user
        else:
            return


