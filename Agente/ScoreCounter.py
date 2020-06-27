class ScoreCounter:
    
    def __init__(self, x, y, value=0):
        self.position = PVector(x, y)
        self.score = value
        
    def increaseScore(self):
        self.score += 1
        
    def display(self):
        t = 'Pontos: ' + str(self.score)
        textSize(20)
        fill(50)
        text(t, self.position.x, self.position.y)
        
