from sqlalchemy.orm import Session
from schemas import productUpdate, productCreate
from models import ProductModel


def get_products(db: Session):
    """Função que retorna todos elementos"""
    return db.query(ProductModel).all()


def get_product_by_id(db: Session, product_id: int):
    """Função que recebe um id e retorna somente ele"""
    return db.query(ProductModel).filter(ProductModel.id == product_id).first()


def create_product(db: Session, product: productCreate):
    """Função que cria um novo elemento"""
    db_product = ProductModel(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    """Função que deleta um elemento"""
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if db_product is None:
        return None  # Retorne None se o produto não for encontrado
    
    db.delete(db_product)
    db.commit()
    return db_product


 
def update_product(db: Session, product_id: int, product: productUpdate):
    """Função que atualiza um elemento"""
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

    if db_product is None:
        return None

    if product.nome is not None:
        db_product.nome = product.nome
    if product.descricao is not None:
        db_product.descricao = product.descricao
    if product.preço is not None:
        db_product.preço = product.preço
    if product.categoria is not None:
        db_product.categoria = product.categoria
    if product.email_fornecedor is not None:
        db_product.email_fornecedor = product.email_fornecedor

    db.commit()
    return db_product