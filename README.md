<h2>Телеграм бот с функцией валидации и бьютифаера JSON</h2>

> **Статус проекта:**
>
> 🟢 Поддерживается (активный) 

## Цели и Задачи
Помочь тестировщику быстрее проверить JSON на нарушение синтаксиса

Этот бот при получении JSON:
* Проверяет на ошибки синтаксиса
* Возвращает JSON в удобочитаемом формате

## 🖼 Скриншоты

Стартовое меню:

![image](https://raw.githubusercontent.com/haimerz/tg_json_doctor/refs/heads/main/static/welcome_page.png)

После отправки JSON c ошибкой:

![image](https://raw.githubusercontent.com/haimerz/tg_json_doctor/refs/heads/main/static/fail.png)

Пример работы бьютифаера:

![image](https://raw.githubusercontent.com/haimerz/tg_json_doctor/refs/heads/main/static/success.png)


## 💻 Технологии

* Python
* Библиотека `telebot`

## ⏬ Установка на локальном компьютере

1. Скачать проект
   
2. Создать бота и через [@BotFather](https://t.me/BotFather) и вставить в проекте свой токен от бота

3. Создаём виртуальное окружение внутри папки проекта.
Далее команды для MacOS (для windows инуструкция [есть вот тут](https://realpython.com/python-virtual-environments-a-primer/#create-it))

``` markdown
python3 -m venv venv
```

``` markdown
source venv/bin/activate
```
4. Устанавливаем библиотеки

``` markdown
python3 -m pip install pyTelegramBotAPI
```


5. Запускаем
``` markdown
python3 json_bot.py
```

## Автор

Валерия Успенская ([@haimerzz](https://t.me/haimerzz))
