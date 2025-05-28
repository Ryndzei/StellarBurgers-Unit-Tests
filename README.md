# Дипломный проект. Яндекс Практикум. Задание 1: Юнит-тесты
Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

Процент покрытия 100% — [отчет](htmlcov/index.html)

Реализованные сценарии:

#### Созданы юнит-тесты, покрывающие классы
- [Bun](praktikum/bun.py)
- [Burger](praktikum/burger.py)
- [Ingredient](praktikum/ingredient.py)
- [Database](praktikum/database.py)

---
### Структура репозитория
#### В директории [praktikum](praktikum) содержится код программы

#### Директория [tests](tests) — это пакет, содержащий тесты, разделенные по классам

---
### Библиотеки
- pytest
- pytest-cov
---
### Команды
Установить зависимости
``` shell
pip3 install -r requirements.txt
```
Запустить все тесты
```shell
pytest tests/
```
Открытие pytest-cov отчета на win
``` shell
start htmlcov/index.html
```
