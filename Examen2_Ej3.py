#Ejercicio 3

citasProgramadas = [
    ("Vinicio", "Dra. Gonsalez", "9 de abril", "5 pm"),
    ("Miranda", "Dr. Hernandez", "15 de octubre", "11 am"),
    ("Santiago", "Dr. Dupont", "30 de agosto", "1 pm"),
    ("Leonardo", "Dra. Martinez", "1 de junio", "9 am"),
    ("Malinalli", "Dra. Cruz", "14 de noviembre", "12 pm")
]

citaEliminada = citasProgramadas.pop(2)

print(f"\nCita del {citaEliminada[2]} eliminada\n")

print("====== Citas pendientes ======")
for cita in citasProgramadas:
    print(f"Cita: {cita[0]} con {cita[1]} el {cita[2]} a las {cita[3]}")