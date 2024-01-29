import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import numpy as np
import warnings
import os

from python_speech_features import mfcc
from Gaussian_Mixtures.Gaussian import plot_gmm
from sklearn.mixture import GMM

warnings.filterwarnings('ignore')

def gmm_plotting(array_signal, num):
    mean_c1=[]
    mean_c2=[]
    mean_c =[]

    for signal in array_signal:
     (rate, sig) = wav.read(signal)
     mfcc_feat = mfcc(sig, rate, nfft=int(round(rate/25)))
     mean_c1.append(np.mean(mfcc_feat[:, 1]))
     mean_c2.append(np.mean(mfcc_feat[:, 2]))
     mean_c.append([np.mean(mfcc_feat[:, 1]), np.mean(mfcc_feat[:, 2])])

    gmm = GMM(n_components=4, covariance_type='diag', random_state=10000)
    plot_gmm(gmm, X=mean_c1, Y=mean_c2, All_coefs=mean_c)
    plt.title("Model of %s digit" %(num))
    plt.xlabel('c1')
    plt.ylabel('c2')

for num in range(0,1): #Narazie samo zero
    files = os.listdir("train/%s/train/" %(num))
    for f in range(len(files)):
        files[f] = "train/%s/train/" %(num)+ files[f]
        plt.figure(num)
        gmm_plotting(files[num], num)
        plt.show()
