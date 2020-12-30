address = "username@companyname.com"

# Split the addres on the "@" symbol and select the string after the @ symbol.
# Then split on the "." symbol and select the string before the "." symbol.
domain = address.split("@")[1].split(".")[0]
print(domain)
