#!/bin/bash

# Команды для установки необходимых инструментов на сервере Ubuntu 22.04

# Обновляем список пакетов
apt update

# Устанавливаем git
apt install -y git

# Устанавливаем uv (Python package manager)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Добавляем uv в PATH (может потребоваться перезапуск сессии)
export PATH="$HOME/.cargo/bin:$PATH"

# Устанавливаем Docker
apt install -y docker.io

# Устанавливаем Docker Compose (версия 1, так как скрипт использует docker-compose с дефисом)
apt install -y docker-compose

# Запускаем Docker сервис
systemctl start docker
systemctl enable docker

echo "Установка завершена. Теперь можно запускать deploy_backend.sh"
