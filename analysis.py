import os
import requests
import csv
import datetime
import matplotlib.pyplot as plt

buckets = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

if not os.path.isfile('data.csv'):
    print('Downloading data...')
    try:
        data = requests.get('https://coronavirus.data.gov.uk/downloads/csv/coronavirus-cases_latest.csv')
    except Exception as e:
        print('Failed to retrieve data:')
        print(e)
        exit(1)
    with open('data.csv', 'w') as f:
        f.write(data.text)

# Parse and bucket the data
print('Analysing data...')
with open('data.csv') as f:
    data = csv.reader(f)
    lastUpdated = '0'
    for row in data:
        if row[2] == 'ltla':
            firstDigit = int(str(row[4])[0])
            buckets[firstDigit] = buckets[firstDigit] + 1
        if row[3] != 'Specimen date':
            lastUpdated = max(lastUpdated, row[3])

# Ignore 0s
buckets = buckets[1:]

# Get percentages
total = sum(buckets)
for i in range(0, len(buckets)):
    buckets[i] = 100 * buckets[i] / total

# Plot
print('Plotting data...')
fig, ax = plt.subplots()
ax.plot(range(1, 10), buckets, label = 'COVID stats')
ax.plot(range(1, 10), [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6], label = 'Benford\'s law')
ax.set(xlabel = 'First digit', ylabel = 'Frequency (%)', title = 'UK COVID statistics follow Benford\'s law (as of ' + datetime.date.today().isoformat() + ')')
plt.legend()
if os.environ.get('CI') == 'true' or os.environ.get('HEADLESS') == 'true':
    plt.savefig('output.png')
else:
    plt.show()
