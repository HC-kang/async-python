from odmantic import Model


class BookModel(Model):
    keyword: str
    publisher: str
    price: int
    image: str

    class Config:
        collection = "books"


# MongoDB 구조
# db: fastapi-pj -> collection: books -> document
# {
#    keyword: "aaa",
#    publisher: "bbb",
#    price: 100,
#    image: "....",
# }
