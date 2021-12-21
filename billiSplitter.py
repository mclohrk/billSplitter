import random

friends = {}
dicto = {}
print('Enter the number of friends joining (including you): ')
qtd = int(input())

if qtd > 0:
    print('Enter the name of every friend (including you), each on a new line:')
    for i in range(qtd):
        friends[input()] = 0
    print("Enter the total bill value: ")
    vlt_total = int(input())
    #    y = round((vlt_total / qtd),2)
    #   dicto = dict.fromkeys(friends, y)

    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    resp = input()
    if resp == "Yes":
        y = round((vlt_total / (qtd - 1)), 2)
        dicto = dict.fromkeys(friends, y)
        lucky = random.choice(list(dicto.keys()))
        if lucky in dicto:
            dicto.update({lucky: 0})

        print(lucky, "is the lucky one!")
    if resp == "No":
        y = round((vlt_total / qtd), 2)
        dicto = dict.fromkeys(friends, y)
        print("No one is going to be lucky")
    print(dicto)
else:
    vlt_total = 0
    print("No one is joining for the party")


