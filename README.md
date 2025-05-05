# Class Inheritance Project: Electronics, Computers, and Phones

This Python project demonstrates the concept of class inheritance through a simple hierarchy of electronic devices. The base class `Electronics` is extended by the `Computer` class, which is further extended by the `Phone` class. A driver script is included to interactively create and display instances of each class using user input.

## 📁 Project Structure

```
├── electronics.py     # Base class: Electronics
├── computer.py        # Subclass of Electronics: Computer
├── phone.py           # Subclass of Computer: Phone
└── driver.py          # Main script to run and test the classes
```

## 🔧 How It Works

- `Electronics`: Base class with a brand name.
- `Computer`: Inherits from `Electronics` and adds an operating system attribute.
- `Phone`: Inherits from `Computer` and adds a phone number attribute.
- `driver.py`: Collects user input to instantiate objects from each class and displays their attributes.

## ▶️ Getting Started

To run the project:

1. Make sure all `.py` files are in the same directory.
2. Run the `driver.py` file using Python 3:

```bash
python driver.py
```

You will be prompted to enter brand names, operating systems, and a phone number.

## 💡 Example Output

```
Enter an Electronics Brand: Sony
Enter an Electronics Brand: Apple
Enter an Operating System: macOS
Enter an Electronics Brand: Samsung
Enter an Operating System: Android
Enter a phone number: 123-456-7890

The Electronics Object: Sony

The Computer Project: Apple macOS

The Phone Object: Samsung Android 123-456-7890
```

## 🧠 Concepts Covered

- Class inheritance
- Constructors and method overriding
- Encapsulation (getters and setters)
- Object-oriented design

## 🖊️ Author

Baasim Ahmed  
Intro to Programming – CIS 135  
Joliet Junior College  
