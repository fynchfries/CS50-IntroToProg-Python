def main(): # define main function
  userInput = str(input()) # ask for user input, then store it to variable userInput
  print(convert(userInput)) # call the function and print the converted text

def convert(userInput):
  # Replace each text emoticon with its matching emoji.
  userInput = userInput.replace(":)", "🙂")
  userInput = userInput.replace(":(", "🙁")
  return userInput

main()
