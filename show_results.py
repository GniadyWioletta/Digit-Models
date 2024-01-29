import Training_Models as mn
import numpy as np

try_nr = 10
results = []
params = []
parameters = []

parameters.append(mn.Parameters("",0.02, 0.01, 26, 512, 22, 2, 8, 100, None))
parameters.append(mn.Parameters("",0.025, 0.005, 26, 512, 22, 2, 8, 100, None))
parameters.append(mn.Parameters("",0.02, 0.01, 26, 512, 12, 2, 8, 100, None))
parameters.append(mn.Parameters("",0.03, 0.01, 26, 512, 12, 2, 8, 100, None))
parameters.append(mn.Parameters("",0.022, 0.005, 26, 512, 12, 2, 8, 100, None))
parameters.append(mn.Parameters("",0.035, 0.01, 26, 512, 12, 2, 8, 100, None))
parameters.append(mn.Parameters("",0.02, 0.01, 26, 512, 16, 2, 8, 100, None))

it = 0
for P in parameters:
    results = []

    with open("results.txt", 'a') as file:
        file.write("\nFor params %s" %it + "\n")

    for i in range(20):
        res = []
        for j in range(try_nr):
            res.append(mn.main(P))

        mean = np.mean(res)
        std = np.std(res)

        res = [i, mean, std]
        results.append(res)
        with open("results.txt",'a') as file:
            writable = ""
            for k in range(len(res)):
                writable += str(res[k]) + "\t"
            file.write(writable + "\n")

        print(i, " series done")

    it = np.max(results, 1)
    string = ("The best record: " + str(it[0])+" "+str(it[1])+" "+str(it[2])+"\n")
    print(it, " params: ",string)
    with open("results.txt", 'a') as file:
        file.write(string)

    it = it+1
