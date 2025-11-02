"""Tests de stress et de charge - Suite 4"""
import pytest
import allure
import time
from src.calculator import Calculator


@allure.epic("Calculator API")
@allure.feature("Tests de stress et performance")
class TestCalculatorStress:
    """Tests de charge et stress"""

    @pytest.fixture
    def calc(self):
        return Calculator()

    @allure.story("Charge")
    @allure.title("Plusieurs additions rapides")
    @allure.severity(allure.severity_level.NORMAL)
    def test_multiple_additions(self, calc):
        """Test réussi avec plusieurs opérations"""
        for i in range(100):
            result = calc.add(i, i+1)
            assert result == 2*i + 1

    @allure.story("Charge")
    @allure.title("Boucle de calculs - assertion finale incorrecte")
    def test_loop_calculations_incorrect(self, calc):
        """Ce test échoue à la fin"""
        total = 0
        for i in range(10):
            total = calc.add(total, i)
        # Bug simulé: assertion finale incorrecte
        assert total == 100  # Devrait être 45, donc échec

    @allure.story("Performance")
    @allure.title("Performance avec factorielles")
    def test_factorial_performance(self, calc):
        """Test réussi de performance"""
        start = time.time()
        result = calc.factorial(10)
        duration = time.time() - start
        assert result == 3628800
        assert duration < 1.0  # Doit être rapide

    @allure.story("Performance")
    @allure.title("Test de performance lent - dépasse le timeout")
    @allure.severity(allure.severity_level.MINOR)
    def test_slow_performance_test(self, calc):
        """Test qui prend du temps"""
        time.sleep(0.8)  # Simule une opération lente
        result = calc.multiply(10, 10)
        assert result == 100

    @allure.story("Robustesse")
    @allure.title("Robustesse avec valeurs limites")
    def test_boundary_values(self, calc):
        """Test réussi avec valeurs limites"""
        assert calc.add(0, 0) == 0
        assert calc.multiply(0, 100) == 0
        assert calc.power(1, 1000) == 1

    @allure.story("Robustesse")
    @allure.title("Vérification robustesse - assertion trop stricte")
    def test_robustness_incorrect(self, calc):
        """Ce test échoue - vérification trop stricte"""
        result = calc.divide(1, 3)
        # Bug: comparaison exacte de float
        assert result == 0.33333333333333331  # Pourrait échouer