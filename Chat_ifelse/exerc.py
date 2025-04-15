print("ChatSimples: Olá! Que horas são agora? (Digite apenas a hora, de 0 a 23)")

hora = int(input("Você: "))

if hora >= 0 and hora < 12:
    print("ChatSimples: Bom dia! ☀️")
elif hora >= 12 and hora < 18:
    print("ChatSimples: Boa tarde! 🌤️")
elif hora >= 18 and hora <= 23:
    print("ChatSimples: Boa noite! 🌙")
else:
    print("ChatSimples: Hora inválida. Digite um valor entre 0 e 23.")
