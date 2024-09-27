from pydantic import BaseModel, PositiveFloat, EmailStr, field_validator
from enum import Enum
from datetime import datetime
from typing import Optional


class ProductBase(BaseModel):
    nome: str
    descricao: Optional[str] = None
    preço: PositiveFloat
    categoria: str
    email_fornecedor: EmailStr

    @field_validator("categoria")
    def check_categoria(cls, v):
        if v in [item.value for item in CategoriaBase]:
            return v
        raise ValueError("Categoria inválida")


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

    @field_validator("categoria")
    def check_categoria(cls, v):
        if v is None:
            return v
        if v in [item.value for item in CategoriaBase]:
            return v
        raise ValueError("Categoria inválida")

class CategoriaBase(Enum):
    categoria1 = "Eletrônico"
    categoria2 = "Eletrodoméstico"
    categoria3 = "Móveis"
    categoria4 = "Roupas"
    categoria5 = "Calçados"