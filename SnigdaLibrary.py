class Library:
    def __init__(self, list):
        self.books = list
        self.allBooks = list.copy()

    def display_book(self):
        print(f"We have following collections in library:{snigda}")
        for book in self.books:
            print(book)

    def issue_book(self, book, user):
        if book in self.allBooks:
            if book in self.books:
                print(f"{user} have been issued {book}")
                self.books.remove(book)
                return True
            else:
                print(f"Book is already in use")
                return False
        else:
            print(f"The {book} book is not available in this library")
            return False

    def add_book(self, book):
        self.books.append(book)
        self.allBooks.append(book)
        print(f"The book {book} has been added")

    def return_book(self, book):
        if book in self.allBooks:
           self.books.append(book)
           print(f"The book {book} has been returned")
        else:
            print(f"The book {book} is not of this library")

if __name__ == '__main__':
    snigda = Library(['BRAVE', 'DARKNESS', 'GRAPES', 'VOLCANO', 'LOLITA'])
    while (True):
          print(f"__________Welcome to SNIGDA's library__________\n\nEnter your choice")
          print("0.Display_book")
          print("1.issue_book")
          print("2.add_book")
          print("3.return_book")
          user_choice = input()
          if user_choice not in ['0', '1', '2', '3']:
              continue

          else:
              user_choice = int(user_choice)

          if user_choice == 0:
              book = print(f"Display the books:{snigda.books}")
              print(f"{snigda.allBooks}")
          elif user_choice == 1:
              print("Enter the name of the book to issue: ")
              book = input().upper()
              print(book)
              print("Enter your name: ")
              user = input()
              snigda.issue_book(book, user)

          elif user_choice == 2:
              print("Enter the name of the book to add: ")
              book = input().upper()
              print(book)
              snigda.add_book(book)

          elif user_choice == 3:
              print("Enter the name of the book to return: ")
              book = input().upper()
              print(book)
              snigda.return_book(book)
          else:
              print("The book is not valid")

          print("Press q to quit and c to continue")
          user_choice = input()
          if user_choice == "q":
              exit()
          if user_choice == "c":
              continue
