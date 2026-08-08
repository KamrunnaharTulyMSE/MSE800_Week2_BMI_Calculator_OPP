import random
import string


class WordGuessingGame:

    # Create the game with a maximum number of lives
    def __init__(self, max_lives=6):
        self.max_lives = max_lives
        self.lives = max_lives
        self.used_letters = set()
        self.secret_word = self.get_random_word()
        self.blanks = ["_" for _ in self.secret_word]

    # Select a random word from the list
    def get_random_word(self):
        words = [
            "python",
            "variable",
            "function",
            "iterator",
            "notebook",
            "pipeline",
            "dataset",
            "computer",
            "research",
            "analytics"
        ]

        return random.choice(words)

    # Ask the user to enter a letter
    def prompt_for_letter(self):
        while True:
            guess = input("Guess a letter: ").strip().lower()

            # Check that the user entered only one letter
            if len(guess) != 1 or guess not in string.ascii_lowercase:
                print("Please enter a single A-Z letter.")
                continue

            # Check whether the letter was already used
            if guess in self.used_letters:
                print("You already tried that letter.")
                continue

            return guess

    # Reveal the guessed letter in the word
    def reveal_letters(self, letter):
        found = False

        for i, character in enumerate(self.secret_word):
            if character == letter:
                self.blanks[i] = letter
                found = True

        return found

    # Check whether the whole word has been guessed
    def all_letters_found(self):
        return "_" not in self.blanks

    # Start and control the game
    def play(self):
        print("\nWelcome to Word Guessing!")
        print(f"The word has {len(self.secret_word)} letters.")
        print(" ".join(self.blanks))

        while True:

            # Get a letter from the user
            guess = self.prompt_for_letter()
            self.used_letters.add(guess)

            # Check if the letter is in the secret word
            if self.reveal_letters(guess):
                print("\nWell done! Nice job! You found a letter.")
                print(" ".join(self.blanks))

                # Check if the player guessed the whole word
                if self.all_letters_found():
                    print("\nCongratulations! You guessed the word!")
                    print(f"Word: {self.secret_word}")
                    print("GAME OVER")
                    break

            else:
                # Remove one life for an incorrect guess
                self.lives -= 1
                print(f"\nNope. You lose a life. Lives left: {self.lives}")
                print(" ".join(self.blanks))

                # Check if the player has no lives left
                if self.lives <= 0:
                    print("\nOut of lives!")
                    print(f"The word was: {self.secret_word}")
                    print("GAME OVER")
                    break


def main():

    # Create an object of the WordGuessingGame class
    game = WordGuessingGame()

    # Start the game
    game.play()


if __name__ == "__main__":
    main()