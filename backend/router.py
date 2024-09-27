from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal,get_db
from schemas import productResponse, productUpdate, productCreate
from typing import List
from crud import (
    create_product,
    get_products,
    get_product_by_id,
    delete_product,
    update_product,
)

router = APIRouter()

# rota para buscar todos os produtos
@router.get("/products", response_model=List[productResponse])
def get_all_products(db: Session = Depends(get_db)):
    return get_products(db)

# rota para buscar um produto por id
@router.get("/products/{product_id}", response_model=productResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = get_product_by_id(db, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="O Produto não existe")
    return product 

# rota para criar um produto
@router.post("/products", response_model=productResponse)
def create_new_product(product: productCreate, db: Session = Depends(get_db)):
    return create_product(db, product)

# rota para deletar um produto
@router.delete("/products/{product_id}", response_model=productResponse)
def delete_product_by_id(product_id: int, db: Session = Depends(get_db)):
    product_db = delete_product(db, product_id)
    if product_db is None:
        raise HTTPException(status_code=404, detail="O Produto não existe")
    return product_db

# rota para atualizar um produto
@router.put("/products/{product_id}", response_model=productResponse)
def update_product_by_id(product_id: int, product: productUpdate, db: Session = Depends(get_db)):
    product_db = update_product(db, product_id, product)
    if product_db is None:
        raise HTTPException(status_code=404, detail="O Produto não existe")
    return product_db