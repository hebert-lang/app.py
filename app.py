import random

# Função que gera a introducao():
def gerar_introducao():
    introducoes = ["Um lindo dia começa" "eo hebert tinha acabado de acordar " "e penso hoje tá bom pra jogar um futzinho " ]
return random.choice(introdocoes)

# Função que gera o desenvolvimento da história
def gerar_desenvolvimento():
    desenvolvimentos = ["Entao hebert foi para o futebol", "chegando la ele foi escolhido pra completar o time", "e começou o jogo gooooool do hebert",
                        "deu inicio do meio campo ai vai hebert pegar e sai driblando ",  "mais um goooool do hebert ai termina a partida com 2 gols do hebert"]
    return random.choice(desenvolvimentos)

# Função que gera o final da história
def gerar_final():
    finais = ["Esta começando outro jogo", "gol do adversario  mais gol do adversario ", " ai hebert fala com seu time vamos rapaziada da pra agente ganhar" " nao desanima vamo pra cima",
              "ai comecou o show do hebert 1 gol", "2 gols hebert pega bola leva pro meio "," falta 1 um minuto pra acabar", "foi penalti hebert vai pra cobrança",
            "ele puxa a renponsa vai pra batida ", "ele deu uma cavadinha e"
            , "goooool do time do hebert e eles viram a partida",  " com 3 gols de hebert eles ganharam o jogo"   "e acabou os jogo time do hebert foi campeao."]
    return random.choice(finais)

    # Função principal que gera toda a história
def gerar_historia():
    introducao = gerar_introducao()
    desenvolvimento = gerar_desenvolvimento()
    final = gerar_final()

    historia = f"{introducao} {desenvolvimento} {final}"
    return historia
 
 # Exibe a historia gerada 
 if _name_ == "_main_":
    print(gerar_historia())

 
