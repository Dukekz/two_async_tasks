import asyncio
from typing import Coroutine, List


async def run_first_service():
    await asyncio.sleep(1)
    print("First service is run forever, press Ctrl+C to stop")
    await asyncio.Future()
    

async def run_second_service():
    await asyncio.sleep(1)
    print("Second service is run forever, press Ctrl+C to stop")
    await asyncio.Future()
    

async def main(tasks: List[Coroutine]):
    results = await asyncio.gather(*tasks)
    return results


if __name__ == "__main__":
    try:
        tasks = [run_first_service(), run_second_service()]
        with asyncio.Runner() as runner:
            runner.run(main(tasks))
    except KeyboardInterrupt:
        pass
