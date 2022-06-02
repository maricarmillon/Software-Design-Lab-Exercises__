import random


class Doctor:
    def __init__(self, greeting_message: str, signoff):

        greeting_message: str, hedges: list, qualifers: list,replacements:dict):
    self.greeting_message = greeting_message
    self.signoff_message = signoff_message
    self.history = []
    self.hedges = hedges
    self.qualifers = qualifiers
    ers
    self.replacements = replacements


def greeting(self):
    return self.greeting_message


def farewell(self):
    return self.signoff_message

    def changePerson(self, sentence):
        """Replaces "rst person pronouns with second person pronouns."""

    words = sentence.split()
    replyWords = []

    for word in words:
        replyWords.append(self.replacements.get(word, word))

    return " ".join(replyWords)

    def reply(self, sentence):
        """Implements three di!erent reply strategies."""

    probability = random.randint(1, 5)


if probability in (1, 2):
    # Just hedge
    answer = random.choice(self.hedges)
    elif probability == 3 and len(self.history) > 3:
    # Go back to an earlier topic
    answer = "Earlier you said that " + self.changePerson(random.choice(self.history))
    else:
    # Transform the current input
    answer = random.choice(self.qualifers) + self.changePerson(sentence)

    # Always add the current sentence to the history list
    self.history.append(sentence)

    return answer