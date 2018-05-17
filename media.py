import webbrowser
import fresh_tomatos
class movies():
    def __init__(self,movie_title,trailer_youtube,poster_image):
        self.title=movie_title
        self.trailer_youtube_url=trailer_youtube
        self.poster_image_url=poster_image

    def show_trailer(self):
        webbrowser.open(self.trailer)
