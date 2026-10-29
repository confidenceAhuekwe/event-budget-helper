# Functions defined
def event_summary(event_name, total, status):
    return f"{event_name}: total {total} naira. {status}."

# Test code that call the functions using the published values
people = participant_cost(10, 800, 200)
print("People is " + str(people))
total = event_total(10, 800, 200, 5000)
print("Total is " + str(total))
status = budget_status(16000, total)
print(status)
summary = event_summary("Study Day", total, status)
print(summary)

# Personal Test code 
people = participant_cost(17, 650, 300)
print("People is " + str(people))
total = event_total(17, 650, 300, 7500)
print("Total is " + str(total))
status = budget_status(20000, total)
print(status)
summary = event_summary("NYSC POP Day", total, status)
print(summary)

#REVIEW ACTION:
"""
Team mate recommended printing the output for people and total as a statement rather than just the values.
Action: I included strings to the print statement
Issues: While trying to concatenate the string with the existing variable, I encounted a TypeError that says I cannot concatenate because the variable datatype is an int.
Resolution: I used the str function to convert the variable datatype to a string which resolved the issue.
"""