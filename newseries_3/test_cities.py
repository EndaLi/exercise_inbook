from city_functions import country_city
import unittest

class Test_city_function(unittest.TestCase):

    def test_combine_city_country(self):
        test_result = country_city('santiago','chile')
        self.assertEqual(test_result,'Santiago,Chile')
    def test_combine_city_country_population(self):
        test_result = country_city('santiago','chile','population=5000000')
        self.assertEqual(test_result,'Santiago,Chile - Population=5000000')

unittest.main()
