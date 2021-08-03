import requests
from bs4 import BeautifulSoup
import metadata_parser
import pprint
from time import sleep


def metadata(url):
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET",
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Max-Age": "3600",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
    }
    # pp = pprint.PrettyPrinter(indent=4)
    resp = requests.get(url, headers=headers)
    html = BeautifulSoup(resp.content, "html.parser")
    
    sleep(1)
    
    try:
        page = metadata_parser.MetadataParser(url, search_head_only=False)
    except:
        print("Not Found !!!")
    else:
        metadata = None
        try:
            get_title = "".join(page.get_metadatas("title"))
            get_desc = "".join(page.get_metadatas("description"))
        except:
            print(" ")
        else:
            metadata = {
                "link": url,
                "title": get_title,        
                "description": get_desc
                }
        # pp.pprint(metadata)
        return metadata

def get_links(search_query):
    try:
        from googlesearch import search
    except ImportError:
        print("No Module Found !!!")
    else:
        j = str(search_query)
        query = f"www.(.*{j}.*).in" # Google Dork
        try:
            search_urls = search(query, tld="co.in", lang="en", num=10, stop=10, pause=3.0)
        except:
            print("Search urls Not Found")
        else:
            return search_urls

if __name__ == "__main__":
    get_keyword = input("Enter Search Keyword : ")
    urls = get_links(get_keyword)   # Returns Generator Object
    # print(urls)
    for i in urls:
        sleep(3)
        dic = metadata(i)
        print(dic)
