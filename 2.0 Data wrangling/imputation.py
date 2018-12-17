import pandas
import numpy


def imputation(filename):
    # Pandas dataframes have a method called 'fillna(value)', such that you can
    # pass in a single value to replace any NAs in a dataframe or series. You
    # can call it like this:
    #     dataframe['column'] = dataframe['column'].fillna(value)
    #
    # Using the numpy.mean function, which calculates the mean of a numpy
    # array, impute any missing values in our Lahman baseball
    # data sets 'weight' column by setting them equal to the average weight.
    #
    # You can access the 'weight' colum in the baseball data frame by
    # calling baseball['weight']

    baseball = pandas.read_csv(filename)

    # YOUR CODE GOES HERE

    baseball['weight'] = baseball['weight'].fillna(numpy.mean(baseball['weight']))

    return baseball


if __name__ == "__main__":
    # Path to CSV
    path_to_csv = "Master.csv"

    # Données brutes
    df = pandas.read_csv(path_to_csv)
    print(df.describe())

    # Données compéltées
    imputed_df = imputation(path_to_csv)
    print(imputed_df.describe())