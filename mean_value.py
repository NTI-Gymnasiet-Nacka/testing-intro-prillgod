lista = input()
tal = [int(num.strip()) for num in lista.split(",")]
medelvärdet = sum(tal) / len(tal)
print(medelvärdet)