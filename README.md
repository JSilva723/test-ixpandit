# Test Ixpandit

This app search, Pokemons by name of Poke-API.

## Get started

After cloning the repository on your computer, go to the directory where the `docker-compose.yml` file is located

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
docker exec -it api_ipx python3 test.py
```
### Requeriments

 - Docker
 - Docker-compose