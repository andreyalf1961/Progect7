class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop(Product):

    def __init__(self):
        self.__file_name = "products.txt"

    def get_products(self):
        file = open(self.__file_name, 'r')
        pr = file.read()
        file.close()
        return pr

    def add(self, *products):
        for item in products:
            a = str(item).split(', ')
            if a[0] in self.get_products():
                print(f'Продукт {str(a[0])} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(f'{str(item)}\n')
                file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
