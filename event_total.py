from participant_cost import people
from participant_cost import zeroattendees

def event_total (cost,venue_cost):
    return cost + venue_cost
    

# test
# normal attendee cost 
total=event_total(people,50000)
# zero attendee cost with  non zero venue 
total=event_total(zeroattendees,5000)

# wrote the event cost

# Hand over note
#component: event_total
#Returns: 'total event cost'
#test: normal attendee cost, zero attendee cost with non zero venue"
#Issue: 'none'
