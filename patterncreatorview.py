#import pydoc
from patterncreatorpresenter import PatternCreatorPresenter

class PatternCreatorView():
  """
  Класс PatternCreatorView() для работы с классом PatternCreatorPresenter() (для работы в консоли)
  """
  current_pattern = "Singleton"
  patternCreatorPresenter = PatternCreatorPresenter()
  def start(self):
    """
    Функция start() для начала работы в консоли
    Возвращает краткую информацию о работе команды или предупреждение
    """
    print("\nПрограмма позволяет сгенерировать исходный код по выбранному паттерну\n")
    print("Выберите действие:\n")
    print("show patterns- Демонстрация доступных названий паттернов\n")
    print("show Singleton - Демонстрация текущего кода для паттерна Singleton\n")
    print("show Composite - Демонстрация текущего кода для паттерна Composite\n")
    print("show Proxy - Демонстрация текущего кода для паттерна Proxy\n")
    print("set Singleton - установка текущего паттерна Singleton\n")
    print("set Composite - установка текущего паттерна Composite\n")
    print("set Proxy - установка текущего паттерна Proxy\n")
    print("show current - получить название текущего паттерна\n")
    print("show code - Демонстрация кода текущего паттерна\n")
    print("create code - Создать файл с исходным кодом\n")
    print("set 1 - установка префикса названию 1-го Класса\n")
    print("set 2 - установка префикса названию 2-го Класса и название файла\n")
    print("set 3 - установка префикса названию 3-го Класса (необязательно, если Singleton)\n")
    print("show classes - Демонстрация текущих префиксов\n")
    print("show filename - Демонстрация текущего имени файла\n")
    answer = str(input())
    
    if (answer == "show patterns"):
      
      print("Pattern1: Singleton\n")
      print("Pattern2: Composite\n")
      print("Pattern3: Proxy\n")
      return("Pattern1: Singleton\nPattern2: Composite\nPattern3: Proxy\n")
    elif (answer == "show Singleton"):
      print(self.patternCreatorPresenter.pattern_dict["Singleton"])
      return self.patternCreatorPresenter.pattern_dict["Singleton"]
    elif (answer == "show Composite"):
      print(self.patternCreatorPresenter.pattern_dict["Composite"])
      return self.patternCreatorPresenter.pattern_dict["Composite"]
    elif (answer == "show Proxy"):
      print(self.patternCreatorPresenter.pattern_dict["Proxy"])
      return self.patternCreatorPresenter.pattern_dict["Proxy"]
    elif (answer == "set Singleton"):
      self.current_pattern="Singleton"
      print(f"current pattern = {self.current_pattern}")
      return f"current pattern = {self.current_pattern}"
    elif (answer == "set Composite"):
      self.current_pattern="Composite"
      print(f"current pattern = {self.current_pattern}")
      return f"current pattern = {self.current_pattern}"
    elif (answer == "set Proxy"):
      self.current_pattern="Proxy"
      print(f"current pattern = {self.current_pattern}")
      return f"current pattern = {self.current_pattern}"
    elif (answer == "show current"):
      print(f"current pattern = {self.current_pattern}")
      return f"current pattern = {self.current_pattern}"
    elif (answer == "show code"):
      print(self.patternCreatorPresenter.pattern_dict[self.current_pattern])
      return self.patternCreatorPresenter.pattern_dict[self.current_pattern]
    elif (answer == "create code"):
      code_status=self.patternCreatorPresenter.create_pattern(self.current_pattern)
      print(code_status)
      return code_status
    elif (answer == "set 1"):
      print("Введите префикс")
      answer = str(input())
      paste_status=self.patternCreatorPresenter.paste_class_name(0,answer)
      if(paste_status=="-1"):
        print('Неправильный формат ввода\nФормат:\n"[A-Za-z0-9]+"\n')
        return 'Неправильный формат ввода\nФормат:\n"[A-Za-z0-9]+"\n'
      else:
        print(paste_status)
        return(paste_status)
        
    elif (answer == "set 2"):
      answer = str(input())
      paste_status=self.patternCreatorPresenter.paste_class_name(1,answer)
      if(paste_status=="-1"):
        print('Неправильный формат ввода\nФормат:\n"[A-Za-z0-9]+"\n')
        return 'Неправильный формат ввода\nФормат:\n"[A-Za-z0-9]+"\n'
      else:
        print(paste_status)
        return(paste_status)
    elif (answer == "set 3"):
      answer = str(input())
      paste_status=self.patternCreatorPresenter.paste_class_name(2,answer)
      if(paste_status=="-1"):
        print('Неправильный формат ввода\nФормат:\n"[A-Za-z0-9]+" и без цифры в начале\n')
        return 'Неправильный формат ввода\nФормат:\n"[A-Za-z0-9]+" и без цифры в начале\n'
      else:
        print(paste_status)
        return(paste_status)
    elif (answer == "show classes"):
      
      print(f"Class1 Prefix: - {self.patternCreatorPresenter.names[0]}  \n")
      print(f"Class2 Prefix: - {self.patternCreatorPresenter.names[1]}  \n")
      print(f"Class3 Prefix: - {self.patternCreatorPresenter.names[2]}  \n")
      return(f"Class1 Prefix: - {self.patternCreatorPresenter.names[0]}  \nClass2 Prefix: - {self.patternCreatorPresenter.names[1]}  \nClass3 Prefix: - {self.patternCreatorPresenter.names[2]}  \n")
    elif (answer == "show filename"):
      print(f"{self.patternCreatorPresenter.names[1]+self.patternCreatorPresenter.names_text[1][(self.patternCreatorPresenter.get_num_pattern(self.current_pattern))]}.py")
    else:
      print("Нет такой команды")
      return("UnknownCommand")

if __name__ == "__main__":
  patternCreatorView = PatternCreatorView()
  answer="reload"
  while((answer=="reload")):
    patternCreatorView.start()
    print('\nНапишите "reload", чтобы продолжить работу программы\n')
    answer = input()
    #python patterncreatorview.py