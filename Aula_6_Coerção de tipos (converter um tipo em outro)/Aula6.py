# Conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutaveis e primitivos:
# str, int, float, bool

var = int('1')
var2 = str(var)
var3 = str('True')
var4 = bool(var3)
print(type(var))
print(type(var2))
print(type(var3))
print(type(var4))

# erro vai dar erro pq python é de tipagem forte
# print('1' + 1)
print(int('1'), type(int('1')))
print(type(float('1') + 1))
print(bool(' '))
