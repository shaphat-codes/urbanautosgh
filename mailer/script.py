with open('views.py') as f:
    lines = f.readlines()
    for i in lines:
        if i == "\n":
            i = "a line here"
        print(i)