"""
Reads DNA files, shuffles them, and mutates the given
strands if necessary. Compares two DNA strands to see
which one is better (or if they are tied)

Author: Luc Bibeau
When: October 21, 2025
"""

def read_dna(filename):
    """
    Reads a DNA file and returns the cleaned list of codons
    :param filename: name of file, str
    :return: codons, list
    """
    file = open(filename)
    data = file.read().splitlines()
    file.close()

    dna = []

    for entry in data:
        if not (entry == "ERROR" or entry == ""):
            dna.append(entry)

    return dna


def shuffle(cleaned_dna):
    """
    Cuts the cleaned DNA list into two halves
    and joins them in alternating order
    :param cleaned_dna: cleaned dna, list
    :return: shuffled dna, list
    """
    midpoint = len(cleaned_dna) // 2  # middle index of the list

    left = cleaned_dna[:midpoint]
    right = cleaned_dna[midpoint:]

    shuffled_dna = []

    for i in range(midpoint):
        shuffled_dna.append(left.pop())
        shuffled_dna.append(right.pop())

    return shuffled_dna


def select_strands(shuffled_dna, num_strands):
    """
    Selects num_strands strands and returns it either as a list, string, or none
    :param shuffled_dna: shuffled dna, list
    :param num_strands: number of strands to select, int
    :return: selected strands, list || str || None
    """
    length = len(shuffled_dna)
    if length < num_strands:
        return None
    elif num_strands == 1:
        return shuffled_dna.pop()

    strands = []
    for i in range(num_strands):
        strands.append(shuffled_dna.pop())

    return strands


def strand_stability(dna_strand):
    """
    Gets the stability of a codon
    :param dna_strand: codon, str
    :return: stability, int
    """
    letter = dna_strand[0]

    # default to letter == "U"
    strand_value = 2

    match letter:
        case "C": strand_value = 3
        case "A": strand_value = 4
        case "G": strand_value = 5

    return strand_value


def chain_stability(dna_chain):
    """
    Gets the stability of a chain of DNA
    :param dna_chain: chain of dna, list
    :return: stability, int
    """
    chain_value = 0

    for dna_strand in dna_chain:
        chain_value += strand_stability(dna_strand)

    return chain_value


def needs_mutation(dna_chain):
    """
    Checks if a chain needs a mutation
    :param dna_chain:
    :return:
    """
    chain_value = chain_stability(dna_chain)
    return chain_value < 10


def mutate_chain(dna_chain, shuffled_dna):
    """
    Mutates a dna chain if needed
    :param dna_chain: dna chain, list
    :param shuffled_dna: remaining dna, list
    :return: None
    """
    if needs_mutation(dna_chain) and len(shuffled_dna) > 0:
        num_strands = 1
        strand = select_strands(shuffled_dna, num_strands)
        dna_chain.append(strand)


def compare_chains(chain_1, chain_2):
    """
    Compares the stability of two chains
    and returns the result
    :param chain_1: dna chain, list
    :param chain_2: dna chain, list
    :return: which one wins, str
    """
    chain_1_stability = chain_stability(chain_1)
    chain_2_stability = chain_stability(chain_2)

    chain_1_unstable = chain_1_stability > 14
    chain_2_unstable = chain_2_stability > 14

    if chain_1_unstable and chain_2_unstable:
        return "Both are unstable"

    if chain_1_unstable or chain_2_unstable:
        return "Chain 1 wins" if chain_2_unstable else "Chain 2 wins"

    if chain_1_stability == chain_2_stability:
        return "Tie"

    return "Chain 1 wins" if chain_1_stability > chain_2_stability else "Chain 2 wins"


def main():
    filename = input("Enter a filename: ")
    cleaned_dna = read_dna(filename)
    shuffled_dna = shuffle(cleaned_dna)

    num_strands = 3

    while len(shuffled_dna) > 6:
        chain_1 = select_strands(shuffled_dna, num_strands)
        chain_2 = select_strands(shuffled_dna, num_strands)

        print(f"\nChain 1 before: {chain_1}")
        print(f"Chain 2 before: {chain_2}")

        mutate_chain(chain_1, shuffled_dna)
        mutate_chain(chain_2, shuffled_dna)

        print(f"Chain 1 after: {chain_1}")
        print(f"Chain 2 after: {chain_2}")

        print(compare_chains(chain_1, chain_2))


if __name__ == "__main__":
    main()