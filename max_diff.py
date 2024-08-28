lista = input()
tal = [int(num.strip()) for num in lista.split(",")]
skillnaden = max(tal) - min(tal)
print(skillnaden)
