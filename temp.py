from flask import Flask, render_template
import aiogram as ai

bot = ai.Bot(token='5964735418:AAED-s-7mmcK7x5AD2rRjjjRUbFZloHC78g')
fit = ai.Dispatcher(bot)

app = Flask(__name__)


@fit.message_handler(commands='start')
async def a3(sms: ai.types.message):
    await sms.answer("hi")


@app.route('/')
def a1():
    return render_template("conta.html", vh="1")


if __name__ == '__main__':
    while 1:
        ai.executor.start_polling(fit, skip_updates=0)
        app.run()