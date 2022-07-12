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
docker-compose -f frontend/docker-compose.yml down --remove-orphans
docker-compose -f backend-catalogue/docker-compose.yml down --remove-orphans
docker-compose -f backend-coproduction/docker-compose.yml down --remove-orphans
docker-compose -f backend-auth/docker-compose.yml down --remove-orphans
docker-compose -f backend-logging/docker-compose.yml down --remove-orphans
docker-compose -f interlinker-googledrive/docker-compose.yml down --remove-orphans
docker-compose -f interlinker-ceditor/docker-compose.yml down --remove-orphans
docker-compose -f interlinker-survey/docker-compose.yml down --remove-orphans
docker-compose -f interlink-project/envs/local/docker-compose.yml down --remove-orphans

:Setup
git clone https://github.com/interlink-project/frontend
git clone https://github.com/interlink-project/backend-auth
git clone https://github.com/interlink-project/backend-catalogue
git clone https://github.com/interlink-project/backend-coproduction
git clone https://github.com/interlink-project/backend-logging
git clone https://github.com/interlink-project/interlinker-googledrive
git clone https://github.com/interlink-project/interlinker-survey
git clone https://github.com/interlink-project/interlinker-ceditor

:Build
docker-compose -f frontend/docker-compose.yml build
docker-compose -f backend-catalogue/docker-compose.yml build
docker-compose -f backend-coproduction/docker-compose.yml build
docker-compose -f backend-auth/docker-compose.yml build
docker-compose -f backend-logging/docker-compose.yml build
docker-compose -f interlinker-googledrive/docker-compose.yml build
docker-compose -f interlinker-ceditor/docker-compose.yml build
docker-compose -f interlinker-survey/docker-compose.yml build
docker-compose -f interlink-project/envs/local/docker-compose.yml build

:Run
GOTO Down
GOTO Net
docker-compose -f frontend/docker-compose.yml up -d
docker-compose -f backend-catalogue/docker-compose.yml up -d
docker-compose -f backend-coproduction/docker-compose.yml up -d
docker-compose -f backend-auth/docker-compose.yml up -d
docker-compose -f backend-logging/docker-compose.yml up -d
docker-compose -f interlinker-googledrive/docker-compose.yml up -d
docker-compose -f interlinker-ceditor/docker-compose.yml up -d
docker-compose -f interlinker-survey/docker-compose.yml up -d
docker-compose -f interlink-project/envs/local/docker-compose.yml up -d

GOTO End


:End