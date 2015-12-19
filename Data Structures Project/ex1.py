#!/usr/bin/python
'''
Created on Nov 27, 2015

@author: guy
'''
import string
from collections import defaultdict
from os import listdir
from os.path import isfile, join


def part_a_get_key(item):
    return item[1]

def open_read_file(file_address):
    try:
        rf = open(file_address,'r')
        return rf
    except IOError,message:
        print "Could not open file!",message
        raise(BaseException)


class Aa_which_words_in_text(object):
    '''
    This object represents a search engine machine - it receives a file address
    and can give you the number of words in the file
    '''
    def __init__ (self,file_address):
        self.file_address = file_address;
        self.words_dict = None
    
    def _return_words_from_file_without_punc(self):
        
        #open the file and read it (O(n))
        rf = open_read_file(self.file_address);
        rf_content = rf.read()
        #format the words to ignore spaces, dots and commas (O(n))
        rf_words = rf_content.split()
        #remove punctuation
        rf_words = [word.strip(string.punctuation) for word in rf_words]
        #remove empty words
        rf_words = filter(None,rf_words)
        #ignore upper case
        rf_words = [word.lower() for word in rf_words]
        return rf_words
        
    def _remove_connection_words_from_dic(self,dic):
        forbidden_words = ['is','the','a','an','and']
        for word in forbidden_words:
            try:
                dic.pop(word)
            except KeyError:
                pass
        return dic
    
    def how_many_words_in_file(self):
        ''' function reads the file and saves the words from it 
        in a defaultdict in which the keys are the words, and 
        the values are the amount of times the word exist in file'''
        
        rf_words = self._return_words_from_file_without_punc();
        
        #run on the read file and put it into a dictionary
        defdict = defaultdict(int)
        for word in rf_words:
            defdict[word] = defdict[word] + 1
            
        defdict = self._remove_connection_words_from_dic(defdict)    
        
        # DEBUG
        #print(defdict)
        
        return defdict
        
        
class Ab_which_words_in_text(Aa_which_words_in_text):
    '''
    This object represents a search engine machine - it receives a file address
    and a list of words, and returns the number of appearances of the words
    in the text
    '''
    def __init__(self,file_address,words_list = None):
        Aa_which_words_in_text.__init__(self,file_address)
        self.words_list = words_list
    
    def how_many_words_in_file(self):
        if self.words_list == None:
            return(Aa_which_words_in_text.how_many_words_in_file(self))
        else:
            rf_words = self._return_words_from_file_without_punc();
            #produce a dictionary with only the word list, 
            #count the number of words in rf_words that are same as word list
            #define a dictionary using the words list as keys
            words_dict = dict((el,0) for el in self.words_list)
            #count the number of times the words are in text, if the word read
            #isn't in the words list than skip it
            for word in rf_words:
                try:
                    words_dict[word] = words_dict[word] + 1
                except KeyError:
                    pass
            return(words_dict)    
                
            #debug
            #print(words_dict)
                    
class Ac_tag_docs(object):
    ''' 
    class represents a tag machine - it receives list of docs addresses
    and returns, and give back the words that should be used to tag the words
    inputs: 1. doc_address_list: documents address list
            2. list_size: the size of the list of the tagging words
    outputs: 1. list of words that should be used to tag the words
    '''
    def __init__(self,doc_address_list,list_size):
        self.doc_address_list = doc_address_list
        self.list_size = list_size
    
    
    
    def _most_used_words_in_dict(self,dict_i):
        t = []
        for key, value in dict_i.items():
            t.append((key, value))
        d = sorted(t,key=part_a_get_key)
        return d
        
    def tag_docs_type_a(self):
        ''' in this function we go through doc 1 and returns a dictionary of 
        most used words, (without connection words (a,the,is etc..)
        in second phase we go through the other files and search how many 
        times the words found in first doc were in this files. 
        '''
        #first fase - get all the words from the first doc
        search_engine = Ab_which_words_in_text(self.doc_address_list[0])
        words_dic = search_engine.how_many_words_in_file()
        
        
        #check if there is a list of files and not just one file
        if len(self.doc_address_list) > 1:
            #list of files exist - check for each file how many times the words 
            #from the first file exists, remove all the words that doesn't exist
            #in the new file
            for doc_address in self.doc_address_list[1:]:
                print(doc_address) 
                print(words_dic)
                search_engine = Ab_which_words_in_text(doc_address,words_dic.keys())
                current_words_dic = search_engine.how_many_words_in_file()
                for key,value in current_words_dic.items():
                    if value == 0:
                        words_dic.pop(key)
                    else:
                        words_dic[key] = words_dic[key] + value
    
        #in this point we should have a dictionary with all the possible tag words
        #we need to translate the dictionary into a list of the most common words
        most_used_words = self._most_used_words_in_dict(words_dic)
        print(most_used_words)
        most_used_words_keys = [word_tuple[0] for word_tuple in most_used_words]        
                    
        tag_words = most_used_words_keys[len(most_used_words)-self.list_size:]
        return tag_words
           
if __name__ == '__main__':
    file_address_list = ['test.txt','test2.txt','test3.txt']
    list_size = 3                   
    tag_machine = Ac_tag_docs(file_address_list,list_size)
    tag_words = tag_machine.tag_docs_type_a()
    print(tag_words)

    
        
        
