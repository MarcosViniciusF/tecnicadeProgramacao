estado = input('digite S, C, D ou V: ')
match estado:
    case "S":
        print('Souteiro')
    case "C":
        print('Casado')
    case "D":
        print('Divorciado')
    case "V":
        print('Viúvo')
    case _:
        print('Opção não valida')
