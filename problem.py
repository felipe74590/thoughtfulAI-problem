
def sort(width, height, length, mass):
    
    size = "STANDARD"
    if mass >= 20:
        size = "SPECIAL"

    volume = width * height * length
    if  (width >= 150 or height >= 150 or length >= 150) or volume >= 1000000:
        if size == "SPECIAL":
            return "REJECTED"
        else:
            size = "SPECIAL"

    return size
    


if __name__ == '__main__':
    print(sort(150, 10, 11, 10))  # STANDARD
    print(sort(15, 10, 10, 20))  # SPECIAL
    print(sort(150, 10, 10, 20))  # REJECTED
    print(sort(15, 155, 10, 10))  # SPECIAL
    print(sort(15, 15, 15, 25))  # SPECIAL
    print(sort(1, 1, 1, 0.1))  # STANDARD
    print(sort(10, 15, 15, 5))  # STANDARD
    print(sort(100, 100, 100, 10))  # STANDARD