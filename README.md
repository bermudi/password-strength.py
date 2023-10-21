# Password Strength Analysis Algorithm
This algorithm evaluates the strength of a password based on various criteria. A higher score represents a stronger password, while a lower score indicates potential vulnerabilities.

## Features:
1. Password Length: The score starts by considering the linear length of the password.
1. Character Types: Awards extra points for the presence of:
   - Lowercase letters
   - Uppercase letters
   - Numbers
   - Symbols
1. Dictionary Words: Deducts points if the password matches common dictionary words or phrases.
1. Consecutive and Repeated Characters:
   - Deducts exponential points for consecutive letters and numbers.
   - Deducts exponential points for repeated characters.
1. Leet Speak: Deducts points for common "l33t" speak patterns.
## Scoring Details:
Base points are awarded according to the linear length of the password.
Presence of lowercase, uppercase, numbers, and symbols each add 5 points.
Common dictionary words deduct 20 points each.
Passwords that contain only letters deduct 30 points.
Passwords that contain only numbers deduct 40 points.
Repeated characters result in an exponential deduction based on the count of repetition.
Consecutive letters and numbers each result in an exponential deduction.
Each detected "l33t" speak pattern deducts 15 points.
## Usage:
To evaluate the strength of a password:

python
Copy code
score = password_strength(password)
Where password is the string you wish to evaluate.
