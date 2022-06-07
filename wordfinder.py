from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary.

    >>> wf = WordFinder("words.txt")
    235886 words read

    >>> wf.random()
    ...
    """

    def __init__(self,path_to_file):
        '''Machine to pick random word from file'''
        self.filepath = open(path_to_file,'r')
        self.words_found = []
        self.total_num_words = 0

        self.loop_over_words()
        self.total_num_of_words()

        # Method to loop over the file()
        # Method to return total_num_words()

    def loop_over_words(self):
        '''Loop over all words in file
        Log words found in words_found list
        Increments total_num_words'''
        for line in self.filepath:
            self.words_found.append(line[:-2])
            self.total_num_words += 1


    def total_num_of_words(self):
        '''Returns total_num_words instance attribute'''
        #return f'{self.total_num_of_words} words read'
        print(f'{self.total_num_words} words read')


    def random(self):
        '''Return a random word within the file'''
        return choice(self.words_found)




