

from Vehicle import Vehicle
from Food import Food
from ScoreCounter import ScoreCounter

def setup():
    global vehicle, food, counter
    size(640, 360)
    
    #inicializando carro 
    velocity = PVector(0, 0)
    vehicle = Vehicle(width / 2, height / 2, velocity)
    # Inicializando comida
    food = Food(random(0,640), random(0,360))
    
    #Inicializando o contador
    counter = ScoreCounter(12, 50)

def draw():
    background(255)
    
    counter.display()
        
    # Atualizando posicao do carro 
    vehicle.update()
    vehicle.display()
    
    # Atualizando posicao da comida
    food.update()
    food.display()
    
    # Carro indo até a comida
    calc_distance = vehicle.seek(food.position)
    if calc_distance <= 5:
        # Mudo a comida de lugar
        food.changeLocation(width, height)
        # Aumento a quantidade de pontos
        counter.increaseScore()
        
    print(calc_distance)
