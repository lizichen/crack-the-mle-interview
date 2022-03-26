# ML Case Study Questions

Steps:
- Problem Statement
  - Clarify the requirement
  - Define the problem scope
  - Storage and Scalability 
- Metrics
  - Online metrics
  - Offline metrics
- Architectural Components
- Offline Model building and evaluation:
  - Training Data Generation  
  - Feature Engineering
  - Model training
  - Offline evaluation
- Online Experiment, Evaluation, and Debugging, Iterative improvement
  - Experiment Design

## Regression
*


## Classification
- Fraud Detection
  - Heuristic rules disadvantages: high false positives, easily out-dated, cannot scale. 
  - ML Features:
    - identity(suspicious email address), history, transaction, payment methods, location, network protocals, etc
  - Threshold - precision and recall
    - ROC:  x:False positives, y:True positives
      - True positives: how many fraudsters we block
      - False positives: how many good people we block
    - False negatives: how many fraudsters we allowed.

## Recommendation and Ranking
- Design Newsfeed Ranking
- Design Local Search Ranking
- Decide if an old post would be good for the 'On This Day' (Memories) feature.