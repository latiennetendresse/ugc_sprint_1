from aiohttp import ClientSession

session: ClientSession | None = None


async def get_auth_session() -> ClientSession:
    return session
