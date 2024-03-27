class Slide:
    def __init__(self, slideid=None, slidetitle = None):
        if slideid is not None and slidetitle is not None:
            self.slideid = slideid
            self.slideTitle = slidetitle
        else :
            self.slideid = 1
            self.slideTitle = "Default"
    
class SlideDetail:
    def __init__(self, slideid, songid):
        self.slideid = slideid
        self.songid = songid
