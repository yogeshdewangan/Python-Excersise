import re

str = "d 10.116.1.216 sfd 2.2.2.3 sdfsdf"
print (re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", str))

pat = re.compile(r"\s((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.){3}((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9]))")

match = re.findall(pat, str)

print (match)

