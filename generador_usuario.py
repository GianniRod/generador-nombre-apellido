from random import randint

nombres = ["Marcos", "Lucas", "Julian", "Enzo", "Jose", "Massimo", "Alessandro", "Giancarlo", "Thomas", "Bruno", 
           "Carla", "Maria", "Laura", "Lorena", "Ana", "Gabriela", "Florencia", "Mariana", "Camila", "Valentina", 
           "Martin", "Juan", "Pablo", "Agustin", "Leandro", "Nicolas", "Federico", "Gonzalo", "Mauricio", "Ezequiel", 
           "Cristina", "Luisa", "Gabriela", "Paola", "Veronica", "Bianca", "Carina", "Luna", "Romina", "Sofia", 
           "Miguel", "Fernando", "Ricardo", "Andres", "Javier", "Eduardo", "Maximiliano", "Gustavo", "Alejandro", 
           "Emilia", "Lucia", "Isabel", "Sara", "Candela", "Martina", "Emma", "Carolina", "Abril", "Micaela", 
           "Mauricio", "Facundo", "Marcelo", "Matias", "Ignacio", "Guillermo", "Julio", "Lautaro", "Tomas", "Tobias",
           "Elena", "Victoria", "Lola", "Violeta", "Juana", "Paula", "Sol", "Rocio", "Carla", "Loreto",
           "Renata", "Aurora", "Gala", "Frida", "Miranda", "Belen", "Margarita", "Natalia", "Camila", "Candela",
           "Marta", "Cecilia", "Clara", "Dalma", "Sofia", "Florencia", "Gabriela", "Pilar", "Rosa", "Sara",
           "Daniel", "Santiago", "Ramon", "Adrian", "Mario", "Esteban", "Enrique", "Pablo", "Joaquin", "Diego",
           "Felix", "Evaristo", "Gaspar", "Maximo", "Matias", "Teodoro", "Vicente", "Ulises", "Tomas", "Roberto"]
apellidos = ["Rodriguez", "Mateo", "Batallini", "Armani", "Alvarez", "Zuculini", "Perez", "Barboza", "Jackson", "Ditta", 
             "Lopez", "Garcia", "Martinez", "Perez", "Sanchez", "Gonzalez", "Gomez", "Diaz", "Fernandez", "Alonso", 
             "Gimenez", "Silva", "Gutierrez", "Castro", "Santos", "Pereyra", "Romero", "Ruiz", "Luna", "Vega", 
             "Gonzalez", "Perez", "Garcia", "Lopez", "Gomez", "Martinez", "Fernandez", "Sanchez", "Diaz", "Alonso", 
             "Silva", "Gimenez", "Pereyra", "Santos", "Castro", "Vega", "Romero", "Ruiz", "Luna", "Medina"]

nombrelegido = ""
apellidoelegido = ""

while nombrelegido != "Giancarlo" or apellidoelegido != "Rodriguez":
    nombreazar = randint(0, len(nombres) - 1)
    apellidoazar = randint(0, len(apellidos) - 1)
    nombrelegido = nombres[nombreazar]
    apellidoelegido = apellidos[apellidoazar]
    print(f"{nombrelegido} {apellidoelegido}")
