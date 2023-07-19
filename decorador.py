def decorador_imprimir(func):
    def mensagem(*args):
        resp = func(*args)
        msg = f'''CAPITAL: {args[0]} TAXA: {args[1]} TEMPO: {args[2]}
RESULTADO: {resp}'''
        print(msg)
        return(resp)
    return mensagem

@decorador_imprimir
def juros_simples(capital, taxa, tempo):
    return capital * (taxa / 100) * tempo

retorno = juros_simples(1000, 5, 10)

def juros_potemcia(capital, taxa, tempo):
    return capital * (taxa / 100) * (tempo ** 1.1)
