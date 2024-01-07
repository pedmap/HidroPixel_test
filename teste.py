lista = [1,2,4,8,16,32,64,128] 
# Definindo a posição relativa dos pixels vizinhos
# lin viz = lin centro + dlin(i)
# col viz = col centro + dcol(i)

# Definindo os dicionários para as posições relativas
dlin_dic = {
    1: -1,
    2: 0,
    4: 1,
    8: 1,
    16: 1,
    32: 0,
    64: -1,
    128: 1
    }
dcol_dic = {
    1: 1,
    2: 1,
    4: 1,
    8: 0,
    16: -1,
    32: -1,
    64: -1,
    128: 0
    }
a = []
for item in lista:
    a.append(dlin_dic[item])
    print(a)