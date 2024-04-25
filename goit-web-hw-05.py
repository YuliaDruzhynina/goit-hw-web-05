import platform
from datetime import datetime, timedelta
import aiohttp
import asyncio

async def main():

    #async with aiohttp.ClientSession() as session:
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session: #для макбука обязательно иначе Error SSL  
        async with session.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5&date={period}') as response:#id=5 для двух конкретных валют
            result = await response.json()
            return result


if __name__ == "__main__":
    index_day = int(input("Enter the number of days: "))
    day_today = datetime.now()
    results = []
    try:
        if index_day <=10:
            for i in range(1, index_day+1): 
                day_currency = day_today - timedelta(days=i)
                period = day_currency.strftime("%d.%m.%Y")                         
                if platform.system() == 'Windows':
                    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
                r = asyncio.run(main())
                results.append({period: r})
                print(results)
        else: 
            print("Enter number days less than or equal to 10.")        
    except Exception as e:
        print(f"An error occurred: {e}")
             