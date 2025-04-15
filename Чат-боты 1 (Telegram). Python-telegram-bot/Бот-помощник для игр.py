# Импортируем необходимые классы.
import logging
import os
import random
from telegram.ext import Application, MessageHandler, filters, CommandHandler
from telegram import ReplyKeyboardMarkup
from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)
reply_keyboard = [['/dice', '/timer']]
dice_keyboard = [['/6', '/20'],
                  ['/6x2'],
                    ['/back']]
time_keyboard = [['/30sec'],
                  ['/1min'], ['/5min'],
                    ['/back']]
markup_start = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
markup_dice = ReplyKeyboardMarkup(dice_keyboard, one_time_keyboard=False)
markup_timer = ReplyKeyboardMarkup(time_keyboard, one_time_keyboard=False)
markup_timer_close = ReplyKeyboardMarkup([['/close']], one_time_keyboard=False)
logger = logging.getLogger(__name__)


async def start(update, context):
    """Отправляет сообщение когда получена команда /start"""
    user = update.effective_user
    await update.message.reply_html(
        rf"Привет {user.mention_html()}! Я бот помощник по играм",
    reply_markup=markup_start)


async def dice(update, context):
    """Отправляет сообщение когда получена команда /dice"""
    user = update.effective_user
    await update.message.reply_html("Выберите, что кинуть", reply_markup=markup_dice)


async def dice_6(update, context):
    """Отправляет сообщение когда получена команда /dice"""
    await update.message.reply_html(f'{random.randint(1, 6)}', reply_markup=markup_dice)


async def dice_20(update, context):
    """Отправляет сообщение когда получена команда /dice"""
    await update.message.reply_html(f'{random.randint(1, 20)}', reply_markup=markup_dice)


async def dice_6x2(update, context):
    """Отправляет сообщение когда получена команда /dice"""
    await update.message.reply_html(f'{random.randint(1, 6)}, {random.randint(1, 6)}', reply_markup=markup_dice)


async def back(update, context):
    user = update.effective_user
    await update.message.reply_html(
        rf"Привет {user.mention_html()}! Я бот помощник по играм",
    reply_markup=markup_start)


async def timer(update, context):
    """Отправляет сообщение когда получена команда /dice"""
    user = update.effective_user
    await update.message.reply_html("Выберите, сколько времени засечь", reply_markup=markup_timer)


async def sec_30(update, context):
    await set_timer(update, context, 30, 'cекунд')


async def task(context, TIMER, time):
    """Выводит сообщение"""
    await context.bot.send_message(context.job.chat_id, text=f'КУКУ! {TIMER}{time} прошли!')


def remove_job_if_exists(name, context):
    """Удаляем задачу по имени.
    Возвращаем True если задача была успешно удалена."""
    current_jobs = context.job_queue.get_jobs_by_name(name)
    if not current_jobs:
        return False
    for job in current_jobs:
        job.schedule_removal()
    return True


# Обычный обработчик, как и те, которыми мы пользовались раньше.
async def set_timer(update, context, TIMER, time):
    """Добавляем задачу в очередь"""
    chat_id = update.effective_message.chat_id
    # Добавляем задачу в очередь
    # и останавливаем предыдущую (если она была)
    job_removed = remove_job_if_exists(str(chat_id), context)
    context.job_queue.run_once(task, TIMER, chat_id=chat_id, name=str(chat_id), data=TIMER)

    text = f'Вернусь через {TIMER}{time}!'
    if job_removed:
        text += ' Старая задача удалена.'
    await update.effective_message.reply_text(text)


async def unset(update, context):
    """Удаляет задачу, если пользователь передумал"""
    chat_id = update.message.chat_id
    job_removed = remove_job_if_exists(str(chat_id), context)
    text = 'Таймер отменен!' if job_removed else 'У вас нет активных таймеров'
    await update.message.reply_text(text)


def main():
    # Создаём объект Application.
    # Вместо слова "TOKEN" надо разместить полученный от @BotFather токен
    application = Application.builder().token(BOT_TOKEN).build()

    # Создаём обработчик сообщений типа filters.TEXT
    # из описанной выше асинхронной функции echo()
    # После регистрации обработчика в приложении
    # эта асинхронная функция будет вызываться при получении сообщения
    # с типом "текст", т. е. текстовых сообщений.
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("dice", dice))
    application.add_handler(CommandHandler("6", dice_6))
    application.add_handler(CommandHandler("20", dice_20))
    application.add_handler(CommandHandler("6x2", dice_6x2))
    application.add_handler(CommandHandler("back", back))
    application.add_handler(CommandHandler("timer", timer))
    application.add_handler(CommandHandler("30sec", sec_30))
    application.add_handler(CommandHandler("set", set_timer))
    # application.add_handler(CommandHandler("1min", min_1))
    # application.add_handler(CommandHandler("5min", min_5))

    # Запускаем приложение.
    application.run_polling()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()