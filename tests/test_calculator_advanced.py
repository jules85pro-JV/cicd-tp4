"""Tests avancés - Suite 2 avec edge cases"""
import pytest
import allure
from src.calculator import Calculator


@allure.epic("Calculator API")
@allure.feature("Opérations avancées et edge cases")
class TestCalculatorAdvanced:
    """Tests avancés avec cas limites"""

    @pytest.fixture
    def calc(self):
        return Calculator()

    # Tests de puissance - CERTAINS RÉUSSISSENT
    @allure.story("Puissance")
    @allure.title("Puissance de nombres positifs")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_power_positive(self, calc):
        result = calc.power(2, 3)
        assert result == 8

    @allure.story("Puissance")
    @allure.title("Puissance à la zéro")
    def test_power_zero_exponent(self, calc):
        result = calc.power(5, 0)
        assert result == 1

    @allure.story("Puissance")
    @allure.title("Puissance négative")
    def test_power_negative_exponent(self, calc):
        result = calc.power(2, -2)
        assert result == 0.25

    @allure.story("Puissance")
    @allure.title("Puissance avec base négative - assertion incorrecte")
    @allure.severity(allure.severity_level.NORMAL)
    def test_power_negative_base_incorrect(self, calc):
        """Ce test échoue - bug dans l'assertion"""
        result = calc.power(-2, 2)
        assert result == -4  # Devrait être 4, donc échec

    # Tests de racine carrée - CERTAINS ÉCHOUENT
    @allure.story("Racine carrée")
    @allure.title("Racine carrée d'un nombre positif")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_sqrt_positive(self, calc):
        result = calc.sqrt(16)
        assert result == 4.0

    @allure.story("Racine carrée")
    @allure.title("Racine carrée de zéro")
    def test_sqrt_zero(self, calc):
        result = calc.sqrt(0)
        assert result == 0.0

    @allure.story("Racine carrée")
    @allure.title("Racine carrée d'un nombre négatif - exception")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_sqrt_negative(self, calc):
        with pytest.raises(ValueError):
            calc.sqrt(-4)

    @allure.story("Racine carrée")
    @allure.title("Racine carrée décimale - assertion incorrecte")
    def test_sqrt_decimal_incorrect(self, calc):
        """Ce test échoue - précision incorrecte"""
        result = calc.sqrt(2)
        # Bug simulé: assertion trop stricte
        assert result == 1.4142135623730951  # Pourrait échouer à cause de précision float

    # Tests de factorielle - MÉLANGE RÉUSSITE/ÉCHEC
    @allure.story("Factorielle")
    @allure.title("Factorielle de zéro")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_factorial_zero(self, calc):
        result = calc.factorial(0)
        assert result == 1

    @allure.story("Factorielle")
    @allure.title("Factorielle de nombres positifs")
    def test_factorial_positive(self, calc):
        assert calc.factorial(5) == 120
        assert calc.factorial(3) == 6

    @allure.story("Factorielle")
    @allure.title("Factorielle d'un nombre négatif - exception")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_factorial_negative(self, calc):
        with pytest.raises(ValueError):
            calc.factorial(-1)

    @allure.story("Factorielle")
    @allure.title("Factorielle de 10 - vérification incorrecte")
    def test_factorial_10_incorrect(self, calc):
        """Ce test échoue intentionnellement"""
        result = calc.factorial(10)
        assert result == 3628800  # Correct, mais testons avec valeur fausse
        # Commentaire: en fait cette assertion est correcte, mais créons un échec
        assert result == 999999  # Cette assertion échoue