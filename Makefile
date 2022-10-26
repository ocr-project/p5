run:
	FLASK_APP=server flask run --host=0.0.0.0
build:
	cp server.py docker/server.py
	cp model.pickle docker/model.pickle
	DOCKER_BUILDKIT=1 docker build docker -t ndma/ocr-p5
push:
	docker push ndma/ocr-p5