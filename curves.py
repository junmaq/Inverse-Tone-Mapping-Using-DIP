import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


#text_file = open("dorfCurves.txt", "r")
#lines = text_file.readlines()
#
#for i in range(201):
#    line=lines[3+i*6].split('  ')
#    I=[float(l) for l in line]
#    np.save("curves/I_%0.3d"%i,np.array(I))
#    line=lines[5+i*6].split('  ')
#    B=[float(l) for l in line]    
#    np.save("curves/B_%0.3d"%i,np.array(B))    
#    
#text_file.close()

def func(x,gamma):
    return x**gamma
sel=[8,9,168,167]
Gammas_sel=[]
for i in sel:
    I=np.load("curves/I_%0.3d.npy"%i)
    B=np.load("curves/B_%0.3d.npy"%i)
    popt, pcov = curve_fit(func, I[1:], B[1:])
    Gammas_sel.append(popt[0])
    print(np.sqrt(np.sum((B-func(I,popt[0]))**2)/len(B)))

#np.save("gammas_sel.npy",np.array(Gammas))
#
#plt.figure()
#for i in range(201):
#    I=np.load("curves/I_%0.3d.npy"%i)  
#    B=np.load("curves/B_%0.3d.npy"%i)    
#    if i not in sel:
#        plt.plot(I,B,'lightsteelblue')
#for i in sel:
#    I=np.load("curves/I_%0.3d.npy"%i)  
#    B=np.load("curves/B_%0.3d.npy"%i)    
#    
#    plt.plot(I,B,'navy')
#
#plt.show()

plt.figure()
#for i in range(201):
for j,i in enumerate(sel):
    I=np.load("curves/I_%0.3d.npy"%i)    
    B=np.load("curves/B_%0.3d.npy"%i)    
    B_=func(I,Gammas_sel[j])
    if i in sel:
        plt.plot(I,B_,'r')
#    else:
        plt.plot(I,B,'b')

plt.show()


