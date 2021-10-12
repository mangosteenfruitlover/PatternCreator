# PatternCreator


## Демонстрация


https://replit.com/@DianaKoriepanov/patterncreator


## Команды перед запуском


### Библиотеки для тестирования

pip install ffmpeg


pip install pydub


pip install pytest

### Тестирование


bash tests.bash


### Библиотеки для документации


pip install pydoc


### Создание документации в html

bash doc.bash


### Запуск

python main.py


## Документация


### Класс PatternCreatorPresenter() позволяет сгенерировать исходный код по паттернам со своими названиями классов.

Конструктор класса PatternCreatorPresenter() создаёт словарь с кодом по паттернам

Функция check_pattern_name класса PatternCreatorPresenter() проверяет префикс названия класса и файла

Функция find_pattern класса PatternCreatorPresenter() проверяет наличие паттерна в словаре

Функция get_num_patter класса PatternCreatorPresenter() выдаёт индекс паттерна для взаимодействия с префиксами

Функция paste_class_name класса PatternCreatorPresenter() обновляет префикс названия класса паттерна, проверяя наличие индекса паттерна в словаре

Функция create_pattern класса PatternCreatorPresenter() создаёт файл с исходным кодом паттерна

### Класс PatternCreatorView() для работы с классом PatternCreatorPresenter() (для работы в консоли)

Функция start() для начала работы в консоли
Возвращает краткую информацию о работе команды или предупреждение

### Класс TestPatternCreator() проводит модульные тесты для PatternCreatorPresenter

Функция obj_reset() пересоздаёт объект класса PatternCreatorPresenter для удобного проведения тестирования 

Функция test_check_pattern_name() проверяет, что функция check_pattern_name() из PatternCreatorPresenter правильно проверяет формат префикса названия класса 

Функция test_create_pattern() проверяет, что функция create_pattern() из PatternCreatorPresenter правильно возращает название файла со сгенерированным исходным кодом по паттернам со своими названиями классов

Функция test_get_num_pattern() проверяет, что функция get_num_pattern() из PatternCreatorPresenter правильно выдаёт индекс 

Функция test_paste_class_name() проверяет, что функция paste_class_name() из PatternCreatorPresenter правильно обновляет префикс названия класса по индексу

Функция test_find_pattern() проверяет, что функция find_pattern() из PatternCreatorPresenter правильно проверяет наличие паттерна в словаре 