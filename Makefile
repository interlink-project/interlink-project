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
	cd .. && git clone https://github.com/interlink-project/backend-catalogue
	cd .. && git clone https://github.com/interlink-project/backend-coproduction
	cd .. && git clone https://github.com/interlink-project/backend-channels
	# interlinkers
	cd .. && git clone https://github.com/interlink-project/interlinker-survey
	cd .. && git clone https://github.com/interlink-project/interlinker-googledrive
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
	
.PHONY: down
down: ## Stops all containers and removes volumes
	cd ../backend-acl && make down
	cd ../backend-auth && make down
	cd ../backend-catalogue && make down
	cd ../backend-coproduction && make down
	cd ../backend-channels && make down

	# interlinkers
	cd ../interlinker-etherpad && make down
	cd ../interlinker-googledrive && make down
	cd ../interlinker-survey && make down

	cd ../frontend && make down
	cd ../backend-proxy && make down
	docker network rm traefik-public || true

.PHONY: up
up: down net ## Run containers (restarts them if already running)
	cd ../backend-proxy && make up

	# platform components
	cd ../backend-acl && make integrated
	cd ../backend-auth && make integrated
	cd ../backend-catalogue && make integrated
	cd ../backend-coproduction && make integrated
	cd ../backend-channels && make integrated

	# interlinkers
	cd ../interlinker-etherpad && make integrated
	cd ../interlinker-googledrive && make integrated
	cd ../interlinker-survey && make integrated

	# frontend
	cd ../frontend && make integrated

.PHONY: restart
restart: ## Run containers (restarts them if already running)
	cd ../backend-proxy && make up
	cd ../backend-auth && make integrated
	cd ../backend-catalogue && make integrated
	cd ../backend-coproduction && make integrated
	cd ../backend-channels && make integrated
	cd ../backend-acl && make integrated

	cd ../interlinker-googledrive && make integrated
	cd ../interlinker-survey && make integrated
	cd ../interlinker-etherpad && make integrated

.PHONY: devbuild
devbuild: ## Build containers
	cd ../backend-proxy && make up
	cd ../backend-auth && make devbuild
	cd ../backend-catalogue && make devbuild
	cd ../backend-coproduction && make devbuild
	cd ../backend-channels && make devbuild
	cd ../backend-acl && make devbuild
	
	# interlinkers
	cd ../interlinker-etherpad && make devbuild
	cd ../interlinker-googledrive && make devbuild
	cd ../interlinker-survey && make devbuild
	cd ../frontend && make devbuild

.PHONY: prodbuild
prodbuild: ## Build containers
	cd ../backend-acl && make prodbuild
	cd ../backend-auth && make prodbuild
	cd ../backend-catalogue && make prodbuild
	cd ../backend-coproduction && make prodbuild
	cd ../backend-channels && make prodbuild
	cd ../backend-proxy && make up

	# interlinkers
	cd ../interlinker-etherpad && make prodbuild
	cd ../interlinker-googledrive && make prodbuild
	cd ../interlinker-survey && make prodbuild
	cd ../frontend && make prodbuild

.PHONY: upb
upb: down net builddev up ## Build and run containers

.PHONY: seed
seed: ## Set initial data
	cd ../backend-catalogue && make seed
	cd ../backend-coproduction && make seed
	
.PHONY: diagrams
diagrams: ## Test containers
	rm -rf images/docker-composes
	mkdir -p images/docker-composes
	sh diagrams.sh 
	find .. -maxdepth 1 -name "*.docker-compose.png" -exec mv -f {} ./docs/images/docker-composes \;