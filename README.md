## YaCut

## Описание
YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис. 

## Стек использованных технологий
- Python 
- Flask
- Flask-SQLAlchemy
- Flask-WTF

## Как развернуть проект
```
git clone https://github.com/MrEgor123/yacut
```

## Команды запуска
Создать вирутальное окружение:
```
python3 -m venv venv
```
Активировать виртуальное окржуение (Windows / Linux(MacOS)):
```
venv\Scripts\activate.bat
```
```
source venv/bin/activate
```
Установить зависимости:
```
pip install -r requirements.txt
```
Отредактировать и переименовать  `.env.template`. в  `.env` 
Применить миграции:
```
flask db upgrade
```
Запустить сервер:
```
flask run
```
web интерфейс будет доступен по адресу: http://localhost:5000/

## Автор
- Чарушин Егор
- Профиль GitHub: https://github.com/MrEgor123
