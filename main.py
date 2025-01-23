def sound_effect(number):
    reply = ""
    if number % 3 == 0:
        reply += "Fizz"
    if number % 5 == 0:
        reply += "Buzz"
    if reply == "":
        reply += "No fizzing... No buzzing..."
    print(reply)
    return reply