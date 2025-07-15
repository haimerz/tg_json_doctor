# Для подключение библиотеки telebot нужно в google colab добавить: !pip install pyTelegramBotAPI
from telebot import TeleBot, types
import json

# Инициализация бота
bot = TeleBot(token='YOUR_TOKEN', parse_mode='html')

# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    # отправляем ответ на команду '/start'
    bot.send_message(
        chat_id=message.chat.id,
        text='🩺 *Добро пожаловать в JSON-клинику!*\n\n'
             'Я ваш код-терапевт, готовый диагностировать и лечить JSON-строки.\n\n'
             'Пришлите мне JSON для обследования, и я:\n'
             '• Проверю его валидность\n'
             '• Отформатирую для лучшей читаемости\n'
             '• Подсвечу структуру\n\n'
             'Жду вашего пациента (JSON-строку) на осмотр!',
        parse_mode='Markdown'
    )

# обработчик всех остальных сообщений
@bot.message_handler()
def message_handler(message: types.Message):
    try:
        # пытаемся распарсить JSON из текста сообщения
        payload = json.loads(message.text)
    except json.JSONDecodeError as ex:
        # при ошибке взникнет исключение 'json.JSONDecodeError'
        # преобразовываем исключение в строку и выводим пользователю
        error_msg = str(ex).replace('Expecting', 'Ожидается').replace('line', 'строка')
        bot.send_message(
            chat_id=message.chat.id,
            text=f'🚨 *Экстренный диагноз!*\n\n'
                 f'Обнаружена синтаксическая травма:\n'
                 f'<code>{error_msg}</code>\n\n'
                 f'💊 Рекомендации:\n'
                 f'1. Проверьте указанное место\n'
                 f'2. Исправьте ошибку\n'
                 f'3. Повторите отправку',
            parse_mode='HTML'
        )
        # выходим из функции
        return
    
    # если исключения не возникло - значит был введен корректный JSON
    # форматируем его в красивый текст :) (отступ 2 пробела на уровень, сортировать ключи по алфавиту)
    text = json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False)
    # и выводим пользователю
    bot.send_message(
        chat_id=message.chat.id,
        text=f'🏥 *Результаты обследования* 🏥\n\n'
             f'✅ Пациент абсолютно здоров!\n'
             f'📋 Красиво оформленный JSON:\n'
             f'<code>{text}</code>\n\n'
             f'💉 Лечение успешно завершено!',
        parse_mode='HTML'
    )


# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()


if __name__ == '__main__':
    main()