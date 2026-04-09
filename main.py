import asyncio
import aiohttp
from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent
from db import init_db, insert_news
from ai_description import generate_description

BASE_URL = "https://www.24sata.hr/news"
HEADERS = {
    "User-Agent": UserAgent().random
}

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL, headers=HEADERS) as resp:
            html = await resp.text()
            soup = BS(html, "html.parser")
            items = soup.find_all("div", {"class": "card__content"})
            init_db()


            for item in items:
                title_tag = item.find("h2")
                if not title_tag:
                    continue
                title = title_tag.text.strip()
                description = await generate_description(title)


                article = item.find_parent("div", class_="card")
                if not article:
                    continue
                img_tag = article.find("img")

                image_url = img_tag.get("src") if img_tag else None

                link = article.find("a").get("href")
                insert_news(image_url, title, link, description)
                await asyncio.sleep(4)

if __name__ == "__main__":
    asyncio.run(main())