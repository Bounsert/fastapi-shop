from sqlalchemy.orm import Session
from typing import List,Optional
from ..models.category import Category
from ..schemas.сategory import CategoryCreate

class CategoryRepository:
    def __init__(self ,db: Session):
        self.db = db

    def get_all(self) -> List[Category]:
        return self.db.query(Category).all()


    def get_bu_id(self, category_id:int) -> Optional[Category]:
        return self.db.query(Category).filter(Category.id == category_id).first()
    
    def get_by_slug(self, slug:str) -> Optional[Category]:
        return self.db.query(Category).filter(Category.slug == slug).first()
    
    def create(self, categort_data: CategoryCreate) -> Category:
        db_category = Category(**categort_data.model_dump())
        self.db.add(db_category)
        self.db.commit()
        self.db.refresh()
        return db_category
