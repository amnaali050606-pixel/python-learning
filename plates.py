def main():
    vanity_plate = input(" enter vanity plate code: ")
    if is_valid(vanity_plate) == True :
        print("valid")
    else:
        print("invalid")
def is_valid(vanity_plate):
    number_start = True 
    for i in vanity_plate:
      if 2 <= len(vanity_plate) <= 6 
      and if vanity_plate[0].isalpha() and vanity_plate[1].isalpha()
      and if i.isalpha():
          number_start = False
    else:
        return True
    return True   
main()