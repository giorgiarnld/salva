from progress import percentage

def update(book, page):

    book["current_page"] = page
    book["progress"] = percentage(book)

    if page >= book["total_pages"]:
        book["status"] = "Completed"

    return book
