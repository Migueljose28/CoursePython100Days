def life_in_weeks(age):
    quantity_weeks_between_zero_for_ninety = 90 * 52
    weeks_through_age = age * 52
    weeks_left = quantity_weeks_between_zero_for_ninety - weeks_through_age
    print(f"You have {weeks_left} weeks left.")
life_in_weeks(56)
