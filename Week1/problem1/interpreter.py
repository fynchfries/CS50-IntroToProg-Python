def main():
  x, y, z = input("Expression: ").strip().split()
  calculate(x, y, z)

# calculator
def calculate(x, y, z):
  match y:
    case "+":
      sum = float(x) + float(z)
      print(round(sum, 1))

    case "-":
      difference = float(x) - float(z)
      print(round(difference, 1))

    case "/":
      quotient = float(x) / float(z)
      print(round((quotient, 1)))

    case "*":
      product = float(x) * float(z)
      print(round(product, 1))

main()
