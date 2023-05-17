import pandas as pd
from tabulate import tabulate


class PerItem:
    def __init__(self, per_type, price):
        self.per_type = per_type
        self.price = price

    def __repr__(self):
        return f"{self.price} / {self.per_type}"

    def __str__(self):
        return f"{self.price} / {self.per_type}"


# currency is philippine peso
grocery_items = {
    "Fruit": {"Apple": PerItem("Kg", 170),
              "Banana": PerItem("Kg", 100),
              "Orange": PerItem("Kg", 150)},

    "Vegetable": {"Carrot": PerItem("Kg", 100),
                  "Potato": PerItem("Kg", 80),
                  "Cabbage": PerItem("Kg", 50)},

    "Meat": {"Pork": PerItem("Kg", 200),
             "Beef": PerItem("Kg", 250),
             "Chicken": PerItem("Kg", 150)},

    "Dairy": {"Milk": PerItem("L", 100),
              "Cheese": PerItem("Pack", 50),
              "Yogurt": PerItem("Cup", 50)},

    "Beverage": {"Water": PerItem("Bottle", 20),
                 "Juice": PerItem("Bottle", 50),
                 "Soda": PerItem("Bottle", 30)},

    "Snack": {"Chips": PerItem("Pack", 50),
              "Biscuits": PerItem("Pack", 30),
              "Candy": PerItem("Pack", 20)}
}


def list_items(g_items: dict, index: int = None) -> (pd.DataFrame, str):
    index = index if index is not None else int(input("Enter category: "))
    category = list(g_items.keys())[index]
    return pd.DataFrame([[x, y] for x, y in g_items[category].items()], columns=[category, "Price"]), category


def list_categories(g_items: dict) -> pd.DataFrame:
    return pd.DataFrame([[x, len(y)] for x, y in g_items.items()], columns=["Category", "Items"])


def select_item(g_items: dict, category: str, index: int = None) -> (str, PerItem):
    index = index if index is not None else int(input("Enter item: "))
    item = list(g_items[category].keys())[index]
    return item, g_items[category][item]


def how_much(item: str, per_item: PerItem, quantity: int = None) -> list:
    quantity = quantity if quantity is not None else int(input("Enter quantity: "))
    if quantity == 0:
        return []
    else:
        return [item, per_item, f"{quantity} {per_item.per_type}", per_item.price * quantity]


def proceed_to_checkout(receipt: list):
    print(tabulate(receipt, headers=["Item", "Per Item", "Quantity", "Price"], tablefmt="psql"))
    total = sum([x[-1] for x in receipt])
    print(f"Total: {total}")
    payment = int(input("Enter payment: "))
    if payment >= total:
        print(f"Change: {payment - total}")
    else:
        print("Insufficient payment")


def y_n(question: str) -> bool:
    while True:
        answer = input(question).lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Invalid answer")
            continue


def main(items: dict) -> None:
    receipt = []
    while True:
        categories = list_categories(items)
        print(tabulate(categories, headers="keys", tablefmt="psql"))

        list_grocery = list_items(items)
        print(tabulate(list_grocery[0], headers="keys", tablefmt="psql"))

        item = select_item(items, list_grocery[1])
        print(f"{item[0]} {item[1]}")

        h_many = how_much(item[0], item[1])
        receipt.append(h_many) if h_many != [] else None

        if y_n("Proceed to checkout? (y/n): "):
            proceed_to_checkout(receipt)
            return None
        else:
            continue


if __name__ == '__main__':
    main(grocery_items)
    pass
