# Базовый образ Jenkins
FROM jenkins/jenkins:lts

# Установка ntpdate и других нужных пакетов
USER root
RUN apt-get update && \
    apt-get install -y ntpdate iputils-ping  chrony python3-pip python3-venv && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Возвращаемся к пользователю Jenkins
USER jenkins