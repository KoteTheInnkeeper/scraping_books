from typing import Dict, Union, Callable

from app import web_bookshelf

USER_CHOICE = """Enter one of the following
- 'b' to look at only 5-star books.
- 'c' to look for the cheapest books.
- 'n' to just get the next available book on the catalogue.
- 'q' to exit. """

COMMAND_PROMPT = "\nEnter your choice: "


def print_best_books():
    """
        Sort the books in 'web_bookshelf' and will only show the top 5 books.
    :return:
    """
    best_books = sorted(web_bookshelf.content, key=lambda x: (x.rating * -1, x.price))[:10]
    for book in best_books:
        print(book)


def print_five_stars_books():
    """
        Prints only the five stars books.
    :return: None
    """
    best_books = sorted(web_bookshelf.content, key=lambda x: x.price)
    for book in best_books:
        if book.rating == 5:
            print(f"-> {book}")


def print_cheapest_books():
    print("The cheapest books are shown below:")
    cheapest_books = sorted(web_bookshelf.content, key=lambda x: x.price * -1)
    for book in cheapest_books:
        print(f"-> {book}")



def look_next():
    print("Not implemented yet.")
    pass


def quit_program():
    print("Thank you for using this program!")
    exit()


def main_menu():
    operations = {
        'b': print_five_stars_books,
        'c': print_cheapest_books,
        'n': look_next,
        'q': quit_program
    }
    user_input = input(COMMAND_PROMPT).lower().strip()
    try:
        to_perform = operations[user_input]
        to_perform()
    except KeyError:
        print(f"{user_input} is not a valid input. Try again.")


print(USER_CHOICE)
_ = True
while _:
    main_menu()
