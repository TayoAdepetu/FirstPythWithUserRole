from fastapi import FastAPI

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Think Python",
        "author": "Allen B. Downey",
        "publisher": "O'Reilly Media",
        "published_date": "2021-01-01",
        "page_count": 1234,
        "language": "English",
    },
    {
        "id": 2,
        "title": "Django By Example",
        "author": "Antonio Mele",
        "publisher": "Packt Publishing Ltd.",
        "published_date": "2021-01-19",
        "page_count": 1023,
        "language": "English",
    },
    {
        "id": 3,
        "title": "The Web Socket Handbook",
        "author": "Alex Diaconu",
        "publisher": "PXinyu Wang",
        "published_date": "2019-01-05",
        "page_count": 3677,
        "language": "English",
    },
    {
        "id": 4,
        "title": "Head First JavaScript",
        "author": "Helen Smith",
        "publisher": "O'Reilly Media",
        "published_date": "2013-11-23",
        "page_count": 540,
        "language": "English",
    },
    {
        "id": 5,
        "title": "Head First HTML5 Programming",
        "author": "Eric T. Freeman",
        "publisher": "O'Reilly Media",
        "published_date": "1999-08-25",
        "page_count": 3006,
        "language": "English",
    },
    {
        "id": 6,
        "title": "Algorithms and Data Structures in Python",
        "author": "Kent Lee",
        "publisher": "Springer, Inc.",
        "published_date": "2006-11-15",
        "page_count": 9282,
        "language": "English",
    },
]
