# database.py

Este arquivo contém a configuração do banco de dados.

## Componentes

### `engine`
Cria o motor do banco de dados utilizando as credenciais do PostgreSQL.

### `SessionLocal`
Instância de sessão usada para interagir com o banco de dados.

### `Base`
Classe base para os modelos declarativos do SQLAlchemy.

### `get_db()`
Função geradora que gerencia as sessões do banco de dados.


::: backend.database.get_db
