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

    def test_get_yt_link(self):
        ytLint = "https://www.youtube.com/watch?v=1IszT_guI08"
        self.assertEqual(self.temp.get_yt_link('Arrabiata'), ytLint)

    def test_get_meal_category(self):
        category = "Vegetarian"
        self.assertEqual(self.temp.get_meal_category('Arrabiata'), category)

    def test_get_meal_area(self):
        area = "Italian"
        self.assertEqual(self.temp.get_meal_area('Arrabiata'), area)

    def test_instructions_exception(self):
        self.assertRaises(TypeError, self.temp.get_instructions, 1)

    def test_picture_exception(self):
        self.assertRaises(TypeError, self.temp.get_meal_picture, 2)

    def test_tags_exception(self):
        self.assertRaises(TypeError, self.temp.get_meal_tags, 3)

    def test_yt_link_exception(self):
        self.assertRaises(TypeError, self.temp.get_yt_link, True)

    def test_category_exception(self):
        self.assertRaises(TypeError, self.temp.get_meal_category, False)

    def test_area_exception(self):
        self.assertRaises(TypeError, self.temp.get_meal_area, None)


    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()