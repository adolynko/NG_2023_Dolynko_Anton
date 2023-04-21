size = int(input("input size"))
gap = 0

def cube(size,gap):
    if gap < size:
        print(size * " " + "*"+ gap * 2 * " " + "*" + size * " ")
        cube(size - 1, gap + 1)
        print(size * " " + "*"+ gap * 2 * " " + "*" + size * " ")   

cube(size, gap)
