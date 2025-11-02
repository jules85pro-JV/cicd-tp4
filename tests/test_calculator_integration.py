"""Tests d'intégration - Suite 3"""
import pytest
import allure
import time
from src.calculator import Calculator


@allure.epic("Calculator API")
@allure.feature("Tests d'intégration")
class TestCalculatorIntegration:
    """Tests d'intégration combinant plusieurs opérations"""

    @pytest.fixture
    def calc(self):
        return Calculator()

    @allure.story("Opérations combinées")
    @allure.title("Chaîne d'opérations complexes")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_complex_chain_operations(self, calc):
        """Test réussi avec opérations chaînées"""
        with allure.step("Calcul complexe"):
            result = calc.add(10, 5)
            result = calc.multiply(result, 2)
            result = calc.subtract(result, 10)
            result = calc.divide(result, 5)
        assert result == 4.0

    @allure.story("Opérations combinées")
    @allure.title("Calcul avec racine et puissance")
    def test_sqrt_and_power(self, calc):
        """Test réussi combinant sqrt et power"""
        result = calc.sqrt(16)
        result = calc.power(result, 3)
        assert result == 64.0

    @allure.story("Opérations combinées")
    @allure.title("Calcul incorrect - ÉCHEC")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_complex_calculation_incorrect(self, calc):
        """Ce test échoue - logique incorrecte"""
        result = calc.add(5, 3)
        result = calc.multiply(result, 2)
        # Bug simulé: assertion incorrecte
        assert result == 15  # Devrait être 16, donc échec

    @allure.story("Performance")
    @allure.title("Test d'intégration rapide")
    def test_fast_integration(self, calc):
        """Test rapide d'intégration"""
        result = calc.factorial(5) / calc.power(2, 3)
        assert result == 15.0

    @allure.story("Performance")
    @allure.title("Test d'intégration lent")
    @allure.severity(allure.severity_level.NORMAL)
    def test_slow_integration(self, calc):
        """Test lent simulant un calcul complexe"""
        time.sleep(0.3)
        result = 0
        for i in range(5):
            result = calc.add(result, calc.factorial(i))
        assert result == 34

    @allure.story("Edge Cases")
    @allure.title("Opérations avec très grands nombres")
    def test_large_numbers(self, calc):
        result = calc.add(999999999, 1)
        assert result == 1000000000

    @allure.story("Edge Cases")
    @allure.title("Opérations avec très petits nombres")
    def test_small_numbers(self, calc):
        result = calc.multiply(0.0001, 0.0001)
        assert result == 0.00000001

    @allure.story("Edge Cases")
    @allure.title("Vérification de précision décimale - ÉCHEC")
    def test_decimal_precision_issue(self, calc):
        """Ce test peut échouer à cause de la précision des float"""
        result = calc.divide(1, 3)
        # Bug simulé: comparaison stricte de float
        assert result == 0.3333333333333333  # Pourrait échouer