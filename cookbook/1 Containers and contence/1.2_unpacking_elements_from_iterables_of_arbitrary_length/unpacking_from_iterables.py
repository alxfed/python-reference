"""
Unpacking from iterables of arbitrary length
"""


record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record  # the asterisk instead of unknown number of variables

print(phone_numbers)

# only the last variables

*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]

print(current)

# splitting of strings

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')

print(sh)
print(homedir)

# the trash variables are exemplified by "_"

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record

print(year)
