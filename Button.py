class Button(object):
    
    def __init__(self, rect, color_string):
        self.rect = rect
        self.color_string = color_string
        
    def toggle_color(self):
        if "dark_" not in self.color_string:
            self.color_string = "dark_" + self.color_string
        else:
            self.color_string = self.color_string[5:]