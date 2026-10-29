from event_total import total
from budget_status import status


def event_summary(total, status, event_name):
        return f"{event_name}: total {total} naira, {status}."

print(event_summary(total, status, "Study day"))

print(event_summary(total, status, "Group Two"))

# Hand over note
#component: event_summary
#Returns: 'final output string'
#test: main test, different event name  "
#Issue: 'none'