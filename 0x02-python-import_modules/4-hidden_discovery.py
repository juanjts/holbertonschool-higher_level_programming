#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    lista = dir(hidden_4)
    elements = len(lista)
    for i in range(elements):
        if lista[i][0] != "_" and lista[i][1] != "_":
            print("{}".format(lista[i]))
