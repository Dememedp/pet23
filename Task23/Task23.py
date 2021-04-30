def split(str, symbol):
    array_of_str = list()
    helpstr = ""
    for letter in str:
        if letter == symbol:
            array_of_str.append(helpstr)
            helpstr = ""
        else:
            helpstr += letter
    array_of_str.append(helpstr)
    return array_of_str

str = input("input your string\n")
symbol = input("input split symbol\n")
print(split(str, symbol))