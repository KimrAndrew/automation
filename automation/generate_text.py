# Why isn't syntax highliting working as expected here???
from faker import Faker
from random import shuffle

fake = Faker()

texts = [fake.text() for _ in range(10)]

phones = [fake.phone_number() for _ in range(10)]

emails = [fake.email() for _ in range(10)]

bad_emails = ['justaname','space.in.name @example.org', 'missing@adomain','@naname.com','.@noname.com','nolastname.@example.net','noperiods@examplecom','noatsymbolexample.net']
bad_phone_numbers = ['wherearethenumbers','(123 123 1234', '123) 123 1234', '123 -123-1234','123-123-123','123-123-12345','123--123  1234', '']

#print(texts)
#print(phones)
#print(emails)

combined_content = texts + phones + emails + bad_emails + bad_phone_numbers
shuffle(combined_content)

mixed_notes = ' '.join(combined_content)
with open('documents/mixed_notes.txt','w') as file:
    file.write(mixed_notes)

