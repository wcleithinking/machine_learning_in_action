from numpy import linalg as la
import numpy as np
import svdRec

myMat = np.mat(svdRec.loadExData3())
# U, Sigma, VT = la.svd(myMat)
# Sig2 = Sigma ** 2
# print(sum(Sig2)*0.9)
# print(sum(Sig2[:2]))

result = svdRec.recommend(myMat, 1, estMethod=svdRec.standEst)
print(result)
result = svdRec.recommend(myMat, 1, estMethod=svdRec.svdEst)
print(result)

svdRec.imgCompress(2)