# ------------------ OBSERVER PATTERN ------------------

# Observer interface
class WeatherObserver:
    def update(self, temperature):
        pass

# Concrete Observer: Display devices
class PhoneDisplay(WeatherObserver):
    def update(self, temperature):
        print(f"Phone display shows temperature: {temperature}°C")

class TVDisplay(WeatherObserver):
    def update(self, temperature):
        print(f"TV display shows temperature: {temperature}°C")

# Subject: Weather Station
class WeatherStation:
    def __init__(self):
        self.observers = []
        self.temperature = 0.0

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def set_temperature(self, temperature):
        self.temperature = temperature
        self.notify_observers()

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature)


# ------------------ STRATEGY PATTERN ------------------

# Strategy interface
class SortingStrategy:
    def sort(self, array):
        pass

# Concrete strategies
class BubbleSort(SortingStrategy):
    def sort(self, array):
        print("Sorting array using Bubble Sort")
        n = len(array)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]

class QuickSort(SortingStrategy):
    def sort(self, array):
        print("Sorting array using Quick Sort")
        self.quick_sort(array, 0, len(array) - 1)

    def quick_sort(self, array, low, high):
        if low < high:
            pi = self.partition(array, low, high)
            self.quick_sort(array, low, pi - 1)
            self.quick_sort(array, pi + 1, high)

    def partition(self, array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1

# Context class
class SortContext:
    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy

    def execute_strategy(self, array):
        self.strategy.sort(array)


# ------------------ SINGLETON PATTERN ------------------

# Singleton class
class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            print("Establishing Database Connection...")
        return cls._instance

    def execute_query(self, query):
        print(f"Executing Query: {query}")


# ------------------ FACTORY PATTERN ------------------

# Product interface
class Shape:
    def draw(self):
        pass

# Concrete products
class Circle(Shape):
    def draw(self):
        print("Drawing a Circle")

class Square(Shape):
    def draw(self):
        print("Drawing a Square")

# Factory class
class ShapeFactory:
    def get_shape(self, shape_type):
        if shape_type is None:
            return None
        if shape_type.upper() == "CIRCLE":
            return Circle()
        elif shape_type.upper() == "SQUARE":
            return Square()
        return None


# ------------------ ADAPTER PATTERN ------------------

# Existing interface
class ModernPaymentSystem:
    def process_payment(self, amount):
        pass

# Legacy class (adaptee)
class OldPaymentSystem:
    def make_payment(self, amount):
        print(f"Processing payment of: ${amount} using the old system.")

# Adapter class
class PaymentAdapter(ModernPaymentSystem):
    def __init__(self, old_system):
        self.old_system = old_system

    def process_payment(self, amount):
        self.old_system.make_payment(amount)


# ------------------ DECORATOR PATTERN ------------------

# Component interface
class Coffee:
    def get_description(self):
        pass

    def cost(self):
        pass

# Concrete component
class BasicCoffee(Coffee):
    def get_description(self):
        return "Basic Coffee"

    def cost(self):
        return 2.0

# Decorator class
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self.decorated_coffee = coffee

    def get_description(self):
        return self.decorated_coffee.get_description()

    def cost(self):
        return self.decorated_coffee.cost()

# Concrete decorators
class MilkDecorator(CoffeeDecorator):
    def get_description(self):
        return self.decorated_coffee.get_description() + ", Milk"

    def cost(self):
        return self.decorated_coffee.cost() + 0.5

class SugarDecorator(CoffeeDecorator):
    def get_description(self):
        return self.decorated_coffee.get_description() + ", Sugar"

    def cost(self):
        return self.decorated_coffee.cost() + 0.2


# ------------------ MAIN CLASS ------------------

if __name__ == "__main__":
    # 1. Observer Pattern Demo
    print("---- Observer Pattern Demo ----")
    station = WeatherStation()
    phone_display = PhoneDisplay()
    tv_display = TVDisplay()
    station.add_observer(phone_display)
    station.add_observer(tv_display)
    station.set_temperature(25.5)

    # 2. Strategy Pattern Demo
    print("\n---- Strategy Pattern Demo ----")
    array = [10, 5, 2, 8, 7]
    context = SortContext()
    context.set_strategy(BubbleSort())
    context.execute_strategy(array)
    context.set_strategy(QuickSort())
    context.execute_strategy(array)

    # 3. Singleton Pattern Demo
    print("\n---- Singleton Pattern Demo ----")
    db1 = DatabaseConnection()
    db1.execute_query("SELECT * FROM users")

    # 4. Factory Pattern Demo
    print("\n---- Factory Pattern Demo ----")
    shape_factory = ShapeFactory()
    shape1 = shape_factory.get_shape("CIRCLE")
    shape1.draw()
    shape2 = shape_factory.get_shape("SQUARE")
    shape2.draw()

    # 5. Adapter Pattern Demo
    print("\n---- Adapter Pattern Demo ----")
    old_system = OldPaymentSystem()
    payment_system = PaymentAdapter(old_system)
    payment_system.process_payment(100)

    # 6. Decorator Pattern Demo
    print("\n---- Decorator Pattern Demo ----")
    coffee = BasicCoffee()
    coffee = MilkDecorator(coffee)
    coffee = SugarDecorator(coffee)
    print(f"{coffee.get_description()} costs ${coffee.cost()}")
