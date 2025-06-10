import csv 

with open('reed.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=job_list[0].keys())
    writer.writeheader()
    writer.writerows(job_list)

print("CSV saved: reed.csv")