import re

email = input("Email: ")
phone = input("Phone: ")
log = input("Enter log text: ")

print("Valid email" if re.fullmatch(r"[\w.+-]+@[\w-]+\.[\w.]+", email) else "Invalid email")
print("Valid phone" if re.fullmatch(r"(\+91)?[6-9]\d{9}", phone) else "Invalid phone")
print("Transaction IDs:", re.findall(r"TXN\d+", log))