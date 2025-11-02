"""Tests unitaires de base de la calculatrice - Suite 1"""
import pytest
import allure
import time
from src.calculator import Calculator


@allure.epic("Calculator API")
@allure.feature("Opérations arithmétiques de base")
class TestCalculatorBasic:
    """Tests unitaires de base"""

    @pytest.fixture
    def calc(self):
        return Calculator()

    # Tests d'addition - TOUS RÉUSSISSENT
    @allure.story("Addition")
    @allure.title("Addition de deux nombres positifs")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_positive(self, calc):
        result = calc.add(5, 3)
        assert result == 8

    @allure.story("Addition")
    @allure.title("Addition avec zéro")
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_with_zero(self, calc):
        result = calc.add(10, 0)
        assert result == 10

    @allure.story("Addition")
    @allure.title("Addition de nombres négatifs")
    def test_add_negative(self, calc):
        result = calc.add(-5, -3)
        assert result == -8

    @allure.story("Addition")
    @allure.title("Addition nombres décimaux")
    def test_add_decimal(self, calc):
        result = calc.add(3.5, 2.7)
        assert result == pytest.approx(6.2)

    # Tests de soustraction - TOUS RÉUSSISSENT
    @allure.story("Soustraction")
    @allure.title("Soustraction basique")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_subtract_positive(self, calc):
        result = calc.subtract(10, 3)
        assert result == 7

    @allure.story("Soustraction")
    @allure.title("Soustraction avec résultat négatif")
    def test_subtract_negative_result(self, calc):
        result = calc.subtract(3, 10)
        assert result == -7

    # Tests de multiplication - TOUS RÉUSSISSENT
    @allure.story("Multiplication")
    @allure.title("Multiplication de nombres positifs")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_multiply_positive(self, calc):
        result = calc.multiply(5, 3)
        assert result == 15

    @allure.story("Multiplication")
    @allure.title("Multiplication par zéro")
    def test_multiply_by_zero(self, calc):
        result = calc.multiply(10, 0)
        assert result == 0

    @allure.story("Multiplication")
    @allure.title("Multiplication de nombres négatifs")
    def test_multiply_negative(self, calc):
        result = calc.multiply(-5, -3)
        assert result == 15

    # Tests de division - CERTAINS ÉCHOUENT
    @allure.story("Division")
    @allure.title("Division normale")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_divide_normal(self, calc):
        result = calc.divide(10, 2)
        assert result == 5.0

    @allure.story("Division")
    @allure.title("Division par zéro - doit échouer")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_divide_by_zero(self, calc):
        with pytest.raises(ValueError, match="Division par zéro"):
            calc.divide(10, 0)

    @allure.story("Division")
    @allure.title("Division décimale")
    def test_divide_decimal(self, calc):
        result = calc.divide(7, 2)
        assert result == 3.5

    # Test qui échoue intentionnellement (bug simulé)
    @allure.story("Division")
    @allure.title("Division avec vérification incorrecte - ÉCHEC")
    @allure.severity(allure.severity_level.NORMAL)
    def test_divide_incorrect_assertion(self, calc):
        """Ce test échoue intentionnellement pour démontrer les rapports d'échec"""
        result = calc.divide(20, 4)
        # Bug simulé: assertion incorrecte
        assert result == 6  # Devrait être 5, donc ce test échoue

    # Test qui prend du temps (performance)
    @allure.story("Performance")
    @allure.title("Test rapide (< 100ms)")
    @allure.severity(allure.severity_level.MINOR)
    def test_fast_operation(self, calc):
        result = calc.add(1, 1)
        assert result == 2

    @allure.story("Performance")
    @allure.title("Test lent simulé (> 500ms)")
    @allure.severity(allure.severity_level.NORMAL)
    def test_slow_operation(self, calc):
        time.sleep(0.5)  # Simule une opération lente
        result = calc.multiply(10, 10)
        assert result == 100