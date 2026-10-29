def participant_cost(attendees, food_per_person, transport_per_person):
    return attendees * (food_per_person + transport_per_person)


def event_total (attendees, food_per_person, transport_per_person, venue_cost):
    people = participant_cost(attendees, food_per_person, transport_per_person)
    return people + venue_cost 

def budget_status(budget, total):
    if total <= budget:
        return "Within budget"
    else:
        return "Over budget"

def event_summary(event_name, total, status):
    return f"{event_name}: total {total} naira. {status}."

# Test code that call the functions using the published values
people = participant_cost(10, 800, 200)
print(people)

total= event_total(10, 800, 200, 5000)
print ("total=",total, "naira")

status= budget_status(16000,total)
print (status)

summary = event_summary("Study Day", total, status)
print(summary)


# Another Test code 
people = participant_cost(17, 650, 300)
print("People is " + str(people))
total = event_total(17, 650, 300, 7500)
print("Total is " + str(total))
status = budget_status(20000, total)
print(status)
summary = event_summary("NYSC POP Day", total, status)
print(summary)