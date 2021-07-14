VERSION=v0.0.1
DOCKER_IMAGE=zhenshaw/zf-captcha-crack



## help: help for this project
help: Makefile
	@echo "Usage:\n  make [command]"
	@echo
	@echo "Available Commands:"
	@sed -n 's/^##//p' $< | column -t -s ':' |  sed -e 's/^/ /'


## requirements: install requirements with pip3.
requirements:
	@pip3 install -r requirements.txt


## freeze: freeze requirements with pip3.
freeze:
	@pip3 freeze > requirements.txt


## run: run in develop mode with uvicorn.
run:
	@python app.py


## image: build docker image.
image:
	@docker build -t $(DOCKER_IMAGE) .


## push: build docker image and push.
push: image
	@docker push $(DOCKER_IMAGE)


## compose: build and run with docker-compose.
compose: image
	@docker-compose up -d --build
