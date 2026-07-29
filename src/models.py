from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    total_pages: int
    current_page: int = 0
    status: str = "Reading"
