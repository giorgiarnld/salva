from src.statistics import summary

def test_statistics():

    books = [
        {
            "status": "Completed"
        },
        {
            "status": "Reading"
        }
    ]

    assert summary(books)["completed"] == 1
