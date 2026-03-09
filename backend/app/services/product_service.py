from sqlalchemy.orm import Session
from typing import List
from ..repositories.product_repositori import ProductRepository
from ..repositories.category_repositories import CategoryRepository
from ..schemas.product import ProductResponse, ProductListResponse, ProductCreate , ProductBase
from fastapi import HTTPException, status

class ProductService:
    def __init__(self,db:Session):
        self.product_repository = ProductRepository(db)
        self.category_repository = CategoryRepository(db)

    def get_all_product(self) -> ProductListResponse:
        products = self.product_repository.get_all()
        product_response = [ProductResponse.model_validate(prod) for prod in products]
        return ProductListResponse(products=product_response,total=len(product_response))
    def get_products_by_id(self, product_id: int) -> ProductResponse:
        product = self.product_repository.get_by_id(product_id)
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Product with id {product_id} not found'
            )
        return ProductResponse.model_validate(product)
    def get_products_by_category(self,category_id:int) -> ProductListResponse:
        category = self.category_repository.get_bu_id(category_id)
        if not category:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Category with id {category_id} not found'
            )
        products = self.product_repository.get_by_category(category_id)
        products_responce = [ProductResponse.model_validate(prod) for prod in products]
        return ProductListResponse(products=products_responce, total=len(products_responce))
    def create_product(self,product_data:ProductCreate) -> ProductResponse:
        category = self.category_repository.get_bu_id(product_data.category_id)
        if not category:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Categpory with id {product_data.category_id} does not exist"
            )
        product = self.product_repository.create(product_data)
        return ProductResponse.model_validate(product)