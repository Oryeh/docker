import os

def run_bot(bot_file):
    try:
        # Загрузка и выполнение бота из файла
        exec(open(bot_file).read())
    except Exception as e:
        print(f"Error running bot: {e}")

if __name__ == "__main__":
    # Путь к файлу бота, который пользователь создал
    user_bot_file = "main.py"
    
    if os.path.exists(user_bot_file):
        run_bot(user_bot_file)
    else:
        print("User bot file not found.")
