# syntax = docker/dockerfile:experimental
#Start from an image that suit your device
FROM python:3.9-slim

RUN --mount=type=cache,target=/root/.cache/pip pip install torch --extra-index-url https://download.pytorch.org/whl/cpu

RUN --mount=type=cache,target=/root/.cache/pip pip install --upgrade "Flask==2.1.2" "flask-restx>=0.5.1" "Werkzeug<=2.1.2"
RUN --mount=type=cache,target=/root/.cache/pip pip install --disable-pip-version-check --upgrade scikit-learn

RUN --mount=type=cache,target=/root/.cache/pip pip install --disable-pip-version-check --upgrade sentence_transformers

RUN mkdir /app
WORKDIR /app
COPY model.pickle /app
COPY server.py /app
COPY flax-sentence-embeddings_stackoverflow_mpnet-base /root/.cache/torch/sentence_transformers/flax-sentence-embeddings_stackoverflow_mpnet-base

CMD ["bash", "-c", "FLASK_APP=server flask run --host=0.0.0.0 --port=80"]