[![Build](https://github.com/fga-eps-mds/2021.1-PC-GO1-Archives/workflows/Compilação/badge.svg)](https://github.com/fga-eps-mds/2021.1-PC-GO1-Archives/actions/workflows/build.yml)
[![Style](https://github.com/fga-eps-mds/2021.1-PC-GO1-Archives/workflows/Estilo/badge.svg)](https://github.com/fga-eps-mds/2021.1-PC-GO1-Archives/actions/workflows/style.yml)
[![Tests](https://github.com/fga-eps-mds/2021.1-PC-GO1-Archives/workflows/Testes/badge.svg)](https://github.com/fga-eps-mds/2021.1-PC-GO1-Archives/actions/workflows/test.yml)

# API de Gerenciamento de Arquivos do SysArq

[![codecov](https://codecov.io/gh/fga-eps-mds/2021.1-PC-GO1-Archives/branch/main/graph/badge.svg?token=CY2SSE56VM)](https://codecov.io/gh/fga-eps-mds/2021.1-PC-GO1-Archives)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=fga-eps-mds_2021.1-PC-GO1-Archives&metric=alert_status)](https://sonarcloud.io/dashboard?id=fga-eps-mds_2021.1-PC-GO1-Archives)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=fga-eps-mds_2021.1-PC-GO1-Archives&metric=security_rating)](https://sonarcloud.io/dashboard?id=fga-eps-mds_2021.1-PC-GO1-Archives)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=fga-eps-mds_2021.1-PC-GO1-Archives&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=fga-eps-mds_2021.1-PC-GO1-Archives)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=fga-eps-mds_2021.1-PC-GO1-Archives&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=fga-eps-mds_2021.1-PC-GO1-Archives)

[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=fga-eps-mds_2021.1-PC-GO1-Archives&metric=bugs)](https://sonarcloud.io/dashboard?id=fga-eps-mds_2021.1-PC-GO1-Archives)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=fga-eps-mds_2021.1-PC-GO1-Archives&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=fga-eps-mds_2021.1-PC-GO1-Archives)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=fga-eps-mds_2021.1-PC-GO1-Archives&metric=code_smells)](https://sonarcloud.io/dashboard?id=fga-eps-mds_2021.1-PC-GO1-Archives)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=fga-eps-mds_2021.1-PC-GO1-Archives&metric=sqale_index)](https://sonarcloud.io/dashboard?id=fga-eps-mds_2021.1-PC-GO1-Archives)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=fga-eps-mds_2021.1-PC-GO1-Archives&metric=ncloc)](https://sonarcloud.io/dashboard?id=fga-eps-mds_2021.1-PC-GO1-Archives)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=fga-eps-mds_2021.1-PC-GO1-Archives&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=fga-eps-mds_2021.1-PC-GO1-Archives)

A API de Gerenciamento de Arquivos do *SysArq* compõe a arquitetura de microsserviços do sistema *[SysArq](https://fga-eps-mds.github.io/2021.1-PC-GO1/)*.

Esse microsserviço é responsável pelo *CRUD* ([veja a definição](https://developer.mozilla.org/pt-BR/docs/Glossary/CRUD)), pesquisa e filtragem de documentos. **[Saiba mais](https://fga-eps-mds.github.io/2021.1-PC-GO1/documentation/)**

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

### Testes e Verificação de Estilo

-  Para **testar** a aplicação, utilize o ***pytest***. Por exemplo:
   ```
      sudo docker-compose run web pytest --cov
   ```
   **Observação**: Só serão aceitas contribuições com 90% de cobertura de código.

- Para **verificar o estilo de código** da aplicação, utilize o ***flake8***. Por exemplo:
   ```
      sudo docker-compose run web flake8
   ```
   **Observação**: Só serão aceitas contribuições com o estilo correto.

**ATENÇÃO**: Execute os comandos dentro da **`pasta`** do repositório.

## Documentação

### Como contribuir

- Leia o [guia de contribuição](CONTRIBUTING.md)
