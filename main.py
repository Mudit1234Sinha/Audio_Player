from replit import audio
import time
from os import system

main_message = """
+: volume up
-: volume down
k: add loop
j: remove loop
<space>: play/pause
"""

def show_status(source):
  time.sleep(0.2)
  system("clear")
  vbar = '|' * int(source.volume * 20)
  vper = int(source.volume * 100)
  pp = "⏸️" if source.paused else "▶️"

  print(f"volume: {vbar} {vper}% \n")
  print(f"Looping {source.loops_remaining} time(s)")
  print(f" TIme Remaining: {source.get_remaining()}")
  print(f"Playing: {pp}")
  print(main_message)

def main():
  source = audio.play_file("Juanitos - Exotica.mp3")
  time.sleep(1)
  show_status(source)


  while True:
    choice = input("Enter command")
    if choice == '+':
      source.volume +=0.1
    if choice == '-':
      source.volume -=0.1
    elif choice =='k':
      source.set_loop(source.loops_remaining + 1)
    elif choice == 'j':
      source.set_loop(source.loops_remaining - 1)

    elif choice == " ":

      source.paused = not source.paused
    show_status(source)

main()
