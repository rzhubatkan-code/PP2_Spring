receipt_text = """... (receipt text) ..."""

prices = re.findall(r'(\d[\d\s]*,\d{2})\s+Стоимость', receipt_text)

clean_prices = [p.replace(' ', '') for p in prices]
print("All prices", clean_prices) # Find all prices 

product_names = re.findall(r'\d+\.\s*\n(.*?)\n', receipt_text)

print("Product name")
for name in product_names:
    print(f"- {name.strip()}") #Find all product names

    total_match = re.search(r'ИТОГО:\s*([\d\s]+,\d{2})', receipt_text)
if total_match:
    total_str = total_match.group(1).replace(' ', '').replace(',', '.')
    total_amount = float(total_str)
    print(f"Total sum {total_amount} tenge") # Calculate total amount

    date_time = re.search(r'(\d{2}\.\d{2}\.\d{4}\s\d{2}:\d{2}:\d{2})', receipt_text)

if date_time:
    print(f"Data and time: {date_time.group(1)}") #Date and time

    payment_method = re.search(r'([А-Яа-я\s]+):\s*[\d\s]+,\d{2}\s*ИТОГО', receipt_text)

if payment_method:
    print(f"Payment method: {payment_method.group(1).strip()}") # Find Payment method

    import re
import json

def parse_receipt(text):

    items = []
    pattern = r'\d+\.\s*\n(.*?)\n.*?\n([\d\s]+,\d{2})\s+Стоимость'
    matches = re.findall(pattern, text, re.DOTALL)
    
    for name, price in matches:
        items.append({
            "name": name.strip(),
            "price": float(price.replace(' ', '').replace(',', '.'))
        })

    # 2. Метаданные
    total = re.search(r'ИТОГО:\s*([\d\s]+,\d{2})', text).group(1)
    date_time = re.search(r'Время:\s*([\d\s.:]+)', text).group(1)
    payment = re.search(r'([А-Яа-я\s]+):\s*[\d\s]+,\d{2}\s*ИТОГО', text).group(1)

    output = {
        "store": "EUROPHARMA",
        "date_time": date_time.strip(),
        "payment_method": payment.strip(),
        "items": items,
        "total_amount": float(total.replace(' ', '').replace(',', '.'))
    }
    return json.dumps(output, ensure_ascii=False, indent=4)

print(parse_receipt(receipt_text)) #JSON



