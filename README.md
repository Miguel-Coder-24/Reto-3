Reto 3
Create a repo with the class exercise
Restaurant scenario: You want to design a program to calculate the bill for a customer's order in a restaurant.
Create a class diagram with all classes and their relationships.
```mermaid
classDiagram
    class MenuItem {
        -name: str
        -price: float
        +__init__(name: str, price: float)
        +__str__(): str
    }

    class Beverage {
        -alcoholic: bool
        +__init__(name: str, price: float, alcoholic: bool)
        +__str__(): str
    }

    class Appetizer {
        -vegetarian: bool
        +__init__(name: str, price: float, vegetarian: bool)
        +__str__(): str
    }

    class MainCourse {
        -vegetarian: bool
        +__init__(name: str, price: float, vegetarian: bool)
        +__str__(): str
    }

    class Order {
        -items: List[MenuItem]
        +__init__()
        +add_item(item: MenuItem): void
        +total(): float
        +show_order(): void
    }

    MenuItem <|-- Beverage
    MenuItem <|-- Appetizer
    MenuItem <|-- MainCourse
    Order --> MenuItem : contains

    %% Menu items as pseudo-instances
    class Coke {
        <<Beverage>> 
        +name = "Coke"
        +price = 1.5
        +alcoholic = false
    }

    class Water {
        <<Beverage>> 
        +name = "Water"
        +price = 1.0
        +alcoholic = false
    }

    class Wine {
        <<Beverage>> 
        +name = "Wine"
        +price = 5.0
        +alcoholic = true
    }

    class Beer {
        <<Beverage>> 
        +name = "Beer"
        +price = 4.0
        +alcoholic = true
    }

    class Salad {
        <<Appetizer>> 
        +name = "Salad"
        +price = 3.5
        +vegetarian = true
    }

    class Fries {
        <<Appetizer>> 
        +name = "Fries"
        +price = 2.5
        +vegetarian = true
    }

    class Soup {
        <<Appetizer>> 
        +name = "Soup"
        +price = 3.0
        +vegetarian = false
    }

    class Pizza {
        <<MainCourse>> 
        +name = "Pizza"
        +price = 8.0
        +vegetarian = true
    }

    class Burger {
        <<MainCourse>> 
        +name = "Burger"
        +price = 9.5
        +vegetarian = false
    }

    class Pasta {
        <<MainCourse>> 
        +name = "Pasta"
        +price = 7.5
        +vegetarian = true
    }

    %% Linking instances to their classes
    Beverage <|.. Coke
    Beverage <|.. Water
    Beverage <|.. Wine
    Beverage <|.. Beer
    Appetizer <|.. Salad
    Appetizer <|.. Fries
    Appetizer <|.. Soup
    MainCourse <|.. Pizza
    MainCourse <|.. Burger
    MainCourse <|.. Pasta
