import telebot
import requests

TOKEN = 'ENTER YOUR BOT API'
bot = telebot.TeleBot(TOKEN)
URL = 'https://api.binance.com/api/v3/ticker/price?symbol=BTSUSDT'

@bot.message_handler(commands=['start'])
def send_welcome(message):
	print(message.text)
	bot.reply_to(message, "سلام:)  خیلی خوش اومدی به ربات کریپتو چیکار میتونم براتون کنم؟!")


@bot.message_handler(commands=['info'])
def send_info(message):
	print(message.text)
	bot.reply_to(message, 'خب اول از اینکه سلام !، خب حقیقتا این بات برای قیمت دهی زنده ارز های دیجیتاله و شما به راحتی با وارد کردن سیمبول مناسب قیمت اون ارز که میخواید رو بدست میارید')

@bot.message_handler(commands=['ID'])
def send_id(message):
	print(message.text)
	bot.reply_to(message, 'اگر نظر جذابی برای بات دارید یا میخواید ازش انتقادی کنید به این ایدی پیام خودتون رو بفرستید @sumset63holy')

@bot.message_handler(commands=['guid'])
def send_guid(message):
	print(message.text)
	bot.reply_to(message, 'ببین برای اینکه بتونی با بات کار کنی باید از این سیمبول (x)usdt استفاده کنی بجای xتو باید اون ارز مورد نظرت رو بزنی بطور مثال btcusdt الان در اینجا قیمت بیت کوین به دلار به من نمایش داده میشه')


@bot.message_handler(commands=['help'])
def send_help(message):
	print(message.text)
	bot.reply_to(message, '''
	/start for work with bot
	/info for info about bot
	/ID for send your comment to owner
	/guid some exaple of the bot work
	''')


@bot.message_handler(func=lambda m: True)
def show_price(message):
	symbol = message.text.upper()
	respone = requests.get(f'https://api.binance.com/api/v3/ticker/price?symbol={symbol}')
	if respone.status_code == 200:
		data = respone.json()
		bot.reply_to(message,  f'{data['symbol']} price is{data['price']}')
	else:
		bot.reply_to(message, 'این وسط یچی اشتباه ...   /help')

bot.infinity_polling()
