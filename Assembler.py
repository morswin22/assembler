import SymbolTable

f = open('test.asm')
code = f.readlines()
f.close()

lines = []
for line in code:
  lines.append(line[:-1])

symbols = SymbolTable.SymbolTable()

