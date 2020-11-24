import requests

class Meals:

    def get_meal_by_name(self, name):
        if not isinstance(name, str):
            raise TypeError
        else:
            link = "https://www.themealdb.com/api/json/v1/1/search.php?s="
            meal = requests.get(link + name)
            return meal.json()

    def get_meal_by_id(self, id):
        if not isinstance(id, str):
            raise TypeError
        else:
            link = "https://www.themealdb.com/api/json/v1/1/lookup.php?i="
            meal = requests.get(link + id)
            return meal.json()

    def get_instructions(self, name):
        if not isinstance(name, str):
            raise TypeError
        else:
            link = "https://www.themealdb.com/api/json/v1/1/search.php?s="
            meal = requests.get(link + name)
            return meal.json()['meals'][0]['strInstructions']

    def get_meal_picture(self, name):
        if not isinstance(name, str):
            raise TypeError
        else:
            link = "https://www.themealdb.com/api/json/v1/1/search.php?s="
            meal = requests.get(link + name)
            return meal.json()['meals'][0]['strMealThumb']

    def get_meal_tags(self, name):
        if not isinstance(name, str):
            raise TypeError
        else:
            link = "https://www.themealdb.com/api/json/v1/1/search.php?s="
            meal = requests.get(link + name)
            return meal.json()['meals'][0]['strTags']

    def get_yt_link(self, name):
        if not isinstance(name, str):
            raise TypeError
        else:
            link = "https://www.themealdb.com/api/json/v1/1/search.php?s="
            meal = requests.get(link + name)
            return meal.json()['meals'][0]['strYoutube']