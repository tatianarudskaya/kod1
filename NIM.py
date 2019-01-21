import random

#check for win condition
def winCondition (summ, lastAction, goal, endGame):
  if summ == goal:
    print (lastAction, "wins!")
    endGame = True
  elif summ > goal:
    print (lastAction, "looses")
    endGame = True
  return endGame

#Players action
def inputFromPlayer (step, summ, goal, playerPick, lastAction, endGame):
  print ("\n___________________\nPlayers turn:")
  try:
    print ("Введи число от 1 до", step)
    playerPick = int(input())
    lastAction = "Player"
  except ValueError:
    print ("Так, вводи число, не выделывайся")
  while playerPick not in range(1, step+1):
    print ("Давай ещё раз - от 1 до", step, "я в тебя верю")
    try:
      print ("Введи число от 1 до", step)
      playerPick = int(input())
      lastAction = "Player"
    except ValueError:
      print ("Так, вводи число, не выделывайся")
  print (lastAction, "picked number", playerPick)
  summ = summ + playerPick
  print ("Сумма чисел равна", summ)
  endGame = winCondition (summ, lastAction, goal, endGame)
  return (step, summ, goal, playerPick, lastAction, endGame)

#Update variables
#def variablesUpdate

#Computer action
def computerAction (step, summ, goal, firstTurn, lastAction, endGame):
  print ("\n___________________\nComputers turn:")
  if firstTurn == 0:
    if (goal - 1) % step == 0:
      computerPick = random.randrange(1, (step + 1))
      lastAction = "Computer"
      print (lastAction, "picked number", computerPick)
      summ = summ + computerPick
      firstTurn = 2
      print ("Сумма чисел равна", summ)
    else:
      computerPick = (goal - 1) % step
      lastAction = "Computer"
      print (lastAction, "picked number", computerPick)
      summ = summ + computerPick
      firstTurn = 2
      print ("Сумма чисел равна", summ)
  else:
    if goal - summ <= step:
      computerPick = goal - summ
      lastAction = "Computer"
      endGame = True
      print (lastAction, "picked number", computerPick)
      summ = summ + computerPick
      print ("Сумма чисел равна", summ)
    else:
      if (goal - 1 - summ) % step == 0:
        computerPick = random.randrange(1, (step + 1))
        lastAction = "Computer"
        print (lastAction, "picked number", computerPick)
        summ = summ + computerPick
        print ("Сумма чисел равна", summ)
      else:
        computerPick = (goal - 1 - summ) % step
        lastAction = "Computer"
        print (lastAction, "picked number", computerPick)
        summ = summ + computerPick
        print ("Сумма чисел равна", summ)
  endGame = winCondition (summ, lastAction, goal, endGame)
  return (step, summ, goal, firstTurn, lastAction, endGame)

resultSumm = 0
k = 0
N = 0
whoMadeLastPick = 0
firstTurn = 2
endGame = False
playerPick = 0

print ("_________NIM_________")

#Start of the game: player picks step and goal:
while k < 2:
  try:
    k = int(input("Введи максимальный шаг (не менее 2)\n"))
  except ValueError:
    print ("Так, вводи число, не выделывайся")
while N / k < 2:
  try:
    N = int(input("Введи пороговое число (хотя бы в два раза больше, чем шаг)\n"))
  except ValueError:
    print ("Так, вводи число, не выделывайся")

#Player picks first or second turn:
while (1 < firstTurn or firstTurn < 0):
  try:
    firstTurn = int(input("Хочешь сделать первыйх ход?\n0 - если нет, 1 - если да.\n"))
  except ValueError:
    print ("Выбери 0 или 1, пожалуйста!")

#New Gameplay:
while endGame == False:
  if firstTurn == 1:
    k, resultSumm, N, playerPick, whoMadeLastPick, endGame = inputFromPlayer (k, resultSumm, N, playerPick, whoMadeLastPick, endGame)
    if endGame == True:
      break
    else:
      k, resultSumm, N, firstTurn, whoMadeLastPick, endGame = computerAction (k, resultSumm, N, firstTurn, whoMadeLastPick, endGame)
  else:
    k, resultSumm, N, firstTurn, whoMadeLastPick, endGame = computerAction (k, resultSumm, N, firstTurn, whoMadeLastPick, endGame)
    if endGame == True:
      break
    else:
      k, resultSumm, N, playerPick, whoMadeLastPick, endGame = inputFromPlayer (k, resultSumm, N, playerPick, whoMadeLastPick, endGame)
