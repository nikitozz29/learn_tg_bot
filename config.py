import dotenv
import os

dotenv.load_dotenv()

BOT_TOKEN= os.getenv('BOT_TOKEN')
DEEP_SEEK_TOKEN = os.getenv('DEEP_SEEK_TOKEN')
# PROXY = f'https://{os.getenv("PROXY")}'
# PROXY = f'https://openai.javarush.com/v1'