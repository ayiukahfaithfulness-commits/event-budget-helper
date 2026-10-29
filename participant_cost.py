def participant_cost (attendees, food_per_person, transport_per_person):
    return attendees * (food_per_person + transport_per_person)
    
people = participant_cost(10, 800, 200)
zeroattendees = participant_cost(0, 800, 200)

# Tests:
#normal attendee test
#print (participant_cost(10, 800, 200)) # expected flow: 10,000

#Zero attendee test
#print (participant_cost(0, 800, 200)) # expected flow: 0

# Hand over note
#component: participant_cost
#Returns: 'total cost per atttendeee'
#test: normal attendee test, zero attendees test"
#Issue: 'none'