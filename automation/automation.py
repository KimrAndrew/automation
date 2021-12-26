import re

valid_email_pattern = r'(?:\w+\.)?(?:w+\.)?\w+@\w+\.\w{1,3}'
valid_phone_pattern = r'\b(?:\d{3}|\(\d{3}\))[\. -]?\d{3}[\. -]?\d{4}(?:x\d+)?'

def get_mixed_notes():
    with open('documents/mixed_notes.txt','r') as notes_file:
        return notes_file.read()

mixed_notes = get_mixed_notes()

print(re.findall(valid_email_pattern,mixed_notes))
print(re.findall(valid_phone_pattern,mixed_notes))



