import json
def process_books():
    input_ptr = open("books.json")
    outer_dic = json.load(input_ptr)
    value = outer_dic.get("booklist")
    return value

def help_me(list_of_books):
    for book in list_of_books:
        title = book.get("book")
        author = book.get("name")
        year = book.get("year")
        print(f"title: {title}\n author: {author}\n year:{year}")

def main():
    list_of_books = process_books()
    help_me(list_of_books)

main()
