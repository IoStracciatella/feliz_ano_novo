import time
from datetime import datetime

def feliz_2025():
    print("Aguardando 2025...")

    iterador = 0
    
    while True:
        presente = datetime.now()

        if presente.year == 2025 and presente.month == 1 and presente.day == 1 and presente.hour == 0 and presente.minute == 0 and presente.second == 0:
            if iterador < 366:  # Corrigido para 366 mensagens
                print("\nFELIZ 2025!!!!!!! :D")
                iterador += 1
            else:
                break
        time.sleep(2)

feliz_2025()

# feliz 2025, fiz esse código só pra deixar registrado esse fim de ano :)
