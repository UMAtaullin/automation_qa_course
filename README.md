# automation_qa_course

automation_qa_course
│
├── pages/                  # Классы страниц (Page Objects)
│   ├── __init__.py
│   ├── base_page.py        # Базовый класс с общими методами
│   └── elements_page.py    # Конкретная страница (например, страница с веб-элементами)
│
├── locators/               # Локаторы элементов
│   ├── __init__.py
│   └── elements_page_locators.py   # Локаторы для страницы elements_page
│
├── tests/                  # Тесты
│   ├── __init__.py
│   ├── conftest.py         # Фикстуры pytest (например, инициализация драйвера)
│   └── test_elements.py    # Тесты для страницы с элементами
│
├── utils/                   # Вспомогательные утилиты (опционально)
│   ├── __init__.py
│   └── helpers.py           # Например, функции для работы с данными, логирование
│
├── data/                    # Тестовые данные (опционально)
│   └── test_data.json
│
├── reports/                 # Папка для отчётов (Allure, HTML и т.д.)
│
├── requirements.txt         # Зависимости проекта
├── pytest.ini               # Конфигурация pytest
└── README.md                # Описание проекта