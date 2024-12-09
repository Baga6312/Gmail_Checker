import smtplib
import dns.resolver
from termcolor import colored
import concurrent.futures

def verify_email(email):
    """Verify the existence of an email by checking its MX records and SMTP server."""
    try:
        domain = email.split('@')[-1]

        mx_records = dns.resolver.resolve(domain, 'MX')
        mx_host = str(mx_records[0].exchange)

        server = smtplib.SMTP(mx_host)
        server.helo()
        server.mail('test@example.com')
        code, message = server.rcpt(email)  

        server.quit()

        return email, True if code == 250 else False
    except Exception as e:
        print(f"Error checking {email}: {e}")
        return email, False

def check_emails_from_file(input_file):
    """Read emails from a file and display the results with colors and proper alignment."""
    try:
        with open(input_file, 'r') as f:
            email_list = [line.strip() for line in f]
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
        return

    email_width = max(len(email) for email in email_list)

    status_width = 12  
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(verify_email, email) for email in email_list]

        for future in concurrent.futures.as_completed(futures):
            email, exists = future.result()
            email_colored = colored(email, 'cyan') 
            found_colored = colored('[   FOUND   ]       ', 'green') if exists else colored('[ NOT FOUND ]       ', 'red')

            print( f"{found_colored.rjust(status_width)}" + f"{email_colored.ljust(email_width)}"   )

input_file = 'email.txt' 
check_emails_from_file(input_file)

