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

x = "51b668db85cab9e40c69f0b78a3d578b5549ca0cc65929be5992b0386feda81704d3035894c6d97751cc95796c00eb424fb540" # hex in row
print(HEX_row2norm(x))