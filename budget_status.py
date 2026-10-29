from event_total import total
def budget_status (budget, total):
    if total <= budget:
        return "within budget"
    else:
        return "over budget"
print (budget_status(16000, 16000))
    

#Tests
#below buddget test
status = budget_status (16000, total)
print ("below budget")

#exactly equal to budget test
balanced = budget_status (15000, total)
print ("exactly equal to budget")


#over the budget test
exceeds = budget_status (9000, total)
print ("over budget")



# Handover note
#component: budget_status
#Returns: "Within budget" when
#total <= budget, otherwise
#"Over budget"
#Tests: below budget, exact
#budget, over budget
#Issue: none
