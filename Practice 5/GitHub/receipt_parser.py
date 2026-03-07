import re
import json

def parse_receipt(receipt_text):
    
    product_names = re.findall(r'\d+\.\n(.*?)\n\d+,\d+\s+x', receipt_text, re.DOTALL)
    
    
    prices_raw = re.findall(r'x\s+([\d\s,]+)\n', receipt_text)
    
    clean_prices = []
    for p in prices_raw:
        
        p_first_part = p.strip().split()[0]
        
        p_clean = p_first_part.replace(' ', '').replace(',', '.')
        clean_prices.append(float(p_clean))

    def safe_search(pattern, text, group=1):
        match = re.search(pattern, text)
        return match.group(group).strip() if match else None

    
    total_raw = safe_search(r'ИТОГО:\n([\d\s,]+)', receipt_text)
    total_sum = float(total_raw.replace(' ', '').replace(',', '.')) if total_raw else 0.0

    
    date_time = safe_search(r'Время:\s+(\d{2}\.\d{2}\.\d{4}\s+\d{2}:\d{2}:\d{2})', receipt_text)

    
    payment = safe_search(r'(Банковская карта|Наличные)', receipt_text)

    
    output = {
        "store": "EUROPHARMA Астана",
        "date": date_time,
        "payment_method": payment,
        "items": [name.strip().replace('\n', ' ') for name in product_names],
        "item_prices": clean_prices,
        "total_amount": total_sum
    }

    return output


receipt_content = """
ДУБЛИКАТ
Филиал ТОО EUROPHARMA Астана
БИН 080841000762
НДС Серия 58002
 № 0014371
Касса 300-190
Смена 10
Порядковый номер чека №61
Чек №2331180266
Кассир Аптека 17-1
ПРОДАЖА
1.
Натрия хлорид 0,9%, 200 мл, фл
2,000 x 154,00
308,00
Стоимость
308,00
2.
Борный спирт 3%, 20 мл, фл.
1,000 x 51,00
51,00
Стоимость
51,00
3.
Шприц 2 мл, 3-х комп. (Bioject)
2,000 x 16,00
32,00
Стоимость
32,00
4.
Система для инфузии Vogt Medical
2,000 x 60,00
120,00
Стоимость
120,00
5.
Шприц 5 мл, 3-х комп. 
1,000 x 310,00
310,00
Стоимость
310,00
6.
AURA Ватные диски №150
1,000 x 461,00
461,00
Стоимость
461,00
7.
Чистая линия скраб мягкий 50 мл
1,000 x 381,00
381,00
Стоимость
381,00
8.
Чистая линия  скраб очищающийабрикос 50 мл
1,000 x 386,00
386,00
Стоимость
386,00
9.
Чистая линия скраб мягкий 50 мл
1,000 x 381,00
381,00
Стоимость
381,00
10.
Nivea шампунь 3в1мужской  400 мл
1,000 x 414,00
414,00
Стоимость
414,00
11.
Pro Series Шампунь яркий цвет 500мл
1,000 x 841,00
841,00
Стоимость
841,00
12.
Pro Series бальзам-ополаскивательдля длител ухода за окрашеннымиволосами Яркий цвет 500мл
1,000 x 841,00
841,00
Стоимость
841,00
13.
Clear шампунь Актив спорт 2в1мужской  400 мл
1,000 x 1 200,00
1 200,00
Стоимость
1 200,00
14.
Bio World (HYDRO THERAPY)Мицеллярная вода 5в1, 445мл
1,000 x 1 152,00
1 152,00
Стоимость
1 152,00
15.
Bio World (HYDRO THERAPY) Гель-муссдля умывания с гиалуроновойкислотой, 250мл
1,000 x 1 152,00
1 152,00
Стоимость
1 152,00
16.
[RX]-Натрия хлорид 0,9%, 100 мл, фл.
1,000 x 168,00
168,00
Стоимость
168,00
17.
[RX]-Дисоль р-р 400 мл, фл.
1,000 x 163,00
163,00
Стоимость
163,00
18.
Тагансорбент с иономи серебра №30,пор.
1,000 x 1 526,00
1 526,00
Стоимость
1 526,00
19.
[RX]-Церукал 2%, 2 мл, №10, амп.
2,000 x 396,00
792,00
Стоимость
792,00
20.
[RX]-Андазол 200 мг, №40, табл.
1,000 x 7 330,00
7 330,00
Стоимость
7 330,00
Банковская карта:
18 009,00
ИТОГО:
18 009,00
в т.ч. НДС 12%:
0,00
Фискальный признак:
2331180266
Время: 18.04.2019 11:13:58
г. Нур-султан,Казахстан, Мангилик Ел,19, нп-5
Оператор фискальных данных: АО"Казахтелеком"Для проверки чека зайдите на сайт:consumer.oofd.kz
ФИСКАЛЬНЫЙ ЧЕК
ФП
ИНК ОФД: 311559
Код ККМ КГД (РНМ): 620300145311
ЗНМ: SWK00034965
WEBKASSA.KZ
"""

if __name__ == "__main__":
    
    result = parse_receipt(receipt_content)
    
    #
    print(json.dumps(result, ensure_ascii=False, indent=4))