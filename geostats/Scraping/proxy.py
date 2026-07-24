from urllib.request import Request, urlopen
import urllib.request
from lxml import etree
import re
import random

def setProxy(proxy_pool = ['41.58.162.46','167.114.102.230','81.161.61.110','183.89.171.128',\
    '110.74.222.103','35.235.75.244']):
    """[summary]

    Args:
        proxy_pool (list, optional): [description]. Defaults to ['41.58.162.46','167.114.102.230','81.161.61.110','183.89.171.128',\ '110.74.222.103','35.235.75.244'].

    Returns:
        [type]: [description]
    """
    from fake_useragent import UserAgent
    ua = UserAgent()
    header = ua.random
    Proxy_url = random.choice(proxy_pool)
    proxy_support = urllib.request.ProxyHandler({'http': Proxy_url})
    opener = urllib.request.build_opener(proxy_support)
    opener.addheaders = [('User-Agent',header)]
    return opener


def parseHtml(url):
    """[summary]

    Args:
        url ([type]): [description]

    Returns:
        [type]: [description]
    """
    try:
        rs1 = urllib.request.urlopen(url).read()
        return etree.HTML(rs1)
    except Exception as e:
        print(e.strerror)

def url_FromString(myString = 'This is an example http://example.com/blah"'):
    """[summary]

    Args:
        myString (str, optional): [description]. Defaults to 'This is an example http://example.com/blah"'.

    Returns:
        [type]: [description]
    """
    return re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', myString)

def number_FromString(mystring = "There are 2 apples for 4 persons"):
    """[summary]

    Args:
        mystring (str, optional): [description]. Defaults to "There are 2 apples for 4 persons".

    Returns:
        [type]: [description]
    """
    temp = re.findall(r'\d+', mystring)
    return list(map(int, temp))