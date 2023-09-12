#part1
def padel_court_cost(court_type) :
     if court_type == "indoor" :
          return 30 
     elif court_type == 'outdoor': 
       return 20 
#part2

def rackets_cost(racket_brand) : 
     if racket_brand == " bullpadel" : 
          return 100
     elif racket_brand == " nox" : 
          return 140 
     elif racket_brand == "suix" :
          return 200
     
#part3

     def padel_balls_cost(ball_boxes) :
          if ball_boxes == "one": 
               return 2
          elif ball_boxes == "two":
               return 3.5
          elif ball_boxes == "three" :
               return 5 

#part4 



def padel_game_cost():
     court_type = input("would you like an idoor court or outdoor?:")
     racket_brand = input("racket brand options (bullpadel/nox/suix) please choose:")
     ball_boxes = input(int("how many ball boxes do you need?:(max :3)"))
     cost = padel_court_cost(court_type) + rackets_cost(racket_brand)+ padel_balls_cost(ball_boxes)
     return cost

print(padel_game_cost())