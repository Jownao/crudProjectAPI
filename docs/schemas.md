# schemas.py

Define as validações e serializações de dados com Pydantic.

## Classes

### `ProductBase`
- **nome**: Nome do produto.
- **descricao**: Descrição opcional.
- **preço**: Preço do produto.
- **categoria**: Categoria do produto.
- **email_fornecedor**: E-mail do fornecedor.
::: backend.schemas.ProductBase

### `productCreate`
Herdado de `ProductBase`. Usado para criação de produtos.
::: backend.schemas.productCreate

### `productResponse`
Herdado de `ProductBase`. Inclui o ID e a data de criação.
::: backend.schemas.productResponse

### `productUpdate`
Herdado de `ProductBase`. Todos os campos são opcionais para atualização parcial.
::: backend.schemas.productUpdate

### `CategoriaBase`
::: backend.schemas.CategoriaBase