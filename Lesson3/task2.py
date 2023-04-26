size = int(input("input size : "))
gap = 1

def cube(size,gap):
    if size != 1:
        print(size * " " + gap * "*" + size * " ")
        cube(size - 1, gap + 2)
        print(size * " " + gap * "*" + size * " ")
    

cube(size, gap)

