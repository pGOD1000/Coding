def first_geo_question():
    question = input("Who is the current president of Nigeria")
    if (question == "President Bola Ahmed Tinubu"):
        return "Nice one"
    else:
        return "Try again"
        question = input("Who is the current president of Nigeria")
    if (question == "President Bola Ahmed Tinubu"):
        return "Nice one"
    
start = first_geo_question()
print(start)