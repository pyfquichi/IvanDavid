f = open("scores.txt", "w")

while True: 
  participant = input("Participant name > ")

  if participant == "quit":
    print("Quitting...")
    break

  score = input("Score for " + participant + "> ")
   
  if score == "quit":
    print("Quitting...")
    break

  f.write(participant + "," + score + "\n")

f.close()


