from src.progress import percentage

def test_progress():

    book = {
        "current_page": 50,
        "total_pages": 100
    }

    assert percentage(book) == 50
