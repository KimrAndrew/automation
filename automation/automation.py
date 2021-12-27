import re

valid_email_pattern = r'(?:\w+\.)?(?:w+\.)?\w+@\w+\.\w{1,3}'
valid_phone_pattern = r'\b(?:\d{3}|\(\d{3}\))[\. -]?\d{3}[\. -]?\d{4}(?:x\d+)?'

def get_mixed_notes():
    with open('documents/mixed_notes.txt','r') as notes_file:
        return notes_file.read()

mixed_notes = get_mixed_notes()

valid_emails = re.findall(valid_email_pattern,mixed_notes)
valid_phones = re.findall(valid_phone_pattern,mixed_notes)

with open('documents/emails.txt','a') as emails:
    for email in valid_emails:
        emails.write(email + '\n')

with open('documents/phone_numbers.txt','a') as phone_nums:
    for num in valid_phones:
        phone_nums.write(num+'\n')





