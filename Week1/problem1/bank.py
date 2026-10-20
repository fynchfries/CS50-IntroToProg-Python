def main():
  greet = str(input("Greeting: ")).strip()

  if greet == "hello":
    print("$0")
  elif greet.startswith("h"):
    print("$20")
  else:
    print("$100")

main()
