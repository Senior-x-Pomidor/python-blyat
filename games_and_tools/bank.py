from datetime import datetime

from games_and_tools import googol

last_update = "29.06.2025"

def big_text(text):



    if text == "sparkasse":
        print("\033[1;31m   _____                  __                      \033[0m")
        print("\033[1;31m  / ___/____  ____ ______/ /______ ______________ \033[0m")
        print("\033[1;31m  \__ \/ __ \/ __ `/ ___/ //_/ __ `/ ___/ ___/ _ \\""\033[0m")
        print("\033[1;31m ___/ / /_/ / /_/ / /  / ,< / /_/ (__  |__  )  __/\033[0m")
        print("\033[1;31m/____/ .___/\__,_/_/  /_/|_|\__,_/____/____/\___/ \033[0m")
        print("\033[1;31m    /_/                                           \033[0m")
        print("Kontoauszug vom: "+str(datetime.today().replace(microsecond=0))+"\n")
        print("Sparkasse wird gerade renoviert, es sind nicht alle Funktionen verfügbar")
        print(" \n \n \n")
def clear_terminal():
    # \033[H setzt den Cursor oben links, \033[J löscht bis zum Ende
    print("\033[H\033[J", end="")
def farbig(text, farbcode):
    return f"\033[{farbcode}m{text}\033[0m"

##########################################################






##########################################################
def bank_main():

    big_text("sparkasse")
    print("\033[1;31m------------------------------------------------------------------------------\033[0m")
    print("Kontostand: "+googol.display_money_value()+"€")
    print("\033[1;31m------------------------------------------------------------------------------\033[0m")
    print("Kein Geld?")
    print("Melde dich beim Jobcenter oder Spiele einfach ein Spiel. Pro Sieg bekommst du:")
    print("\033[1;31m------------------------------------------------------------------------------\033[0m")
    print("-Hangman vs Computer(offline/online): 100€")
    print("")
    print("")
    input("Enter drücken zum Verlassen der Bank...")
    return


if __name__ == "__main__":
     bank_main()