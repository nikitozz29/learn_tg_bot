import aiofiles



class Reader:

    def __init__(self, path: str):
        self._path = path

    async def load(self) -> str:
        async with aiofiles.open(self._path, 'r', encoding='UTF-8') as file:
            response = await file.read()
            return response