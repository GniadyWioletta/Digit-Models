import our_functions as ours
import warnings
import pickle

warnings.filterwarnings('ignore')


def Files_list(num, par, series_nr):
    # files_test = os.listdir("train/%s/test/" %(num))
    # for f in range(len(files_test)):
    #     files_test[f] = "train/%s/test/" %(num)+ files_test[f]
    files_test = ours.Load_records(num, True, series_nr)

    #Gets he MFCC parameters for every digit 0-9
    for digit in range(0,len(files_test)):
        MFCC_num_test = ours.MFCC(files_test[digit], par)
        with open('MFCC_test_temp/MFCC_test_%s_%s.pkl' % (num, digit), 'wb') as file:  # save
            pickle.dump(MFCC_num_test, file)


def Save_Test(par, series_nr):
    for i in range(0,10):
        Files_list(i, par, series_nr)


#if __name__ == '__main__':
   # main()

