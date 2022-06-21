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
	cd .. && git clone https://github.com/interlink-project/backend-auth
	cd .. && git clone https://github.com/interlink-project/backend-catalogue
	cd .. && git clone https://github.com/interlink-project/backend-coproduction
	cd .. && git clone https://github.com/interlink-project/backend-logging

	# interlinkers
	cd .. && git clone https://github.com/interlink-project/interlinker-survey
	cd .. && git clone https://github.com/interlink-project/interlinker-googledrive
	cd .. && git clone https://github.com/interlink-project/interlinker-ceditor
  
.PHONY: down
down: ## Stops all containers and removes volumes
	cd ../backend-auth && make down
	cd ../backend-catalogue && make down
	cd ../backend-coproduction && make down
	cd ../backend-logging && make down

	# interlinkers
	cd ../interlinker-ceditor && make down
	cd ../interlinker-googledrive && make down
	cd ../interlinker-survey && make down

	# cd ../frontend && make down
	
	cd ./envs/local && docker-compose down --remove-orphans
	docker network rm traefik-public || true

.PHONY: start
start: down net ## Run containers (restarts them if already running)
	cd ./envs/local && docker-compose up -d

	# platform components
	cd ../backend-auth && make integrated
	cd ../backend-catalogue && make integrated
	cd ../backend-coproduction && make integrated
	cd ../backend-logging && make integrated

	# interlinkers
	# cd ../interlinker-ceditor && make integrated
	cd ../interlinker-googledrive && make integrated
	cd ../interlinker-survey && make integrated

	# frontend
	# cd ../frontend && make integrated

.PHONY: build
build: ## Build containers
	cd ./envs/local && docker-compose build

	cd ../backend-auth && make build
	cd ../backend-catalogue && make build
	cd ../backend-coproduction && make build
	cd ../backend-logging && make build
	
	# interlinkers
	cd ../interlinker-ceditor && make build
	cd ../interlinker-googledrive && make build
	cd ../interlinker-survey && make build

	cd ../frontend && make build

.PHONY: upb
upb: down net build up ## Build and run containers

.PHONY: seed
seed: ## Set initial data
	cd ../backend-catalogue && make localseed
	cd ../backend-coproduction && make seed
	
.PHONY: applymigrations
applymigrations: ## Set initial data
	# cd ../backend-coproduction && make migrations message="treeitems"
	cd ../backend-catalogue && make applymigrations
	cd ../backend-coproduction && make applymigrations
	
.PHONY: restartcontainers
restartcontainers: ## Run containers (restarts them if already running)
	cd ./envs/local && docker-compose down --remove-orphans
	cd ./envs/local && docker-compose up -d

	cd ../backend-auth && make integrated
	cd ../backend-catalogue && make integrated
	cd ../backend-coproduction && make integrated
	cd ../backend-logging && make integrated

	cd ../interlinker-googledrive && make integrated
	cd ../interlinker-survey && make integrated
	# cd ../interlinker-ceditor && make integrated

	# cd ../frontend && make integrated

.PHONY: restart
restart: restartcontainers applymigrations seed ## Run containers (restarts them if already running)	

.PHONY: fullrestart
fullrestart:
	make down
	docker volume prune -f
	make start
	# cd ../backend-catalogue && make migrations message="treeitems"
	# cd ../backend-coproduction && make migrations message="treeitems"
	make applymigrations
	make seed

.PHONY: up
up: start applymigrations seed ## Run containers and seeds them with data
	
.PHONY: diagrams
diagrams: ## Test containers
	rm -rf images/docker-composes
	mkdir -p images/docker-composes
	sh diagrams.sh 
	find .. -maxdepth 1 -name "*.docker-compose.png" -exec mv -f {} ./docs/source/components/docker-composes \;