def main():
  filename = input("File name: ").strip()
  exlist(filename)


def exlist(filename):
  filename = filename.lower()

  match filename:
    case _ if filename.endswith(".gif"):
      print("image/gif")
    case _ if filename.endswith((".jpg", ".jpeg")):
      print("image/jpeg")
    case _ if filename.endswith(".png"):
      print("image/png")
    case _ if filename.endswith(".pdf"):
      print("application/pdf")
    case _ if filename.endswith(".txt"):
      print("text/plain")
    case _ if filename.endswith(".zip"):
      print("application/zip")
    case _:
      print("application/octet-stream")


main()
