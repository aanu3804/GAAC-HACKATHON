# Probabilistic Data Structure for Real-Time Event Tracking

## Problem Statement
Design a probabilistic data structure that tracks the frequency of millions of real-time events with minimal memory and supports accurate percentile queries.

### Constraints:
- Achieve sub-linear space complexity while maintaining a low error margin.
- Support mergeable properties for distributed environments.

---

## Solution Overview
Our approach involves designing a memory-efficient probabilistic data structure that can:

1. Track the frequency of millions of real-time events with sub-linear memory usage.
2. Provide percentile-based insights, such as median or 90th percentile queries, with high accuracy.
3. Operate seamlessly in distributed systems by supporting mergeable properties.

### Core Idea
We utilize **Count-Min Sketch (CMS)** to store frequency data compactly. These data structures maintain an acceptable error margin while requiring significantly less memory than traditional solutions. By merging multiple instances of the structure, we enable scalable tracking across distributed nodes, addressing real-world constraints in handling large-scale event data.

---

## Tech Stack

### **Language:**
- **Python**: Core programming language for implementing the algorithm.

### **Libraries:**
- **NumPy**: For efficient numerical operations and array management.
- **Random**: Used to simulate random event streams for testing the Count-Min Sketch.
- **Hashlib**: For generating unique and deterministic hash values for events.

### **Algorithm:**
- **Count-Min Sketch**: For efficient frequency estimation with sub-linear memory usage.
- **Percentile Calculation**: For obtaining insights like the median and 90th percentile.

---

## Implementation Plan

### **Phase 1: Research and Design**
- Resaerched about probabilistic data structures like Count-Min Sketch and quantile summaries

### **Phase 2: Core Algorithm Implementation**
1. **Count-Min Sketch (CMS):**
   - Selected Probabilistic data structure to estimate the frequency of events with sub-linear memory.
   - Configurable error margins to ensure high accuracy.

2. **Percentile Calculation:**
   - Algorithm to provide approximate percentile-based queries.
   - Ensures scalability for real-time systems.

### **Phase 3: Testing and Optimization**
- Conduct rigorous testing with synthetic and real-world datasets.
- Optimize memory and response times for large-scale scenarios.

---

## Expected Outcomes
- A highly memory-efficient data structure capable of tracking real-time events.
- Accurate percentile queries (e.g., medians) with minimal computation overhead.
- A scalable solution suitable for distributed environments.


---

## Challenges and Contingency Plan

### **1. Memory Efficiency and Error Margin**
- **Challenge:** Ensuring low error margins with minimal memory usage.
- **Solution:** Optimize CMS parameters (e.g., width, depth) to balance memory and accuracy.

### **2. Scalability in Distributed Systems**
- **Challenge:** Merging CMS instances from distributed nodes while maintaining accuracy.
- **Solution:** Design mergeable structures and use distributed frameworks (e.g., AWS Lambda) to minimize overhead.
---

## How to Run the Project

### **Prerequisites:**
- Python 3.7 or higher
- Install required libraries: `numpy`

```bash
pip install numpy
```
-Install required library : `mmh3`
```bash
pip install mmh3
```

### **Steps:**
1. Clone the repository:
   ```bash
   git clone https://github.com/aanu3804/GAAC-HACKATHON.git
   cd GAAC-HACKATHON
   ```
2. Run the script:
   ```bash
   python main.py
   ```
3. Observe outputs for estimated frequencies, error margins, and percentile queries.

---
**Code Was provided in main.py in this repository**
### *Sample Output*
![image](https://github.com/user-attachments/assets/6dce5838-a0c1-4dea-b868-bb18fa5ac2ec)

------------------------------------------------------------------- End Of the Document ---------------------------------------------------------------
