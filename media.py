import urllib
import webbrowser

class Movie():
    def __init__(self, mtitle, sline, piurl, traurl):
        self.title = mtitle
        self.storyline = sline
        self.poster_image_url = piurl
        self.trailer_youtube_url = traurl
        
    def show_trailer(self):
        webbrowser.open( self.trailer_youtube_url)
        
