class Ball():
    def __init__(self, xPos = 0, yPos = 0, r = 0, xSpeed = 0, ySpeed = 0):
        self.x = xPos
        self.y = yPos
        self.radius = r
        self.dx = xSpeed
        self.dy = ySpeed
    def ruch(self):
        self.x += self.dx
        self.y += self.dy
    def collision(self, other, delta):
        odlegloscX = abs(self.x + other.x)
        odlegloscY = abs(self.y + other.y)
        
