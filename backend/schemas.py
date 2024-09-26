from pydantic import BaseModel, PositiveFloat, EmailStr, Field
from enum import Enum
from datetime import datetime
from typing import Optional


class ProductBase(BaseModel):
    nome: str
    descricao: Optional[str] = None
    preço: PositiveFloat
    categoria: str
    email_fornecedor: EmailStr


class productCreate(ProductBase):
    pass

class productResponse(ProductBase):
    id: int
    dt_criado: datetime

    class Config:
        from_attributes = True

class productUpdate(ProductBase):
    nome: Optional[str] = None
    descricao: Optional[str] = None
    preço: Optional[PositiveFloat] = None
    categoria: Optional[str] = None
    email_fornecedor: Optional[EmailStr] = None