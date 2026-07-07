import random

def main():
    level =  get_level()
    score = 0 

    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x+y
        
        for j in range(3):
             
            try:
                answer = int(input(f" {x} + {y} = "))
                if answer == correct_answer:
                    score += 1 
                    break
                else:
                    print("EEE") 
                if j == 2 :
                    print(f"{x}+{y} = {correct_answer}")
            except ValueError:
                print("EEE")
                if j == 2 :
                    print(f"{x} + {y} = {correct_answer}")

    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input(" enter level:"))
            if level in (1,2,3):
             return level
        except ValueError:
            continue

def generate_integer(level):
        if level == 1 :
            return random.randint(0,9)
        elif level == 2 :
            return random.randint(10,99)
        elif level == 3 :
            return random.randint(100,999)
        else:
            raise ValueError
        
main()