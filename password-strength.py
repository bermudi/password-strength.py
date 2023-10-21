import math
import re

def leet_speak_penalty(password):
    """Calculate penalty for using l33t speak patterns."""
    # Convert the password to lowercase for case-insensitive checks
    password_lower = password.lower()
    
    # Common l33t speak substitutions
    leet_substitutions = {
        '4': 'a',
        '3': 'e',
        '1': 'i',
        '0': 'o',
        '7': 't',
        '$': 's',
        '5': 's'
    }
    
    penalty = 0
    for leet_char, alpha_char in leet_substitutions.items():
        if leet_char in password_lower:
            penalty += 15  # Penalty for each detected l33t speak pattern
    
    return penalty

def further_modified_password_strength(password):
    """Evaluate the strength of a password."""
    # Adjusted base points due to password length
    score = len(password) * 10  # Linear function for length
    
    # Extra points for different character types
    if any(c.islower() for c in password):
        score += 5
    if any(c.isupper() for c in password):
        score += 5
    if any(c.isdigit() for c in password):
        score += 5
    if any(not c.isalnum() for c in password):  # symbols
        score += 5
    
    # Deducting points for dictionary words
    common_words = ["password", "123456", "admin", "welcome", "user"]
    for word in common_words:
        if word in password.lower():
            score -= 20
    
    # Deducting points for letters only or numbers only
    if password.isalpha():
        score -= 30
    if password.isdigit():
        score -= 40
    
    # Deducting points for repeated characters
    char_count = {}
    for c in password:
        char_count[c] = char_count.get(c, 0) + 1
    for count in char_count.values():
        if count > 1:
            score -= math.pow(count, 3)  # Increased penalty for repetitions
    
    # Deducting points for consecutive letters and numbers
    consec_letters = len(re.findall(r"(?:[a-zA-Z]{2,})", password))
    consec_numbers = len(re.findall(r"(?:\d{2,})", password))
    score -= math.pow(consec_letters, 3) * 2  # Increased penalty for consecutive letters
    score -= math.pow(consec_numbers, 3) * 2  # Increased penalty for consecutive numbers
    
    # Deducting points for l33t speak patterns
    score -= leet_speak_penalty(password)
    
    return max(score, 0)  # Ensure that the score isn't negative
