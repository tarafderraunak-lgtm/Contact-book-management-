Contact Book CLI
A lightweight, terminal-based Contact Management System built with Python. This application allows users to store, search, view, and delete contact information efficiently.

✨ Features
Add/Update Contacts: Save new names and phone numbers. If a contact already exists, the system prompts for an update.

Search Functionality: Find contacts quickly using partial name matches (case-insensitive).

Formatted View: View all saved contacts in a clean, tabular layout.

Safety Checks: Includes confirmation prompts before deleting data to prevent accidental loss.

Clean CLI: Simple numbered menu for easy navigation.

🚀 Getting Started
Prerequisites
Python 3.x installed on your machine.

Installation
Clone the repository (or download the source code):

Bash
git clone https://github.com/yourusername/contact-book.git
cd contact-book
Run the application:

Bash
python contact_book.py
🛠️ Usage
Once the program is running, follow the on-screen menu:

Press 1 to add a new person.

Press 2 to see your entire list.

Press 3 to find a specific person by name.

Press 4 to remove a contact.

Press 5 to safely exit the program.

📂 Project Structure
Plaintext
.
├── contact_book.py  # Main Python script containing all logic
└── README.md        # Project documentation
📝 Future Roadmap
[ ] Data Persistence: Save contacts to a .json or .csv file so data isn't lost on exit.

[ ] Email Support: Add a field for email addresses.

[ ] Input Validation: Use Regex to ensure phone numbers follow a specific format.
