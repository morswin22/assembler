from SymbolTable import *

if __name__ == '__main__':
  with open('test.asm') as file:
    lines = file.read().strip().split('\n')
      
  symbols = SymbolTable()
