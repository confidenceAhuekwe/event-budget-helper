def participant_cost(attendees, food_per_person, transport_per_person):
    return (attendees * food_per_person) + (attendees * transport_per_person)


def event_total (venue_cost, attendees, food_per_person, transport_per_person):
    people=participant_cost(attendees, food_per_person, transport_per_person)
    return venue_cost + people

def budget_status(budget, total):
    if total <= budget:
        return "Within budget"
    else:
        return "Over budget"


people = participant_cost(10, 800, 200)
print(people)

total= event_total(5000, 10, 800, 200)
print ("total=",total, "naira")

status= budget_status(16000,total)
print (status)