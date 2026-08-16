# =======================================================
# РАЗРАБОТЧИК: Еламан Оспан
# СПЕЦИАЛИЗАЦИЯ: Python Backend & Automation Developer
# ТЕЛЕГРАМ: https://t.me/coderela
# ПРОФИЛЬ FL.RU: https://www.fl.ru/users/elamanospan20/portfolio/
# ГИТХАБ: https://github.com/ela-creatorr
# =======================================================



import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

URL = "https://books.toscrape.com/"
print("\n[СТАРТ] Подключаюсь к интернет-магазину книг: " + URL)

response = requests.get(URL)

if response.status_code == 200:
    print("[УСПЕХ] Сайт загружен. Начинаю сбор товаров...\n")
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Ищем все карточки товаров на странице
    book_cards = soup.find_all("article", class_="product_pod")
    
    # Списки для 4 разных колонок Excel
    titles = []
    prices = []
    availabilities = []
    ratings = []
    
    for index, book in enumerate(book_cards, 1):
        # 1. Извлекаем название книги
        title = book.find("h3").find("a")["title"]
        
        # 2. Извлекаем цену
        price = book.find("p", class_="price_color").text
        
        # 3. Извлекаем статус наличия (В наличии / Нет)
        stock_text = book.find("p", class_="availability").text.strip()
        
        # 4. Извлекаем рейтинг (находится в названии класса, например, "star-rating Three")
        rating_classes = book.find("p", class_="star-rating")["class"]
        rating = rating_classes[1]  # Забирает слово количества звезд (One, Two, Three...)
        
        # Складываем всё в память компьютера
        titles.append(title)
        prices.append(price)
        availabilities.append(stock_text)
        ratings.append(rating)
        
        # Показываем живой процесс сбора в терминале
        print(f"📦 Товар №{index} добавлен:")
        print(f"   📖 Название: {title[:40]}...")
        print(f"   💰 Цена: {price} | ⭐ Рейтинг: {rating} | 📥 Статус: {stock_text}\n")
        
        time.sleep(0.2) # Небольшая пауза для эффекта анимации
        
    # Формируем большую таблицу из 4 колонок
    data = {
        "Название книги": titles,
        "Цена": prices,
        "Рейтинг (звезд)": ratings,
        "Наличие на складе": availabilities
    }
    
    df = pd.DataFrame(data)
    
    output_file = "books_catalog.xlsx"
    df.to_excel(output_file, index=False)
    
    print(f"🎉 [ФИНИШ] Сбор завершен! Создана база данных: '{output_file}'")
else:
    print(f"❌ Ошибка подключения к магазину: {response.status_code}")
