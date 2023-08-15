import telebot
from telebot import types

bot = telebot.TeleBot('6071585787:AAGJ5VRQtKCgXDrbyTftXkdYTcUybP69K5o')

user_data = {} 

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f"Hello, {message.from_user.first_name}")
    bot.send_message(message.chat.id, "Enter your parameters, to do this enter /parameters.")

@bot.message_handler(commands=['parameters'])
def user_data_age(message):
    bot.send_message(message.chat.id, "Enter your age (years)")
    bot.register_next_step_handler(message, age_info)

def age_info(message):
    user_data[message.chat.id] = {"age": message.text.strip()}
    bot.send_message(message.chat.id, "Enter your gender (female/male)")
    bot.register_next_step_handler(message, gender_info)

def gender_info(message):
    user_data[message.chat.id]["gender"] = message.text.strip()
    bot.send_message(message.chat.id, "Enter your height (cm)")
    bot.register_next_step_handler(message, height_info)

def height_info(message):
    user_data[message.chat.id]["height"] = float(message.text.strip())
    bot.send_message(message.chat.id, "Enter your weight (kg)")
    bot.register_next_step_handler(message, weight_info)

def weight_info(message):
    user_data[message.chat.id]["weight"] = float(message.text.strip())
    bot.send_message(message.chat.id, "Enter your activity level (ranging from 1 to 5)")
    bot.register_next_step_handler(message, activitylev_info)

def activitylev_info(message):
    user_data[message.chat.id]["activitylev"] = int(message.text.strip())
    data = user_data[message.chat.id]
    result = f"Name: {message.from_user.first_name}\nAge: {data['age']}\nGender: {data['gender']}\nHeight: {data['height']}\nWeight: {data['weight']}\nActivity Level: {data['activitylev']}"
    bot.send_message(message.chat.id, result)
    parameters_info(message)

def parameters_info(message):
    markup = types.ReplyKeyboardMarkup()  
    btn1 = types.KeyboardButton("Confirm parameters")
    btn2 = types.KeyboardButton("Change parameters")
    markup.row(btn1, btn2)
    bot.send_message(message.chat.id, "Choose an option:", reply_markup=markup)