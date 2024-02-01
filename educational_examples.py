"""
L
E
G
B
Акроним LEGB представляет собой порядок поиска переменных в Python,
в который описывает четыре различные области видимости в которых интерпретатор ищет значения переменных.
LEGB расшифровывается следующим образом:
Local (локальная): Переменные, определенные внутри функции, считаются локальными и видны только в пределах этой функции
Enclosing (внешняя): Эта область связана с поиском переменных в объемлющих функциях. Если у вас есть вложенные функции,
внутренние функции имеют доступ к переменным внешней (объемлющей) функции.
Global (глобальная): Переменные, определенные на верхнем уровне файла или явно помеченные как глобальные,
находятся в глобальной области видимости. Они доступны из любого места в файле.
Built-in (встроенная): Эта область видимости связана с встроенными именами в Python,
такими как print, len, str и другие. Эти имена всегда доступны в любой области видимости без явного импорта.
При поиске значения переменной интерпретатор Python сначала проверяет локальную область видимости (Local),
затем область внешних функций (Enclosing), далее глобальную (Global) и, наконец, встроенную (Built-in),
если переменная не найдена в предыдущих областях. Этот порядок обеспечивает правильный поиск
и использование переменных в различных частях программы."""
from time import sleep, time

CACHE = {}


def slow(n, a):
    global CACHE
    #  Указывает, что внутри функции будет использоваться глобальная переменная CACHE.
    #  Глобальные переменные могут быть изменены внутри функции,
    #  но для их использования внутри функции необходимо явно указать, что это глобальная переменная.
    key = f'slow_{n}_{a}'
    if key in CACHE:
        return CACHE[key]

    sleep(n)

    result = n ** 2 + a
    CACHE[key] = result
    return result  # Local (локальная)


def slow2(n, a):
    global CACHE
    #  Указывает, что внутри функции будет использоваться глобальная переменная CACHE.
    #  Глобальные переменные могут быть изменены внутри функции,
    #  но для их использования внутри функции необходимо явно указать, что это глобальная переменная.
    key = f'slow2_{n}_{a}'
    if key in CACHE:
        return CACHE[key]

    sleep(n)

    result = n ** 2 - a
    CACHE[key] = result
    return result  # Local (локальная)


start = time()
print(slow(1, 2))
print(slow(2, 1))
print(slow(3, 12))
print(slow(1, 5))
print(slow(2, 7))
print(slow(2, 1))
print(slow2(1, 2))
print(slow2(2, 1))
print(slow2(3, 12))
print(slow2(1, 5))
print(slow2(2, 7))
print(slow2(2, 1))
# print(slow(3))

print(f'Execution time {time() - start}')
print(CACHE)