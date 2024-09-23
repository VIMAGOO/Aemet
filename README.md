# AEMET

Aquest projecte correspon a l'activitat <https://xtec.dev/python/urllib3/>

Utilitza dades de l'[AEMET](https://www.aemet.es).

## Docker

Instal.la docker:

```sh
curl -L sh.xtec.dev/docker.sh | sh
su - ${USER}
```

Executa el contenidor:

```sh
docker run -it registry.gitlab.com/xtec/python/aemet
```

## Develop

```sh
$ poetry update
$ poetry run python app/app.py
```

Pots obtenir una API Key a [AEMET OpenData](https://opendata.aemet.es/centrodedescargas/inicio) i modificar el fitxer `config.json`.

### Docker

A l'hora de desenvolupar l'aplicació:

```sh
$ docker build --tag aemet .
$ docker run -it aemet
```

Si debug:

```sh
$ docker run --rm -it aemet /bin/sh
```
