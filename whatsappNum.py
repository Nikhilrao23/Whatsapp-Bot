from bs4 import BeautifulSoup

html = '''

# Add Your div class with "Infinite-list" Here. Copy and Paste the whole Element HERE.
'''

def concatenate(contact):
    contact = contact.split()
    return "".join(contact)

def main():

    number_of_contacts = 0
    soup = BeautifulSoup(html, "html.parser")

    for i in soup.find_all("span"):
        if i.get('class') == ['emojitext', 'ellipsify'] and i.get('title') is not None:
            print (concatenate(i.get_text()))
            number_of_contacts += 1
    print ("The total Number of contacts are %s" %(number_of_contacts))

if __name__ == '__main__':
    main()
