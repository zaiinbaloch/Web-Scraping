from bs4 import BeautifulSoup
import requests 

url = "https://books.toscrape.com/catalogue/category/books_1/index.html"
response = requests.get(url)

if response.status_code == 200:
    print("Page loaded successfully")

    # Parse the page content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all book titles (inside <h3> tags within 'article.product_pod')
    books = soup.find_all('article', class_='product_pod')

    for i, book in enumerate(books, start=1):
        # Book title is in the 'title' attribute of the <a> inside <h3>
        title = book.h3.a['title']
        print(f"Book {i}: {title}")
        print("------------------------------------------------------------")

else:
    print("Page not loaded successfully") 
    print("Error code: ", response.status_code)
