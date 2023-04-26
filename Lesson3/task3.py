library = {}

def addBook():
    global name 
    name = input("input name : ")
    author = input("input author : ")
    numberOfPages = input("input number of pages : ")
    genre = input("input genre : ")
    binding = input("input binding : ")
    myName = {name:{"author": author, "pages": numberOfPages,"genre": genre, "binding": binding}}

    library.update(myName)
    print(library)

def editBook():
    edit = input("choose item for editing: name, author, number of pages, genre, binding : ")
    changes = input("input changes : ").lower()
    library[name][edit] = changes
    print(library)

def findBookName():
    bookName = input("input found book : ")
    for value in library:
        if value == bookName:
            print("book is exist")

def deleteBook():
    print("enter book name for deleting : ")
    try:
        name = input()
        library.pop(name)
        print(library)
    except:
        print("book doesn`t exist")

def start():
    while True:
        choose = input(
"""input command :
1 - add book
2 - remove book
3 - edit book
4 - find book
5 - exit
""")
        match choose:
            case("1"):
                print("you must add name, author, number of pages, genre, binding (hard/soft)")
                addBook()
            case("2"):
                deleteBook()
            case('3'):
                editBook()
            case("4"):
                findBookName()
            case("5"):
                exit()
            case(_):
                print("Wrong command")

start()
