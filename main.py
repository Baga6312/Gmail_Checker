import subprocess
import sys

def run_generate_script(first_name, last_name, domain, output_file, num_emails=10000000):
    """Run the email generation script."""
    try:
        print(f"Generating {num_emails} emails for {first_name} {last_name}...")
        subprocess.run(['python3', 'generate_emails.py', first_name, last_name, domain, output_file, str(num_emails)])
        print(f"Emails generated and saved to {output_file}")
    except Exception as e:
        print(f"Error generating emails: {e}")
        sys.exit(1)

def run_check_script(input_file):
    """Run the email checking script."""
    try:
        print(f"Checking emails in {input_file}...")
        subprocess.run(['python3', 'check_emails.py', input_file])
    except Exception as e:
        print(f"Error checking emails: {e}")
        sys.exit(1)

def main():
    # Get user inputs
    first_name = input("Enter first name: ").strip()
    last_name = input("Enter last name: ").strip()
    domain = input("Enter domain (e.g., example.com): ").strip()
    output_file = input("Enter output file name for generated emails (e.g., email.txt): ").strip()

    run_generate_script(first_name, last_name, domain, output_file)

    run_check_script(output_file)

if __name__ == "__main__":
    main()

