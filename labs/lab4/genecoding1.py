"""
Reads DNA files and prints a selected portion of a shuffled strand

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
    midpoint = len(cleaned_dna) // 2

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
    elif length == 1:
        return shuffled_dna.pop()

    strands = []
    for i in range(num_strands):
        strands.append(shuffled_dna.pop())

    return strands


def main():
    filename = input("Enter a filename: ")
    cleaned_dna = read_dna(filename)
    shuffled_dna = shuffle(cleaned_dna)

    num_strands = 6

    dna_chain = select_strands(shuffled_dna, num_strands)

    print(dna_chain)


if __name__ == "__main__":
    main()