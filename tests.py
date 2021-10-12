from patterncreatorpresenter import PatternCreatorPresenter

class TestPatternCreator():
  """
  Класс TestPatternCreator() проводит модульные тесты для PatternCreatorPresenter
  """
  names=["Class1","Class2","Class3"]
  patternCreatorPresenter = PatternCreatorPresenter()

  def obj_reset(self):
    """
    Функция obj_reset() пересоздаёт объект класса PatternCreatorPresenter для удобного проведения тестирования 
    """
    self.patternCreatorPresenter = PatternCreatorPresenter()
  def test_check_pattern_name(self):
    """
    Функция test_check_pattern_name() проверяет, что функция check_pattern_name() из PatternCreatorPresenter правильно проверяет формат префикса названия класса 
    """
    self.obj_reset()
    assert self.patternCreatorPresenter.check_pattern_name("ClassTest") == True
    ###
    assert self.patternCreatorPresenter.check_pattern_name("1ClassTest") == False
    ###
    assert self.patternCreatorPresenter.check_pattern_name("Class/Test") == False
    ###
    assert self.patternCreatorPresenter.check_pattern_name("ClassTest1") == True
    

  def test_create_pattern(self):
    """
    Функция test_create_pattern() проверяет, что функция create_pattern() из PatternCreatorPresenter правильно возращает название файла со сгенерированным исходным кодом по паттернам со своими названиями классов
    """
    self.obj_reset()
    assert self.patternCreatorPresenter.create_pattern("Singleton") == '''class Class1SingletonMeta(type):
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


class Class2Singleton(metaclass=Class1SingletonMeta):
    def some_business_logic(self):
        """
        Наконец, любой одиночка должен содержать некоторую бизнес-логику,
        которая может быть выполнена на его экземпляре.
        """

        # ...


if __name__ == "__main__":
    # Клиентский код.

    s1 = Class2Singleton()
    s2 = Class2Singleton()

    if id(s1) == id(s2):
        print("Class2Singleton works, both variables contain the same instance.")
    else:
        print("Class2Singleton failed, variables contain different instances.")'''
    assert self.patternCreatorPresenter.create_pattern("Unknown") == '''Unknown'''
  def test_get_num_pattern(self):
    """
    Функция test_get_num_pattern() проверяет, что функция get_num_pattern() из PatternCreatorPresenter правильно выдаёт индекс 
    """
    self.obj_reset()
    assert self.patternCreatorPresenter.get_num_pattern("Singleton") == 0
    assert self.patternCreatorPresenter.get_num_pattern("Composite") == 1
    assert self.patternCreatorPresenter.get_num_pattern("Proxy") == 2
    assert self.patternCreatorPresenter.get_num_pattern("Unknown") == -1
    

  def test_paste_class_name(self):
    """
    Функция test_paste_class_name() проверяет, что функция paste_class_name() из PatternCreatorPresenter правильно обновляет префикс названия класса по индексу
    """
    self.obj_reset()
    assert self.patternCreatorPresenter.paste_class_name(0,"Class1") == "0"
    assert self.patternCreatorPresenter.paste_class_name(1,"Class2") == "1"
    assert self.patternCreatorPresenter.paste_class_name(2,"Class3") == "2"
    assert self.patternCreatorPresenter.paste_class_name(3,"Unknown") == "-1"
    assert self.patternCreatorPresenter.paste_class_name(0,"1Class1") == "1Class1"
    
  def test_find_pattern(self):
    """
    Функция test_find_pattern() проверяет, что функция find_pattern() из PatternCreatorPresenter правильно проверяет наличие паттерна в словаре 
    """
    self.obj_reset()
    assert self.patternCreatorPresenter.find_pattern("Singleton") == True
    ###
    assert self.patternCreatorPresenter.find_pattern("Composite") == True
    ###
    assert self.patternCreatorPresenter.find_pattern("Proxy") == True
    ###
    assert self.patternCreatorPresenter.find_pattern("Unknown") == False
    