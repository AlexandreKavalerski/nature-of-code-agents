
class Food():

    def __init__(self, x, y):
        self.position = PVector(x, y)
        self.r = 10

    def display(self):
        fill(255, 120, 120)
        noStroke()
        strokeWeight(1)
        with pushMatrix():
            translate(self.position.x, self.position.y)
            rect(0, 0, self.r, self.r)
            
    def changeLocation(self, limit_x, limit_y):
        self.position.x = random(0, limit_x)
        self.position.y = random(0, limit_y)
