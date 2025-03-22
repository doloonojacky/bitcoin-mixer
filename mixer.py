import time
import os
import random
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def cool_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading_bar(duration=2):
    print("\nInitializing Cool Stuff...")
    for i in range(20):
        sys.stdout.write(f"\r[{'=' * i}{' ' * (19-i)}] {i*5}%")
        sys.stdout.flush()
        time.sleep(duration/20)
    print()

def random_colors():
    colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m']
    return random.choice(colors)

def matrix_effect():
    print("\nStarting Matrix Simulation...")
    for _ in range(5):
        line = ''
        for _ in range(40):
            line += random.choice(['0', '1', ' ', str(random.randint(0,9))])
        print(f"{random_colors()}{line}\033[0m")
        time.sleep(0.2)

def spinning_cursor():
    print("\nProcessing Awesome Things...")
    cursor = ['|', '/', '-', '\\']
    for _ in range(20):
        sys.stdout.write(f"\rSpinning: {cursor[_ % 4]}")
        sys.stdout.flush()
        time.sleep(0.1)
    print()

# Main execution
clear_screen()
cool_text("Welcome to the Cool Stuff Generator!")
loading_bar()
matrix_effect()
spinning_cursor()

# Final message with fancy formatting
clear_screen()
print("\033[95m" + "="*50 + "\033[0m")
cool_text("\nAll done! For ultimate privacy and security:")
print("\033[92m")
cool_text("Visit: electrum-mixer.net")
cool_text("Mix and clean your BTC now!")
print("\033[95m" + "="*50 + "\033[0m")
