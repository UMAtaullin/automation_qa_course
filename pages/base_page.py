from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Базовый класс для всех страниц проекта.
    Содержит общие методы для работы с веб-элементами: ожидания, скролл, открытие URL.
    """

    def __init__(self, driver, url):
        """
        Инициализация базовой страницы.
        :param driver: экземпляр веб-драйвера (Chrome, Firefox и т.д.)
        :param url: URL страницы, с которой будем работать
        """
        self.driver = driver
        self.url = url

    def open(self):
        """Открывает указанную страницу в браузере."""
        print(f"Opening {self.url}")  # Можно заменить на логирование
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        """
        Ожидает появления элемента в DOM и его видимости на странице.
        Возвращает первый найденный элемент (WebElement).
        !!! ВНИМАНИЕ: в текущей реализации используется
            EC.visibility_of_all_elements_located, который возвращает список.
            Правильнее использовать EC.visibility_of_element_located.
        """
        # Ошибка: all_elements_located возвращает список, а метод ожидает один элемент
        # return wait(self.driver, timeout).until(
        #     EC.visibility_of_all_elements_located(locator)
        # )
        # Правильный вариант:
        return wait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def elements_are_visible(self, locator, timeout=5):
        """
        Ожидает появления хотя бы одного элемента, удовлетворяющего локатору,
        и возвращает список всех видимых элементов.
        !!! В текущей версии используется EC.visibility_of_element_located,
            что возвращает один элемент, а не список. Название метода предполагает множественность.
        """
        # Ошибка: visibility_of_element_located возвращает один элемент
        # return wait(self.driver, timeout).until(
        #     EC.visibility_of_element_located(locator)
        # )
        # Правильный вариант:
        return wait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )

    def element_is_present(self, locator, timeout=5):
        """
        Ожидает присутствия элемента в DOM (даже если он невидим).
        Возвращает WebElement.
        """
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=5):
        """
        Ожидает присутствия в DOM хотя бы одного элемента по локатору.
        Возвращает список всех найденных элементов.
        """
        return wait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def element_is_not_visible(self, locator, timeout=5):
        """
        Ожидает, когда элемент станет невидимым или исчезнет из DOM.
        Возвращает True или сам элемент (зависит от реализации expected_conditions).
        """
        return wait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def element_is_clickable(self, locator, timeout=5):
        """
        Ожидает, когда элемент станет видимым и доступным для клика.
        Возвращает WebElement.
        """
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        """
        Прокручивает страницу так, чтобы переданный элемент оказался в видимой области.
        Полезно, если элемент находится внизу страницы и нужно проскроллить до него.
        :param element: WebElement, к которому нужно проскроллить.
        """
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
