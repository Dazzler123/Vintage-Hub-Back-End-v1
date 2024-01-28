from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.entity.user_mst import UserMst, Base
from app.models.user_mst_dto import UserMstDTO


class UserService:

    # ===== This function is used to create new user =====
    def create_user(self: UserMstDTO):
        engine = create_engine("mysql+mysqlconnector://root:1234@localhost:3306/vintage_hub_db", echo=True)
        Base.metadata.create_all(bind=engine)

        Session = sessionmaker(bind=engine)
        session = Session()

        user = UserMst(self.name, self.address, self.nic, self.email, self.contactNo, self.drivingLicenseNo,
                       self.gender, self.username, self.password)

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
