import random

def scramble(word):
    word = list(word)
    random.shuffle(word)
    return ''.join(word)

# Word list
words = [
    "algorithm", "function", "variable", "condition", "exception",
    "recursion", "boolean", "integer", "library", "iteration",
    "compile", "execute", "syntax", "binary", "debugging",
    "operator", "constant", "argument", "package", "framework"
]

score = 0

print("🎮 Welcome to Word Scramble Game!\nGuess the original word from the scrambled version.\n")

# Game loop
for i in range(5):
    original = random.choice(words)
    scrambled = scramble(original)

    print(f"\nWord {i+1}: {scrambled}")
    guess = input("Your guess: ")

    if guess.lower() == original:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! The correct word was: {original}")

print(f"\n🏁 Game Over! Your score: {score}/5")
