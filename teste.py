frequenciaCardioR = int(input())
frequenciaCardioA = int(input())
oxigenio = int(input())

soma = frequenciaCardioR * 3
soma2 = frequenciaCardioR * 2


if frequenciaCardioA < soma2:
    if oxigenio > 97:
        print("aumentar")

if frequenciaCardioA > soma:
    print('Diminuir')
elif oxigenio < 95:
    print("diminuir")   


else:
    print("manter")
