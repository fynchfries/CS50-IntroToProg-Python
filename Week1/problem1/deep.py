def main():
  answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
  output(answer)

def output(ans):
  ans = ans.strip().lower()
  if ans in ("42", "forty-two", "forty two"):
    print("Yes")
  else:
    print("No")

main()
