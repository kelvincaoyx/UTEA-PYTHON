def markChecker(mark):
    if mark >= 80:
        return "level 4"
    elif mark >= 70:
        return "level 3"
    elif mark >= 60:
        return "level 2"
    elif mark >= 50:
        return "level 1"
    else:
        return "Level R"

mark = int(input("Please enter your mark: "))

print("You have a ", markChecker(mark))
