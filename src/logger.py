from datetime import datetime


def info(*args):
    timestamp = datetime.utcnow()
    print(f'{timestamp} INFO:\t', *args)
