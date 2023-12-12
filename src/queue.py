import asyncio

from aio_pika import connect, IncomingMessage, ExchangeType, Message

from src import logger


async def get_connection():
    connection = await connect("amqp://user:password@localhost:35672")
    channel = await connection.channel(publisher_confirms=False)
    exchange = await channel.declare_exchange('test_exchange', ExchangeType.DIRECT)
    queue = await channel.declare_queue('test_queue', durable=True)
    await queue.bind(exchange, routing_key='test')
    return connection, channel


async def publish_message(message):
    connection, channel = await get_connection()
    exchange = await channel.get_exchange('test_exchange')

    message = Message(message.encode())

    await exchange.publish(message, routing_key='test')

    await connection.close()


async def publish_messages_bulk(messages):
    connection, channel = await get_connection()
    exchange = await channel.get_exchange('test_exchange')

    for message in messages:
        rmq_message = Message(message.encode())
        await exchange.publish(rmq_message, routing_key='test')
        logger.info(f' [queue] Sent message "{message}"')

    await connection.close()


async def process_messages(handler):
    connection, channel = await get_connection()
    queue = await channel.get_queue('test_queue')

    async def on_message(message: IncomingMessage):
        async with message.process():
            body = message.body.decode()
            logger.info(f' [queue] Received message "{body}"')
            await handler(body)
            logger.info(f' [queue] Handled message "{body}"')

    await queue.consume(on_message)

    await asyncio.Future()