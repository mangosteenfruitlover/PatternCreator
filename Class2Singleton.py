class Class1SingletonMeta(type):
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
        print("Class2Singleton failed, variables contain different instances.")