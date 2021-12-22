from decimal import Decimal
import math
import decimal


def same_one(N,A, n):
    for k in range(n - 1):
        decimal.getcontext().prec = 3
        a = Decimal(math.sqrt((N[k][1] - 1) ** 2 + w ** 2))
        A += a
    return A


w = 4
N = [[1,4],[1,4],[1,4]]
n = len(N)
r = 0
A = 0
a = 0
S = {-1}

for i in range(n):
    if N[i][1] == 1:
        r += 1
        if r == n:
            A = w * (n - 1)
            print('Всі стовпи з висотою 1')
            print("Потрібна довжина дроту: ", A)

    elif N[0][1] == N[i][1]:
        r += 1
        if r == n:
            o = same_one(N,A, n)
            print('Всі стовпи мають одинакову максимальну висоту, але не 1')
            print("Потрібна довжина дроту: ", o)

    else:
        for k in range(n - 1):
            if N[k][1] >= N[k + 1][1]:
                N[k + 1][1] = 1
                a = math.sqrt((N[k][1] - 1) ** 2 + w ** 2)
                A += a

            else:
                if k in S and N[k + 1][1] - N[k][1] >= N[k][1] - 1:
                    a = math.sqrt((N[k + 1][1] - N[k][1]) ** 2 + w ** 2)
                    A += a
                    S.add(k)
                    S.add(k + 1)

                elif k in S and N[k + 1][1] - N[k][1] < N[k][1] - 1:
                    N[k + 1][1] = 1
                    a = math.sqrt((N[k][1] - 1) ** 2 + w ** 2)
                    A += a
                    S.add(k)
                    S.add(k + 1)


                else:
                    N[k][1] = 1
                    a = math.sqrt((N[k + 1][1] - 1) ** 2 + w ** 2)
                    A += a
                    S.add(k)
                    S.add(k + 1)
        print(N)
        print("Всі стовпи різної максимальної висоти")
        print("Потрібна довжина дроту M: ", A)
        break
