"""
Zadanie 7.4: biblioteka filmow
Jest w stanie przechowywać informacje na temat filmów, które znajdują się w systemie. Każdy film powinien mieć następujące atrybuty:
Tytuł
Rok wydania
Gatunek
Liczba odtworzeń
Umożliwia przechowywanie informacji na temat seriali. Każdy serial powinien mieć następujące atrybuty:
Tytuł
Rok wydania
Gatunek
Numer odcinka
Numer sezonu
Liczba odtworzeń
Filmy i seriale mają metodę play, która zwiększa liczbę odtworzeń danego tytułu o 1.
Po wyświetleniu serialu jako string pokazują się informacje o konkretnym odcinku, np.: “The Simpsons S01E05” (gdzie po S pokazany jest numer sezonu w notacji dwucyfrowej, natomiast po E - numer odcinka, również w zapisie dwucyfrowym).
Po wyświetleniu filmu jako string widoczne są tytuł i rok wydania np. “Pulp Fiction (1994)”.
Przechowuje filmy i seriale w jednej liście.
Dodatkowo:

Napisz funkcje get_movies oraz get_series, które będą filtrować listę i zwracać odpowiednio tylko filmy oraz tylko seriale. Posortuj listę wynikową alfabetycznie.
Napisz funkcję search, która wyszukuje film lub serial po jego tytule.
Napisz funkcję generate_views, która losowo wybiera element z biblioteki, a następnie dodaje mu losową (z zakresu od 1 do 100) ilość odtworzeń.
Napisz funkcję, która uruchomi generate_views 10 razy.
Napisz funkcję top_titles(), która zwróci wybraną ilość najpopularniejszych tytułów z biblioteki. Dla chętnych: dodaj do funkcji parametr content_type, którym wybierzesz czy mają zostać pokazane filmy, czy seriale.
Zadania dla chętnych
Napisz funkcję, która za pomocą pętli dodaje pełne sezony seriali do biblioteki. Funkcja powinna przyjmować parametry takie jak: tytuł serialu, rok wydania, gatunek, numer sezonu, liczba odcinków do dodania.
Do klasy reprezentującej serial, dopisz metodę, która wyświetla ilość odcinków danego serialu dostępnych w bibliotece.
Niech program po uruchomieniu działa w następujący sposób:

Wyświetli na konsoli komunikat Biblioteka filmów.
Wypełni bibliotekę treścią.
Wygeneruje odtworzenia treści za pomocą funkcji generate_views.
Wyświetli na konsoli komunikat Najpopularniejsze filmy i seriale dnia <data>, gdzie <data> to bieżąca data w formacie DD.MM.RRRR.
Wyświetli listę top 3 najpopularniejszych tytułów.
"""
import random
from operator import attrgetter

class Films:
    def __init__(self, title, rel_year, f_type, views):
        self.title = title
        self.rel_year = rel_year
        self.f_type = f_type
        self.views = views

    def __str__(self):
        return f'{self.title} ({self.rel_year}) Views: {self.views}'
    
    def __play__(self):
        self.views += 1
        return self.views


class Series(Films):
    def __init__(self, s_number, e_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.s_number = s_number
        self. e_number =  e_number

    def __str__(self):
        return f'{self.title} S{self.s_number:02d}E{self.e_number:02d} Views: {self.views}'

show_list = [
    Films(title="Matrix", rel_year="1999", f_type="Sci-Fi", views=1),
    Series(title="Wiedzmin", rel_year="2019", f_type="fantasy", views=2, s_number=1, e_number=6),
    Series(title="Supernatural", rel_year="2005", f_type="Sci-Fi", views=3, s_number=15, e_number=12),
    Films(title="Matrix: Reaktywacja", rel_year="2003", f_type="Sci-Fi", views=4),
    Series(title="Mandalorian", rel_year="2019", f_type="Sci-Fi", views=5, s_number=2, e_number=3),
    Films(title="Matrix: Rewolucje", rel_year="2003", f_type="Sci-Fi", views=6),
    Films(title="Doctor Sleep", rel_year="2019", f_type="Horror", views=666),
    Series(title="Doctor WuHaO", rel_year="2005", f_type="Sci-Fi", views=1, s_number=8, e_number=13),
    Series(title="Vikings", rel_year="2666", f_type="Sci-Fi", views=1, s_number=15, e_number=2),
    Films(title="Venom", rel_year="2019", f_type="Sci-Fi", views=17),
    Films(title="Predator", rel_year="2018", f_type="Sci-Fi", views=55)
    ]

def get_series(list_of_shows):
    """
    Get series from "show_list" list and sort them by title parameter of it is class.
    """
    series = []
    for i in list_of_shows:
        if isinstance(i, Series):
            series.append(i)
    series = sorted(series, key=attrgetter("title"))
    return series

def get_movies(list_of_shows):
    """
    Get movies from "show_list" list and sort them by title parameter of it is class.
    """
    movies = []
    for i in list_of_shows:
        if not isinstance(i, Series):
            movies.append(i)
    movies = sorted(movies, key=attrgetter("title"))
    return movies


def search(list_of_shows):
    user_show = input("Find move or series by title: ").capitalize()
    for i in list_of_shows:
        if user_show == i.__getattribute__("title"):
            print(f"Your show is: {i}")


def generate_views(list_of_shows):
    show = random.choice(list_of_shows)
    setattr(show, "views", getattr(show, "views") + random.randint(1,100))


def generate_views_10_times(list_of_shows):
    for _ in range(10):
        generate_views(list_of_shows)


def top_titles(list_of_shows, content_type):
    """
    Get top titles by Series or by Movies. 
    reverse parameter = True - sorted from most views
    """
    if content_type == "Movies":
        list_of_contents = sorted(get_movies(list_of_shows), key=attrgetter("views"), reverse=True)
    elif content_type == "Series":
        list_of_contents = sorted(get_series(list_of_shows), key=attrgetter("views"), reverse=True)
    return list_of_contents





#series = get_series(show_list)
#for i in series:
#    print(i)

#movies = get_movies(show_list)
#for i in movies:
#    print(i)




#search(show_list)




generate_views_10_times(show_list)

for i in top_titles(show_list, "Movies"):
    print(i)
for i in top_titles(show_list, "Series"):
    print(i)