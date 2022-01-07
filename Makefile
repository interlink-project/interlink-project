SHELL := /bin/bash
# include .env
# export $(shell sed 's/=.*//' .env)

ifeq (service,$(firstword $(MAKECMDGOALS)))
  RUN_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  $(eval $(RUN_ARGS):;@:)
endif

.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: net
net: ## Creates needed network to communicate through different docker-compose files
	docker network create traefik-public || true

.PHONY: setup
setup: ## Clones all components
	cd .. && git clone https://github.com/interlink-project/frontend
	# platform components
	cd .. && git clone https://github.com/interlink-project/backend-proxy
	cd .. && git clone https://github.com/interlink-project/backend-acl
	cd .. && git clone https://github.com/interlink-project/backend-auth
	cd .. && git clone https://github.com/interlink-project/backend-teammanagement
	cd .. && git clone https://github.com/interlink-project/backend-catalogue
	cd .. && git clone https://github.com/interlink-project/backend-coproduction
	# interlinkers
	cd .. && git clone https://github.com/interlink-project/interlinker-filemanager
	cd .. && git clone https://github.com/interlink-project/interlinker-googledrive
	cd .. && git clone https://github.com/interlink-project/interlinker-forum
	cd .. && git clone https://github.com/interlink-project/interlinker-etherpad


.PHONY: update
update: ## Updates all repositories
	cd ../frontend && git pull origin master
	# platform components
	cd ../backend-proxy && git pull origin master
	cd ../backend-acl && git pull origin master
	cd ../backend-auth && git pull origin master
	cd ../backend-catalogue && git pull origin master
	cd ../backend-coproduction && git pull origin master
	cd ../backend-proxy && git pull origin master
	cd ../backend-teammanagement && git pull origin master
	
.PHONY: down
down: ## Stops all containers and removes volumes
	cd .. && docker-compose -f backend-proxy/docker-compose.yml -f backend-proxy/docker-compose.dev.yml down --volumes --remove-orphans
	cd .. && docker-compose -f backend-acl/docker-compose.yml -f backend-acl/docker-compose.integrated.yml down --volumes --remove-orphans
	cd .. && docker-compose -f backend-auth/docker-compose.yml -f backend-auth/docker-compose.integrated.yml down --volumes --remove-orphans
	cd .. && docker-compose -f backend-teammanagement/docker-compose.yml -f backend-teammanagement/docker-compose.integrated.yml down --volumes --remove-orphans
	cd .. && docker-compose -f backend-catalogue/docker-compose.yml -f backend-catalogue/docker-compose.integrated.yml down --volumes --remove-orphans
	cd .. && docker-compose -f backend-coproduction/docker-compose.yml -f backend-coproduction/docker-compose.integrated.yml down --volumes --remove-orphans
	
	cd .. && docker-compose -f frontend/docker-compose.yml -f frontend/docker-compose.integrated.yml down --volumes --remove-orphans
	# interlinkers
	cd .. && docker-compose -f interlinker-googledrive/docker-compose.yml -f interlinker-googledrive/docker-compose.integrated.yml down --volumes --remove-orphans
	cd .. && docker-compose -f interlinker-etherpad/docker-compose.yml -f interlinker-etherpad/docker-compose.integrated.yml down --volumes --remove-orphans
	cd .. && docker-compose -f interlinker-forum/docker-compose.yml -f interlinker-forum/docker-compose.integrated.yml down --volumes --remove-orphans
	cd .. && docker-compose -f interlinker-filemanager/docker-compose.yml -f interlinker-filemanager/docker-compose.integrated.yml down --volumes --remove-orphans
	docker network rm traefik-public || true

.PHONY: up
up: down net ## Run containers (restarts them if already running)
	cd .. && docker-compose -f backend-proxy/docker-compose.yml -f backend-proxy/docker-compose.dev.yml up -d
	cd .. && docker-compose -f backend-acl/docker-compose.yml -f backend-acl/docker-compose.integrated.yml up -d
	cd .. && docker-compose -f backend-auth/docker-compose.yml -f backend-auth/docker-compose.integrated.yml up -d
	cd .. && docker-compose -f backend-teammanagement/docker-compose.yml -f backend-teammanagement/docker-compose.integrated.yml up -d
	cd .. && docker-compose -f backend-catalogue/docker-compose.yml -f backend-catalogue/docker-compose.integrated.yml up -d
	cd .. && docker-compose -f backend-coproduction/docker-compose.yml -f backend-coproduction/docker-compose.integrated.yml up -d
	
	cd .. && docker-compose -f frontend/docker-compose.yml -f frontend/docker-compose.nginx.yml up -d

	# interlinkers
	cd .. && docker-compose -f interlinker-googledrive/docker-compose.yml -f interlinker-googledrive/docker-compose.integrated.yml up -d
	cd .. && docker-compose -f interlinker-filemanager/docker-compose.yml -f interlinker-filemanager/docker-compose.integrated.yml up -d
	cd .. && docker-compose -f interlinker-etherpad/docker-compose.yml -f interlinker-etherpad/docker-compose.integrated.yml up -d
	# cd .. && docker-compose -f interlinker-forum/docker-compose.yml -f interlinker-forum/docker-compose.integrated.yml up -d


.PHONY: builddev
builddev: ## Build containers
	cd .. && docker-compose -f frontend/docker-compose.yml -f frontend/docker-compose.integrated.yml build
	
	cd .. && docker-compose -f backend-proxy/docker-compose.yml -f backend-proxy/docker-compose.dev.yml build
	cd .. && docker-compose -f backend-acl/docker-compose.yml -f backend-acl/docker-compose.integrated.yml build
	cd .. && docker-compose -f backend-auth/docker-compose.yml -f backend-auth/docker-compose.integrated.yml build
	cd .. && docker-compose -f backend-teammanagement/docker-compose.yml -f backend-teammanagement/docker-compose.integrated.yml build
	cd .. && docker-compose -f backend-catalogue/docker-compose.yml -f backend-catalogue/docker-compose.integrated.yml build
	cd .. && docker-compose -f backend-coproduction/docker-compose.yml -f backend-coproduction/docker-compose.integrated.yml build
	
	# interlinkers
	cd .. && docker-compose -f interlinker-googledrive/docker-compose.yml -f interlinker-googledrive/docker-compose.integrated.yml build
	cd .. && docker-compose -f interlinker-etherpad/docker-compose.yml -f interlinker-etherpad/docker-compose.integrated.yml build
	cd .. && docker-compose -f interlinker-forum/docker-compose.yml -f interlinker-forum/docker-compose.integrated.yml build
	cd .. && docker-compose -f interlinker-filemanager/docker-compose.yml -f interlinker-filemanager/docker-compose.integrated.yml build

.PHONY: buildprod
buildprod: ## Build containers
	cd .. && docker-compose -f frontend/docker-compose.yml build
	
	cd .. && docker-compose -f backend-proxy/docker-compose.yml build
	cd .. && docker-compose -f backend-acl/docker-compose.yml build
	cd .. && docker-compose -f backend-auth/docker-compose.yml build
	cd .. && docker-compose -f backend-teammanagement/docker-compose.yml build
	cd .. && docker-compose -f backend-catalogue/docker-compose.yml build
	cd .. && docker-compose -f backend-coproduction/docker-compose.yml build
	
	# interlinkers
	cd .. && docker-compose -f interlinker-googledrive/docker-compose.yml build
	cd .. && docker-compose -f interlinker-etherpad/docker-compose.yml build
	cd .. && docker-compose -f interlinker-forum/docker-compose.yml build
	cd .. && docker-compose -f interlinker-filemanager/docker-compose.yml build

.PHONY: upb
upb: down net builddev up ## Build and run containers

.PHONY: test
test: upb ## Test containers
	cd ../interlinker-googledrive && ./tests-start.sh
	cd ../interlinker-filemanager && ./tests-start.sh
	cd ../interlinker-etherpad && ./tests-start.sh

.PHONY: seed
seed: ## Set initial data
	cd ../backend-catalogue && make seed
	cd ../backend-coproduction && make seed
	python3 initial_data.py
	
.PHONY: diagrams
diagrams: ## Test containers
	rm -rf images/docker-composes
	mkdir -p images/docker-composes
	sh diagrams.sh 
	find .. -maxdepth 1 -name "*.docker-compose.png" -exec mv -f {} ./docs/images/docker-composes \;