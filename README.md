# SpellingBeeSolver
Simple little script to fetch, solve, and subsequently enter the answers to The New York Times' Spelling Bee minigame.

## Usage

Using SpellingBeeSolver is quite simple and can be run from the command line (provided SpellingBeeSolver.py is either in the current directory or in your PATH). 

In its simplest form, you can fetch and solve the current Spelling Bee puzzle on the NYTimes website, and the potentially acceptable words printed.

```bash
python SpellingBeeSolver.py
```

If you'd like the words to be automatically entered into the Spelling Bee window, you can use the ```-e/-enter``` argument. After a 5-second delay, the words will be automatically typed and entered into the game. Make sure you've navigated to the Spelling Bee window and make it the active window on your system.

```bash
python SpellingBeeSolver.py -e
```

If you need mroe time to navigate to the Spelling Bee window, use the ```-d/-delay``` argument to modify the time delay.

```bash
python SpellingBeeSolver.py -e -d 15
```

If you'd like to solve for previous puzzles, or just some collection of letters of your choosing, use the ```-c/-center_letter``` and ```-o/-outer_letters``` arguments. You can use any number of outer letters. The ```-e/-enter``` keyword can still be used, but the words won't be accepted, so there is not much use.

```bash
python SpellingBeeSolver.py -c a -o bcdefghi
```

## Extras

The file SpellingBeeWords.txt is included as the collection of all words that may/may not be accepted by Spelling Bee. 
