from src import queue


async def create(file_ids: list[str]):
    await queue.publish_messages_bulk(file_ids)
