from pydantic import BaseModel, Field


class CatageryBase(BaseModel):
    name: str = Field(..., min_length=5,max_length=100,
        description="Category name")
    slug: str = Field(...,min_length=5,max_length=100,
        description="URL-friendly catagory name")

class CategoryCreate(CatageryBase):
    pass

class CategoryResponse(CatageryBase):
    id: int = Field(...,description='Unique category identifier')

    class Config:
        form_attributes = True