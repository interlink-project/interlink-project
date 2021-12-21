@ECHO OFF
CLS
ECHO 1.Build
ECHO 2.Run
ECHO 3.Down
ECHO.

CHOICE /C 123 /M "Enter your choice:"

:: Note - list ERRORLEVELS in decreasing order
IF ERRORLEVEL 3 GOTO Down
IF ERRORLEVEL 2 GOTO Run
IF ERRORLEVEL 1 GOTO Build

:Net
docker network create traefik-public || true

:Down
docker-compose -f frontend/docker-compose.yml down --volumes --remove-orphans
docker-compose -f backend/proxy.docker-compose.yml -f backend/proxy.docker-compose.override.yml down --volumes --remove-orphans
docker-compose -f backend/backend.docker-compose.yml -f backend/backend.docker-compose.override.yml down --volumes --remove-orphans
docker-compose -f backend/monitoring.docker-compose.yml -f backend/monitoring.docker-compose.override.yml down --volumes --remove-orphans
docker-compose -f interlinker-googledrive/docker-compose.yml -f interlinker-googledrive/docker-compose.integrated.yml down --volumes --remove-orphans
docker-compose -f interlinker-etherpad/docker-compose.yml -f interlinker-etherpad/docker-compose.integrated.yml down --volumes --remove-orphans
docker-compose -f interlinker-forum/docker-compose.yml -f interlinker-forum/docker-compose.integrated.yml down --volumes --remove-orphans
docker-compose -f interlinker-filemanager/docker-compose.yml -f interlinker-filemanager/docker-compose.integrated.yml down --volumes --remove-orphans

:Setup
rm -rf .git
git clone https://github.com/interlink-project/backend
git clone https://github.com/interlink-project/frontend
git clone https://github.com/interlink-project/interlinker-filemanager
git clone https://github.com/interlink-project/interlinker-googledrive
git clone https://github.com/interlink-project/interlinker-forum
git clone https://github.com/interlink-project/interlinker-etherpad

:Build
docker-compose -f frontend/docker-compose.yml build
docker-compose -f backend/proxy.docker-compose.yml -f backend/proxy.docker-compose.override.yml build
docker-compose -f backend/backend.docker-compose.yml -f backend/backend.docker-compose.override.yml build
docker-compose -f backend/monitoring.docker-compose.yml -f backend/monitoring.docker-compose.override.yml build
docker-compose -f interlinker-googledrive/docker-compose.yml -f interlinker-googledrive/docker-compose.integrated.yml build
docker-compose -f interlinker-etherpad/docker-compose.yml -f interlinker-etherpad/docker-compose.integrated.yml build
docker-compose -f interlinker-forum/docker-compose.yml -f interlinker-forum/docker-compose.integrated.yml build
docker-compose -f interlinker-filemanager/docker-compose.yml -f interlinker-filemanager/docker-compose.integrated.yml buildGOTO End

:Run
GOTO Down
GOTO Net
docker-compose -f backend/proxy.docker-compose.yml -f backend/proxy.docker-compose.override.yml up -d
docker-compose -f backend/backend.docker-compose.yml -f backend/backend.docker-compose.override.yml up -d
docker-compose -f interlinker-googledrive/docker-compose.yml -f interlinker-googledrive/docker-compose.integrated.yml up -d
docker-compose -f interlinker-etherpad/docker-compose.yml -f interlinker-etherpad/docker-compose.integrated.yml up -d
docker-compose -f interlinker-forum/docker-compose.yml -f interlinker-forum/docker-compose.integrated.yml up -d
docker-compose -f interlinker-filemanager/docker-compose.yml -f interlinker-filemanager/docker-compose.integrated.yml up -d
GOTO End


:End