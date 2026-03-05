#TODO make it with pip install -e .
# in project root_dir after setup.py defined


# Раннее тестирование позволяет сэкономить время позднее
# Тесты показывают наличие ошибок, а не отсутсвие
# Тесты не должны дублировать логику тестируемого кода
# Тесты не должны использовать ВСЕ наборы входных параметров
#TODO make it with pip install -e .
# in project root_dir after setup.py defined


# Раннее тестирование позволяет сэкономить время позднее
# Тесты показывают наличие ошибок, а не отсутсвие
# Тесты не должны дублировать логику тестируемого кода
# Тесты не должны использовать ВСЕ наборы входных параметров
# Тесты должны покрывать "кластеры" входных параметров
# Тесты должны обнаруживать новые ошибки (pescicide paradox)
# Тесты покрывают как успешные, так и ошибочные кейсы

from math_demo import (
    add, 
    add_with_bug,
    calculate_tax_bugged,
    calculate_tax
)

def test_addition():
    assert add(2,2) == 4
    assert add(0,0) == 0
    assert add(7,6) == 13
    print("Test addition passed")


def test_addition_with_bug():
    assert add_with_bug(2,2) == 4
    assert add_with_bug(0,0) == 0
    assert add_with_bug(7,6) == 13
    print("Test bugged addition passed")

def test_addition_duplicate():
    assert add(5, 6) == 6 + 7
    print("Test Duplicate ADDITION PASSED")


def test_tax_calculator():
    assert calculate_tax_bugged(1000) == 150
    assert calculate_tax_bugged(100) == 15
    assert calculate_tax_bugged(10) == 1.5
    assert calculate_tax_bugged(1) == 0.15
    assert calculate_tax_bugged(234) == 35.1
    print("Test TAX    CALCULATOR PASSED")
    assert calculate_tax_bugged(2.34) == 0.351 #0.351

def tax_calculator_pesticide():
    assert calculate_tax(1000) == 150
    assert calculate_tax(100) == 15
    assert calculate_tax(10) == 1.5
    assert calculate_tax(1) == 0.15
    assert calculate_tax(234) == 35.1
    print("Test UNBUGGED TAX CALCULATOR PASSED")
    assert calculate_tax(2.34) == 0.35


if name == "__main__":
    test_addition()
    test_addition_with_bug()
