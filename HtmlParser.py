# pip install bs4
import requests
import bs4
import sys

def request_page(url):
    try:
        return requests.get(url).content
    except Exception as e:
        print(e)
        return False

def process_page(html):
    try:
        dom = bs4.BeautifulSoup(html)

        # finds first p rag
        print('----dom.p----')
        print(dom.p)

        # finds all anchor tags
        print('----dom.find_all("a")----')
        print(dom.find_all('a'))

        # css selector
        print('----dom.select("html head title")----')
        print(dom.select("html head title"))

        # immediate children as a list
        print(dom.contents)

        # immediate children as a generator exp
        for child in dom.children:
            print(child)

        # finds all children recursively as a generator exp
        for element in dom.descendants:
            print(element)

        page_to_tree(dom.html, 0)

    except Exception as e:
        print(e)

def page_to_tree(dom, indent):
    if not dom or not dom.name:
        print('-' * indent + '<' + dom + '>')
        return
    print('-' * indent + '<' + dom.name + '>')
    for child in dom.children:
        page_to_tree(child, indent + 1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("python3 HtmlParser.py <url>")
    else:
        page = request_page(sys.argv[1])
        if page:
            process_page(page)