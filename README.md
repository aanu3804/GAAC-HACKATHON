# 
## Problem Statement
**Probabilistic Data Structure for Real-Time Event Tracking**<br />
Design a probabilistic data structure that tracks the frequency of millions of real-time events with minimal memory and supports accurate percentile queries.<br />
Constraints:
- Achieve sub-linear space complexity while maintaining a low error margin.
- Support mergeable properties for distributed environments.




## **Solution Overview**

Our approach involves designing a memory-efficient probabilistic data structure that can:  
1. Track the frequency of millions of real-time events with sub-linear memory usage.  
2. Provide percentile-based insights, such as median or 90th percentile queries, with high accuracy.  
3. Operate seamlessly in distributed systems by supporting mergeable properties.

### **Core Idea**  
We utilize **count-min sketches** or **approximate quantile algorithms** to store frequency data compactly. These data structures maintain an acceptable error margin while requiring significantly less memory than traditional solutions.  
By merging multiple instances of the structure, we enable scalable tracking across distributed nodes, addressing real-world constraints in handling large-scale event data.

---

## **Tech Stack**

- **Python**: Core programming language for implementing the algorithm.  
- **NumPy**: For efficient numerical operations and array management.  
- **Flask/FastAPI**: To expose the solution as a REST API for real-time data ingestion and querying.  
- **Docker**: For containerizing the application and ensuring portability across environments.  
- **AWS Lambda**: For scalable and serverless deployment.  
- **GitHub Actions**: To automate testing and CI/CD pipelines.

### **Why These Technologies?**  
- **Python** provides a rich ecosystem for numerical and algorithmic development.  
- **NumPy** ensures computational efficiency for large datasets.  
- **Flask** simplifies exposing functionalities as APIs, enabling integrations with other systems.  


---

## **Implementation Plan**

### **Phase 1: Research and Design**  
- Study probabilistic data structures like count-min sketches and quantile summaries.  
- Define key performance metrics (error margin, mergeability, etc.).


### **Phase 2: Core Algorithm Implementation**

In this phase, we implemented two key algorithms to ensure memory-efficient event tracking and accurate percentile queries:

1. **Count-Min Sketch (CMS)**:  
   - A probabilistic data structure used to estimate the frequency of events with sub-linear memory requirements.  
   - Provides high accuracy with configurable error margins.

2. **Approximate Quantile Algorithm**:  
   - Tracks approximate ranks and percentiles of events.  
   - Facilitates insights such as medians and other percentile-based queries.  

These algorithms form the backbone of our solution, ensuring scalability and efficiency in handling real-time event data



### **Phase 3: Testing and Optimization**  
- Conduct rigorous testing with synthetic and real-world event datasets.  
- Optimize memory and response times for large-scale scenarios.  



---

## **Expected Outcome**

By the end of this project, we aim to achieve:  
- A highly memory-efficient data structure capable of tracking real-time events.  
- Accurate percentile queries (e.g., medians) with minimal computation overhead.  
- A scalable solution suitable for distributed environments.  
- Real-world applicability in scenarios like analytics, telemetry, and monitoring systems.  

**Potential Benefits:**  
- Reduced infrastructure costs due to sub-linear memory requirements.  
- Faster insights into event frequency trends, aiding in decision-making.  
- Seamless integration into existing systems via RESTful APIs.




### **Challenges**

While developing this solution, we anticipate the following challenges and have outlined strategies to tackle them:

#### **1. Memory Efficiency and Error Margin**
- **Challenge**: Ensuring that the data structures, like Count-Min Sketch and Approximate Quantile, maintain low error margins while using minimal memory, especially when scaling up to millions of events.
- **Solution**: We will optimize the parameters of the data structures (e.g., width and depth for Count-Min Sketch) and perform extensive testing to tune these parameters for the best trade-off between memory usage and accuracy.

#### **2. Scalability in Distributed Systems**
- **Challenge**: Merging data structures from distributed nodes while ensuring that the overall solution scales efficiently and maintains accuracy.
- **Solution**: We will design mergeable data structures that can easily combine data from different sources. To manage scalability, we will use a distributed framework (e.g., Kafka, AWS Lambda) to ensure seamless merging and minimize communication overhead.

#### **3. Real-Time Data Processing**
- **Challenge**: Handling real-time event ingestion and query processing without introducing significant latency.
- **Solution**: We will implement efficient algorithms for real-time data processing and use techniques like batching and windowing to process events in manageable chunks.

#### **4. Integration with External Systems**
- **Challenge**: Integrating the solution with external systems, especially when handling different data formats and protocols.
- **Solution**: If APIs are implemented, we will standardize input/output formats (e.g., JSON) and provide clear documentation for integration with other systems.

#### **5. Testing with Large-Scale Datasets**
- **Challenge**: Testing the solution with large datasets that mimic real-world conditions can be difficult, particularly when dealing with millions of events.
- **Solution**: We will create synthetic datasets for testing and use cloud services to simulate large-scale data environments. Performance testing tools will be used to assess the system’s efficiency.


