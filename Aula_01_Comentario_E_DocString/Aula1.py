# o caractere # é utilizado para comentarios de linha unica
# para criação de varias linhas é utilizado """ ou ''' ante e depois das
# linhas mais isso é chamado DocString

"""
Posso escrever uma docString assim
"""
''' Assim tambem '''

# Aula sobre a função PRINT
# CRLF no Windows \r\n para criar um linha nova
# LF \n uma linha nova

print("Hello World!")
print(12, 34, 1011, sep="-", end='##\r\n##')
print(56, 78, sep="-", end='\n##')
print(9, 10, sep="-")

# Normalização Unicode (formas de normalização NFC, NFD, NFKC e NFKD)
print('\u00e1')
print('\u0061\u0301')
print("'\u00e1' == '\u0061\u0301'", '\u00e1' == '\u0061\u0301')
print('\N{Latin Capital Letter A}')
print('willian')
