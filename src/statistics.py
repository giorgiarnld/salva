def summary(books):

    completed = sum(
        1
        for book in books
        if book["status"] == "Completed"
    )

    return {
        "books": len(books),
        "completed": completed
    }
