from survey import AnonymousSurvey

question = "what job?"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("Enter q to stop")
while True:
    response = input("job: ")
    if response == "q":
        break
    my_survey.store_response(response)

print("--END--")
my_survey.show_result()