import math
import sys

def lab1(filename):
  character = {}
  characters = 0

  with open(filename, encoding = 'utf-8') as file:
    for line in file:
      for char in line:
        if char in character:
            character[char]+=1
        else:
            character[char]=1
        characters += 1

  print("\nLiczba unikalnych występujących znaków: " + str(len(character)))
  print("Łącznie odczytano: " + str(characters)+ " znaków")
  print(character)

  sum = 0
  entropy = 0

  for k,v in character.items():
    pk = v/characters
    p = 1/pk
    ie_bits = math.log(p,2)
    print(str(k) + " ie = " + str("{:.2f}".format(round(ie_bits, 2))))
    
    hxi = pk * ie_bits
    entropy += hxi
    
    sum += pk

  print("{:.2f}".format(round(entropy, 2)))
  print(sum)
  print("\n")

def main():
  for arg in sys.argv[1:]:
    lab1(arg)

if __name__ == "__main__":
  main()