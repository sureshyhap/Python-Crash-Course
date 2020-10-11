import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    """Tests city_country function"""
    def test_city_country(self):
        formatted = city_country("santiago", "chile")
        self.assertEqual(formatted, "Santiago, Chile")


unittest.main()



