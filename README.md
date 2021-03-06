# Shift + Enter by Changellenge
Задания Виртуальной IT стажировки Shift + Enter от Changellenge по направлению "Python-разработчик", KPMG

## Скиллы
Необходимы знания проектирования баз данных, основы юнит-тестирования, знание Python.
Требуется: 
1. Получить информацию с сайта с помощью собственной программы
парсинга данных.
2. Написать юнит-тесты по проверке и выборке данных с сайта, а также по
проверке базы данных.
3. Создать базу данных с использованием SQLite в Python и добавлять
в нее данные.

## Задание 1. Парсинг данных

Написать программу получения информации с [сайта госзакупок](https://zakupki.gov.ru/epz/order/extendedsearch/results.html), которая считывала бы данные и сохраняла их в удобном для дальнейшей работы формате.
Код также должен выводить номер закупки и начальную цену.

### Реализация
* [Парсинг](task_one.py) - BeatifulSoup
* [Сохранение в файл](main.py)

### Пример карточки с сайта госзакупок
![delete](https://user-images.githubusercontent.com/68865736/164988624-108a1554-fbe8-459a-ae5c-a6a6d6a8573b.PNG)

### Результат
Данные сохраняются в виде таблицы в отдельном файле (.csv)
| |Номер                                                                                        |Начальная цена                              |
|------|---------------------------------------------------------------------------------------------|--------------------------------------------|
|0     |                                          № 32110894272                                      |38 285 120,64 ₽                             |
|1     |                                          № 32211090096                                      |185 000,00 ₽                                |
|2     |                                          № 32211090077                                      |255 000,00 ₽                                |
|3     |                                          № 32211090047                                      |185 000,00 ₽                                |




## Задание 2. Юнит тест

Написать юнит тесты для [Задания 1](https://github.com/Aziz-Dadoboev/shift_enter_kpmg/edit/main/README.md#%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-1-%D0%BF%D0%B0%D1%80%D1%81%D0%B8%D0%BD%D0%B3-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85)

### Реализация
* [Файл](test_task_two.py)

## Задание 3. База данных

Спроектировать базу данных по закупкам и проверить ее работу при помощи юнит-теста.

### Реализация 
* [База данных](task_three.py) - SQLite
* [Юнит-тесты](test_taskThree.py)

### Результат
![delete](https://user-images.githubusercontent.com/68865736/164989905-b8196cc7-6354-42d2-85e0-b232a7331002.PNG)



## Полезные ссылки

* [Статья](https://habr.com/ru/post/280238/) про Web Scraping с помощью Python.
* [Статья](https://habr.com/ru/post/568334/) о парсинге сайтов.
* [Статья](https://pythonworld.ru/moduli/modul-unittest.html) о модуле unittest с примерами использования различных проверок.
* [Руководство](https://pythonru.com/osnovy/sqlite-v-python) по SQLite в Python.
