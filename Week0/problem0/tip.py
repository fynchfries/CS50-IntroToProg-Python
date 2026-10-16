def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    if "$" in d:
      dToF = float(d.replace("$", ""))
    return dToF

def percent_to_float(p):
    # TODO
    if "%" in p:
      pToF = float(p.replace("%", ""))
    return pToF * 0.01

main()
