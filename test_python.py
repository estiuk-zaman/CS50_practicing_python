name = input("Whats your name? ")

match name:
    case "Estiuk" | "istii":
        print("Hlw v2 or v1")
    # case "istii":
    #     print("Hlw v1")
    case "Oishik":
        print("Hlw old")
    case _:
        print("Who?")