from numpy import *
import svdRec

myMat = mat(svdRec.loadExData())
test1 = svdRec.ecludSim(myMat[:,0], myMat[:,4])
test2 = svdRec.ecludSim(myMat[:,0], myMat[:,0])
print(test1, test2)
test1 = svdRec.cosSim(myMat[:,0], myMat[:,4])
test2 = svdRec.cosSim(myMat[:,0], myMat[:,0])
print(test1, test2)
test1 = svdRec.pearsSim(myMat[:,0], myMat[:,4])
test2 = svdRec.pearsSim(myMat[:,0], myMat[:,0])
print(test1, test2)

result = svdRec.recommend(myMat, 2)
print(result)
result = svdRec.recommend(myMat, 2, simMeans=svdRec.ecludSim)
print(result)
result = svdRec.recommend(myMat, 2, simMeans=svdRec.pearsSim)
print(result)