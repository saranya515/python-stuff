import csv
import json
with open('datafile.csv', 'r') as f:
	reader = csv.DictReader(f)
	out = [obj for obj in reader]
with open("result3.json", "w") as f:
	f.write(json.dumps(out))