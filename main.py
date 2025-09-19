import random 
words_list = [
    "apple",
    "banana",
    "grape",
    "orange",
    "mango",
    "pear",
    "peach",
    "cherry",
    "dog",
    "cat",
    "lion",
    "tiger",
    "horse",
    "zebra",
    "eagle",
    "shark",
    "whale",
    "table",
    "chair",
    "pencil",
    "school",
    "house",
    "garden",
    "river",
    "mountain",
    "ocean",
    "cloud",
    "rain",
    "snow",
    "star",
    "moon",
    "sun",
    "earth",
    "book",
    "music",
    "dance",
    "happy",
    "smile",
    "green",
    "blue",
    "black",
    "white",
    "gold",
    "king",
    "queen",
    "friend",
    "family",
    "game",
    "train",
    "plane",
    "truck"
]


# Hangman stages list
hangman_stages = [
    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|/
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|/
       |   /
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|/
       |   / /
       |
    --------
    """
]


chosen_word=random.choice(word_list)
print(chosen_word)
print(hangman_stages[len(hangman_stages)-1])

placeholder=""
for p in range(len(chosen_word)):
    placeholder+=" _"
print(placeholder)

# Game Starts
Game_over=False
correct_letters=[]
chance=5
while not Game_over:
    print(f"YOU HAVE {chance} lives ")
    
    guess=input("Guess the letter: ").lower()
    if guess in correct_letters:
        print("You've already guessed")
    display=""
    for letter in chosen_word:
        if letter == guess:
            display+=letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+=letter
        else:
            display+='_'+" " 
                
    print(f"guess again :{display}")  

    if guess not in chosen_word:
        chance-=1
        print(f"You have guessed{guess}, that's not in the word. You lose a life.")
        if chance==0:
            Game_over=True
            print(f"IT WAS {chosen_word} YOU LOSE")
    if "_" not in display:
        Game_over=True
        print("YOU WON")   

    print(hangman_stages[chance])         


