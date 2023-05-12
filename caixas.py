A = int(input())
B = int(input())
C = int(input())
soma = A + B

if soma < C:
    print('foi possivel fazer em uma viagem')

if A < C:
    if B > C:
        print('foi possivel fazer em 2 viagens')

if A < C:
    if B >= C:
        print('foi possivel fazer em 2 viagens')

if A <= B:
    if B >= C:
        print('foi possivel fazer em 2 viagens')

if A <= B:
    if B <= C:
        print('foi possivel fazer em 2 viagens')

if B <= C:
    if A > C:
        print('foi possivel fazer em 2 viagens')



if A >= C and B >= C or B >= C and A >= C:
    print('foi possivel fazer em 3 viagens')
    