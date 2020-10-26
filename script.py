import random

# Duplicando a sequência
def duplicacao_sequencia(seq_dna):
    return 2*seq_dna

# Probabilidade de mundança - Randomizado
# A função especifica se a cada base nitrogenada muta ou não muta
def probabilidade_mutacao(lista_probabilidade,prob):
    
    lista_armazenar = []
    # Armazenar os valores randomicos
    for valores_probabilidade in lista_probabilidade:

        if valores_probabilidade <= prob:
           lista_armazenar.append("Muta") 
        else:
            lista_armazenar.append("Não Muta")
    
    return lista_armazenar

# Retornar a lista de probabilidade
def lista_probabilidade(seq_dna):

    lista_probabilidade = []

    for _ in seq_dna:
        
        lista_probabilidade.append(random.random())

    return lista_probabilidade



# Função de Retorno de G ou C - Receber G ou C

#1 SABER SE É GC OU AT
#2 SABER SE É G OU C  OU SE É A OU T

def conhecer_gc_at(valor_probabilidade,prob_gc):

    if valor_probabilidade <= prob_gc:
        return "GC"
    else:
        return "AT"

def gerar_g_c_a_t(base_mutada,valor_probabilidade):

    if base_mutada == "GC":

        if valor_probabilidade <= 0.5:
            return "G"
        else:
            return "C"
    else:
        if valor_probabilidade <=0.5:
            return "A"
        else:
            return "T"


# Função para substituir as bases nitrogenadas que sofreram mutação

def substituicao_mutacao(seq_dna,prob_mutacao,prob_gc):

    armazenamento_duplicado = duplicacao_sequencia(seq_dna)
    gerar_probabilidade_mutacao = lista_probabilidade(armazenamento_duplicado)
    verificar_muta_naomuta =  probabilidade_mutacao(gerar_probabilidade_mutacao,prob_mutacao)
    gerar_probabilidade_bases = lista_probabilidade(armazenamento_duplicado)

    # Enumerate da o do index , pois o for da so o valor
    lista_final = []
    for enum,base_nitrogenada in enumerate(armazenamento_duplicado):
        # se vai ou não mutar 

        if verificar_muta_naomuta[enum] == "Muta":
            base_nitrogenada_gc_at = conhecer_gc_at(gerar_probabilidade_bases[enum],prob_gc)
            base_nitrogenada_g_c_a_t = gerar_g_c_a_t(base_nitrogenada_gc_at,gerar_probabilidade_bases[enum])
            lista_final.append(base_nitrogenada_g_c_a_t)
        else:
            lista_final.append(base_nitrogenada)

    # concantenar a sua lista sem deixar espaço
    return "".join(lista_final)
# __ = dnderman

if  __name__ == "__main__":
    probabilidade_ocorrencia_mutacao = float(input("Digite a probabilidade de ocorrência de mutação"))
    probabilidade_gc = float(input("Digite a probabilidade de ocorrência de GC"))
    seq_dna = str(input("Digite a sequência de DNA"))
    resultado = substituicao_mutacao(seq_dna,probabilidade_ocorrencia_mutacao,probabilidade_gc)
    print(resultado)


    








