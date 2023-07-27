a = 'A'
b = 'B'
c = 1.1
string = 'a = {} b = {} c = {:.2f}'
formato = string.format(a, b, c)
print(formato)

string = 'a = {0} b = {1} c = {2:.2f}'
formato = string.format(a, b, c)
print(formato)

string = 'a = {nome} b = {nome2} c = {nome3:.2f}'
formato = string.format(nome=a, nome2=b, nome3=c)
print(formato)
