import urllib,re
from bs4 import BeautifulSoup
from urlparse import urlparse
import string

class WebCrawler(object):

    def __init__(self,source_url,depth):
        # source_url should be of type http://example.ext/..., depth is the depth links will be exctracted from the
        # source_url
        self._SourceUrl = source_url
        self._Depth = depth
        self.Url_list = []
        self._main()

    Depth = property(fget=lambda self: self._Depth, doc="The Depth of links search from the source url")
    SourceUrl = property(fget=lambda self: self._SourceUrl, doc="The initial Url to start crawl from")

    def _main(self):
        self._MyFile = file('URL_List.txt', 'wt')
        self._Crawler(self._SourceUrl,self._Depth)
        self._MyFile.close()
        temp = open("URL_List.txt", "r")
        lines = [line for line in temp if line.strip()]
        lines.sort()
        counter = 0
        prev = None
        for i in lines:
            if prev == i:
                continue
            else:
                prev = i
                self.Url_list.append(i)
                counter += 1
            # How many links to save in the Object, replace to get bigger tree.
            if counter == 30:
                break
        temp.close()

    def Scrap(self,link):
        # link - web page to get text from
        url = link
        html = urllib.urlopen(url).read()
        soup = BeautifulSoup(html)

        # kill all script and style elements
        for script in soup(["script", "style"]):
            script.extract()    # rip it out

        # get text
        text = soup.get_text(separator=' ')

        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)
        text = filter(lambda x: x in string.printable, text)
        File = file('test_file.txt','wt')
        File.write(text)
        File.close()
        return 'test_file.txt'

    def _Crawler(self,base_url,depth):
        """
        A webcrawler that start to crawl from the base url and reach to depth of depth
        """
        if depth == 0: return
        Parsedurl = urlparse(base_url)
        PreURL = Parsedurl.scheme + '://' + Parsedurl.netloc
        SecURL = Parsedurl.scheme + ':'
        for i in re.findall('''<a href="(.[^"']+)"''', urllib.urlopen(base_url).read(), re.I):
            if "#" in i:
                i = base_url + i
            elif ("http" not in i) and ("//" not in i):
                i = PreURL + i
            elif ("http") not in i:
                i = SecURL + i
            if " " in i:
                continue
            self._Crawler(i,depth-1)
            if depth == 1: self._MyFile.write(i + '\n')

        self._MyFile.write(base_url + '\n')



