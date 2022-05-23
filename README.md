# Test Ixpandit

This app search, Pokemons by name of Poke-API.

## Get started

After cloning the repository on your computer.

For `START`,&nbsp; you should run
```sh
docker-compose up -d
```
Await up server, when this be done, go to [Ixpandit APP](https://localhost:3000) 

For `CLOSE`,&nbsp; you should run
```sh
docker-compose down
```
For run the `TESTS`,&nbsp; it is necessary that the server is up.
```sh
docker exec -it ixpandit_api_1 python3 test.py
```
### Requeriments

 - Docker
 - Docker-compose