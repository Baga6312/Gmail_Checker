# Email Generation and Verification Tool

This project provides a tool to **generate** a list of email permutations based on a person's first name, last name, and domain, and then **verify** whether each generated email exists.

## Overview

1. **Email Generation**: The tool creates a large set of potential email addresses by combining different case variations, patterns, random numbers, and special characters for a given first name, last name, and domain.
2. **Email Verification**: After generating the emails, the tool checks whether each email exists by contacting the mail server of the domain and verifying the recipient.

## Files

- `generate_emails.py`: The script that generates email permutations based on the given first name, last name, and domain.
- `check_emails.py`: The script that checks the existence of each email by verifying the SMTP server.
- `main.py`: The main script that coordinates the generation and verification process.

---
# Installation 
  ```
  git clone https://github.com/Baga6312/Email_Checker 
  cd Email_Checker
  pip3 install -r requirements.txt
  ```
# Example usage
  ```
  python3 main.py 
  
  Enter first name: 
Enter last name: 
Enter domain (e.g., example.com): 
Enter output file name for generated emails (e.g., email.txt): 
Generating 10000000 emails for  ...
  ```
you will be prompted to enter some informations and then the script will check for validity of every email in the `email.txt`
```
[ NOT FOUND ]       jHON.DoeGG{1908@gmail.com
[ NOT FOUND ]       JDOETaH1908@gmail.com
[ NOT FOUND ]       doeeSK`6776@gmail.com
[ NOT FOUND ]       jhondoeNt4896@gmail.com
[ NOT FOUND ]       dOEJhonAfxBT1908@gmail.com
[ NOT FOUND ]       DOE.JHONTp2Q1908@gmail.com
[ NOT FOUND ]       DOEq~*IV1908@gmail.com
[ NOT FOUND ]       doe.jhon!0)9537@gmail.com
[ NOT FOUND ]       jDoe=1>`84896@gmail.com
[ NOT FOUND ]       doeJhon{_1908@gmail.com
[ NOT FOUND ]       DoE~7L+r1908@gmail.com
[ NOT FOUND ]       JhoND_t6776@gmail.com
[ NOT FOUND ]       jhon*/1724@gmail.com
[ NOT FOUND ]       JHONd]`W9537@gmail.com
[ NOT FOUND ]       Jhon.doe(/1724@gmail.com
[ NOT FOUND ]       JHON.DoebPBZ9537@gmail.com
[ NOT FOUND ]       JhonDk_^64896@gmail.com
[ NOT FOUND ]       Jdoe7"M!q9537@gmail.com
[ NOT FOUND ]       jhonDOEzC'4896@gmail.com
[ NOT FOUND ]       doe.JHONqwB9537@gmail.com
