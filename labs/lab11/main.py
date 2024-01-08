"""
Bioinformatics is a field where biologists use the power of computers
to help analyze biological data, such as DNA.

DNA can be represented as a long string of 4 characters: A, T, G, and C.

In this lab, we will create a graph of DNA using the squiggle method
as described in the The following link:

 - https://squiggle.readthedocs.io/en/latest/methods.html#squiggle

Our DNA data comes from the following article:

 - https://gab41.lab41.org/the-walk-of-life-4d352212a099


"""
import turtle


### Testing DNA sequences, implemented as a python dictionary.
### i.e. DNA['Human'] will return a snippet of the human DNA string
DNA = {
    'Human' :  'ATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAGGCTGCTGGTGGTCTACCCTTGGACCCAGAGGTTCTTTGAGTCCTTTGGGGATCTGTCCACTCCTGATGCTGTTATGGGCAACCCTAAGGTGAAGGCTCATGGCAAGAAAGTGCTCGGTGCCTTTAGTGATGGCCTGGCTCACCTGGACAACCTCAAGGGCACCTTTGCCACACTGAGTGAGCTGCACTGTGACAAGCTGCACGTGGATCCTGAGAACTTCAGGCTCCTGGGCAACGTGCTGGTCTGTGTGCTGGCCCATCACTTTGGCAAAGAATTCACCCCACCAGTGCAGGCTGCCTATCAGAAAGTGGTGGCTGGTGTGGCTAATGCCCTGGCCCACAAGTATCACTAA',
    'Rat' : 'ATGGTGCACCTGACTGATGCTGAGAAGGCTGCTGTTAATGGCCTGTGGGGAAAGGTGAACCCTGATGATGTTGGTGGCGAGGCCCTGGGCAGGCTGCTGGTTGTCTACCCTTGGACCCAGAGGTACTTTGATAGCTTTGGGGACCTGTCCTCTGCCTCTGCTATCATGGGTAACCCTAAGGTGAAGGCCCATGGCAAGAAGGTGATAAACGCCTTCAATGATGGCCTGAAACACTTGGACAACCTCAAGGGCACCTTTGCTCATCTGAGTGAACTCCACTGTGACAAGCTGCATGTGGATCCTGAGAACTTCAGGCTCCTGGGCAACATGATTGTGATTGTGTTGGGCCACCACCTGGGCAAGGAATTCTCCCCCTGTGCACAGGCTGCCTTCCAGAAGGTGGTGGCTGGAGTGGCCAGTGCCCTGGCTCACAAGTACCACTAA', 
    'Rhesus' :  'ATGGTGCATCTGACTCCTGAGGAGAAGAATGCCGTCACCACCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAGGCTGCTGGTGGTCTACCCTTGGACCCAGAGGTTCTTTGAGTCCTTTGGGGATCTGTCCTCTCCTGATGCTGTTATGGGCAACCCTAAGGTGAAGGCTCATGGCAAGAAAGTGCTTGGTGCCTTTAGTGATGGCCTGAATCACCTGGACAACCTCAAGGGTACCTTTGCCCAGCTCAGTGAGCTGCACTGTGACAAGCTGCATGTGGATCCTGAGAACTTCAAGCTCCTGGGCAACGTGCTGGTGTGTGTGCTGGCCCATCACTTTGGCAAAGAATTCACCCCGCAAGTGCAGGCTGCCTATCAGAAAGTGGTGGCTGGTGTGGCTAATGCCCTGGCCCACAAGTACCACTAA', 
    'Chimpanzee' : 'ATGGTGCACCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAGGCTGCTGGTGGTCTACCCTTGGACCCAGAGGTTCTTTGAGTCCTTTGGGGATCTGTCCACTCCTGATGCTGTTATGGGCAACCCTAAGGTGAAGGCTCATGGCAAGAAAGTGCTCGGTGCCTTTAGTGATGGCCTGGCTCACCTGGACAACCTCAAGGGCACCTTTGCCACACTGAGTGAGCTGCACTGTGACAAGCTGCACGTGGATCCTGAGAACTTCAGGCTCCTGGGCAACGTGCTGGTCTGTGTGCTGGCCCATCACTTTGGCAAAGAATTCACCCCACCAGTGCAGGCTGCCTATCAGAAAGTGGTGGCTGGTGTGGCTAATGCCCTGGCCCACAAGTATCACTAA'
}
"""

Squiggle’s DNA visualization method is based on the UCSC .2bit format 
and the Qi et. al Huffman coding method. In essence, a DNA sequence is 
first converted into binary using the 2bit encoding scheme that maps 
T to 00, C to 01, A to 10, and G to 11. For example:

ATGC

becomes:

10001101

"""

dna_to_code_dict = {
    'T': '00',
    'C': '01',
    'A': '10',
    'G': '11'
}

"""
Exercise 1

Given a DNA sequence, return a coded sequence of 1's and 0's.
You will use the dna_to_code_dict to map between base and
the code.

HINT: this is extrememly similar to the book's exercise 12.7.5 
where you implement a translation service.

i.e.

> dna_to_code('A')
'10'
> dna_to_code('T')
'00'
> dna_to_code('G')
'11'
> dna_to_code('C')
'01'
> dna_to_code('AA')
'1010'
> dna_to_code('AATT')
'10100000'

"""

def dna_to_code(dna):
    coded = ''

    # use the accumulator pattern to process each character of
    # the input dna string.  Convert each character to it's
    # coded counterpart using dna_to_code_dict
    
    return coded


### These draw functions are provided for you to use in Exercise 2
    
def draw_0(t):    
    t.right(80)
    t.forward(3)
    t.left(80)

def draw_1(t):
    t.left(80)
    t.forward(3)
    t.right(80)
    
######


"""
Exercise 2

Given a coded sequence and a color, graph the sequence
by looping over every character (either 0 or 1) and call 
the appropriate draw function provided above.

"""
def draw_coded(coded, color):
    # A turtle is already setup for you
    t = turtle.Turtle()
    t.penup()
    t.speed(0)
    t.goto(-300,-100)
    t.color(color)
    t.pendown()

    # process every character in the coded string and
    # call the corresponding draw function as provided
    # above.

"""
Exercise 3

With draw_coded written, we can create a DNA visualization
using the following sequence of commands:

> code = dna_to_code('AGTTGC')
> draw_coded(code, 'red')

To make it more convenient, complete the following
visualize function such that we can pass in a DNA sequence
instead of a coded sequence.  Our user will mainly 
interact with visualize instead of draw_coded.
"""
def visualize(dna, color):
    # perform the entire operation of visualizing a
    # DNA sequence
    pass
    
# The main function simply visualize 4 sample DNA sequences
# in different colors.  Your output would look similar to the
# image at https://gab41.lab41.org/the-walk-of-life-4d352212a099 
def main():
    visualize(DNA['Human'],'red')
    visualize(DNA['Rat'],'green')
    visualize(DNA['Rhesus'],'blue')
    visualize(DNA['Chimpanzee'],'pink')
