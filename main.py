import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import random


class HealthAssistant:
    def __init__(self):
        self.daily_health_tips = []
        self.exercise_videos = []
        self.nutrition_data = {}
        self.sleep_data = {}
        self.meditation_guides = []

    def scrape_health_tips(self):
        self.daily_health_tips = []
        websites = [
            "https://www.healthwebsite1.com",
            "https://www.healthwebsite2.com",
        ]

        for website in websites:
            try:
                response = requests.get(website)
                soup = BeautifulSoup(response.content, "html.parser")

                tips = soup.find_all("div", class_="health-tip")
                for tip in tips:
                    self.daily_health_tips.append(tip.text.strip())
            except requests.exceptions.RequestException as e:
                print(f"Error scraping data from {website}: {e}")

    def fetch_exercise_videos(self):
        self.exercise_videos = []
        websites = [
            "https://www.fitnesswebsite1.com",
            "https://www.fitnesswebsite2.com",
        ]

        for website in websites:
            try:
                response = requests.get(website)
                soup = BeautifulSoup(response.content, "html.parser")

                videos = soup.find_all("div", class_="exercise-video")
                for video in videos:
                    self.exercise_videos.append(video["src"])
            except requests.exceptions.RequestException as e:
                print(f"Error fetching data from {website}: {e}")

    def scrape_nutrition_data(self):
        self.nutrition_data = {}
        database_url = "https://www.nutritiondatabase.com"

        try:
            response = requests.get(database_url)
            soup = BeautifulSoup(response.content, "html.parser")

            foods = soup.find_all("div", class_="food-item")
            for food in foods:
                name = food.find("h3").text
                calories = food.find("span", class_="calories").text
                carbs = food.find("span", class_="carbs").text
                fats = food.find("span", class_="fats").text
                protein = food.find("span", class_="protein").text

                self.nutrition_data[name] = {
                    "calories": calories,
                    "carbs": carbs,
                    "fats": fats,
                    "protein": protein,
                }
        except requests.exceptions.RequestException as e:
            print(f"Error scraping data from {database_url}: {e}")

    def track_sleep_patterns(self):
        self.sleep_data = {}

        for _ in range(7):
            date = random.choice(
                [
                    "2022-01-01",
                    "2022-01-02",
                    "2022-01-03",
                    "2022-01-04",
                    "2022-01-05",
                    "2022-01-06",
                    "2022-01-07",
                ]
            )
            duration = random.choice([6.5, 7.2, 8.1, 7.8, 6.9, 7.5, 8.3])
            quality = random.choice([1, 2, 3, 4, 5])

            self.sleep_data[date] = {"duration": duration, "quality": quality}

    def scrape_meditation_guides(self):
        self.meditation_guides = []
        websites = [
            "https://www.meditationwebsite1.com",
            "https://www.meditationwebsite2.com",
        ]

        for website in websites:
            try:
                response = requests.get(website)
                soup = BeautifulSoup(response.content, "html.parser")

                guides = soup.find_all("div", class_="meditation-guide")
                for guide in guides:
                    self.meditation_guides.append(guide.text.strip())
            except requests.exceptions.RequestException as e:
                print(f"Error scraping data from {website}: {e}")

    def show_daily_health_tips(self):
        for tip in self.daily_health_tips:
            print("-" * 50)
            print(tip)
            print("-" * 50)

    def show_exercise_videos(self):
        for video in self.exercise_videos:
            print("-" * 50)
            print(f"Exercise Video: {video}")
            print("-" * 50)

    def log_meal(self, meal):
        if meal in self.nutrition_data:
            print(f"Logging meal: {meal}")
            print("Meal details:")
            print(f"Calories: {self.nutrition_data[meal]['calories']}")
            print(f"Carbs: {self.nutrition_data[meal]['carbs']}")
            print(f"Fats: {self.nutrition_data[meal]['fats']}")
            print(f"Protein: {self.nutrition_data[meal]['protein']}")
        else:
            print(f"Meal not found in the nutrition database.")

    def generate_sleep_report(self):
        dates = sorted(self.sleep_data.keys())
        durations = [self.sleep_data[date]["duration"] for date in dates]
        qualities = [self.sleep_data[date]["quality"] for date in dates]

        plt.figure(figsize=(10, 6))
        plt.plot(dates, durations, label="Sleep Duration")
        plt.plot(dates, qualities, label="Sleep Quality")
        plt.xlabel("Dates")
        plt.ylabel("Values")
        plt.title("Sleep Patterns")
        plt.legend()
        plt.show()

    def show_meditation_guides(self):
        for guide in self.meditation_guides:
            print("-" * 50)
            print(guide)
            print("-" * 50)


# Example usage of the HealthAssistant class
assistant = HealthAssistant()
assistant.scrape_health_tips()
assistant.scrape_nutrition_data()
assistant.fetch_exercise_videos()
assistant.track_sleep_patterns()
assistant.scrape_meditation_guides()

assistant.show_daily_health_tips()
assistant.show_exercise_videos()

assistant.log_meal("Chicken Breast")
assistant.log_meal("Salad")
assistant.log_meal("Pizza")

assistant.generate_sleep_report()

assistant.show_meditation_guides()
