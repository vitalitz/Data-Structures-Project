from WebCrawler import WebCrawler
# to use this class you should have the BS4 library, installation for python 2.7 - 'sudo apt-get install python-bs4' or install beautifulsoup4 packege
from RedBlackTree import RBTree
from ex1 import Ac_tag_docs
"""
The is a search engine, given a source URL, it will crawl to the depth given and extract all link in page.
Next it will convert all the links to a list, and for each link it will create a text file with the text contained in the URL
After that The engine is checking how many times each word appears in the URL text, and will build a red black tree
according to the appearance of the searched words.
"""
# For usage without WebCrawler comment next lines.
print "Enter the URL you wish to crawl.."
print 'Usage  - "http://www.bbc.com/sport/0/football/" <-- With the double quotes'
Requrl = input("Crawl this URL :>>")
print 'usage - 1, for higher integer might take time'
print "Enter a depth to crawl >> 1"
ReqDepth = input("Crawl this depth :>>")
# For usage without WebCrawler, replace next line with : ReqWords = list of words

"""
instantiations
"""
# This is the WebCrawler class, to use without comment the next line
Search_Engine = WebCrawler(Requrl,ReqDepth)

RedBlack = RBTree()
test = file('test.txt','wt')
Tree_flow = file('tree_flow.txt','wt')
# For usage without WebCrawler:
# Replace "Search_Engine.Url_list" with list of Urls.
# comment "Search_Engine.Scrap(i)" line
# Replace "Curr_link_text with a text file address matching the i Url
for i in Search_Engine.Url_list:
    print i
    Curr_link_text = Search_Engine.Scrap(i)
    Dictionary = Ac_tag_docs([Curr_link_text],3)
    Dictionary = Dictionary.tag_docs_type_a()
    print Dictionary
    RedBlack.insert_new_leaf(Dictionary,i)
RedBlack.greatest(RedBlack._root,test,Tree_flow)
RedBlack.inorder(RedBlack._root,test)
RedBlack.preorder(RedBlack._root,test)
RedBlack.delete(RedBlack._root)
RedBlack.minimum_value()
RedBlack.maximum_value()
# The URLs ordered from highest words appearances to lowest.
test.close()
# The Tree relations file.
Tree_flow.close()
print("End of program")



