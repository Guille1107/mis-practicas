def calcular_saldo_final(depositos: list, tasa_interes:float)->float:
    if len(depositos) == 0:
        return 0.0
    return (calcular_saldo_final(depositos[:-1],tasa_interes) + depositos[-1]) * (1 + tasa_interes)

depositos = [1000, 2000, 1500]
tasa = 0.05

saldo_final = calcular_saldo_final(depositos, tasa)
print( saldo_final)