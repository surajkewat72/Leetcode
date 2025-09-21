from sortedcontainers import SortedList

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.price_map = {}
        for shop, movie, price in entries:
            self.price_map[(shop, movie)] = price

        self.available = {}
        for shop, movie, price in entries:
            if movie not in self.available:
                self.available[movie] = SortedList()
            self.available[movie].add((price, shop))

        self.rented = SortedList()

    def search(self, movie: int) -> List[int]:
        if movie not in self.available:
            return []
        return [shop for price, shop in self.available[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        price = self.price_map[(shop, movie)]
        self.available[movie].remove((price, shop))
        self.rented.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.price_map[(shop, movie)]
        self.rented.remove((price, shop, movie))
        self.available[movie].add((price, shop))

    def report(self) -> List[List[int]]:
        return [[shop, movie] for price, shop, movie in self.rented[:5]]
