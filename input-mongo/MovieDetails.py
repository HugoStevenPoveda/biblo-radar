class MovieDetails:
    def __init__(self, title, genres, plot, full_plot, year, released, score):
        self.title = title
        self.genres = genres
        self.plot = plot
        self.full_plot = full_plot
        self.year = year
        self.released = released
        self.score = score

    def __str__(self):
        return (f"Title: {self.title}\n"
                f"Genres: {', '.join(self.genres)}\n"
                f"Plot: {self.plot}\n"
                f"Full Plot: {self.full_plot}\n"
                f"Year: {self.year}\n"
                f"Released: {self.released.strftime('%Y-%m-%d') if self.released else 'N/A'}\n"
                f"Score: {self.score}\n"
                + "-" * 40)


class MovieDetailsBuilder:
    def __init__(self):
        self.title = ""
        self.genres = []
        self.plot = ""
        self.full_plot = ""
        self.year = 0
        self.released = None
        self.score = 0.0

    def set_title(self, title):
        self.title = title
        return self

    def set_genres(self, genres):
        self.genres = genres
        return self

    def set_plot(self, plot):
        self.plot = plot
        return self

    def set_full_plot(self, full_plot):
        self.full_plot = full_plot
        return self

    def set_year(self, year):
        self.year = year
        return self

    def set_released(self, released):
        self.released = released
        return self

    def set_score(self, score):
        self.score = score
        return self

    def build(self):
        return MovieDetails(self.title, self.genres, self.plot, self.full_plot, self.year, self.released, self.score)
