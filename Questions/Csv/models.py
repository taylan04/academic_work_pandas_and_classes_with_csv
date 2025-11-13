class Restaurant():
    def __init__(self, name, neighborhood):
        self.name = name
        self.neighborhood = neighborhood
        self.items = []

    def add_item(self, item):
        self.items.append(item)