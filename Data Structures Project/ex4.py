'''
Created on Jan 11, 2016

@author: guy
'''

from math import floor,sqrt
import ex1

class FileX(object):
    def __init__(self,rec_word_list,address):
        self.rec_words_list = rec_word_list
        self.address = address;


class HashTable(object):
    '''
    class builds an hash table  
    '''

    def __init__(self,M):
        '''
        builds the hash table
        '''
        self.M = M;
        self.prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 
                           37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 
                           79, 83, 89, 97, 101, 103, 107, 109, 113, 
                           127, 131, 137, 139, 149, 151, 157, 163, 
                           167, 173, 179, 181, 191, 193, 197, 199, 
                           211, 223, 227, 229, 233, 239, 241, 251, 
                           257, 263, 269, 271, 277, 281, 283, 293, 
                           307, 311, 313, 317, 331, 337, 347, 349]
        self.hash_table = ['nil' for i in range(M)];
        
    def _prime_num(self,index):
        return (self.prime_list[index%len(self.prime_list)])
    
    def _hash_function(self,key):
        ''' function gets a key and returns the hashed value '''
        A = (sqrt(5) - 1)/2
        letters = list(key)
        sum = 0;
        for i in range(len(letters)):
            sum = sum + ord(letters[i])*sqrt(self._prime_num(i))    
        hval = int(floor(self.M*((sum*A)%1)))
        return hval
    
    def add_file(self,file_x):
        ''' function receives a file- file_x, and put it in the hush table
        file_x is a record containing:
        address,rec_words_list '''
        for key in file_x.rec_words_list:
            hval = self._hash_function(key)
            if self.hash_table[hval] == 'nil':
                #check for an empty list
                self.hash_table[hval] = [(key,[file_x.address])]
                print("Entered a new word!")
                print("Word: " + key)
                print(hval)
            else:
                #list exists, now we need to check if the word exist in the list
                found = 0;
                for word_tup in self.hash_table[hval]:
                    #word exists, so add the file to the list
                    if word_tup[0] == key:
                        word_tup[1].append(file_x.address)
                        found = 1;
                        print("Entered to an existing word!")
                        print("Word: " + key)
                        print(hval)
                        break;
                if found == 0:
                    #word doesn't exists, so add it
                    self.hash_table[hval].append((key,[file_x.address]))
                    print("Entered a new word to an existing list")
                    print("Word: " + key)
                    print(hval)
            
    def get_files(self,word):
        ''' function gets a word and search for files with this word'''
        hval = self._hash_function(word)
        if self.hash_table[hval] == 'nil':
            #check for an empty list
            print("No files for this word")
        else:
            #list exists, now we need to check if the word exist in the list
            found = 0;
            for word_tup in self.hash_table[hval]:
                if word_tup[0] == word:
                    found = 1;
                    print("Found Files")
                    return(word_tup)
                    break;
            if found == 0:
                #word doesn't exists, so add it
                print("Word doesn't exist")

        
if __name__ == '__main__':
    ht = HashTable(20) 
    tag_machine = ex1.Ac_tag_docs(['test.txt'],1000)
    words_test = tag_machine.tag_docs_type_a()
    for word in words_test:
        file_x = FileX([word],word)
        ht.add_file(file_x)
    population = [0 for x in ht.hash_table]
    i = 0;
    for x in ht.hash_table:
        if x != 'nil':
            population[i] = len(x);
        i = i + 1
    print(population)
    print(words_test)