#!/usr/bin/env python
"""OOP Project

library management system
"""


class Library:
    def __init__(self, bookList, name):
        self.bookList = bookList
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"{self.name} we have following books in our library.")
        sno = 1
        for book in self.bookList:
            print(f"{sno} {book}")
            sno += 1

    def lendBook(self, book, name):
        if book in self.bookList:
            if book not in self.lendDict:
                self.lendDict.update({book: name})
                print("lender-book database has been update. you can take the book now")
            else:
                print(f"book is already being used by {self.lendDict[book]}")

    def addBook(self, book):
        self.bookList.append(book)
        print("book has been added to the book list.")

    def returnBook(self, book):
        if book in self.bookList:
            if book in self.lendDict.keys():
                self.lendDict.pop(book)
                print("thank you book is received")
            else:
                print(f"this book is {book} not in use.")
        else:
            print(f"this book is not relate to our database")


if __name__ == "__main__":
    BenLibrary = Library(
        ["Python", "Java", "Data Science", "Web Scraping", "Data Mining"], "Ben"
    )

    while True:
        print(
            f"welcome to the {BenLibrary.name} library. Enter your choice to continue"
        )
        print("1 Display Books")
        print("2 Lend a Book")
        print("3 Add a Book")
        print("4 Return a Book")
        user_choice = input()
        if user_choice not in ["1", "2", "3", "4"]:
            print("please enter a valid option")
            continue
        else:
            user_choice = int(user_choice)
        if user_choice == 1:
            BenLibrary.displayBooks()
        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend:")
            user_name = input("Enter your name:")
            BenLibrary.lendBook(book, user_name)
        elif user_choice == 3:
            book = input("Enter the name of the book you want to add")
            BenLibrary.addBook(book)
        elif user_choice == 4:
            book = input("Enter the name of the book you want to return")
            BenLibrary.returnBook(book)
        else:
            print("not a valid option")
        print("Press q to quit and c to continue....")

        user_choice2 = ""

        while user_choice2 != "c" and user_choice2 != "q":
            user_choice2 = input()
            if user_choice2 == "q":
                exit()
            elif user_choice2 == "c":
                continue
