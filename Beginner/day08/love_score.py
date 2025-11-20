def calculate_love_score(name1: str, name2: str):
    list_letter = list((name1 + name2).lower().replace(" ", ""))
    
    true_score, love_score = 'true', 'love'
    true_points = love_points = 0

    for i in list_letter:
        true_points += 1 if i in true_score else 0
        love_points += 1 if i in love_score else 0

    print(f"{true_points}{love_points}")

calculate_love_score("Angela Yu", "Jack Bauer")
