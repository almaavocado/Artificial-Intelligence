import sys

'''
Notes:
P(X_t|x_t-1) * P(x_t-1);
P(e_t|X_t) * P(X_t|x_t-1) * 
'''


def hmm(prob, length, evidenceVariables):
  b = float(prob[1])
  c = float(prob[2])
  d = float(prob[3])
  f = float(prob[4])

  if evidenceVariables[length-1] == 't':
    e = d

  else:
    e = (1 - d)

  #base case
  if len(evidenceVariables) == 0:
    a = [float(prob[0]), (1 - float(prob[0]))]


# method for filtering
def filtering(evidenceVariables, length, a, px_t, pe_t):
    # base case
    if length == 0:
        return a
    # recursive
    else:
        e = []
        if evidenceVariables[length - 1] == 't':
            e = pe_t.copy()
        else:
            e = [1 - pe_t[0], 1 - pe_t[1]]

        trueVar = [px_t[0], 1 - px_t[0]]
        falseVar = [px_t[1], 1 - px_t[1]]

        # for i in trueVar:
        # t = [i * evidenceVariables[0]]

        # for j in falseVar:
        # f = [i * evidenceVariables[1]]

        # use helper method for recursive case
        prob = hmmRecursiveHelperMethod(trueVar, falseVar, filtering(evidenceVariables, length - 1, a, px_t, pe_t))
        # print(prob)

        # take the unormalized value and normalize it
        unnormalizedValue = [x * y for x, y in zip(e, prob)]
        result = normalize(unnormalizedValue)
        return result


# hmm recursive helper method
def hmmRecursiveHelperMethod(trueList, falseList, eV):
    for i in trueList:
        true = [i * eV[0]]
        # print(true)
        # print(true)

    for j in falseList:
        false = [i * eV[1]]
        # print("f")
        # print(false)

    r = (true, false)

    t = [(i * eV[0]) for i in trueList]
    # print("t")
    # print(t)

    f = [(i * eV[1]) for i in falseList]
    # print("f")
    # print(f)
    ans = [x + y for x, y in zip(t, f)]
    # print(ans)

    return ans


# normalize method takes in the unormalized value
def normalize(unormalizedValue):
    # find alpha first
    alpha = 1 / (unormalizedValue[0] + unormalizedValue[1])
    # normalize the value
    normalizedValue = [i * alpha for i in unormalizedValue]
    return normalizedValue


# main method
def main():
    # https://stackoverflow.com/questions/16869467/command-line-arguments-reading-a-file
    # https://www.tutorialspoint.com/How-to-read-a-file-from-command-line-using-Python
    '''
    This doesn't work. What if we have 4 testcases of 5, 6, etc. And more evidence variables.. :(
      allVariables = []
      allVariables.append(contents)
      #print(allVariables)
      #line 1
      #prob variables first
      probVars = contents[0:5]
      #probVars.append(contents[1:5])
      #print(probVars)
      #evidence variables
      evidenceVars = contents[5:7]
      #evidenceVars.append(contents[5:7])
      #print(evidenceVars)
      #line2
      probVars2 = contents[7:12]
      #probVars2.append(contents[8:12])
      #print(probVars2)
      evidenceVars2 = contents[12:]
      #evidenceVars2.append(contents[12:])
      #print(evidenceVars2)

      #for eachItem in allVariables:
        #probVariables = hmmRecursive(allVariables[:5], allVariables[5:])
        #print(probVariables)

      one = hmmRecursive(probVars, evidenceVars)
      two = hmmRecursive(probVars2, evidenceVars2)

      print(one)
      print(two)
    '''
    with open(sys.argv[1], 'r') as prob:
        # print (contents)
        for commas in prob:
            prob = commas.replace("\n", "")
            prob = prob.split(",")
            # print("f")
            # print(prob)

            # P(X_t|x_t-1) * P(x_t-1)
            # P(e_t|X_t) * P(X_t|x_t-1)
            a = [float(prob[0]), 1 - float(prob[0])]
            px_t = [float(prob[1]), float(prob[2])]
            pe_t = [float(prob[3]), float(prob[4])]
            evidenceVariables = prob[5:]
            # find length of evidence variable
            length = len(evidenceVariables)

            # calculate test case probability
            testCase = filtering(evidenceVariables, length, a, px_t, pe_t)

            # print(testCase[0], testCase[1])
            # output looks good :)
            print("{0}--><{1:.4f},{2:.4f}>".format(prob, testCase[0], testCase[1]))


# call main
main()