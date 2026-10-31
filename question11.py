FILE = "library.txt"

def read_books():
    try:
        with open(FILE) as f:
            return [l.strip().split(",") for l in f if l.strip()]
    except FileNotFoundError:
        return []

while True:
    ch = input("\n1.Add  2.Search  3.Report  4.Exit : ")
    if ch == "1":
        with open(FILE, "a") as f:                      # append new entry
            f.write(input("Title: ") + "," + input("Author: ") + "\n")
    elif ch == "2":
        key = input("Enter title or author: ").lower()
        for b in read_books():
            if key in (b[0].lower(), b[1].lower()):
                print(b[0], "-", b[1])
    elif ch == "3":
        books = read_books()
        author = input("Author for report: ").lower()
        print("Total books:", len(books))
        print("Books by author:", sum(b[1].lower() == author for b in books))
    elif ch == "4":
        break