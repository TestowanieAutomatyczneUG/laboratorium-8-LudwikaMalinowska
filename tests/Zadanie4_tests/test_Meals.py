import unittest

from Zadanie4.Meals import Meals

class TestMeal(unittest.TestCase):

    def setUp(self):
        self.temp = Meals()

    def test_get_instructions(self):
        instructions = "Bring a large pot of water to a boil. Add kosher salt to the boiling water, then add the pasta. Cook according to the package instructions, about 9 minutes.\r\nIn a large skillet over medium-high heat, add the olive oil and heat until the oil starts to shimmer. Add the garlic and cook, stirring, until fragrant, 1 to 2 minutes. Add the chopped tomatoes, red chile flakes, Italian seasoning and salt and pepper to taste. Bring to a boil and cook for 5 minutes. Remove from the heat and add the chopped basil.\r\nDrain the pasta and add it to the sauce. Garnish with Parmigiano-Reggiano flakes and more basil and serve warm."
        self.assertEqual(self.temp.get_instructions('Arrabiata'), instructions)

    def test_get_meal_picture(self):
        pictureLink = "https://www.themealdb.com/images/media/meals/ustsqw1468250014.jpg"
        self.assertEqual(self.temp.get_meal_picture('Arrabiata'), pictureLink)

    def test_get_meal_tags(self):
        tags = "Pasta,Curry"
        self.assertEqual(self.temp.get_meal_tags('Arrabiata'), tags)


    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()