import os
import re
import requests
from datetime import datetime

TOKEN = os.getenv("BALE_TOKEN")
SOURCE = os.getenv("SOURCE_CHANNEL")
TARGET = os.getenv("TARGET_CHANNEL")

ADD_PRICE = 50000

def get_messages():
    # بعداً اتصال کامل بله را اینجا قرار می‌دهیم
    return None

def convert_price(text):
    numbers = re.findall(r'\d[\d,]*', text)

    if len(numbers) < 4:
        return None

    values = [int(x.replace(",", "")) for x in numbers[:4]]

    values = [x + ADD_PRICE for x in values]

    return f"""🟡 آبشده محمدلو

📊 قیمت لحظه‌ای طلا

🟢🔻 خرید: {values[0]:,}
🔴🔻 فروش: {values[1]:,}

🟢🔻 گرم خرید: {values[2]:,}
🔴🔻 گرم فروش: {values[3]:,}

⏰ {datetime.now().strftime('%H:%M')}
"""

print("Gold bot running...")
