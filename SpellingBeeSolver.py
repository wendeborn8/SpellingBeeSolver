##############################################################################
# Required Imports

from time import sleep
import argparse

##############################################################################
# Construct the list of words

eng = open('SpellingBeeWords.txt', 'r').read().splitlines()

##############################################################################
# Solver function

def solve(center_letter = None, outer_letters = None, enter = False, delay = 10,
          url = 'https://www.nytimes.com/puzzles/spelling-bee'):
    
    # If center_letter and outer_letters are not provided, fetch the current puzzle
    if center_letter is None and outer_letters is None:
        
        import selenium
        from bs4 import BeautifulSoup as bs
        
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options = options)
        
        driver.get(url)
        html = driver.page_source
        driver.close()
        
        soup = bs(html, 'html5lib')
    
        center_letter = soup.find_all('svg', "hive-cell center")[0].text
        outer_letters = [letter.text for letter in soup.find_all('svg', "hive-cell outer")]

    #Reduce to words only containing the appropriate letters
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    bad_letters = [letter for letter in alphabet if (letter not in outer_letters and letter != center_letter)]
    
    words = [word for word in eng if (not any([bad_letter in word for bad_letter in bad_letters]) and center_letter in word)]
    words.sort(key = len, reverse = True)
    
    # Enter words into Spelling Bee window
    # Navigation to window is not done automatically. User must manually navigate to Spelling Bee window
    if enter:
        
        from pynput.keyboard import Key, Controller
        kyb = Controller()
        
        print('Navigate to Spelling Bee window now...')
        print(f'Entering words in {delay} seconds...')
        for i in range(delay):
            print('    ', delay - i)
            sleep(1)
    
        for word in words:
            
            kyb.type(word)
            sleep(0.05)
                
            kyb.press(Key.enter)
            kyb.release(Key.enter)
    
    return words

##############################################################################

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description = 'Solve Spelling Bee.')
    parser.add_argument('-e', '--enter', default = False, help = 'Enter words into Spelling Bee window.', action = 'store_true')
    parser.add_argument('-c', '--center_letter', default = None, type = str, help = 'Use specific center letter')
    parser.add_argument('-o', '--outer_letters', default = None, type = str, help = 'Use specific outer letters.')
    parser.add_argument('-d', '--delay', default = 5, type = int, help = 'Delay (in seconds) before words are entered.')
    args = parser.parse_args()
    
    enter, center_letter, outer_letters, delay = \
        args.enter, args.center_letter, args.outer_letters, args.delay
    
    words = solve(enter = enter, center_letter = center_letter, outer_letters = outer_letters, delay = delay)
    print(words)
    
