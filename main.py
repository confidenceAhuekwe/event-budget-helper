def participant_cost(attendees, food_per_person, transport_per_person):
    return (attendees * food_per_person) + (attendees * transport_per_person)


people = participant_cost(10, 800, 200)
print(people)