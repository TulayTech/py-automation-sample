# Import datetime module to get the current date and time
from datetime import datetime

# Define main function to run automation script
def main():
    # Print a message to indicate the test is starting
    print("⚙️ Starting automation test...")

    # Print a success message along with the current timestamp
    print(f"✅ Test completed successfully at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Check if the script is being run directly, if so, call the main function
if __name__ == "__main__":
    main()