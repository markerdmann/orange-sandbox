import orange
import orngEnsemble

training_data = orange.ExampleTable('training.tab')
print 'training data loaded'
forest = orngEnsemble.RandomForestLearner(examples=training_data, trees=100, name="forest")
print 'forest trained'

test_data = orange.ExampleTable('test.tab')
print 'test data loaded'

def b_dev(a, p):
    from math import log
    if p > 0.99:
        p = 0.99
    if p < 0.01:
        p = 0.01
    return -(a * log(p, 10) + (1 - a) * log((1-p), 10))

results = [b_dev(int(d.getclass().value), forest(d, orange.GetProbabilities)[1]) for d in test_data]
print sum(results)/len(results)