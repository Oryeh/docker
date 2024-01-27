FROM python:3.10

# Установка рабочей директории в контейнере
WORKDIR /usr/src/app

# Копирование зависимостей проекта и установка их
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Копирование всего содержимого текущей директории в рабочую директорию
COPY . .

# Команда для запуска вашего бота
CMD ["python", "bot.py"]
