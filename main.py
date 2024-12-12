import hashlib
import numpy as np
import random

# Count-Min Sketch class
class CountMinSketch:
    def __init__(self, width, depth):
        """
        Initialize a Count-Min Sketch with specified width and depth.

        - width: The width of the sketch (number of columns).
        - depth: The depth of the sketch (number of hash functions).
        """
        self.width = width
        self.depth = depth
        # Initialize the CMS table (2D array)
        self.table = np.zeros((depth, width), dtype=int)

    def hash(self, item, i):
        """
        Generate a hash for an item using a specific hash function (indexed by i).
        """
        return int(hashlib.md5(f"{item}{i}".encode('utf-8')).hexdigest(), 16) % self.width

    def add(self, item):
        """
        Add an item to the CMS table by hashing it and incrementing the corresponding cells.
        """
        for i in range(self.depth):
            # Compute hash and increment the corresponding counter in the table
            hash_value = self.hash(item, i)
            self.table[i][hash_value] += 1

    def estimate(self, item):
        """
        Estimate the frequency of an item in the CMS table.
        """
        estimates = []
        for i in range(self.depth):
            hash_value = self.hash(item, i)
            estimates.append(self.table[i][hash_value])

        # Return the minimum count (approximation)
        return min(estimates)

# Function to simulate event stream
def generate_random_events(num_events):
    events = []
    for _ in range(num_events):
        # Simulating random event generation
        events.append(random.choice(['login', 'logout', 'purchase', 'view', 'share', 'click']))
    return events

# Initialize CMS with width 1000 and depth 10
cms = CountMinSketch(width=1000, depth=10)

# Generate a million events (simulate an event stream)
events = generate_random_events(1000000)

# Add events to CMS
for event in events:
    cms.add(event)

# Get frequency estimates for each event
unique_events = set(events)
event_frequencies = {}
for event in unique_events:
    event_frequencies[event] = cms.estimate(event)

print("Estimated Event Frequencies:")
print(event_frequencies)

# Step 2: Calculate Percentiles (90th Percentile, Median)
# Get the frequencies of all events
frequencies = list(event_frequencies.values())

# Sort the frequencies to compute percentiles
frequencies.sort()

def calculate_percentile(percentile, data):
    """
    Calculate the specified percentile from sorted data.
    """
    index = int(np.ceil((percentile / 100) * len(data))) - 1
    return data[index]

# Calculate 90th percentile and median
percentile_90 = calculate_percentile(90, frequencies)
median = calculate_percentile(50, frequencies)

print(f"90th Percentile Frequency: {percentile_90}")
print(f"Median Frequency: {median}")
