email = input("Type your email:")
def valid_email(email):
    if "@" in email:
        if "." in email:
            return True
        else:
            return False
    else:
        return False
print(valid_email(email))



