cd .. 
docker run --rm -it --name dcv -v $(pwd):/input pmsipilot/docker-compose-viz render -m image frontend/docker-compose.devintegrated.yml && mv docker-compose.png frontend.docker-compose.png
docker run --rm -it --name dcv -v $(pwd):/input pmsipilot/docker-compose-viz render -m image backend-coproduction/docker-compose.devintegrated.yml && mv docker-compose.png coproduction.docker-compose.png
docker run --rm -it --name dcv -v $(pwd):/input pmsipilot/docker-compose-viz render -m image backend-catalogue/docker-compose.devintegrated.yml && mv docker-compose.png catalogue.docker-compose.png
docker run --rm -it --name dcv -v $(pwd):/input pmsipilot/docker-compose-viz render -m image backend-auth/docker-compose.devintegrated.yml && mv docker-compose.png auth.docker-compose.png

# interlinkers
docker run --rm -it --name dcv -v $(pwd):/input pmsipilot/docker-compose-viz render -m image interlinker-ceditor/docker-compose.devintegrated.yml && mv docker-compose.png ceditor.docker-compose.png
docker run --rm -it --name dcv -v $(pwd):/input pmsipilot/docker-compose-viz render -m image interlinker-googledrive/docker-compose.devintegrated.yml && mv docker-compose.png googledrive.docker-compose.png
docker run --rm -it --name dcv -v $(pwd):/input pmsipilot/docker-compose-viz render -m image interlinker-survey/docker-compose.devintegrated.yml && mv docker-compose.png survey.docker-compose.png