# router.py

Define as rotas da API para gerenciamento de produtos.

## Endpoints

### `GET /products`
Retorna a lista de todos os produtos.
::: backend.router.get_all_products

### `GET /products/{product_id}`
Retorna um produto específico com base no ID.
::: backend.router.get_product

### `POST /products`
Cria um novo produto.
::: backend.router.create_new_product

### `DELETE /products/{product_id}`
Deleta um produto pelo ID.
::: backend.router.delete_product_by_id

### `PUT /products/{product_id}`
Atualiza os detalhes de um produto pelo ID.
::: backend.router.update_product_by_id





