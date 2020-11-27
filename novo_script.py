# Importar bibliotecas
import random 
import argparse 

# Código para probabilidades de mutação


def gerar_mutacao(base_nitrogenada,prob_mutar,prob_gc):
    if random.random() <= prob_mutar:
         if random.random() <= prob_gc:
            if random.random() <= 0.5:
                base_nitrogenada = "G"
            else:
                base_nitrogenada = "C"
         else:
            if random.random()<= 0.5:
                base_nitrogenada = "A"
            else:
                base_nitrogenada = "T"
    else:
        base_nitrogenada = base_nitrogenada

    return base_nitrogenada


def substituicao(seq_dna,prob_mutar,prob_gc):
    
    lista_final = []

    for base_nitrogenada in seq_dna:
         resultado = gerar_mutacao(base_nitrogenada,prob_mutar,prob_gc)

         lista_final.append(resultado)
    
    return "".join(lista_final)
  

if  __name__ == "__main__":

    parser = argparse.ArgumentParser(description = "Um programa que calcula as probabilidades de mutações")
    parser.add_argument('--S','--sequencia', dest = "seq_dna",required = True, help = "Digite a Sequência", type = str)
    parser.add_argument('--P','--probabilidade', dest = "prob_mutar",required = True, help = "Digite a probabilidade de ocorrência de mutação", type = float)
    parser.add_argument('--G', '--prob', dest = "prob_gc", required = True, help = "Digite a probabilidade de ocorrência de GC", type = float)  
    args = parser.parse_args()
    seq_dna = args.seq_dna
    prob_mutar = args.prob_mutar
    prob_gc = args.prob_gc
    seq_dna_duplicada = seq_dna + seq_dna
    verificacao = substituicao(seq_dna,prob_mutar,prob_gc)
    if len(verificacao) == len(seq_dna):
        print("Está correto")
    else:
        print("Não está correto")
        
    
    print(verificacao)
    
        


    








