def main():
  mass = int(input("m: "))
  speedOfLight = 300000000
  convertToJoules(mass, speedOfLight)

def convertToJoules(mass, speedOfLight):
  toJoules = (mass * pow(speedOfLight, 2))
  return print(f'E: {toJoules}')

main()
                          