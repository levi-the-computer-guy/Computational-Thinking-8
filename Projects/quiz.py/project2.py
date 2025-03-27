# Beginning: create varibles
fastfood_points = 0
healthyfood_points= 0


# asking questions on healthy vs unhealthy types of food, mainly connecting foods together(french fries vs sweet potatos etc)
answer = input("Would you rather A) eat french fries, or B) eat a sweet patoto?")
if answer == "A":
    fastfood_points += 1
elif answer == "B":
    healthyfood_points += 1


answer = input("Would you rather A) drink a milkshake, or B) drink a glass of milk?")
if answer == "A":
    fastfood_points += 1
elif answer == "B":
    healthyfood_points += 1


answer = input("Would you rather A) eat a donut, or B) eat a bagel?")
if answer ==  "A":
    fastfood_points += 1
elif answer == "B":
    healthyfood_points += 1


answer = input("Would you rather A) drink soda, or B) drink a smoothie?")
if answer == "A":
    fastfood_points += 1
elif answer == "B":
    healthyfood_points += 1


answer = input("Would you rather A) eat fried chicken, or B) eat grilled chicken?")
if answer == "A":
        fastfood_points += 1
elif answer == "B":
    healthyfood_points += 1


answer = input("Would you rather A) drink a redbull, or B) get good sleep?")
if answer == "A":
    fastfood_points += 1
elif answer == "B":
    healthyfood_points += 1


    # end of quiz
if fastfood_points > healthyfood_points:
    print("you like fast food!")
elif fastfood_points < healthyfood_points:\
    print("you like healthy foods!")