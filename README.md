[![Build](https://github.com/fga-eps-mds/2021.1-PC-GO1-Archives/workflows/Compilação/badge.svg)](https://github.com/fga-eps-mds/2021.1-PC-GO1-Archives/actions/workflows/build.yml)
[![Style](https://github.com/fga-eps-mds/2021.1-PC-GO1-Archives/workflows/Estilo/badge.svg)](https://github.com/fga-eps-mds/2021.1-PC-GO1-Archives/actions/workflows/style.yml)
[![Tests](https://github.com/fga-eps-mds/2021.1-PC-GO1-Archives/workflows/Testes/badge.svg)](https://github.com/fga-eps-mds/2021.1-PC-GO1-Archives/actions/workflows/test.yml)

# API de Gerenciamento de Arquivos do SysArq

A API de Gerenciamento de Arquivos do *SysArq* compõe a arquitetura de microsserviços do sistema *[SysArq](https://fga-eps-mds.github.io/2021.1-PC-GO1/)*.

Esse microsserviço é responsável pelo *CRUD* ([veja a definição](https://developer.mozilla.org/pt-BR/docs/Glossary/CRUD)), cadastro, pesquisa e filtragem dos documentos. **[Saiba mais](https://fga-eps-mds.github.io/2021.1-PC-GO1/documentation/)**

## Execução

### Requisitos
 - ***`Docker`*** - [veja como instalar](https://docs.docker.com/engine/install/);
 - ***`docker-compose`***, no mínimo a versão *`1.29.0`* - [veja como instalar](https://docs.docker.com/compose/install/).

### Executar

1. Clone esse repositório - [veja como clonar um repositório](https://docs.github.com/pt/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository);

2. Crie, utilizando o arquivo ***env-reference***, o *`.env`* dentro da **pasta do repositório**;

3. Execute, dentro da **pasta do repositório**, o comando:
   ```
    sudo docker-compose up
   ```

4. Acesse [http://0.0.0.0:8002/](http://0.0.0.0:8002) no navegador. 

### Testes

1. Acesse o container:
   ```
      sudo docker exec -ti 20211-pc-go1-archives_web_1 sh
   ```

2. Utilize o ***pytest***. Por exemplo:
   ```
      pytest --cov
   ```
   **Observação**: Só serão aceitas contribuições com 90% de cobertura de código.

### Verificação de Estilo

1. Acesse o container:
   ```
      sudo docker exec -ti 20211-pc-go1-archives_web_1 sh
   ```

2. Utilize o ***flake8***. Por exemplo:
   ```
      flake8
   ```
   **Observação**: Só serão aceitas contribuições com o estilo correto.

## Documentação

`TO-DO`
