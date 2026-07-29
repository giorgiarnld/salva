def percentage(book):

    if book["total_pages"] == 0:
        return 0

    return round(
        book["current_page"] /
        book["total_pages"] * 100,
        2
    )
