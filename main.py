import numpy as np
import mmh3  # MurmurHash for independent hash functions
import random

class EnhancedCountMinSketch:
    def __init__(self, width, depth, seeds):
        self.width = width
        self.depth = depth
        self.seeds = seeds  # Independent seeds for MurmurHash
        self.table = np.zeros((depth, width), dtype=int)
        self.total_count = 0  # Track total events

    def hash(self, item, i):
        # Use MurmurHash with independent seeds
        return mmh3.hash(item, self.seeds[i]) % self.width

    def add(self, item):
        for i in range(self.depth):
            hash_value = self.hash(item, i)
            self.table[i][hash_value] += 1
        self.total_count += 1

    def estimate(self, item):
        estimates = [self.table[i][self.hash(item, i)] for i in range(self.depth)]
        return min(estimates)

    def merge(self, other):
        if self.width != other.width or self.depth != other.depth:
            raise ValueError("Dimensions of Count-Min Sketches must match for merging.")
        self.table += other.table
        self.total_count += other.total_count

    def calculate_error_margin(self):
        return self.total_count / self.width

def generate_random_events(num_events):
    events = []
    for _ in range(num_events):
        events.append(random.choice(['login', 'logout', 'purchase', 'view', 'share', 'click']))
    return events

def calculate_percentile(percentile, data):
    index = int(np.ceil((percentile / 100) * len(data))) - 1
    return data[index]

if __name__ == "__main__":
    seeds = [13, 29, 47, 59, 71, 89, 101, 113, 131, 151]  # Independent seeds
    cms1 = EnhancedCountMinSketch(width=10**8, depth=10, seeds=seeds)  # Increased width
    cms2 = EnhancedCountMinSketch(width=10**8, depth=10, seeds=seeds)

    events1 = generate_random_events(500000)
    events2 = generate_random_events(500000)

    for event in events1:
        cms1.add(event)

    for event in events2:
        cms2.add(event)

    cms1.merge(cms2)

    unique_events = set(events1 + events2)
    event_frequencies = {event: cms1.estimate(event) for event in unique_events}

    error_margin = cms1.calculate_error_margin()

    print("Estimated Event Frequencies:")
    print(event_frequencies)
    print(f"Error Margin: ±{error_margin:.2f}%")

    frequencies = sorted(event_frequencies.values())
    percentile_90 = calculate_percentile(90, frequencies)
    median = calculate_percentile(50, frequencies)

    print(f"90th Percentile Frequency: {percentile_90}")
    print(f"Median Frequency: {median}")
