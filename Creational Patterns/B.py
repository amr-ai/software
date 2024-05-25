class Product:
    def __init__(self):
        self.part1 = None
        self.part2 = None

    def __str__(self):
        return f"Part1: {self.part1}, Part2: {self.part2}"


class Builder:
    def build_part1(self):
        pass

    def build_part2(self):
        pass

    def get_result(self):
        pass


class ConcreteBuilder1(Builder):
    def __init__(self):
        self.product = Product()

    def build_part1(self):
        self.product.part1 = "Part1 built by Builder1"

    def build_part2(self):
        self.product.part2 = "Part2 built by Builder1"

    def get_result(self):
        return self.product


class ConcreteBuilder2(Builder):
    def __init__(self):
        self.product = Product()

    def build_part1(self):
        self.product.part1 = "Part1 built by Builder2"

    def build_part2(self):
        self.product.part2 = "Part2 built by Builder2"

    def get_result(self):
        return self.product


class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.build_part1()
        self.builder.build_part2()


if __name__ == "__main__":
    builder1 = ConcreteBuilder1()
    builder2 = ConcreteBuilder2()

    director = Director(builder1)
    director.construct()
    product1 = builder1.get_result()
    print(product1)

    director = Director(builder2)
    director.construct()
    product2 = builder2.get_result()
    print(product2)
