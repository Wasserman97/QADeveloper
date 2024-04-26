# API Consulta IBGE

Este projeto é uma API simples para consultar informações sobre estados brasileiros e distritos na API do IBGE.

## Instalação

Para utilizar esta API, siga os passos abaixo:

1. Clone este repositório para o seu ambiente local.
2. Certifique-se de ter o Java JDK e o Maven instalados.
3. Execute o comando `mvn clean install` na raiz do projeto para compilar e empacotar o projeto.
4. Após a compilação bem-sucedida, execute o comando `java -jar target/ApiConsultaIBGE.jar` para iniciar o servidor.
5. O servidor estará disponível em `http://localhost:8080`.

## Uso

Você pode utilizar a API para consultar informações sobre estados brasileiros e distritos. Veja alguns exemplos de requisições:

### Consultar informações de um estado específico:

Substitua `{uf}` pela sigla do estado desejado.

### Consultar informações de um distrito específico:


Substitua `{id}` pelo ID do distrito desejado.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um problema ou enviar um pull request.

## Licença

Este projeto está licenciado sob a [Licença MIT](https://opensource.org/licenses/MIT).
