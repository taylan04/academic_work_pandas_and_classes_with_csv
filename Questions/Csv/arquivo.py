import csv

def read_file():
    restaurants = []
    try:
        with open("pedidos_e_avaliacoes.csv", mode="r", encoding="UTF-8") as doc:
            reader = csv.reader(doc)
            for line in reader:
                restaurants.append(line)
    except Exception as ex:
        print(f"{ex}")
    return restaurants[1:]
        