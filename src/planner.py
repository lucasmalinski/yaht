import json
from datetime import datetime
from pathlib import Path
import time



# --- CONFIGURAÇÕES ---
MAIN_DIR =  Path(__file__).resolve().parent.parent
HISTORY_PATH = MAIN_DIR / "data/historico_de_habitos.json"
HABITS_PATH = MAIN_DIR / "habits.txt"
HABITS = ["take your meds", "track macros", "daily exercise", "apply skincare", "have lunch", "take 50 min of CS50", "jump 100x", "add a daily journal entry", "register expenses"]

# ==========================================
# 1. LÓGICA CENTRAL (Testável)
# ==========================================

def load_data(file_path):
    """Carrega os dados. Recebe o caminho do arquivo como parâmetro para facilitar testes."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_data(data, file_path):
    """Salva os dados. Recebe o caminho do arquivo como parâmetro."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def validate_date(date_str):
    """Valida o formato da data (dd-mm-yyyy)."""
    try:
        datetime.strptime(date_str, "%d-%m-%Y")
        return True
    except ValueError:
        return False

def process_habit_entry(habit_data, date, daily_habits):
    """
    Apenas atualiza o dicionário com os hábitos do dia.
    Foco dos testes automatizados.
    """
    habit_data[date] = daily_habits
    return habit_data

# ==========================================
# 2. INTERFACE DE USUÁRIO - CLI (Excluída dos testes CI)
# ==========================================

def add_entry_cli(habit_data):
    today = datetime.now().strftime("%d-%m-%Y")
    while True:
        askday = input("\n    Data a ser registrada (HOJE = 0 / OU dd-mm-yyyy) - ").strip()
        if askday == '0':
            day = today
            break
        elif validate_date(askday):
            day = askday
            break
        else:
            print("    Formato de data inválida. Insira a data no formato dd-mm-yyyy.")

    print(f"    O dia selecionado é {day}\n")
    done = {}

    for habit in HABITS:
        while True:
            answer = input(f"    Você realizou '{habit}'? [insira y para sim / n para não] - ").strip().lower()
            if answer in ['y', 'yes', 'n', 'no']:
                done[habit] = answer in ['y', 'yes']
                break
            print("    Favor responder no formato válido (y/n).")

    # Chamada daLógica central
    process_habit_entry(habit_data, day, done)
    
    # Salvamos o arquivo
    save_data(habit_data, HISTORY_PATH)
    print("\n    Salvando entrada diária...")

def view_tracker_cli(habit_data):
    if habit_data:
        print("\nHistórico do registro de hábitos:")
        for date, habits in habit_data.items():
            print(f"    {date}: {habits}")
            print("")
        time.sleep(2)
    else:
        print("    Sem entradas no histórico.\n")
        time.sleep(2.5)

def main():
    habit_data = load_data(HISTORY_PATH)

    while True:
        print(f"Tracker de Hábitos Diários | Dados salvos em: {HISTORY_PATH}\n")
        print("1. Adicionar entrada a uma data\n2. Visualizar Tracker\n3. Sair do programa")

        menu = input("\nInsira uma das opções do menu: (1/2/3) - ").strip()
        if menu == "1":
            add_entry_cli(habit_data)
        elif menu == "2":
            view_tracker_cli(habit_data)
        elif menu == "3":
            print("    Fechando programa...")
            break
        else:
            print("    Favor selecionar uma entrada válida do menu (1/2/3).")

if __name__ == "__main__":
    main()