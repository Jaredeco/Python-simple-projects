import  random

wc1 = 0
wc2 = 0
for i in range(10):
    poss = ["paper", "rock", "scissors"]

    player1 = random.choice(poss)
    player2 = random.choice(poss)

    if player1 == "rock" and player2 == "rock":
        print("Draw with a rock!(P1:Rock, P2:Rock)")
    elif player1 == "rock" and player2 == "paper":
        print("Player2 wins!(P1:Rock, P2:Paper)")
        wc2 +=1
    elif player1 == "rock" and player2 == "scissors":
        print("Player1 wins!(P1:Rock, P2:Scissors)")
        wc1 += 1
    elif player1 == "paper" and player2 == "paper":
        print("Draw with paper!(P1:Paper, P2:Paper)")
    elif player1 == "paper" and player2 == "rock":
        print("Player1 wins!(P1:Paper, P2:Rock)")
        wc1 += 1
    elif player1 == "paper" and player2 == "scissors":
        print("Player2 wins!(P1:Paper, P2:Scissors)")
        wc2 += 1
    elif player1 == "scissors" and player2 == "scissors":
        print("Draw with scissors!(P1:Scissors, P2:Scissors)")
    elif player1 == "scissors" and player2 == "paper":
        print("Player1 wins!(P1:Scissors, P2:Paper)")
        wc1 += 1
    elif player1 == "scissors" and player2 == "rock":
        print("Player2 wins!(P1:Scissors, P2:Rock)")
        wc2 += 1
    elif player2 == "rock" and player1 == "rock":
        print("Draw with a rock!")
    elif player2 == "rock" and player1 == "paper":
        print("Player1 wins!(P1:Paper, P2:Rock)")
        wc1 += 1
    elif player2 == "rock" and player1 == "scissors":
        print("Player2 wins!(P1:Scissors, P2:Rock)")
        wc2 += 1
    elif player2 == "paper" and player1 == "paper":
        print("Draw with paper!(P1:Paper, P2:Paper)")
    elif player2 == "paper" and player1 == "rock":
        print("Player2 wins!(P1:Rock, P2:Paper)")
        wc2 += 1
    elif player2 == "paper" and player1 == "scissors":
        print("Player1 wins!(P1:Scissors, P2:Paper)")
        wc1 += 1
    elif player2 == "scissors" and player1 == "scissors":
        print("Draw with scissors!(P1:Scissors, P2:Scissors)")
    elif player2 == "scissors" and player1 == "paper":
        print("Player2 wins!(P1:Paper, P2:Scissors)")
        wc2 += 1
    elif player2 == "scissors" and player1 == "rock":
        print("Player1 wins!(P1:Rock, P2:Scissors)")
        wc2 += 1

print("Player1:")
print(wc1)
print("Player2:")
print(wc2)