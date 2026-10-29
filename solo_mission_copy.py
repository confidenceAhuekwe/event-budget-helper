def budget_remaining(budget, food, transport):
    
    return budget - food - transport
    


def budget_message(name, remaining):
   
    return [f"{name} has {remaining} naira remaining."]


balance = budget_remaining(15000, 9000, 2000)
print(balance)

result = budget_message("Mary", balance)
print(result)

