# two_async_tasks
 Run two different asyncio tasks on one event loop.

 For example, I needed to run RabbitMQ aio-pika consumer and a web service with aiohttp library, together on one event loop.

 With upgrading some projects to python 3.11+ I encountered that now it's not recomended to use event loop directly
 that's why I tryed don't use this scheme tested years ago:

 loop = asyncio.get_event_loop()
 future = asyncio.gather(
     run_first_service_forever(),
     run_second_service_forever(),
 )
 loop.run_until_complete(future)
