from python_speech_features import mfcc, delta
import scipy.io.wavfile as wav
import os


def MFCC(file, par):
    (rate, sig) = wav.read(file)
    mfcc_f = mfcc(sig, rate, appendEnergy=False, winstep=par.winstep, winlen=par.winlen,
                  nfilt=par.nfilt, nfft=par.nfft, ceplifter=par.ceplifter)
    if par.if_d == "Delta":
        mfcc_output = delta(mfcc_f, 1) #delta
    elif par.if_d == "DeltaDelta":
        mfcc_output = delta(delta(mfcc_f, 1), 1) #deltadelta
    else :
        mfcc_output = mfcc_f

    return mfcc_output


def Load_records(num, test_files, line=0):
    files = os.listdir("records/%s/" % (num)) #Gets the files  from given number
    speakers = []
    files_output = []
    i = 0
    with open('test_series.txt') as test: #Serie for a test
        for l in test:
            if i == line:
                speakers = l.strip().split(' ')
                break
            i = i+1

    for it in range(len(speakers)):
        speakers[it] = int(speakers[it])
    speakers.sort()

    if not test_files:
        for nr in range(len(files)):
            if nr not in speakers:
                files_output.append("records/%s/" % (num) + files[nr])
    else:
        for nr in range(len(files)):
            if nr in speakers:
                files_output.append("records/%s/" % (num) + files[nr])

#    print(files_output)
    return files_output
