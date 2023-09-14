# Проект асинхронного парсера PEP
## Описание
Проект асинхронного парсера PEP представляет собой консольную утилиту для получения обновлений PEP и их статусов. Утилита разработана на языке программирования Python с использованием библиотеки Scrapy

## Технологии
Основные технологии, использованные в проекте:

* Python
* Scrapy

## Запуск проекта:
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/osukhankin/scrapy_parser_pep.git
```


Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

  ```
  source env/bin/activate
  ```

* Если у вас windows

  ```
  source env/scripts/activate
  ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```


Запустить скрипт:

```
scrapy crawl pep
```
## Справка
Утилита предоставляет возможность получать обновления PEP, их статусы и ведет подсчет каждого статуса PEP.
 
## Результаты

Результаты работы утилиты выводятся в csv формате в директорию results:

* **pep_date_time.csv** - файл-сводка с номером/названием/статусом каждого PEP.
* **status_summary_date_time.csv** - файл-сводка кол-во pep в каждом статусе

## Лог исполнения
Лог работы утилиты пишется в консоль


## Ссылки
* [Репозиторий проекта](https://github.com/osukhankin/scrapy_parser_pep.git)
* [Документация](https://github.com/osukhankin/scrapy_parser_pep/wiki)

## Автор
Суханкин Олег - [osukhankin@yandex.ru](mailto:osukhankin@yandex.ru)

