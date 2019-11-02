import argparse
import pandas as pd
import matplotlib.pyplot as plt
import os

def main():
    # fig, axes = plt.subplots(2, 2, figsize=(8, 8))
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", dest="file", help="input data file")

    args = parser.parse_args()
    file = args.file

    diabetes = pd.read_csv(filepath_or_buffer=file, sep=' ', header=0)
    print(diabetes)
    diabetes_df = pd.DataFrame(data=diabetes)


    plt.plot(diabetes_df['age'])
    plt.title('age deviation by index')
    plt.xlabel('index')
    plt.ylabel('age deviation')
    plt.show()

    plt.scatter(diabetes_df['age'], diabetes_df['bmi'])
    plt.title('age and bmi')
    plt.xlabel('age')
    plt.ylabel('bmi')
    plt.show()

    # print(diabetes_df.info())
    #
    # axes[0][0].scatter(diabetes_df['age'], diabetes_df['bmi'])
    # axes[0][1].scatter(diabetes_df['glu'], diabetes_df['y'])
    # print(axes)

    # plt.scatter([diabetes_df['age'], diabetes_df['bmi']], [(diabetes_df['tc'], diabetes_df['ldl'])])

    plt.scatter(diabetes_df['age'], diabetes_df['bmi'], color='b')
    plt.scatter(diabetes_df['tc'], diabetes_df['ldl'], color='r')
    plt.show()








if __name__ == "__main__":
    main()