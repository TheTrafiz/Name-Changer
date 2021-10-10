friends = [ "Batman", "Cat Man", "Fat Man", "Cockroach Man"]
while True:
  print (friends)
  change = input("Do you want to change any of these characters?" + str(friends))
  if change == "yes" or change == "Yes":
    who = input("Type the name of the character you want to change: ")
    if who == friends[0] or who == friends[1] or who == friends[2] or who == friends[3]:
      place = friends.index(who)
      swap = input ("Type the name you want to swap the character " + who + " with: ")
      friends[place] = swap
    else:
      print("I do not recogise that number. Try again.")
  elif change == "No" or change == "no":
    break
  else:
    print("I do not recognise that answer. Try again.")
  
print("End of changes.")
  
    

      