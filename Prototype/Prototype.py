class Address:
    def __init__(self, city, street_address, country) -> None:
        self.city = city
        self.street_address = street_address
        self.country = country

    def __str__(self) -> str:
        return f'{self.street_address}, {self.city}, {self.country}'


class Person:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address

    def __str__(self) -> str:
        return f'{self.name} lives at {self.address}'


if __name__ == "__main__":
    john = Person("John", address=Address("123 London Road", "London", "UK"))
    print(john)
    jane = john
    jane.name = "Jane"
    print(john)
    print(jane)
