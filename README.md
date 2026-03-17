# Journal Projects

Проект для управления записями пользователей и генерации AI-отчётов через Telegram-бота и FastAPI.

## Структура проекта

```
journal-projects/
├── telegram-journal-bot/   # Telegram-бот для ведения записей
├── sheets-ai-report/       # FastAPI-сервис для генерации отчётов с AI
└── .gitignore             # Исключения для Git (секреты, venv и т.д.)
```

## Компоненты

### 1. telegram-journal-bot

Telegram-бот, который позволяет пользователям:
- Создавать записи в своём журнале
- Отслеживать активность
- Взаимодействовать с системой через удобный интерфейс

**Запуск:**
```bash
cd telegram-journal-bot
python bot.py
```

### 2. sheets-ai-report

FastAPI-сервис для:
- Генерации аналитических отчётов на основе записей
- Интеграции с Google Sheets
- Использования AI для анализа данных

**Запуск:**
```bash
cd sheets-ai-report
uvicorn main:app --reload
```

## Установка

### Требования

- Python 3.8+
- pip
- Виртуальное окружение (рекомендуется)

### Шаги установки

1. Клонировать репозиторий:
```bash
git clone https://github.com/vsanyanov-ux/journal-projects.git
cd journal-projects
```

2. Установить зависимости для каждого компонента:

**Для telegram-journal-bot:**
```bash
cd telegram-journal-bot
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**Для sheets-ai-report:**
```bash
cd sheets-ai-report
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Настроить файлы конфигурации:

- Создать `creds.json` для Google API (в папке `sheets-ai-report`)
- Добавить токены и ключи в `.env` файлы

## Конфигурация

### Переменные окружения

Создайте `.env` файлы в соответствующих папках:

**telegram-journal-bot/.env:**
```env
TELEGRAM_BOT_TOKEN=your_bot_token_here
DATABASE_URL=your_database_url
```

**sheets-ai-report/.env:**
```env
OPENAI_API_KEY=your_openai_key
GOOGLE_CREDENTIALS_PATH=./creds.json
```

### Google Sheets API

1. Создать проект в Google Cloud Console
2. Включить Google Sheets API
3. Создать сервисный аккаунт
4. Скачать `creds.json` и поместить в папку `sheets-ai-report/`

## Развёртывание на сервере

### Systemd Services

На VPS используются systemd-сервисы:

```bash
# Перезапуск служб после обновления кода
systemctl restart telegram-journal-bot
systemctl restart sheets-ai-report

# Проверка статуса
systemctl status telegram-journal-bot
systemctl status sheets-ai-report
```

### Обновление кода

1. Внести изменения в файлы на GitHub
2. На сервере выполнить:
```bash
cd /opt/journal-projects
git pull origin main
systemctl restart telegram-journal-bot
systemctl restart sheets-ai-report
```

## Безопасность

⚠️ **Важно:**
- Никогда не коммитьте файлы `creds.json`, `.env` или другие файлы с секретами
- Все чувствительные данные добавлены в `.gitignore`
- Используйте Personal Access Token для работы с GitHub

## Лицензия

Этот проект создан для личного использования.

## Контакты

Автор: vsanyanov-ux  
GitHub: [vsanyanov-ux](https://github.com/vsanyanov-ux)
