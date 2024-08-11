import pandas as pd
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination

data = pd.read_csv('heart.csv')

print("First few rows of the dataset:")
print(data.head())
print("\nColumns in the dataset:")
print(data.columns)

model = BayesianNetwork([
    ('age', 'heartdisease'),
    ('gender', 'heartdisease'),
    ('family', 'heartdisease'),
    ('diet', 'heartdisease'),
    ('lifestyle', 'heartdisease'),
    ('cholestrol', 'heartdisease')
])

model.fit(data, estimator=MaximumLikelihoodEstimator)

infer = VariableElimination(model)

q1 = infer.query(variables=['heartdisease'], evidence={'cholestrol': 2})
print("\nQuery for 'heartdisease' given 'cholestrol=2':")
print(q1)

q2 = infer.query(variables=['heartdisease'], evidence={'diet': 1})
print("\nQuery for 'heartdisease' given 'diet=1':")
print(q2)

