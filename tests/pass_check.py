def is_acceptable_password(password: str) -> bool:
    passwd = []
    for letter in password:
        passwd.append(letter)
    if len(passwd) >= 6:
        return True
    else:
        return False


print("Example:")
print(is_acceptable_password("short"))
