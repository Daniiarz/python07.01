name = input()
avtandil = "Avtandil"
age = int(input())

if name == avtandil and age == 35 and False:
    print(True, "Vy Avtandil")
else:
    print(False, "Vy ne Avtandil")

name2 = input()
tilek = "Tilek"
age2 = int(input())

if name2 == tilek or age2 >= 18 or True:
    print(True, "Vy Tilek, libo vam bolshe 18")
else:
    print(False, "Vy ne Tilek, i vam ne bolshe 18")


name3 = input()
hobby = input()
salta = "Salta"
salta_hobby = "Anime"
age = int(input())
kursy = input()

if (name3 == salta and hobby == salta_hobby) or age > 23:
    print(True, "Vy Salta, i vashe hobby Anime, ili vam bolshe 23")
elif kursy == "GeekTech":
    print("GeekTech")
else:
    print(False)
name3 = input()

if name3 == "Salta":
    print("Name is Salta")
elif name3 == "Daniiar":
    print("Name is Daniiar")
elif name3 == "Samat":
    print("Name is Samat")
else:
    print("Vy ne odin in 3 vyshe ukazannyh")
