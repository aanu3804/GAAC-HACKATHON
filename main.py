import hashlib
import numpy as np
import random

class CountMinSketch:
    def __init__(self, width, depth):
        self.width = width
        self.depth = depth
   
        self.table = np.zeros((depth, width), dtype=int)
        self.total_count = 0  # Track total events

    def hash(self, item, i):
        return int(hashlib.md5(f"{item}{i}".encode('utf-8')).hexdigest(), 16) % self.width

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

# Main function to demonstrate functionality
if __name__ == "__main__":

    cms1 = CountMinSketch(width=10000, depth=10)  # Larger width for reduced error margin
    cms2 = CountMinSketch(width=10000, depth=10)

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
    print(f"Error Margin: ±{error_margin:.2f}")

    frequencies = sorted(event_frequencies.values())
    percentile_90 = calculate_percentile(90, frequencies)
    median = calculate_percentile(50, frequencies)

    print(f"90th Percentile Frequency: {percentile_90}")
    print(f"Median Frequency: {median}")
