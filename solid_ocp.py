from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    
    
class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color 
        self.size = size 

# Wrong 

# class ProductFilter:
#     def filter_by_color(self, products, color):
#         for p in products:
#             if p.color == color: yield p
    
#     def filter_by_size(self, products, size):
#         for p in products:
#             if p.size == size: yield p 


class Specification:
    def is_satisfied(self, item):
        pass 
    
    def __and__(self, spec):
        return AndSpecification(self, spec)
    

class Filter:
    def filter(self, items, spec):
        pass


class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(
            lambda spec: spec.is_satisfied(item),
            self.args
        ))


class ColorSpecification(Specification):
    
    def __init__(self, color):
        self.color = color 
    
    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    
    def __init__(self, size):
        self.size = size
    
    def is_satisfied(self, item):
        return item.size == self.size


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == '__main__':

    apple  = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    ball = Product('Ball', Color.RED, Size.MEDIUM)
    
    products = [apple, tree, ball]
    bf = BetterFilter() # init a filter obj
    
    green_spec = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green_spec):
        print(f'- {p.name} is green')
    
    print('-' * 20)
    
    large_spec = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large_spec):
        print(f' - {p.name} is large')
    
    print('-' * 20)
    
    large_green_spec = large_spec & ColorSpecification(Color.GREEN)
    for p in bf.filter(products, large_green_spec):
        print(f'- {p.name} is large and green')