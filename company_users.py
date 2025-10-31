companies = {}

while True:
    line = input()
    if line == "End":
        break

    company, emp_id = line.split(" -> ")
    if company not in companies:
        companies[company] = {}
    
    if emp_id not in companies[company]:
        companies[company][emp_id] = None

for company, ids in companies.items():
    print(company)
    for emp_id in ids.keys():
        print(f"-- {emp_id}")
