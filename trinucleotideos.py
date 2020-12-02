# Caso queria contar 3 nucleotídeos

# Importando pacote analise de sequências

from Bio. Seq import Seq


# Sequências são declaradas como objeto por isso precisa do método "Seq". Não dá para ser usado como uma string sequencia = "ATGGGC"

sequencia = Seq ("ATGGGCCCCC")
cont = {}

for i in ['A', 'T', 'C', 'G']:
  for j in ['A', 'T', 'C', 'G']:
    for a in  ['A', 'T', 'C', 'G']:
      cont[i+j+a] = 0



for k in range(len(sequencia)-2):
  cont[sequencia[k]+sequencia[k+1]+sequencia[k+2]] += 1

print(cont)