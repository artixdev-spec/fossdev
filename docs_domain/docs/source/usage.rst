Использование
=============

Установка пакета в режиме разработки:

.. code-block:: bash

   pip install -e .

Пример:

.. code-block:: python

   from sales import build_report, read_sales

   sales = read_sales("sales.txt")
   print(build_report(sales))

Для файла::

   Кофе,напитки,150.5,2
   Круассан,выпечка,90,3

отчёт будет таким::

   Отчёт о продажах

   выпечка: 270.00
   напитки: 301.00

   Итого: 571.00
