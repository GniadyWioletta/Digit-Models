import key_functions as key
from sklearn.mixture import GaussianMixture
import numpy as np
import warnings
import pickle

warnings.filterwarnings('ignore')


def Model_GMM(data, par):
    model = GaussianMixture(n_components=par.components, covariance_type='diag', max_iter=par.max_iter,
                            random_state=par.random_state ).fit(data)
    return model


def Making_files(num, par, series_nr):
    # files = os.listdir("train/%s/train/" %(num))
    # for f in range(len(files)):
    #     files[f] = "train/%s/train/" %(num)+ files[f]
    files = key.Load_records(num, False, series_nr)

    #Calculate MFCC parameters
    MFCC_num= key.MFCC(files[0], par)

    for f in range(1,len(files)):
         mfcc_p = key.MFCC(files[f], par)
         MFCC_num = np.concatenate((MFCC_num, mfcc_p), axis=0)

    #Model for given number
    model = Model_GMM(MFCC_num, par)

    with open('GMM_Models_temp/GMM_%s.pkl' %(num), 'wb') as file: #save
         pickle.dump(model, file)

def Save_Model(parameters, series_nr):
    for i in range(0,10):
        Making_files(i, parameters, series_nr)


#if __name__ == '__main__':
  #  main()




