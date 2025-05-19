import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_divider():
    print("-" * 50)

def show_intro():
    print("🎓 Student Portfolio")
    print_divider()
    print("Name: John Doe")
    print("Course: BS Computer Science")
    print("School: Example University")
    print("Email: john.doe@example.com")
    print_divider()

def show_projects():
    print("📁 Projects")
    print_divider()
    print("1. Grade Calculator - A simple Python program to compute student grades.")
    print("2. Attendance Tracker - CLI-based app to manage attendance.")
    print("3. Personal Budget App - Tracks expenses and shows summaries.")
    print_divider()

def show_skills():
    print("🛠 Skills")
    print_divider()
    print("- Python")
    print("- HTML & CSS")
    print("- Git & GitHub")
    print("- Problem Solving")
    print_divider()

def main():
    clear_screen()
    show_intro()
    show_projects()
    show_skills()
    print("Thank you for viewing my portfolio!")

if __name__ == "__main__":
    main()
