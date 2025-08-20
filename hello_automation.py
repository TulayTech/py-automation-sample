"""
DAY 1: Test Steps

GOAL:
Create a simple script that collects user's name, allow user to add
test steps, and save info in a file called 'day1_log.txt'.

SCRIPT STEPS:
1. Ask user for their name.
2. Ask what step they want to log as completed (ex: 'checked login screen')
3. Save info into a file called 'day1_log.txt'.
4. Prints confirmation so the user knows it worked.
5. Print date and time of completion.
"""
# IMPORT MODULES
from datetime import datetime # datetime module to get the current date and time
from pathlib import Path # Allows us to work with files in a cleaner way

# Define main function to run automation script
def main():
    # Print a message to indicate the test is starting
    print("⚙️ Starting automation test... \n")

    # Ask user to enter their name. Use strip function to remove extra white spaces
    name = input("Who's working on this project? \n").strip()

    # Ask user to enter the name of the test step that they completed
    print(f"{name}, enter the name of the test step you would like to log: " )
    step = input ("").strip()

    # Building a user friendly log entry string. EX: "Tester: Alice | Step: Checked login screen"
    entry = f"Tester: {name} | Step: {step}\n"

    # Add file path where log will be saved. Saving into the same folder as this script
    log_file = Path(__file__).parent / "day1_log.txt"

    # Open the file in "append" mode. If file doesn't exist, create it, if so, add file at the end of the log, do not erase.
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(entry)

    # Print result and a success message along with the current timestamp
    print(f"✅ Step logged: {entry.strip()} (saved in {log_file})")
    print(f"✅ Added '{step}' successfully | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Check if the script is being run directly, if so, call the main function
if __name__ == "__main__":
    main()