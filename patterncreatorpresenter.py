import re

class PatternCreatorPresenter():
  '''
  Класс PatternCreatorPresenter() позволяет сгенерировать исходный код по паттернам со своими названиями классов.
  '''
  names=["Class1","Class2","Class3"]
  names_text=[["SingletonMeta","Component","Subject"],["Singleton","Composite","Proxy"],[None,"Leaf","RealSubject"]]
  pattern_dict=dict()
  def __init__(self):
    '''
    Конструктор класса PatternCreatorPresenter() создаёт словарь с кодом по паттернам
    '''
    self.pattern_dict={"Singleton":f'''class {self.names[0]}SingletonMeta(type):
    """
    В Python класс Одиночка можно реализовать по-разному. Возможные способы
    включают себя базовый класс, декоратор, метакласс. Мы воспользуемся
    метаклассом, поскольку он лучше всего подходит для этой цели.
    """

    _instances = dict()

    def __call__(cls, *args, **kwargs):
        """
        Данная реализация не учитывает возможное изменение передаваемых
        аргументов в `__init__`.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class {self.names[1]}Singleton(metaclass={self.names[0]}SingletonMeta):
    def some_business_logic(self):
        """
        Наконец, любой одиночка должен содержать некоторую бизнес-логику,
        которая может быть выполнена на его экземпляре.
        """

        # ...


if __name__ == "__main__":
    # Клиентский код.

    s1 = {self.names[1]}Singleton()
    s2 = {self.names[1]}Singleton()

    if id(s1) == id(s2):
        print("{self.names[1]}Singleton works, both variables contain the same instance.")
    else:
        print("{self.names[1]}Singleton failed, variables contain different instances.")''',"Composite":'''from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class {self.names[0]}Component(ABC):
    """
    Базовый класс Компонент объявляет общие операции как для простых, так и для
    сложных объектов структуры.
    """

    @property
    def parent(self) -> {self.names[0]}Component:
        return self._parent

    @parent.setter
    def parent(self, parent: {self.names[0]}Component):
        """
        При необходимости базовый Компонент может объявить интерфейс для
        установки и получения родителя компонента в древовидной структуре. Он
        также может предоставить некоторую реализацию по умолчанию для этих
        методов.
        """

        self._parent = parent

    """
    В некоторых случаях целесообразно определить операции управления потомками
    прямо в базовом классе Компонент. Таким образом, вам не нужно будет
    предоставлять конкретные классы компонентов клиентскому коду, даже во время
    сборки дерева объектов. Недостаток такого подхода в том, что эти методы
    будут пустыми для компонентов уровня листа.
    """

    def add(self, component: {self.names[0]}Component) -> None:
        pass

    def remove(self, component: {self.names[0]}Component) -> None:
        pass

    def is_composite(self) -> bool:
        """
        Вы можете предоставить метод, который позволит клиентскому коду понять,
        может ли компонент иметь вложенные объекты.
        """

        return False

    @abstractmethod
    def operation(self) -> str:
        """
        Базовый Компонент может сам реализовать некоторое поведение по умолчанию
        или поручить это конкретным классам, объявив метод, содержащий поведение
        абстрактным.
        """

        pass


class {self.names[2]}Leaf({self.names[0]}Component):
    """
    Класс Лист представляет собой конечные объекты структуры. Лист не может
    иметь вложенных компонентов.

    Обычно объекты Листьев выполняют фактическую работу, тогда как объекты
    Контейнера лишь делегируют работу своим подкомпонентам.
    """

    def operation(self) -> str:
        return {self.names[2]}"Leaf"


class {self.names[1]}Composite({self.names[0]}Component):
    """
    Класс Контейнер содержит сложные компоненты, которые могут иметь вложенные
    компоненты. Обычно объекты Контейнеры делегируют фактическую работу своим
    детям, а затем «суммируют» результат.
    """

    def __init__(self) -> None:
        self._children: List[{self.names[0]}Component] = []

    """
    Объект контейнера может как добавлять компоненты в свой список вложенных
    компонентов, так и удалять их, как простые, так и сложные.
    """

    def add(self, component: {self.names[0]}Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: {self.names[0]}Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        """
        Контейнер выполняет свою основную логику особым образом. Он проходит
        рекурсивно через всех своих детей, собирая и суммируя их результаты.
        Поскольку потомки контейнера передают эти вызовы своим потомкам и так
        далее, в результате обходится всё дерево объектов.
        """

        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Branch({'+'.join(results)})"


def client_code(component: {self.names[0]}Component) -> None:
    """
    Клиентский код работает со всеми компонентами через базовый интерфейс.
    """

    print(f"RESULT: {component.operation()}", end="")


def client_code2(component1: {self.names[0]}Component, component2: {self.names[0]}Component) -> None:
    """
    Благодаря тому, что операции управления потомками объявлены в базовом классе
    Компонента, клиентский код может работать как с простыми, так и со сложными
    компонентами, вне зависимости от их конкретных классов.
    """

    if component1.is_composite():
        component1.add(component2)

    print(f"RESULT: {component1.operation()}", end="")


if __name__ == "__main__":
    # Таким образом, клиентский код может поддерживать простые компоненты-
    # листья...
    simple = {self.names[2]}Leaf()
    print("Client: I've got a simple component:")
    client_code(simple)
    print("\n")

    # ...а также сложные контейнеры.
    tree = {self.names[1]}Composite()

    branch1 = {self.names[1]}Composite()
    branch1.add({self.names[2]}Leaf())
    branch1.add({self.names[2]}Leaf())

    branch2 = {self.names[1]}Composite()
    branch2.add({self.names[2]}Leaf())

    tree.add(branch1)
    tree.add(branch2)

    print("Client: Now I've got a composite tree:")
    client_code(tree)
    print("\n")

    print("Client: I don't need to check the components classes even when managing the tree:")
    client_code2(tree, simple)''',"Proxy":'''from abc import ABC, abstractmethod


class {self.names[0]}Subject(ABC):
    """
    Интерфейс Субъекта объявляет общие операции как для Реального Субъекта, так
    и для Заместителя. Пока клиент работает с Реальным Субъектом, используя этот
    интерфейс, вы сможете передать ему заместителя вместо реального субъекта.
    """

    @abstractmethod
    def request(self) -> None:
        pass


class {self.names[2]}RealSubject({self.names[0]}Subject):
    """
    Реальный Субъект содержит некоторую базовую бизнес-логику. Как правило,
    Реальные Субъекты способны выполнять некоторую полезную работу, которая к
    тому же может быть очень медленной или точной – например, коррекция входных
    данных. Заместитель может решить эти задачи без каких-либо изменений в коде
    Реального Субъекта.
    """

    def request(self) -> None:
        print("{self.names[2]}RealSubject: Handling request.")


class {self.names[1]}Proxy({self.names[0]}Subject):
    """
    Интерфейс Заместителя идентичен интерфейсу Реального Субъекта.
    """

    def __init__(self, real_subject: {self.names[2]}RealSubject) -> None:
        self._real_subject = real_subject

    def request(self) -> None:
        """
        Наиболее распространёнными областями применения паттерна Заместитель
        являются ленивая загрузка, кэширование, контроль доступа, ведение
        журнала и т.д. Заместитель может выполнить одну из этих задач, а затем,
        в зависимости от результата, передать выполнение одноимённому методу в
        связанном объекте класса Реального Субъекта.
        """

        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print("{self.names[1]}Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self) -> None:
        print("{self.names[1]}Proxy: Logging the time of request.", end="")


def client_code(subject: {self.names[0]}Subject) -> None:
    """
    Клиентский код должен работать со всеми объектами (как с реальными, так и
    заместителями) через интерфейс Субъекта, чтобы поддерживать как реальные
    субъекты, так и заместителей. В реальной жизни, однако, клиенты в основном
    работают с реальными субъектами напрямую. В этом случае, для более простой
    реализации паттерна, можно расширить заместителя из класса реального
    субъекта.
    """

    # ...

    subject.request()

    # ...


if __name__ == "__main__":
    print("Client: Executing the client code with a real subject:")
    real_subject = {self.names[2]}RealSubject()
    client_code(real_subject)

    print("")

    print("Client: Executing the same client code with a proxy:")
    proxy = {self.names[1]}Proxy(real_subject)
    client_code(proxy)'''}

  def check_pattern_name(self,pattern_name):
    '''
    Функция check_pattern_name класса PatternCreatorPresenter() проверяет префикс названия класса и файла
    '''


    latin_numeric_pattern = re.compile("[A-Za-z0-9]+")

    if (not pattern_name[0].isdigit()) and (latin_numeric_pattern.fullmatch(pattern_name) is not None):
      return(True)
    else:
      return(False)

  def find_pattern(self,pattern_str):
    '''
    Функция find_pattern класса PatternCreatorPresenter() проверяет наличие паттерна в словаре
    '''
    if pattern_str in self.pattern_dict:
      return(True)
    else:
      return(False)

  def get_num_pattern(self,pattern_str):
    '''
    Функция get_num_patter класса PatternCreatorPresenter() выдаёт индекс паттерна для взаимодействия с префиксами
    '''
    if(self.find_pattern(pattern_str)):
      if(pattern_str=="Singleton"):
        return 0
      elif(pattern_str=="Composite"):
        return 1
      elif(pattern_str=="Proxy"):
        return 2
    else:
      return -1
  def paste_class_name(self,pattern_int,class_name):
    '''
    Функция paste_class_name класса PatternCreatorPresenter() обновляет префикс названия класса паттерна, проверяя наличие индекса паттерна в словаре
    '''
    if (pattern_int == 0 or pattern_int == 1 or pattern_int == 2):
      if self.check_pattern_name(class_name):
        self.names[pattern_int]=class_name
        return(str(pattern_int))
      else:
        return class_name
    else:
      return "-1"
  def create_pattern(self,pattern_str):
    '''
    Функция create_pattern класса PatternCreatorPresenter() создаёт файл с исходным кодом паттерна
    '''
    if not (self.get_num_pattern(pattern_str)==-1):
      with open(f"{self.names[1]+self.names_text[1][self.get_num_pattern(pattern_str)]}.py","w+") as f:
        f.writelines(self.pattern_dict[pattern_str])
      return self.pattern_dict[pattern_str]
    else:
      return f'''{pattern_str}'''

if __name__ == "__main__":
  patternCreatorPresenter=PatternCreatorPresenter()
  print(patternCreatorPresenter.create_pattern("Singleton"))
  #patterncreatorpresenter.py