from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from database import Base


class ProductModel(Base):
    __tablename__ = "products"  # esse será o nome da tabela

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    descricao = Column(String)
    preço = Column(Float)
    categoria = Column(String)
    email_fornecedor = Column(String)
    dt_criado = Column(DateTime(timezone=True), default=func.now())