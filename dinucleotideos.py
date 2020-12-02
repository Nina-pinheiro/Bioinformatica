# Importando pacote analise de sequências

from Bio. Seq import Seq


# Sequências são declaradas como objeto por isso precisa do método "Seq". Não dá para ser usado como uma string sequencia = "ATGGGC"

sequencia = Seq ("ATGGGCCCCC")

# Criando um dicionário
cont = {}

# Loop para contar a quantidade de dinucleotídeos
for i in ['A', 'T', 'C', 'G']:
	for j in ['A', 'T', 'C', 'G']:
		cont[i+j] = 0



for k in range(len(sequencia)-1):
	cont[sequencia[k]+sequencia[k+1]] += 1

print(cont)
