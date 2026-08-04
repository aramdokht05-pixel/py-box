import random 
import datetime
import time

thoughts = [
    "today is a great day to start something new.",
    "believe in your self, everything is possible.",
    "start your day with a smile.",
    "every day is a new opportunity.",
    "success comes from small but consistent efforts.",
    "find peace in the present moment.",
    "you are good enough, just keep going.",
    "dream big and dare to fail.",
    "happiness is a choice, choose it today.",
    "your only limit is your mind.",
    "the best time to start was yesterday. the next best time time is now.",
    "you are stronger than you think.",
    "small steps lead to big results.",
    "believe you can and you're halfway there.",
    "it does not matter how slowy you go as long as you do not stop.",
    "the secret of getting ahead is getting started.",
    "don't watch the clock; do what it does. keep going.",
    "the only way to do great work is to love what you do.",
    "---no problem---",
    "it's oky..."
]
today = datetime.datetime.now().strftime("%A - %d %B %Y")
daily_thought = random.choice(thoughts)

print("\n" + "=" * 60)
print(f"{today}")
print( "=" * 60)
print(f"{daily_thought}")
print( "=" * 60)
    
print("\n ⏳ you have 5 seconds to read....")
time.sleep(5)
print("good by...")
input("press enter to exit...")
