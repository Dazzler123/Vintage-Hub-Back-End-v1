from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.entity.other_accessory_mst import OtherAccessoryMst, Base
from app.models.other_accessory_mst_dto import OtherAccessoryMstDTO


class OtherAccessoryService:

    # ===== This function is used to create new accessory item =====
    def create_other_accessory(self: OtherAccessoryMstDTO):
        engine = create_engine("mysql+mysqlconnector://root:1234@localhost:3306/vintage_hub_db", echo=True)
        Base.metadata.create_all(bind=engine)

        Session = sessionmaker(bind=engine)
        session = Session()

        item = OtherAccessoryMst(self.title, self.make, self.partNumber, self.manufacturer, self.oem,
                                 self.aftermarket, self.condition, self.description, self.compatibility,
                                 self.additionalInfo, self.price, self.negotiable)

        session.add(item)

        try:
            session.commit()
            return True
        except Exception as e:
            print(f"Error committing the transaction: {e}")
            session.rollback()  # Rollback the transaction in case of an error
            return False
        finally:
            session.close()
