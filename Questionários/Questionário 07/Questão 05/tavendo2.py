palavra = input()
espacos = 0
ultimaletra = ""

for letra in palavra:
  if ultimaletra == " ":
    if letra == " ":
      espacos += 1
    else:
      print(espacos)
      espacos = 0
  ultimaletra = letra
