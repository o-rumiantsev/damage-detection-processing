import asyncio

from src.core.analysis.analyze_file import analyze_file
from src.queue import process_messages

asyncio.run(process_messages(analyze_file))
