import json
from datetime import datetime
import os
import time

# Definir os hábitos
HABITS = ["take your meds", "track macros", "daily exercise", "apply skincare", "have lunch", "take 50 min of CS50", "jump 100x", "add a daily journal entry", "register expenses" ]

# Buscar o diretório em que o script está
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Define o nome do arquivo Json a ser salvo
FILE_NAME = os.path.join(SCRIPT_DIR, "habit_tracker.json")

# Load existing habit data from JSON file
def load_data():
    try:
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Salvar entrada de hábitos ao json
def save_data(data):
    with open(FILE_NAME, 'w') as file:
        json.dump(data, file, indent=4)

# Validar formato de data (dd-mm-yyyy)
def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%d-%m-%y")
        return True
    except ValueError:
        return False

# Adicionar entrada ao json
def add_entry(habit_data):
    today = datetime.now().strftime("%d-%m-%y")
    while True:
        askday = input("\n    Data a ser registrada (HOJE = 0 / OU dd-mm-yyyy) - ").strip()
        if askday == '0':
            day = today
            break
        elif validate_date(askday):
            day = askday
            break
        else:
            print("    Invalid date format. Please enter in dd-mm-yyyy format.")

    print(f"    Day selected is {day}\n")
    done = {}

    for habit in HABITS:
        while True:
            answer = input(f"    Did you {habit}? (y/n) - ").strip().lower()
            if answer in ['y', 'yes', 'n', 'no']:
                done[habit] = answer in ['y', 'yes']
                break
            print("    Please enter a valid answer (y/n).")

    # Adiciona ou substitui entrada de um determinado dia
    habit_data[day] = done
    save_data(habit_data)
    print("\n    Saving entry for the day...")

# Visualizar histórico de hábitos
def view_tracker(habit_data):
    if habit_data:
        print("\nCurrent habit tracker status:")
        for date, habits in habit_data.items():
            print(f"    {date}: {habits}")
            print("")
        time.sleep(2)
    else:
        print("    No entries in the tracker yet.\n")
        time.sleep(2.5)

# Main menu loop
def main():
    habit_data = load_data()

    while True:
        print(f"Tracker de Hábitos Diários| Dados salvos em: {FILE_NAME}\n")
        print("1. Adicionar entrada a uma data\n2. Visualizar Tracker\n3. Sair do programa")

        menu = input("\nInsira uma das opções do menu: (1/2/3) - ").strip()
        if menu == "1":
            add_entry(habit_data)
            
        elif menu == "2":
            view_tracker(habit_data)
            
        elif menu == "3":
            print("    Fechando programa...")
            break
        else:
            print("    Favor selecionar uma entrada válida do menu (1/2/3).")
            

if __name__ == "__main__":
    main()
