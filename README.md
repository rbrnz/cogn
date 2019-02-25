# Data Engineer Test *@Cognitivo*

A modelagem dos dados foi feita tendo em mente um Banco de Dados em OLTP, pois para a melhor realizar um Data Warehouse (OLAP) seriam necessárias algumas informações sobre o negócio e de seus processos.

No processo de modelagem dei preferência para a normalização dos dados.

## TODO

Em um segundo momento, seria interessante a criação do Data Warehouse com um foco numa modelagem dimensional e a configuração de um sistema de agendamento de tarefas (e.g. Airflow).

## How to run

Para rodar o etl, é necessário possuir o `Docker` instalado e realizar os seguintes comandos:

```bash
docker-compose -f ./docker/docker-compose.yml up -d

docker exec -it docker_cogn_1 /bin/bash

cd $ETL_HOME

bash etl.sh
```