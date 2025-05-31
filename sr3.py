import json

# Клас для опису фільму
class Movie:
    def __init__(self, title, genre, year, rating):
        self.title = title
        self.genre = genre
        self.year = year
        self.rating = rating

    def to_dict(self):
        return {
            'title': self.title,
            'genre': self.genre,
            'year': self.year,
            'rating': self.rating
        }

    @staticmethod
    def from_dict(data):
        return Movie(data['title'], data['genre'], data['year'], data['rating'])


# Клас для роботи з каталогом фільмів
class MovieCatalog:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie: Movie):
        self.movies.append(movie)

    def save_to_json(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump([movie.to_dict() for movie in self.movies], f, ensure_ascii=False, indent=4)

    def load_from_json(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            self.movies = [Movie.from_dict(data) for data in json.load(f)]

    def filter_by_genre(self, genre):
        return [movie for movie in self.movies if movie.genre.lower() == genre.lower()]

    def sort_by_rating(self, descending=True):
        return sorted(self.movies, key=lambda m: m.rating, reverse=descending)

    def save_selected_to_file(self, selected_movies, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump([movie.to_dict() for movie in selected_movies], f, ensure_ascii=False, indent=4)


# Приклад використання
if __name__ == "__main__":
    catalog = MovieCatalog()
    catalog.add_movie(Movie("Захар Беркут", "історичний", 2019, 7.5))
    catalog.add_movie(Movie("Кіборги", "військовий", 2017, 8.1))
    catalog.add_movie(Movie("Плем'я", "драма", 2014, 7.0))

    # Зберігаємо повний каталог
    catalog.save_to_json("movies.json")

    # Сортуємо за рейтингом
    top_rated = catalog.sort_by_rating()
    catalog.save_selected_to_file(top_rated[:2], "top_movies.json")

    # Фільтруємо за жанром
    drama_movies = catalog.filter_by_genre("драма")
    catalog.save_selected_to_file(drama_movies, "drama_movies.json")
