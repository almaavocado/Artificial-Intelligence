import random

# ------ Part A ---------
print("\nPart A. The sampling probabilities\n")
print("P(C|-s, r) = < 0.8780, 0.1220 >")
print("P(C|-s, -r) = < 0.3103, 0.6897 >")
print("P(R|c, -s, w) = < 0.9863, 0.0137 >")
print("P(R|-c, -s, w) = < 0.8182, 0.1818 >\n")

# ------ Part B ---------
print("Part B. The transition probability matrix\n")
print("\tS1    \tS2   \tS3     \tS4\n")
print("S1\t0.932\t0.007 \t 0.061 \t0\t\n")
print("S2\t0.493 \t0.162 \t 0 \t0.345 \t\n")
print("S3\t0.439 \t0\t0.47 \t0.091 \t\n")
print("S4\t0\t0.155 \t 0.409 \t0.436 \t\n")

# ------ Part C ---------
'''
Possible states from diagram given:

S1 : c = true, r = true, s = false, w = true
s2 : c = true, r = false, s = false, w = true
s3 : c = false, r = true, s = false, w = true
s4 : c = false, r = false, s = false, w = true

We're showing the probablility of P(C|-s, w)

alpha * P(C) * P(-s|C) * P(w|-s)

initialize -s, w as state so (0, 1)
'''
sample = 1000000

state = 3

# part B answers
transitionProbabilities = [[0.932, 0.007, 0.061, 0],
                           [0.493, 0.162, 0, 0.345],
                           [0.439, 0, 0.47, 0.091],
                           [0, 0.155, 0.409, 0.436]]

s1 = [1, 1]
s2 = [1, 0]
s3 = [0, 1]
s4 = [0, 0]

state1 = 0
state2 = 0
state3 = 0
state4 = 0

tempState = 0
randomState = random.randint(1, 4)
if randomState == 1:
    # we are in state1 so set our temp to state1
    tempState = s1
    # we also increment the state count
    state1 += 1
elif randomState == 2:
    # we are in state2 so set our temp to state2
    tempState = s2
    state2 += 1
elif randomState == 3:
    # we are in state3 so set our temp to state3
    tempState = s3
    state3 += 1
elif randomState == 4:
    # we are in state4 so set our temp to state4
    tempState = s4
    state4 += 1


# P(Cloudy=true)
cloudyTrue = 0
# P(Cloudy=false)
cloudyFalse = 0
count = 0

for i in range(sample):
    randomValue = random.uniform(0, 1)
    probability = 0

    for value in range(0, 4):

        probability += transitionProbabilities[state][value]

        # If cloudyTrue increments then P(Cloudy=true), if cloudyFalse increments then P(Cloudy=false)
        if randomValue < probability:
            if value <= 1:
                cloudyTrue += 1
                count += 1
            else:
                cloudyFalse += 1
                count += 1
            state = value
            break

cloudy = (cloudyTrue / count)
notCloudy = (cloudyFalse / count)

cloudy = "{0:.4f}".format(cloudy)
notCloudy = "{0:.4f}".format(notCloudy)

print("\nPart C. The probability for the query\n")
print("P(C|-s, w) = <", cloudy, ",", notCloudy, ">")




