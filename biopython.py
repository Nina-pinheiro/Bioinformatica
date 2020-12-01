# Importante instalar o pip install biopython

# Importando pacote analise de sequências

from Bio. Seq import Seq


# Sequências são declaradas como objeto por isso precisa do método "Seq". Não dá para ser usado como uma string sequencia = "ATGGGC"

sequencia = Seq ("ATGGGC")

# Obtendo a Sequência Complementar
# Precisa de um método também, por que sequencias são declaradas como objeto no biopython

seq_complementar = sequencia.complement()

print(seq_complementar)

# Processo Transcrição DNA- RNAm

sequencia_rna = sequencia.transcribe()

print(sequencia_rna)

# Retornar a sequencia de rna para dna - processo de Transcrição reserva

seq_dna = seq_rna.back_transcribe()

print(seq_dna)

print(sequencia")


# Tradução RNAm - Proteínas

sequencia_rna = sequencia.transcribe()

# tradução

sequencia_proteina = sequencia_rna.translate()
print(sequencia_proteina)