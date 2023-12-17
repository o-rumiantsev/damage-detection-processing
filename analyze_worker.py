import asyncio

from src.core.analysis import analyze_file
from src.queue import process_messages

asyncio.run(process_messages(analyze_file))
