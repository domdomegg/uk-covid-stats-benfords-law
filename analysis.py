import json
import matplotlib.pyplot as plt

buckets = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Parse and bucket the data
with open('data.json') as f:
    data = json.loads(f.read())
    for ltla in data['ltlas']:
        firstDigit = int(str(ltla['dailyLabConfirmedCases'])[0])
        buckets[firstDigit] = buckets[firstDigit] + 1
    lastUpdated = data['metadata']['lastUpdatedAt']

# Ignore 0s
buckets = buckets[1:]

# Get percentages
total = sum(buckets)
for i in range(0, len(buckets)):
    buckets[i] = 100 * buckets[i] / total

# Plot
fig, ax = plt.subplots()
ax.plot(range(1, 10), buckets, label = 'COVID stats')
ax.plot(range(1, 10), [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6], label = 'Benford\'s law')
ax.set(xlabel = 'First digit', ylabel = 'Frequency (%)', title = 'UK COVID statistics follow Benford\'s law (as of ' + lastUpdated[0:10] + ')')
plt.legend()
plt.show()