import openai

import config


class DeepSeekMessage:

    def __init__(self, prompt: str):
        self._prompt = prompt
        self.message_list = self._init_message()

    def _init_message(self):
        message = {
            'role': 'system',
            'content': self._prompt,
        }
        return [message]


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
    async def request(self, message: DeepSeekMessage, model: str = 'deepseek-chat'):
        response = await self._client.chat.completions.create(
            model=model,
            messages=message.message_list,
        )
        return response.choices[0].message.content

