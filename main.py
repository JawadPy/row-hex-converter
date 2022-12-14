def HEX_row2norm(x):
    y = str()
    for i in enumerate(x):
        i = list(i)
        i[0] += 1
        if not i[0] % 2:
            y += f"{i[1]} "
        else:
            y += i[1]
    return y[:len(y)-1]

x = "51b6" # hex in row
print(HEX_row2norm(x))
