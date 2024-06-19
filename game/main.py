'''
🤖 Juego de Piedra, Papel y Tijera 
'''
import random
opciones_a_emojis = {
    "piedra": "✊",
    "papel": "✋",
    "tijera": "✌️"
}
opciones_winner = {
    "ganaste": "🏆",
    "perdiste": "💔",
    "empate": "🤝"
}

# Constantes de colores
COLOR_ROJO = "\033[91m"
COLOR_ROSA = "\033[38;5;205m"
COLOR_NARANJA = "\033[38;5;208m"
RESET_COLOR = "\033[0m"

opciones = ('piedra', 'papel', 'tijera')
opciones_text = ', '.join(opciones).title() # Piedra, Papel, Tijera

def userOptions():
  eleccion = input(f'Elige [{opciones_text}]:').lower()
  while eleccion not in opciones:
    print(f"{COLOR_ROJO}\n❌ Entrada no válida. Inténtalo de nuevo.{RESET_COLOR}")
    eleccion = input(f'Elige [{opciones_text}]:').lower()
  return eleccion
   
def cpuOption():
  return random.choice(opciones)

def winner(opcUser, opcCpu):
  if(opcUser == opcCpu):
    return "empate"
  victorias = {
        "piedra": "tijera",
        "papel": "piedra",
        "tijera": "papel"
    }
  return "usuario" if victorias[opcUser] == opcCpu else "cpu"


def print_score(userWins, cpuWins, roundsPlayed):
    print(f"{COLOR_NARANJA}\nUser {userWins} Ronda[{roundsPlayed}] Cpu {cpuWins}{RESET_COLOR}")
    print(f'{COLOR_NARANJA}**********************\n{RESET_COLOR}')

def print_final_result(userWins, cpuWins):
    if userWins > cpuWins:
        print("¡Ganaste!")
    elif userWins < cpuWins:
        print("¡Perdiste!")
    else:
        print("¡Empate!")

def game():
  rounds = 3
  roundsPlayed = 0
  userWins = 0
  cpuWins=0

  print(f"{COLOR_ROSA}\n¡Bienvenido al juego de Piedra ✊, Papel ✋ o Tijera ✌️ !{RESET_COLOR}")
  print(f"**********************{COLOR_ROSA}Rondas[{rounds}]{RESET_COLOR}**************************\n")
  
  while roundsPlayed < rounds:
    print_score(userWins, cpuWins, roundsPlayed)
    usuario =  userOptions()
    computador = cpuOption()
    ganador = winner(usuario, computador)
    mensaje = ''
    if ganador == 'usuario':
      userWins += 1
      mensaje='ganaste'
    elif ganador == 'cpu':
      cpuWins +=1
      mensaje='perdiste'
    else:
      mensaje=ganador

    print(f"\nUsuario: {opciones_a_emojis[usuario]} VS Cpu: {opciones_a_emojis[computador]}  ==> Usuario {opciones_winner[mensaje]} {mensaje}")
    roundsPlayed += 1
    
  
  print_score(userWins, cpuWins, roundsPlayed)
  print_final_result(userWins, cpuWins)
   
if __name__ == '__main__':
   game()