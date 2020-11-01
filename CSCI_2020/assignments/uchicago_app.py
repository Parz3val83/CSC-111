question_initial = input("Enter a query: ")
print(question_initial)
vater_response = ''
while vater_response != "Because I said so, now go away.":
    vater_response = input("Enter dad's answer: ")
    if vater_response == "Because I said so, now go away.":
        break
    print(vater_response)
    print("Why?")
