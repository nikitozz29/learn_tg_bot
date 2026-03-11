import openai
import config
from pathlib import Path

from .enums import ResourcePath
from .reader import Reader

class DeepSeekMessage:

    def __init__(self, prompt_name: str):
        self._path = ResourcePath.RESOURCE_DIR.value / ResourcePath.PROMPTS_DIR.value / Path(prompt_name + '.txt')
        self.message_list = []

    async def _init_message(self):
        prompt = await self._load_prompt()
        message = [
            {
                'role': 'system',
                'content': prompt,
            }
        ]
        self.message_list.append(message)

    async def _load_prompt(self):
        reader = Reader(self._path)
        response = await reader.load()
        return response

class DeepSeek:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self._token = config.DEEP_SEEK_TOKEN
        self._client = self._create_client()

    def _create_client(self):
        deep_seek_client = openai.AsyncOpenAI(
            api_key=self._token,
            base_url='https://api.deepseek.com/',
        )
        return deep_seek_client
    async def request(self, message: DeepSeekMessage.message_list, model: str = 'deepseek-chat'):

        response = await self._client.chat.completions.create(
            model=model,
            messages=message
        )
        return response.choices[0].message.content

# reader = Reader(
#             enums.ResourcePath.RESOURCE_DIR.value / enums.ResourcePath.PROMPTS_DIR.value / enums.ResourceFileName.RANDOM_FACT.value
#         )
#         prompt = await reader.load()