"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    txt = open(file_path).read()

    return txt

open_and_read_file('gettysburg.txt')


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    

    chains = {}

    words = text_string.split()

    # print(type(words)) prints list of words split on white space
    for i in range(len(words) -2):
        tup = (words[i], words[i + 1])
        # print(tup)

        if tup not in chains.keys():
            chains[tup] = [words[i+2]]
            # print(type(chains[tup]))
        
        else:
            chains[tup].append(words[i+2])
            #print(chains[tup])
            # print(value)
    #print(chains)
    
    # print(chains)
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    lst = list(chains.keys())

    random_key = choice(lst)
    random_word = choice(chains[random_key])
    words.extend(random_key) 
    words.append(random_word)
    new_key = (random_key[1],random_word)


    while True:
        new_word = choice(list(chains[new_key]))
        new_key = (new_key[1], new_word)
        words.append(new_word)

        if new_key not in chains.keys():
            break

        #print(words)        # word 1, word2, word3, word2, word3, word4
        # print(words)

    #input:link(key, random word from value)- put in list
        #get first link, add another link, repeat
    #output: string of words from list

    return ' '.join(words)


input_path = 'gettysburg.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
