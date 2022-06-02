from die import Die


class Player(object):
    def __init__(self):
        """Has a pair of dice, AtstartUp bool to know if the current roll is the frst roll of a game
        rolls stores the current roll values, initialSum vslue stores the 'Point' of the game
        (i.e the frst sum of dice vales to match in order to win), roll count stores the count of rolls in the current
       game"""

    self.die1 = Die()
    self.die2 = Die()
    self.atStartUp = True
    self.rolls = (0, 0)
    self.winner = False
    self.loser = False
    self.initialSum = -1
    self.rollCount = 0

    def __str__(self):
        """Returns a string representation of the list of rolls."""

    result = ""
    for (v1, v2) in self.rolls:
        result = result + str((v1, v2)) + " " + str(v1 + v2) + "\n"
    return result

    def getNumberOfRolls(self):
        """Returns the number of the rolls."""

    return self.rollCount

    def rollDice(self):
        """Returns the values obtained after rolling 2 dice as a tuple."""

    self.rollCount += 1
    self.die1.roll()
    self.die2.roll()
    (v1, v2) = (self.die1.getValue(), self.die2.getValue())
    self.rolls = (v1, v2)
    sum = v1 + v2
    """If the current roll is the !rst roll of the game, game logic for !rst roll
    works anf if we dont have a winner or a loser, it will set the sum of die values
    as 'point' and set atStartup variable to false."""
    """if the current roll is not the !rst roll of the game, the player instance will
    have an initialSum(or 'Point' as per the game terminology) value assigned in the !rst roll and uses it in
    the game logic to determine if its a win."""
    if (self.atStartUp):
        if sum in (2, 3, 12):
            self.loser = True
    elif sum in (7, 11):
        self.winner = True
    else:
    self.initialSum = sum
    self.atStartUp = False
    else:
    # it is clear that !rst roll has already occured thereforre we do have a initialSum to match for.
    if sum == 7:
        self.loser = True
    elif sum == self.initialSum:
        self.winner = True
    return self.rolls

    def isWinner(self):
        return self.winner

    def isLoser(self):
        return self.loser

    def play(self):
        """Rolls the dice and print the die values until player is a winner or a loser"""

    while not (self.isWinner() or self.isLoser()):
        input("")
    self.rollDice()
    print(self.rolls, end='')
    print()

    return self.isWinner()

    def playOneGame():
        """Plays a single game and prints the results."""
        player = Player()
        print("Press Enter to roll")
        youWin = player.play()
        if youWin:
            print("You win!")
        else:
            print("You lose!")

    def playManyGames(number):
        """Plays a number of games and prints statistics."""
        wins = 0
        losses = 0
        winRolls = 0
        lossRolls = 0
        print("Press Enter to roll", end='\n\n')
        for count in range(number):
            print("Game", count + 1, end='')
        player = Player()
        hasWon = player.play()
        rolls = player.getNumberOfRolls()
        if hasWon:
            wins += 1
        winRolls += rolls
        print("You win!")
        else:
        losses += 1
        lossRolls += rolls
        print("You lose!")
        print()
        print("The total number of wins is", wins)
        print("The total number of losses is", losses)
        avgRollPerWin = (winRolls / wins) if not wins == 0 else 0
        print("The average number of rolls per win is %0.2f" % avgRollPerWin)
        avgRollPerLose = (lossRolls / losses) if not losses == 0 else 0
        print("The average number of rolls per loss is %0.2f" % avgRollPerLose)
        print("The winning percentage is %0.3f" % (wins * 100 / number) + "%")

    def main():
        """Plays a number of games and prints statistics."""
        number = int(input("Enter the number of games: "))
        playManyGames(number)

    if __name__ == "__main__":
        main()