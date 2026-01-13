#!/bin/bash

# Скрипт для развертывания бэкенда
# Клонирует или обновляет код, устанавливает зависимости и запускает приложение

DEPLOY_PATH="/home/app"
REPO_URL="https://github.com/bannyvey/twitter-DDD.git"

echo "Начинаем развертывание бэкенда в $DEPLOY_PATH"

# Создаем директорию если не существует
if [ ! -d "$DEPLOY_PATH" ]; then
  echo "Клонируем репозиторий..."
  git clone $REPO_URL $DEPLOY_PATH
else
  echo "Обновляем код..."
  cd $DEPLOY_PATH
  git pull origin main
fi

cd $DEPLOY_PATH

# Устанавливаем зависимости
echo "Устанавливаем зависимости..."
uv pip install -r requirements.txt

# Запускаем через Docker Compose
echo "Запускаем приложение..."
docker-compose down
docker-compose up -d

echo "Развертывание бэкенда завершено"
