#bash tests.bash
#bash doc.bash
#python patterncreatorview.py
from patterncreatorview import PatternCreatorView


patternCreatorView = PatternCreatorView()
answer="reload"
while((answer=="reload")):
  patternCreatorView.start()
  print('\nНапишите "reload", чтобы продолжить работу программы\n')
  answer = input()
  #python patterncreatorview.py