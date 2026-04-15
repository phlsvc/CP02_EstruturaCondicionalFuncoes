def valor_carga(c_estado,peso,c_carga):
    peso=peso*1000
    match c_estado:
        case 1:
            imposto=1.35
        case 2:
            imposto=1.25
        case 3:
            imposto=1.15
        case 4:
            imposto=1.05
        case 5:
            imposto=1.0
    if c_carga<=20:
        precopkg=100.0
    elif c_carga<=30:
        precopkg=250.0
    else:
        precopkg=340.0
    valor=(precopkg* peso )*imposto
    print(f"O valor a ser pago é: R${valor:.2f}")
    return valor
