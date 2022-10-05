# This is a program created for the purpose of scraping news websites and collecting relevant information
# This code was written by Amr Elseweifi for Eshhad

from bs4 import BeautifulSoup
import re
import requests

def main():

    websites = ['https://en.wataninet.com/', 'https://www.coptsunited.com/' ] # Enter the URLs you want to scrape from
    file_name = 'name' # Enter a name for the file

    file = open(file_name + '.txt', 'w', encoding="utf-8")
    # The above line creates a file on the computer where the output will be stored

    for website in websites:
        textContent = str(parser(website, 'Coptic'))
        file.write('\n')
        file.write(website + ':' + remove_tags(textContent) + '\n')
        print(website, ':', remove_tags(textContent))
    # The above lines call the parser function and store the output into the file

    file.close()

def remove_tags(text):
    TAG_RE = re.compile(r'<[^>]+>')
    return TAG_RE.sub('', text)

def parser(page_link, keyword):

    page_response = requests.get(page_link, timeout=5)
    # The above line fetches the content from the URL, using the requests library
    page_content = BeautifulSoup(page_response.content, "html.parser")
    # The above line uses the HTML parser to parse the URLs' contents
    textContent = page_content.find_all("p", text=lambda t: t and keyword in t)
    # The above line searches for the keyword(s)
    return textContent

main()
