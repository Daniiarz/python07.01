is_asian = True
is_american = False

name = input()
age = int(input())
kids = int(input())
print(name)

if name == "Nurtazim":
    print("Asian")
else:
    print("American")

if age > 18:
    print("Mojno voity")
else:
    print("Nelzya")

if kids < 2:
    print("Mojno s detmi")
else:
    print("Nelzya")


if False:
    print("True working!")
else:
    print("Not Working")
