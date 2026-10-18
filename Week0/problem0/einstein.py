def main():
  mass = int(input("m: ")) #ask for the input m(mass), then store it to the mass variable.
  speedOfLight = 300000000 # set the speed of light to that value.
  convertToJoules(mass, speedOfLight) # call the function that calculate the mass and speedoflight to joules.

def convertToJoules(mass, speedOfLight): # defined funtion that calculate the joules, then accept the value passes from the argument.
  toJoules = (mass * pow(speedOfLight, 2)) # formula to get the joules
  return print(f'E: {toJoules}') #display the answer

main() # call the main funtion
