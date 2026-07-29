import csv

def export_csv(books):

    with open(
        "data/exports/books.csv",
        "w",
        newline="",
        encoding="utf8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Title",
            "Author",
            "Progress"
        ])

        for book in books:

            writer.writerow([
                book["title"],
                book["author"],
                book["current_page"]
            ])
