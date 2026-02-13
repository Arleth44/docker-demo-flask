# docker-demo-flask

Ejemplo simple Flask + Docker + GitHub Actions + Docker Hub.

## Run local
python app.py

## Tests
pytest -q

## Coverage
pytest --cov=app --cov-report=term-missing

## Docker
docker build -t docker-demo-flask:local .
docker run --rm -p 5000:5000 docker-demo-flask:local
