import json
import sys
import re

def solve():
    # Чтение JSON объекта
    line = sys.stdin.readline()
    if not line:
        return
    try:
        data = json.loads(line.strip())
    except:
        return

    # Чтение количества запросов
    line = sys.stdin.readline()
    if not line:
        return
    q = int(line.strip())

    for _ in range(q):
        query = sys.stdin.readline().strip()
        if not query:
            continue
        
        # Разбор пути на токены (ключи и индексы)
        # Например: user.friends[0].name -> ['user', 'friends', '[0]', 'name']
        tokens = re.findall(r'[^.\[\]]+|\[\d+\]', query)
        
        current = data
        possible = True
        
        for token in tokens:
            try:
                if token.startswith('[') and token.endswith(']'):
                    # Это индекс массива
                    index = int(token[1:-1])
                    if isinstance(current, list) and 0 <= index < len(current):
                        current = current[index]
                    else:
                        possible = False
                        break
                else:
                    # Это ключ объекта
                    if isinstance(current, dict) and token in current:
                        current = current[token]
                    else:
                        possible = False
                        break
            except:
                possible = False
                break
        
        if possible:
            # Вывод результата в компактном JSON формате
            print(json.dumps(current, separators=(',', ':')))
        else:
            print("NOT_FOUND")

if __name__ == "__main__":
    solve()