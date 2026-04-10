import unittest

# Importadas apenas as funções de backend, ignorando a interface CLI
from src.planner import validate_date, process_habit_entry

class TestHabitTracker(unittest.TestCase):

    # 1. Caminho Feliz 
    def test_process_habit_entry_success(self):
        """Testa se os hábitos são inseridos corretamente no dicionário de dados."""
        # Dado falso
        fake_db = {}
        date = "15-10-24"
        daily_habits = {"tomar remédios": True, "exercício diário": False}
        
        result = process_habit_entry(fake_db, date, daily_habits)
        
        # Validação
        self.assertIn(date, result)
        self.assertTrue(result[date]["tomar remédios"])
        self.assertFalse(result[date]["exercício diário"])

    # 2. Entrada Inválida
    def test_validate_date_invalid_format(self):
        """Testa se a função barra formatos absurdos ou letras."""
        self.assertFalse(validate_date("hoje"))
        self.assertFalse(validate_date("10/10/2024")) # Separador errado (barra em vez de traço)
        self.assertFalse(validate_date("32-01-24"))   # Dia que não existe

    # 3. Caso Limite 
    def test_validate_date_edge_cases(self):
        """Testa validação de datas atípicas, como ano bissexto."""
        # 2024 é bissexto, então 29-02-24 deveria ser aceito
        self.assertTrue(validate_date("29-02-24"))
        
        # 2023 não foi bissexto, então 29-02-23 deveria ser rejeitado
        self.assertFalse(validate_date("29-02-23"))

    # 4. (Overwrite / UPSERT)
    def test_process_habit_entry_overwrite(self):
        """Testa se registrar hábitos no mesmo dia atualiza os dados antigos sem apagar os outros dias."""
        
        # O banco de dados já tem o dia 15 e o dia 14 registrados
        initial_data = {
            "15-08-23": {"tomar remédios": False, "exercício diário": False},
            "14-08-23": {"tomar remédios": True, "exercício diário": True}
        }
        day = "15-08-23"
        
        # Usuário roda o programa de novo no dia 15 e muda as respostas
        new_habits_done = {"tomar remédios": True, "exercício diário": True}
        
        # Chamada da lógica central 
        updated_data = process_habit_entry(initial_data, day, new_habits_done)
        
        # Validação
        self.assertTrue(updated_data["15-08-23"]["tomar remédios"]) # Deve ter mudado para True
        self.assertTrue(updated_data["14-08-23"]["tomar remédios"]) # Dia 14 *não* pode ter sumido ou alterado

if __name__ == '__main__':
    unittest.main()