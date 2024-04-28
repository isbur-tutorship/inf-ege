# ЕГЭ информатика 2024. Повторение

## Содержание
0.  [Введение в программирование](#введение-в-программирование)
2.  [Задание 2 (анализ логического выражения)](#задание-2)
5.  [Задание 5 (исполнитель Редактор)](#задание-5)
6.  [Задание 6 (исполнитель Черепаха)](#задание-6)
8.  [Задание 8 (комбинаторика)](#задание-8)
13. [Задание 13 (IP-адреса и маски подсетей)](#задание-13)
14. [Задание 14 (работа с разными системами счисления)](#задание-14)
17. [Задание 17 (числовая последовательность)](#задание-17)
19. [Задания 19—21 (теория игр)](#задания-1921)
20. [Задания 19—21 (теория игр)](#задания-1921)
21. [Задания 19—21 (теория игр)](#задания-1921)
23. [Задание 23 (рекурсия)](#задание-23)
24. [Задание 24 (обработка строковых данных)](#задание-24)
25. [Задание 25 (перебор чисел)](#задание-25)
26. [Задание 26 (что-то с сортировкой)](#задание-26)
27. [Задание 27 (программирование)](#задание-27)
### Архив
13. [Задание 13 (подсчёт числа путей в графе)](#задание-13-old)


## Введение в программирование

### Содержание
1. [Консольный ввод-вывод](#консольный-ввод-вывод)
    - [Бредогенератор](#бредогенератор)
2. [Условный оператор](#условный-оператор)
    - [Угадайка чисел](#проект-угадайка-чисел) 

### Консольный ввод-вывод

#### Проект: бредогенератор

##### Пререквизиты

- [Поколение Python: команды print() и input()](https://stepik.org/lesson/265077)

##### Вводная теория

Функция `input()` принимает на вход аргумент-строку, которая является приглашением для ввода, которое высвечивается перед курсором:
```python
a = input("Введите наречие:\n")
b = input("Введите глагол:\n")
print(a + b)
```
`\n` — служебная комбинация символов (т.н. экранированный символ), которая обозначает перенос строки. 
Данная программа принимает на вход две строки, а затем выводит результат их конкатенации ("сложения"):
```
> Введите наречие:
> Весело
> Введите глагол:
> Шагать
> Веселошагать
```
Как видите, конкатенация строк "склеивает" их стык-в-стык, не вставляя дополнительно никаких символов. Одной из техник, позволяющих вставлять пробелы между аргументами команды print(), являются f-строки.

f-строка — это строка, кавычки которой предваряет буква f и которая позволяет вставлять значения переменных или целых выражений внутрь строчки при помощи обрамления этих выражений в фигурные скобки `{`, `}`:
```python
a = 123456789
b = 123456

s = f"На Земле живёт не {a} человек, а всего лишь {b} человек. Чтобы убедиться в этом, посмотрите на снимки на Google Картах!"

print(s)
```
Эта программа выведет:
```
> На Земле живёт не 123456789 человек, а всего лишь 123456 человек. Чтобы убедиться в этом, посмотрите на снимки на Google Картах!
```

##### Задание

Написать программу, которая может поддерживать сессии навроде следующей:
```
> Прилагательное, описывающее ваше любимое животное, переведите его в форму наречия:
> Весёлый
> Действие, которое больше всего любит делать это животное:
> бегать
> Пожелание, какое действие вы бы хотели делать чаще:
> спать
> Известная личность:
> Филипп Киркоров
> Программировать - это так весело! Я так взволнована каждый раз, когда сажусь программировать, потому что я люблю бегать. Пейте достаточно жидкости и спите, что бы быть как Филипп Киркоров.
```

##### Источник вдохновения

https://github.com/kying18/beginner-projects/blob/master/madlibs.py

##### Дальнейшие идеи

 - Обернуть программу в Телеграм-бота
 - Научиться работать со словоформами

### Условный оператор

#### Проект: камень—ножницы—бумага

В простой реализации достаточно лишь операций ввода-вывода и условного оператора!

#### Проект: угадайка чисел

##### Пререквизиты

- [Основной блок задач на условный оператор](https://stepik.org/lesson/265081)
- [Хотя бы первые пару задач по циклу while](https://stepik.org/lesson/265121/step/8) — просто чтобы освоиться с его применением.

## Задание 2
Пример задания:
> Логическая функция F задаётся логическим выражением y &and; (x &or; z) &or; &not;(y &or; z) &or; w. На рисунке приведён частично заполненный фрагмент таблицы исинности функции F, содержащий неповторяющиеся строки. Определите, какому столбцу таблицы истинности соответствует каждая из пременных w, x, y, z.

|?|?|?|?|F|
|-|-|-|-|-|
|1| |0|1|0|
| |1|0| |0|
|0|0| |1|0|

> В ответе напишите буквы w, x, y, z в том порядке, в котором идут соответствующие им столбцы. Буквы в ответе пишите подряд, никаких разделителей между буквами ставить не нужно.

Напишем программу на Python ([Е. Барджахаров](https://t.me/televoliks)):
```python
# y ∧ (x ∨ z) ∨ ¬(y ∨ z) ∨ w
print('x y z w')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if (y and (x or z) or (not (y or z)) or w) == 0:
                    print(x, y, z, w)
```
Она выдаёт следующую таблицу:
|x|y|z|w|
|-|-|-|-|
|0|0|1|0|
|0|1|0|0|
|1|0|1|0|

Её можно вырезать при помощи клавиши PrtSc или инструмента "Ножницы" и вставить в Paint, а дальше заняться следующим: по мере открытия новой информации о задаче выделяем целый столбец или строку, меняем их местами с другими столбцами/строками, так получается красиво и наглядно.

Обратим внимание, что в исходной таблице единицы есть во всех столбцах, кроме третьего, а в полученной из программы таблицы есть столбец, состоящий из одних только нулей. Значит, столбец w — третий, поменяем третий и четвёртый столбцы местами:
|x|y|w|z|
|-|-|-|-|
|0|0|0|1|
|0|1|0|0|
|1|0|0|1|

Поменяем местами первую и третью строчки, просто "патамушта" (tip: так мы добьёмся идеального совпадения с исходной таблицей):
|x|y|w|z|
|-|-|-|-|
|1|0|0|1|
|0|1|0|0|
|0|0|0|1|

О, значит,

**Ответ:** xywz.
### Совет
Педантично расставляем скобки при использовании `<=` вместо импликации, ибо может получиться "что-то не то":
```python
> 3 % 3 == 0 <= False
True
> (3 % 3 == 0) <= False
False
```


## Задание 5

> №12237 на kompege
> На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.
> 1. Строится двоичная запись числа N.
> 2. Далее эта запись обрабатывается по следующему правилу:
>    
>     а) если число N чётное, то к этой записи дописываются две последние двоичные цифры;
>    
>     б) если число N нечётное, то в начало числа записывается цифра 1, а в конец числа цифра 0.
>    
> 3. Полученная таким образом запись является двоичной записью искомого числа R.
> переводится в десятичную систему и выводится на экран.
> 
> Например, для исходного числа $11 = 1011_2$ результатом является число $110110_2 = 54$, а для исходного числа $10 = 1010_2$ это
> число $101010_2 = 42$.
> Укажите максимальное число N, после обработки которого с помощью этого алгоритма получается число R, меньшее 100.

```python
for z in range (1,100):
    s = bin(z)[2:]
    if z % 2 == 0:
        s = s + s[-2:]
    else:
        s = "1" + s + "0"
    i = int(s,2)
    if i < 100:
        print(z,i)
        print("---------------------------")
```


## Задание 6

Неплохая обзорная статья по нормальным методам решения: https://ege-study.ru/ru/ege/materialy/informatika/polnyi-kurs-podgotovki-k-ege-po-informatike/zadanie-6

### ХТОНИЧЕСКИЙ метод подсчёта точек при помощи Python (Ray Tracing)

В этом способе используются напрямую объекты библиотеки Tkinter, которую использует пакет turtle.

Пример задачи (из пробника Яндекса - https://education.yandex.ru/ege/variants/597a2693-1f78-45be-8daf-d80e1f937a3d/task/6):
> Исполнитель Черепаха действует на плоскости с декартовой системой координат. В начальный момент Черепаха находится в начале координат, её голова направлена вдоль положительного направления оси ординат, хвост поднят. При опущенном хвосте Черепаха оставляет на поле след в виде линии. В каждый конкретный момент известно положение исполнителя и направление его движения. У исполнителя существует четыре команды:
>
> Поднять хвост, означающая переход к перемещению без рисования;
> Опустить хвост, означающая переход в режим рисования;
> Вперёд nn (где nn — действительное число), вызывающая передвижение Черепахи на nn единиц в том направлении, куда указывает её голова;
> Направо mm (где mm — целое число), вызывающая изменение направления движения на mm градусов по часовой стрелке.
>
> Черепахе был дан для исполнения следующий алгоритм:
> 
> Направо 30 Вперёд 4 Направо 330
> Опустить хвост
> Вперёд 4 Направо 90 Вперёд 7 Направо 45 Вперёд 4242
>
​> Направо 135 Вперёд 11
>
> Определите, сколько точек с целочисленными координатами будут находиться внутри области, ограниченной заданными алгоритмом линиями, включая точки на линиях.

```python
import turtle

# Fullscreen the canvas
screen = turtle.Screen()
screen.setup(1.0, 1.0)

# Begin!
t = turtle.Turtle()

# константа масштабирования рисунка — без масштабирования способ будет давать неправильный результат
scale = 20

# Сместимся по экрану влево и вверх
start = 11*scale
t.penup()
t.goto(-start, start)

# глобальный в рамках скрипта объект, благодаря которому работает магия автоматического подсчёта точек
canvas = t.getscreen().getcanvas()

# Каждый объект на canvas обладает своим ID. Без вникания в исходный код модуля turtle невозможно разобраться,
# какие же объекты по умолчанию создаются на canvas при запуске Черепахи, поэтому воспользуемся следующим наблюдением:
#  - даже в момент, когда перо поднято, на canvas уже присутствует объект, который будет отвечать за отображение
# следующей линии, которую нарисует Черепаха.
#  - соответственно, когда мы опускаем перо, что-то рисуем, а затем поднимается перо, всё нарисованное идёт в
# предыдущий объект, а при поднятии пера создаётся новый, с новым ID
#  - обычно этот ID самый большой из всех, что есть на canvas'е
# Соответственно, метод canvas.find_all() даёт список ID всех объектов на холсте,
# а метод max(canvas.find_all()) даёт ID объекта, в который будет отрисовываться то, что мы будем рисовать
# между следующей парой операций t.pendown() и t.penup()
# Таким образом, в списке lineIDs хранятся ID только тех линий, которые мы нарисовали Черепахой, и ничего более.
lineIDs = []
def forward(n: float):
    n = round(n * scale)
    lineIDs.append(max(canvas.find_all()))
    # Здесь мы делаем небольшой отступ между линиями, чтобы они не накладывались друг на друга.
    # Потому что нам надо, чтобы при прочерчивании линии сквозь стык двух линий рисунка из условия,
    # функция canvas.find_overlapping() выдавала только одну линию, а не две.
    t.penup()
    t.forward(3)
    t.pendown()
    t.forward(n-3)
    t.penup()

def right(n):
    t.right(n)

# mfo — My_Find_Overlapping() — обёртка над методом canvas.find_overlapping()
# метод canvas.find_overlapping(x1, y1, x2, y2) находит список ID объектов, перекрывающихся с прямоугольником,
# натянутым на координаты (x1, y1), (x2, y2)
# смысл обёртки заключается в том, чтобы отфильтровать из найденных ID только те, которые соответствуют
# линиям, нарисованным Черепахой по условию задания 
def mfo(a, b, c, d):
    return [_ for _ in canvas.find_overlapping(a, b, c, d) if _ in lineIDs]

def check(x, y):
    # У черепахи оси координат направлены Ох вправо, а Оу вверх.
    # У холста Ох также направлена вправо, а Оу вниз.
    y = -y
    # Проверка, не находится ли точка на линии
    if len(mfo(x, y, x, y))==1:
        return True
    # Проверка, находится ли точка внутри фигуры:
    # пуск четырёх "лучей" вдоль по коордиантным осям
    # Если луч пересекает одну линию, то, значит, мы находимся внутри многоугольника
    # Если луч пересекает 0 или 2 линии, значит, мы где-то снаружи
    RTX = [
        mfo(x, y, x + 50*scale, y),
        mfo(x, y, x - 50*scale, y),
        mfo(x, y, x, y + 50*scale),
        mfo(x, y, x, y - 50*scale)    
    ]
    return all(len(RTX[i]) == 1 for i in range(4))

# Рисуем по командам из условия:
# Направо 30 Вперёд 4 Направо 330
# Опустить хвост
# Вперёд 4 Направо 90 Вперёд 7 Направо 45 Вперёд 4*2**0.5
# Направо 135 Вперёд 11


right(30)
t.forward(4*scale)
right(330)

forward(4)
right(90)
forward(7)
right(45)
forward(4*2**0.5))
right(135)
forward(11)

# Непосредственно подсчёт подходящих точек
counter = 0
# Фрагмент кода, необходимый для работы визуализации найденных точек
# points = []
for i in range(-15, 16):
    for j in range(-15, 16):
        x, y = i*scale, j*scale
        if check(x, y):
            counter += 1
            # Фрагмент кода, необходимый для работы визуализации найденных точек
            # points.append((x, y))

# Вывод количества найденных подходящих точек
print(counter)

# Код для визуализации найденных точек
# t.penup()
# for point in points:
#     t.goto(point)
#     t.dot()

# Магическая строчка, необходимая для работы окна с Черепашкой
screen.mainloop()
```

Рассмотрим задачу, которую невозможно решить иначе как программным способом:

> kompege #13247
> Черепахе был дан для исполнения следующий алгоритм:
>
> Повтори 243 [Вперёд 78 Направо 120]
> 
> Определите, сколько точек с целочисленными координатами будут находиться внутри области, ограниченной линией, заданной данным алгоритмом. Точки на линии учитывать не следует.

Во-первых, легко заметить, запустив простую программу (ну или подумав немного головой):
```python
t = turtle.Turtle()
for _ in range(243):
    t.forward(78)
    t.right(120)
```
, что число "243" сильно избыточно: Черепаха просто рисует равносторонний треугольник, поэтому достаточно и 3 повторений.
А для нашего способа и необходимо, потому что с точки зрения canvas'a каждая новая линия, нарисованная нашей функций `forward`, поверх старой - это новый объект.

Во-вторых, в данной задаче немного другое условие: точки, попадающие на линию, мы НЕ должны учитывать. Поэтому немного перепишем функцию `check()`:
```python
def check(x, y):
    y = -y
    if len(canvas.find_overlapping(x, y, x, y)) == 1:
        return False # Теперь возвращаем False в случае, если прямоугольник-точка попал на линию
    RTX = [
        mfo(x, y, x + 100 * scale, y),
        mfo(x, y, x - 100 * scale, y),
        mfo(x, y, x, y + 100 * scale),
        mfo(x, y, x, y - 100 * scale)
    ]
    return all(len(RTX[i]) == 1 for i in range(4))
```

Ну вот и всё!

Полный листинг программы:

```python
import turtle

turtle.tracer(False) # Для отключения анимации Черепахи
screen = turtle.Screen()
screen.setup(1.0, 1.0)

# Begin!
t = turtle.Turtle()

scale = 1000000 # О_о ################################
start = 30*scale
t.penup()
t.goto(-start, start+100)

canvas = t.getscreen().getcanvas()
lineIDs = []


def forward(n):
    n = n * scale
    lineIDs.append(max(canvas.find_all()))
    t.penup()
    t.forward(3)
    t.pendown()
    t.forward(n - 3)
    t.penup()


def right(n):
    t.right(n)


def mfo(a, b, c, d):
    return [_ for _ in canvas.find_overlapping(a, b, c, d) if _ in lineIDs]


# Функция проверки того, находится ли точка с данными координатами внутри фигуры или на её границе
def check(x, y):
    y = -y
    if len(canvas.find_overlapping(x, y, x, y)) == 1:
        return False
    RTX = [
        mfo(x, y, x + 100 * scale, y),
        mfo(x, y, x - 100 * scale, y),
        mfo(x, y, x, y + 100 * scale),
        mfo(x, y, x, y - 100 * scale)
    ]
    return all(len(RTX[i]) == 1 for i in range(4))


for _ in range(3):
    forward(78)
    right(120)

print("End of drawing")

counter = 0
for i in range(-100, 100):
    for j in range(-100, 100):
        x, y = i * scale, j * scale
        if check(x, y):
            counter += 1

print(counter)

screen.mainloop()
```

Видели этот scale?
Я последовательно увеличивал это значение, и каждый раз у меня получалось разное количество точек.
Где-то при переходе от 1000 к 10000 оно начало расти довольно медленно.
Наконец, при переходе от 100000 к 1000000 не произошло никакого изменения.

Из чего я делаю вывод, что правильный ответ к этой задаче 2672, а не 2595.
А дело всё в том, что вычисления с плавающей точкой - штука весьма капризная и неточная, и если брать слишком малую точность вычислений, то может так статься, что точки сольются в линию. Хотя на самом деле это может быть далеко не так.

## Задание 8

Задание:
> Шифр кодового замка представляет собой последовательность из пяти символов, каждый из которых является цифрой от 1 до 4. Сколько различных вариантов шифра можно задать, если известно, что цифра 1 встречается ровно два раза, а каждая из других допустимых цифр может встречаться в шифре любое количество раз или не встречаться совсем?

```python
цифры = "1234"

counter = 0
for a in цифры:
    for b in цифры:
        for c in цифры:
            for d in цифры:
                for e in цифры:
                    n = a + b + c + d + e
                    if n.count("1") == 2:
                        counter += 1
print(counter)
```

Перестановки с повторениями:
https://www.matburo.ru/tvart_sub.php?p=calc_PR
Количество перестановок всех объектов делим на количества перестановок внутри групп этих объектов.


## Задание 13

Есть удобная функция в Excel для перевода десятичных чисел в двоичные: `ОСНОВАНИЕ(<КОНВЕРТИРУЕМОЕ ЧИСЛО>; <ОСНОВАНИЕ ЦЕЛЕВОЙ СИСТЕМЫ СЧИСЛЕНИЯ>; <РАЗРЯДНОСТЬ ЧИСЛА>)`. Соответственно, можно сделать такую таблицу:
||Первый байт|Второй байт|Третий байт|Четвёртый байт|Первый байт|Второй байт|Третий байт|Четвёртый байт|
|-|-|-|-|-|-|-|-|-|
|Адрес узла|192|168| 1 | 1 |=ОСНОВАНИЕ(A2;2;8)|=ОСНОВАНИЕ(B2;2;8)|=ОСНОВАНИЕ(C2;2;8)|=ОСНОВАНИЕ(D2;2;8)|
|Маска сети|255|255|255|248|=ОСНОВАНИЕ(A3;2;8)|=ОСНОВАНИЕ(B3;2;8)|=ОСНОВАНИЕ(C3;2;8)|=ОСНОВАНИЕ(D3;2;8)|

И, соответственно, глазками анализировать IP-адрес, применять побитовую конъюнкцию и прочее, прочее.

Это нагляднее, чем использовать встроенную функцию `bin()` в Python: проще не забыть про ведущие нули.

Впрочем, Питону есть чем ответить: функция `format(<ЧИСЛО>, "08b")` делает то же самое.

А ещё в Питоне в стандартной библиотеке есть пакет ipaddress, который может существенно помочь, если создатели задания упорются и решат, что делать этот номер решаемым вручную - не комильфо, и надо будет решать всё тупым перебором.

Чтобы импортировать модуль:
```python
from ipaddress import ip_network
```
### Претификаторы 
(команды для форматированного вывода IP-адресов, полезно использовать во время обучения, бесполезны на экзамене):
```python
'{:_b}'.format(my_ip_address)
```

Быстр в написании, если запомнить магическую комбинацию символов в начале, можно использовать на экзамене. Разбивает IP-адрес в двоичном представлении на тетрады:
```python
nw = ip_network('192.168.1.0/32')
print('{:_b}'.format(nw.network_address))
```
Вывод:
```
1100_0000_1010_1000_0000_0001_0000_0000
```

Красивый и сложный:
```python
def mf(addr):
    return " ".join([format(int(byte), "08b") for byte in str(addr).split(".")])
```

Представляет IP-адрес в виде 4 байтов, представленных в виде двоичного кода, разделённых пробелами:
```python
nw = ip_network('192.168.1.0/32')
print(mf(nw.network_address))
```
Вывод:
```
11000000 10101000 00000001 00000000
```

### Примеры использования пакета ipaddress

\*Догадайтесь сами, что всё это значит\*

```python
nw = ip_network('157.180.63.114/255.255.255.248', False)
addr = nw.network_address
print(mf(addr))
print(mf(nw.broadcast_address))
print(mf(nw.hostmask))
print(mf(nw.netmask))
print(nw.num_addresses)
for addr in nw.hosts():
    print(addr)
```

### Примеры решения задач
> В терминологии сетей TCP/IP маской сети называется двоичное число, определяющее, какая
> часть IP-адреса узла сети относится к адресу сети, а какая — к адресу самого узла в этой сети.
> Адрес сети получается в результате применения поразрядной конъюнкции к заданному адресу
> узла и маске сети.
> Сеть задана IP-адресом 157.180.63.114 и маской сети 255.255.255.248. Сколько в этой сети IP-
> адресов, для которых в двоичной записи IP-адреса суммарное количество единиц в левых двух
> байтах меньше суммарного количества единиц в правых двух байтах? В ответе укажите только
> число.

```python
nw = ip_network('157.180.63.114/255.255.255.248', False)
counter = 0
for i in range(0, nw.num_addresses):
    addr = nw.network_address + i
    addr = bin(int(addr))[2:].zfill(32)
    left = addr[:16]
    right = addr[16:]
    if left.count("1") < right.count("1"):
        counter += 1
print(counter)
```

> В терминологии сетей TCP/IP маской сети называется двоичное число, определяющее, какая
> часть IP-адреса узла сети относится к адресу сети, а какая — к адресу самого узла в этой сети.
> Адрес сети получается в результате применения поразрядной конъюнкции к заданному адресу
> узла и маске сети.
> Сеть задана IP-адресом 255.112.128.136 и маской сети 255.255.Х.0, где Х - число, заданное в
> диапазоне от 0 до 255. Определите минимальное значение Х, для которого для всех IP-адресов
> этой сети в двоичной записи IP-адреса суммарное количество единиц в левых двух байтах не
> менее суммарного количества единиц в правых двух байтах. В ответе укажите только число.

```python
def chuck(nw):
    counter = 0
    for i in range(0, nw.num_addresses):
        addr = nw.network_address + i
        #print(mf(addr))
        addr = bin(int(addr))[2:].zfill(32)
        #print(addr)
        left = addr[:16]
        right = addr[16:]
        if left.count("1") >= right.count("1"):
            counter += 1
    return counter == nw.num_addresses

for i in range(0, 256):
    try:
        nw = ip_network(f'255.112.128.136/255.255.{i}.0', False)
    except:
        continue
    else:
        print(nw.network_address)
        if chuck(nw):
            print(i)
            print(chuck(nw))
            break
```


## Задание 14

| Перевод... | Функция |
|-|-|
| ...из десятичной в двоичную          | `bin(x)` |
| ...из десятичной в восьмеричную      | `oct(x)` |
| ...из десятичной в шестнадцатиричную | `hex(x)` |

Примеры самописных функций перевода:
```python
# 10 -> 13

def encode(x):
    digits = "0123456789abc"
    return digits[x]

def f(x):
    if x < 13:
        return encode(x)
    else:
        return f(x // 13) + encode(x % 13)

print(f(2024))

# 10 -> 6

def g(x):
    if x < 6:
        return str(x)
    else:
        return g(x // 6) + str(x % 6)

print(g(2024))

# 10 -> 7

def h(x):
    s = ""
    while x > 0:
        s = str(x % 7) + s
        x //= 7
    return s

print(h(2024))
```


## Задание 17

### Чтение из файла

```python
f = open("17.txt")
A = f.readlines()
A = [int(x) for x in A]
```
Последняя строчка — более короткая запись для
```python
for i in range(len(A)):
    A[i] = int(A[i])
```
### Собственно решение задачи
#### Перебор пар (троек) последовательных значений
[Пример](https://inf-ege.sdamgia.ru/problem?id=59722)

> Элементы ряда могут принимать целые значения в диапазоне [−10000; 10000]. Определите количество троек элементов последовательности, в которой только одно число трехзначное, а сумма тройки меньше наибольшего числа, оканчивающегося на 17. В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности.

```python
f = open("17.txt")
A = f.readlines()
A = [int(x) for x in A]

max17 = -10000
for x in A:
    if abs(x) % 100 == 17 and x > max17:
        max17 = x

counter = 0
for i in range(len(A) - 2):
    # Пример техники работы с последовательными тройками
    B = []
    for j in range(3):
        B.append(A[i+j])
    C = []
    for j in range(3):
        C.append(len(str(abs(B[j]))))
    if C.count(3) == 1 and sum(B) < max17:
        counter += 1

print(counter)
```
#### Перебор всех возможных пар
Чтобы перебрать все пары различных элементов, можно использовать двойной вложенный цикл, например, так:
```python
max_s = 0
k = 0
for i in range(len(A)):
    for j in range(len(A)):
        s = A[i]+A[j]
        if s % 9 == 0:
            k += 1
            if s > max_s:
                max_s = s
```
Данная программа, при условии, что можно брать любые два элемента последовательности, а не только идущие друг за другом, считает количество пар элементов, сумма которых делится на 9 (переменная `k`), а также находит максимальную из таких сумм (переменная `max_s`).

### Small tip
Остаток от деления отрицательного числа — это _дополнение_ этого числа до делителя, например:
```python
>>> -117 % 100
83
```
Поэтому чтобы не получать неожиданных результатов от операций взятия остатка, надо брать остаток от модуля (`abs(n)`) от этого числа.

## Задания 19—21

> * Задание 1 из домашней работы Флеша *

Можно делать через Excel:

https://docs.google.com/spreadsheets/d/1iB98T5RNAmyIp3He0m0ZHyAwhQTXvJqJ9lKNiY--d8I/edit#gid=525142007

Excel-подобный код для решения задания 19:

```python
def f(n):
    a, b = 7, n
    for i, j in (
        (a + 1, b),
        (a, b + 1),
        (a + b, b),
        (a, a + b)
    ):
        if max(2*i+j, i+2*j) >= 75:
            return True

for i in range(65):
    if f(i):
        print(i)
        break
```

Excel-подобный код для решения задания 20:
```python
def f(a, b):
    wins = []
    for i, j in (
        (a + 1, b),
        (a, b + 1),
        (a + b, b),
        (a, a + b)
    ):
        wins.append(
            max(2*i+j, i+2*j) >= 75 and
            i + j < 75
        )
    if all(wins):
        return True

def g(a, b):
    for i, j in (
        (a + 1, b),
        (a, b + 1),
        (a + b, b),
        (a, a + b)
    ):
        if f(i, j):
            return True
            
for i in range(65):
    if g(7, i):
        print(i)
```

Excel-подобный код для решения 21 задачи:
```python
def f(a, b):
    wins = []
    for i, j in (
        (a + 1, b),
        (a, b + 1),
        (a + b, b),
        (a, a + b)
    ):
        wins.append(
            max(2*i+j, i+2*j) >= 75 and
            i + j < 75
        )
    if all(wins):
        return True

def g(a, b):
    for i, j in (
        (a + 1, b),
        (a, b + 1),
        (a + b, b),
        (a, a + b)
    ):
        if f(i, j):
            return True

def h(a, b): # Петя
    wins = []
    for i, j in (
        (a + 1, b),
        (a, b + 1),
        (a + b, b),
        (a, a + b)
    ):
        wins.append(
            g(i, j) or 
            (max(2*i+j, i+2*j) >= 75 and
                i + j < 75
            )
        )
    if all(wins):
        return True

for i in range(65):
    if h(7, i):
        print(i)
```

Excel-подобный код решения для задания 21 с использованием обобщённых функций:
```python
def Eeee(i, j):
    return max(2*i+j, i+2*j) >= 75

def Meta(a, b, condition, allOrAny = all):
    wins = []
    for i, j in (
        (a + 1, b),
        (a, b + 1),
        (a + b, b),
        (a, a + b)
    ):
        wins.append(condition(i, j))
    if allOrAny(wins):
        return True

def f(a, b):
    return Meta(a, b, lambda i, j: Eeee(i, j) and i+j < 75)

def g(a, b):
    return Meta(a, b, lambda i, j: f(i, j), any)

def h(a, b): # Петя
    return Meta(a, b, lambda i, j: g(i, j) or (Eeee(i, j) and i + j < 75))


for i in range(65):
    if h(7, i):
        print(i)
```

Краткое рекурсивное решение для заданий 20-21:

```python
from functools import lru_cache


@lru_cache(None)
def f(a, b):
    if a > b:
        turns = [(a, b + i) for i in range(1, b+1)]
    elif a < b:
        turns = [(a + i, b) for i in range(1, a+1)]
    else:
        turns1 = [(a, b + i) for i in range(1, b+1)]
        turns2 = [(a + i, b) for i in range(1, a+1)]
        turns = turns1 + turns2

    if a + b > 45:
        return 0
    if any(f(*turn) == 0 for turn in turns):
        return 1
    if all(f(*turn) == 1 for turn in turns):
        return 2
    if any(f(*turn) == 2 for turn in turns):
        return 3
    if all(f(*turn) in (1, 3) for turn in turns):
        return 4

#m = 46
#m_i, m_j = 0, 0
#for i in range(1, 46):
#    for j in range(1, 46):
#        if f(i, j) == 1:
#            if (i + j) < m:
#                m = i + j
#                m_i = i
#                m_j = j
#
#print(m, m_i, m_j)

for i in range(6, 41):
    if f(5, i) == 3:
        print("#"*4, i)
    if f(5, i) == 4:
        print("#"*8, i)
```

## Задание 23
Пример:
>Исполнитель преобразует число на экране.
>У исполнителя есть четыре команды, которым присвоены номера:
>1. Прибавить 1
>2. Прибавить 2
>3. Умножить на 2
>4. Умножить на 3
>Первая команда увеличивает число на экране на 1, вторая увеличивает его на 2, третья умножает на
>2, четвёртая — умножает на 3.
>Программа для исполнителя — это последовательность команд. Например, если в начальный
>момент на экране находится число 1, то программа 213 последовательно преобразует его в 3, 4, 8.
>Сколько существует программ, которые преобразуют исходное число 1 в число 24 и при этом не
>содержат двух последовательных команд сложения и двух последовательных команд умножения?

Программа:
```python
from functools import lru_cache


@lru_cache(maxsize=None)
def f(x, n, s):
    # print(n)
    if x > n:
        return 0
    elif x == n:
        return 1
    elif s == 1 or s == 2:
        return f(x * 2, n, 3) + f(x * 3, n, 4)
    elif s == 3 or s == 4:
        return f(x + 1, n, 1) + f(x + 2, n, 2)
    else:
        return f(x+1, n, 1) + f(x * 3, n, 4) + f(x * 2, n, 3) + f(x+2, n, 2)


print(f(1, 24, 0))
```

## Задание 24
```python
# https://education.yandex.ru/ege/variants/597a2693-1f78-45be-8daf-d80e1f937a3d
# Текстовый файл состоит из символов латинского алфавита в нижнем регистре (a—z) и цифр (0-9).

# Определите в прилагаемом файле максимальную длину подстроки (непрерывной подпоследовательности), которая состоит из повторяющегося слова "yandex". Последнее слово в цепочке может быть неполным. По правилам leet (1337) символ "a" может быть заменён на символ "4", а символ "e" — на символ "3".

# Так, в строке "qyandqqyand3xy4q" есть две подходящие подстроки: "yand" и "yand3xy4".


f = open('24.txt')
s = f.readline()
s = "qyandqqyand3xy4q"

s = s.replace("4", "a").replace("3", "e")
s = s.replace("yandex", "@")
for i in range(len("yandex") - 1, 0, -1):
    substr = "yandex"[:i+1]
    s = s.replace(substr, "$" * (i + 1))
t = ""
for c in s:
    if c not in "@$":
        t += " "
    else:
        t += c
print(t.split())
print(max(x.count("@")*6 + x.count("$") for x in t.split()))
```

## Задание 25
### Перебор с маской
Есть прекрасный модуль `fnmatch`, который позволяет с лёгкостью писать программы к номерам на маски над числами.

[Пример](https://inf-ege.sdamgia.ru/problem?id=60267)
> Среди натуральных чисел, не превышающих $10^10$, найдите все числа, соответствующие маске 1?2157*4, делящиеся на 2024 без остатка. В ответе запишите в первом столбце таблицы все найденные числа в порядке возрастания, а во втором столбце  — соответствующие им результаты деления этих чисел на 2024.
```python
from fnmatch import fnmatch

for n in range(0, 10**10+1, 2024):
    if fnmatch(str(n), "1?2157*4"):
        print(n, n // 2024)
```

С помощью модуля `itertools` можно организовать **молниеносный** перебор, не сильно раздувая программу:

> Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
> - символ "\?" означает ровно одну произвольную цифру;
> - символ "\*" означает любую последовательность цифр произвольной длины; в том числе "\*" может задавать и пустую последовательность. Например, маске 123\*4\?5 соответствуют числа 123405 и 12300425.
> Среди натуральных чисел, не превышающих $10^8$, найдите все числа, соответствующие маске 32\*823 и не делящиеся на 123 без остатка. В ответе запишите в первом столбце таблицы все найденные числа в порядке возрастания, а во втором столбце - соответствующие им частные от деления на 123.
### Перебор делителей
#### Простейшая программа для определения простоты числа

```python
a = int(input("Введите число: "))
k = 0
for i in range(2, a // 2+1):
    if (a % i == 0):
        k = k+1
if (k == 0):
    print("Число простое")
else:
    print("Число не является простым")
```
Пределы, в которых мы ищем делители, просты для понимания: не может быть целочисленного делителя больше, чем половина от числа. Но можно сделать хитрее...


## Задание 26
### Сюжет: администратор и файлы
Пример — задача 225 с kompege.ru
```python
with open("26.txt") as f:
    S, N = [int(_) for _ in f.readline().split()]
    A = [int(_) for _ in f.readlines()]

A.sort(reverse=True)

print(A[:100])

s = 0
i = 0
while s + A[i] < S:
    s += A[i]
    i += 1

for j in range(i, len(A)):
    if A[j] <= S - s:
        s += A[j]
        break
    
print(i + 1, A[j])
```


## Задание 27 


```
/*
    https://inf-ege.sdamgia.ru/problem?id=27424
*/
#include <algorithm>
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main() {
    fstream FILE;
    int N;
    long int sum = 0;
    
    FILE.open("27-B_demo.txt");
    FILE >> N;
    vector<int> A(N), B(N), C(N);
    for (int i = 0; i < N; i++){
        FILE >> A[i] >> B[i];
    }
    FILE.close();

    for (int i = 0; i < N; i++){
        sum += max(A[i], B[i]);
        C[i] = abs(A[i] - B[i]);
    }

    sort(C.begin(), C.end());
    for (int i = 0; i < N; i++){
        if (C[i] % 3 != 0){
            sum -= C[i];
            break;
        }
    }
    
    cout << sum << endl;
    cout << sum % 3 << endl;
}
```


## Архив

## Задание 13 (old)
Возможно решение через Python!
Можно задать граф в одну строчку, записать это всё в словарь, а затем итерироваться по словарю, чтобы подсчитать число вершин. Если нужно что-то исключить, то модифицируем граф.
