FROM python:3.11-slim as requirements-stage
WORKDIR /tmp
RUN pip install poetry
COPY ./pyproject.toml ./poetry.lock* /tmp/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.11-slim
WORKDIR /code
ENV TZ=Asia/Taipei
COPY --from=requirements-stage /tmp/requirements.txt .
RUN apt-get update && apt-get -y install gcc
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY ./app ./app
COPY start.sh .
RUN chmod +x ./start.sh
ENTRYPOINT ["sh", "./start.sh"]