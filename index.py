from textblob import TextBlob
from colorama import init, Fore

class FeelingsAnalyzer:
    def analyze_sentiment(self, text):
        analysis = TextBlob(text)

        if analysis.sentiment.polarity > 0:
            return Fore.GREEN + "positive"
        elif analysis.sentiment.polarity == 0:
            return Fore.YELLOW + "neutral" 
        else:
            return Fore.RED + "negative"

analyzer = FeelingsAnalyzer()
init(autoreset=True) 

def print_dialogue(speaker, text):
    print("╭─", speaker)
    print("│ ", text)
    print("╰─────────────────────────────────────")

print("╭─────────────────────────────────────")
print("│ Welcome to Feelings Analyzer Terminal")
print("│ Type 'exit' to quit")
print("╰─────────────────────────────────────")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    print_dialogue("You", user_input)

    result = analyzer.analyze_sentiment(user_input)
    print_dialogue("Analyzer", f"Sentiment analysis result: {result}")
