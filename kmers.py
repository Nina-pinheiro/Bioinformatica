""" Project
Objective: Count The Kmers
Description: Script that shows the DNA sequences and shows the respective kmers and their frequency.
Author: Nina M. S. P. Machado
Python Major Version: 3.8.2
"""
import collections
import numpy as np
import pandas as pd

from Bio import SeqIO

# Open the file in "fasta" and make a list with the name ID and the respective sequence
seq_records = list(SeqIO.parse("file.fasta", 'fasta'))

def build_kmers(
    sequence, 
    ksize):
  """ Function to calculate the kmers numbers
  Arguments:
      sequence {string} --- DNA Sequence
      ksize {int} --- Ksize number
  Returns:
      int -- Return Kmers numbers
  """

  kmers = list()
  n_kmers = len(sequence) - ksize + 1
    # Loop to store khmers in each sequence
  for i in range(n_kmers):
    kmer = sequence[i:i + ksize]
    kmers.append(kmer)
        
  return kmers, n_kmers

  # It is an example that needs to say the size of Kmer you would like.
ksize = 2


Ids = list()
sequences = list()
sequence_objects = list()
n_kmers = list()


# Loop to store in the list 
for rec in seq_records:    
    Ids.append(rec.id)    
    sequence = str(rec.seq)h
    sequences.append(sequence)
    re = build_kmers(sequence, ksize)
    sequence_objects.append(rec)
    n_kmers.append(rec)  


# Creation of a dataframe to organize the results 
df_sequences = pd.DataFrame({'Identificadores': Ids, 'Dna sequences': sequences, 
                             'kmers': sequence_objects, 'Kmers Number': n_kmers, 'Frequency': map(collections.Counter, sequence_objects)})
df_sequences.head()