lst = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750 }]

result = {}
for el in lst:
    key = el['item']
    value = el['amount']
    if key in result:
        result[key] += value
    else:
        result[key] = value
print(result)
