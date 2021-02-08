def DrawLine():
    print("+|=========================|+")

def DrawTitle(title):
    item = title
    DrawLine()
    print("+| \033[1;33;40m" + item.capitalize() + ((24 - len(item)) * " ") + "\033[0;0;0m|+")
    DrawLine()
