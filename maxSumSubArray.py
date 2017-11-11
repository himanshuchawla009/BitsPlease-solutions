t=raw_input()


for x in range(int(t)):
    n = int(raw_input())

    a = []
    for i in range(int(n)):
        a.append(raw_input())

    sum = 0
    comp = []
    for j in a:
        if int(j) < 0:

            comp.append(sum)
            sum = 0

        else:
            sum = sum + int(j);
    comp.append(sum)

    print(max(comp))
