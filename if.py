male=(input("Are u a male(yes/no): ").lower()=="yes")
tall=(input("Are u a tall(yes/no): ").lower()=="yes")
if male and tall:
    print("You are a tall male")
elif male and not(tall):
    print("You are a short male")
elif not(male) and tall:
    print("You are a tall female")
else:
    print("You are a short female")