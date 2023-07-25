for number in range(10):
    for object in range(number+1, 10):
        print("{:02d}".format(number*10+object), end=", "  if number *10 + object < 89 else "")
print()
