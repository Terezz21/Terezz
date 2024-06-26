import random
import os
from github import Github
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Telegram bot token
TELEGRAM_BOT_TOKEN = '7153583503:AAEzqUTYxjIKYghEvEb6rCsW453xXpeDYUc'

# GitHub access token and repository details
GITHUB_ACCESS_TOKEN = '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'
GITHUB_REPO_NAME = 'Terezz21'
GITHUB_FILE_PATH = 'users_with_numbers.txt'

# Function to generate Hormuud numbers
def generate_hormuud_numbers(n):
    numbers = []
    prefixes = ['61', '68']
    for _ in range(n):
        prefix = random.choice(prefixes)
        number = prefix + ''.join([str(random.randint(0, 9)) for _ in range(7)])
        numbers.append(number)
    return numbers

# Function to generate random names
def generate_random_names(n):
    first_names = ["Ahmed", "Fatima", "Hassan", "Khadija", "Mohamed", "Asha", "Yusuf", "Zahra", "Ali", "Maryam"]
    last_names = ["Ali", "Mohamed", "Hussein", "Abdi", "Ahmed", "Ismail", "Hassan", "Yusuf", "Farah", "Nur"]
    names = []
    for _ in range(n):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        name = f"{first_name} {last_name}"
        names.append(name)
    return names

# Function to generate users with numbers
def generate_users_with_numbers(num_users):
    names = generate_random_names(num_users)
    numbers = generate_hormuud_numbers(num_users)
    users = list(zip(names, numbers))
    return users

# Telegram command handler
def start(update: Update, context: CallbackContext) -> None:
    num_users = 20  # Change this to generate a different number of users
    users_with_numbers = generate_users_with_numbers(num_users)
    
    # Prepare the message
    message = '\n'.join([f"{name}: {number}" for name, number in users_with_numbers])
    
    # Send the message to the Telegram chat
    update.message.reply_text(message)
    
    # Prepare the content for GitHub
    github_content = '\n'.join([f"{name}: {number}" for name, number in users_with_numbers])
    
    # Connect to GitHub
    g = Github(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)
    repo = g.get_repo(botftbot)
    
    # Create or update the file on GitHub
    try:
        contents = repo.get_contents(Botft)
        repo.update_file(contents.path, "Updated users with numbers", github_content, contents.sha)
    except:
        repo.create_file(GITHUB_FILE_PATH, "Created users with numbers", github_content)
    
def main() -> None:
    # Set up the Updater and Dispatcher
    updater = Updater(7153583503:AAEzqUTYxjIKYghEvEb6rCsW453xXpeDYUc)
    dispatcher = updater.dispatcher
    
    # Register the /start command handler
    dispatcher.add_handler(CommandHandler("start", start))
    
    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
