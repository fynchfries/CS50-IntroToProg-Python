def main():
  userInput = str(input())
  convert(userInput)

def convert(userInput):
  if ":(" in userInput:
    print(userInput.replace(":(", "🙂"))
  else:
    print(userInput.replace(":)","🙁"))

main()
