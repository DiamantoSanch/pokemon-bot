import telebot 
from config import token
from logic import Pokemon
from random import randint

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username, randint(140, 160), randint(20, 30))
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['remove'])
def remove(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        Pokemon.pokemons.pop(message.from_user.username)
        bot.reply_to(message, 'Вы удалили своего покемона')
    else:
        bot.reply_to(message, "У вас еще нет покемона")

@bot.message_handler(commands=['name'])
def get_name(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        bot.reply_to(message, "Ты не создал покемона")
    else:
        bot.reply_to(message, Pokemon.pokemons[message.from_user.username].name)

@bot.message_handler(commands=['pic'])
def get_pic(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        bot.reply_to(message, "Ты не создал покемона")
    else:
        bot.send_photo(message.chat.id, Pokemon.pokemons[message.from_user.username].show_img())

@bot.message_handler(commands=['info'])
def info(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        bot.reply_to(message, "Ты не создал покемона")
    else:
        bot.send_message(message.chat.id, Pokemon.pokemons[message.from_user.username].info())

@bot.message_handler(commands=['attack'])
def attack(message):
    if message.reply_to_message:
        enemy = Pokemon.pokemons[message.reply_to_message.from_user.username]
        #bot.send_message(message.chat.id, enemy.pokemon_trainer)
        me = Pokemon.pokemons[message.from_user.username]
        if enemy.pokemon_trainer in Pokemon.pokemons.keys():
            if me.pokemon_trainer in Pokemon.pokemons.keys():
                if enemy.hp > 0:
                    if me.hp > 0:
                        bot.reply_to(message, me.fight(enemy))
                    else:
                        bot.reply_to(message, 'Ваш покемон был побежден, дождитесь когда он восстановится, чтобы атаковать')
                else:
                    bot.reply_to(message, 'Покемон врага уже побежден, его нельзя атаковать')
            else:
                bot.reply(message, 'У вас должен быть покемон, чтобы атаковать противника')
        else:
            bot.reply_to(message, 'У противника должен быть покемон, чтобы его атаковать')
    else:
        bot.reply_to(message, 'Команда должна быть ответом на сообщение того, кого вы хотите атаковать')


bot.infinity_polling(none_stop=True)
