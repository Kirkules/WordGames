class GameDictionary:
    from english_words import get_english_words_set
    from random import sample
    #  TODO: extend to other word sizes
    PENTAWORDS = [word.strip() for word in get_english_words_set(['web2'], lower=True) if len(word) == 5]

    @staticmethod
    def random_word()-> str:
        """Returns a random word from the puzzle word list."""
        return sample(GameDictionary.PENTAWORDS, 1)[0]

    @staticmethod
    def valid_word(word:str) -> str:
        """Returns true if the word is in the dictionary."""
        return 5 == len(word) and word in GameDictionary.PENTAWORDS


GAME_COLORS = dict(zip(["green_bg", "yellow_bg", "black_bg", "white_text_transparent_bg", "black_text_white_bg"], count(1)))

from enum import Enum

class WordlePuzzle:
    """
    A handler for the game logic of a particular instance of the game of Wordle.
    """
    class MatchType(Enum):
        """Enum of ways a letter in a guess can match the puzzle's solution."""
        POSITION = 1    # This letter in the guess and solution at this position are the same.
        WORD = 2        # This letter in the guess is in the solution, but not at the same position.
        NO_MATCH = 3    # This letter in the guess is not in the solution.

    def __init__(self, word=None):
        """Initializes the puzzle with the given `word`, or a random one if None was given."""
        self.solution = word if word else GameDictionary.random_word()
        self.guesses = []

    def guess_feedback(self, guess:str) -> List[MatchType]:
        """
        Produces the feedback for a given `guess` word, meaning a string of grey/yellow/green
        tiles indicating which guess-word letters are wrong, are in the solution but elsewhere,
        or are in the solution and in the same place.

        If the guess-word is empty, returns all black squares. 

        Assumes the guess is the same length as the puzzle solution.
        """
        if not guess:
            return len(self.solution)*["blank"]

        if len(guess) != len(self.solution):
            return ValueError(f"Guesses should contain {len(self.solution)} letters.")

        return list(WordlePuzzle.MatchType.POSITION if guess[i] == self.solution[i] else
                    WordlePuzzle.MatchType.WORD     if guess[i] in self.solution else
                    WordlePuzzle.MatchType.NO_MATCH
                        for i in range(len(guess)))

            
import curses
from itertools import count
class WordleDisplay:
    """
    A handler for displaying the current state of the game of Wordle.
    """
    curses.use_default_colors()
    curses.init_pair(GAME_COLORS["green"], curses.COLOR_GREEN, curses.COLOR_GREEN)
    curses.init_pair(GAME_COLORS["yellow"], curses.COLOR_YELLOW, curses.COLOR_YELLOW)
    curses.init_pair(GAME_COLORS["black"], curses.COLOR_BLACK, curses.COLOR_BLACK)
    curses.init_pair(GAME_COLORS["white_text_transparent_bg"], curses.COLOR_WHITE, -1)
    curses.init_pair(GAME_COLORS["black_text_white_bg"], curses.COLOR_WHITE, -1)

    def __init__(self):
        self.bg_win = curses.newwin(nlines=6, ncols=5)
        self.fg_win = curses.newwin(nlines=6, ncols=5)

    def show_guess(guess_index: int, puzzle: WordlePuzzle):
        guess = puzzle.guesses[guess_index]
        feedback = puzzle.guess_feedback(guess)
        for i in range(1, len(guess)):



    
    @staticmethod
    def show_puzzle(puzzle: WordlePuzzle):
        padded_guesses = puzzle.guesses + ['']*(max(0, 6-len(self.guesses)))

        for i, guess in enumerate(padded_guesses):

        



scr = curses.initscr()
scr.nodelay(False)
curses.curs_set(False)
scr.refresh()

win = curses.newwin(10, 10)
for i in range(5):
    win.addstr(i+1, 1, GREEN_SQUARE*5)

win2 = curses.newwin(10, 10)
for i in range(5):
    win2.addstr(i+1, 1,"X"*5)

win2.overlay(win)
win2.refresh()
win.refresh()

scr.getch()
