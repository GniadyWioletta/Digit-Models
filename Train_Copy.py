import numpy as np
import warnings
import pickle
from Saving_GMM_Models import Save_Model
from python_speech_features import mfcc, delta
import scipy.io.wavfile as wav
import shutil
import pathlib
import os
import eval

warnings.filterwarnings('ignore')

class Parameters(object):

    def __init__(self, if_d, winstep, winlen, nfilt, nfft, ceplifter, N, components, max_iter, random_state):
        self.if_d = if_d #Delta. Default is "" /"", "Delta", "DeltaDelta"

        self.winstep = winstep #the step between successive windows in seconds. Default is 0.01s (10 milliseconds)
        self.winlen = winlen #the length of the analysis window in seconds. Default is 0.025s (25 milliseconds)
        self.nfilt = nfilt #the number of filters in the filterbank, default 26.
        self.nfft = nfft #the FFT size. Default is 512.
        self.ceplifter = ceplifter #apply a lifter to final cepstral coefficients. 0 is no lifter. Default is 22.

        self.components = components
        self.max_iter = max_iter #The number of EM iterations to perform. Default is 100
        self.random_state = random_state #If int, random_state is the seed used by the random number generator;
        # If RandomState instance, random_state is the random number generator;
        # If None, the random number generator is the RandomState instance used by np.random.

def MFCC_eval(file,par):
        (rate, sig) = wav.read(file)
        mfcc_f = mfcc(sig, rate, appendEnergy=False, winstep=par.winstep, winlen=par.winlen,
                      nfilt=par.nfilt, nfft=par.nfft, ceplifter=par.ceplifter)
        if par.if_d == "Delta":
            mfcc_output = delta(mfcc_f, 1)  # delta
        elif par.if_d == "DeltaDelta":
            mfcc_output = delta(mfcc_f, 2)  # deltadelta
        else:
            mfcc_output = mfcc_f

        return mfcc_output

def OpenFile(type, num, index=None):
    if type=="train":
        with open('GMM_Models_temp/GMM_%s.pkl' %(num), 'rb') as file:  #wczytanie
            data = pickle.load(file)
    elif type=="test":
        with open('eval/.pkl' %(num,index), 'rb') as file:  #wczytanie
            data = pickle.load(file)
    return data

def WhatClassIsThat(prob):
    max = np.max(prob)
    index_max = np.argmax(prob)
    return max, index_max

def Likelihood(clasificator, data):
    lh = clasificator.score(data)
    return lh

def Probability_Bayes(lh_x_ci, pc):
    norm = 0 # -> normalization
    for lh in range(0,len(lh_x_ci)): #lh_x_ci -> likelihood
        lh_x_ci[lh] = np.exp(lh_x_ci[lh])
        norm += pc * lh_x_ci[lh]
    p_c_x = []
    for lh in lh_x_ci:
        x = lh*pc/ norm
        p_c_x = np.append(p_c_x, x) #probability gor each class
    return p_c_x

def main():
    series_nr = 1 # series_nr is a nr of the line of test_series.txt file
    parameters = Parameters("", 0.03, 0.01, 26, 512, 22, 2, 8, 100, None)  # Default
    Save_Model(parameters, series_nr)

    files_test_load = []
    files_test = os.listdir("eval/")
    for f in range(len(files_test)):
        files_test_load.append("eval/" + files_test[f])

    list =[]
    import csv

    it = 0
    for file in files_test_load: #Number of numbers
        mfcc_speaker= MFCC_eval(file, parameters)
        lh_x_ci = []
        for i in range(0,10): #Number of classificators
             lh_x_ci = np.append(lh_x_ci, Likelihood((OpenFile("train",i)), mfcc_speaker))

        #Bayes Probability for each Speaker of each number
        pc = 1/len(lh_x_ci)
        [perc, numb]= WhatClassIsThat(Probability_Bayes(lh_x_ci, pc))

        list.append((files_test[it], numb))
        it = it+1


    with open('EVAL.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')

        for t in list:
            writer.writerow(t)

    eval.evaluate('EVAL.csv')

if __name__ == '__main__':
    main()
