# Automation

The purpose of this application is to comb through a text file and extract any Phone Numbers or Emails contained in the supplied file

## What Constitutes as a Valid Phone Number or Email

- Phone numbers must match the basic pattern of xxx-yyy-zzzz or yyy-zzzz
  - Phone numbers do not have to match this format exactly but must have three digits followed by four digits with an optional area code of three digits. If no area code is given, it is presumed to be 206
  - Phone numbers will be stored in a text file of their own, seperate from any emails

- Emails must match the pattern of non-whitespace-characters@some-sub-domain.some-top-level-domain
  - Emails will also be stored in their own text file

### Re: Phone Numbers From Faker

- looking into it the x##### appears to be a reasonably common phone extension: it shouldn't take too long to also add support for numbers with this extension

## Notes About Stored Contact Info

- Information should be stored in ascending order
- No duplicate entries are allowed

PR: [https://github.com/KimrAndrew/automation/pull/1](https://github.com/KimrAndrew/automation/pull/1)
