import random
import string
import itertools

def generate_random_string(length):
    """Generate a random string with letters, digits, and symbols."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def generate_email_permutations(first_name, last_name, domain, max_combinations=10000000):
    """Generate a massive number of email combinations using different case, numbers, and symbols."""
    
    # Normalize inputs
    first_name = first_name.lower()
    last_name = last_name.lower()
    domain = domain.lower()

    # Define basic patterns (initials, full names, and reversed order)
    patterns = [
        "{first}",
        "{last}",
        "{first}.{last}",
        "{first}{last}",
        "{first[0]}{last}",
        "{first}{last[0]}",
        "{last}.{first}",
        "{last}{first}",
    ]

    # Characters to append or modify
    numbers = [str(random.randint(1, 9999)) for _ in range(5)]  # Random numbers
    cases = ["lower", "upper", "capitalize", "random"]  # Random case transformations

    # Helper to randomly change the case of each letter
    def random_case(name):
        return ''.join(random.choice([ch.lower(), ch.upper()]) for ch in name)

    # List to hold all generated emails
    emails = set()  # Use set to avoid duplicates
    count = 0  # Track number of combinations generated

    # Iterate over all combinations of patterns, cases, and numbers
    for pattern in patterns:
        for num in numbers:
            for first_case in cases:
                for last_case in cases:
                    # Apply case transformations
                    first = first_name
                    last = last_name

                    if first_case == "random":
                        first = random_case(first_name)
                    elif first_case == "upper":
                        first = first_name.upper()
                    elif first_case == "capitalize":
                        first = first_name.capitalize()

                    if last_case == "random":
                        last = random_case(last_name)
                    elif last_case == "upper":
                        last = last_name.upper()
                    elif last_case == "capitalize":
                        last = last_name.capitalize()

                    # Add random symbols or numbers to the name
                    random_chars = generate_random_string(random.randint(2, 5))  # Random symbols and numbers

                    # Apply pattern and create email
                    email = pattern.format(first=first, last=last, first0=first[0], last0=last[0])
                    email = f"{email}{random_chars}{num}@{domain}"
                    emails.add(email)

                    count += 1
                    if count >= max_combinations:
                        break
                if count >= max_combinations:
                    break
            if count >= max_combinations:
                break
        if count >= max_combinations:
            break

    return list(emails)

def save_emails_to_file(emails, file_name="email.txt"):
    with open(file_name, 'w') as f:
        for email in emails:
            f.write(email + '\n')
    print(f"Emails saved to {file_name}")

# Example usage
first_name = input("Enter first name: ").strip()
last_name = input("Enter last name: ").strip()
domain = input("Enter domain (e.g., example.com): ").strip()

# Generate emails with up to 10 million combinations
emails = generate_email_permutations(first_name, last_name, domain, max_combinations=10000000)

# Save to a file
save_emails_to_file(emails, "email.txt")

