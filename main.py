# For lie, the options (in the drop-down menu) should be 'tee, fairway, rough, bunker, and green'.
from analysis import read_dictionary, count_clubs_used
from sample_data import shot_data

def main():
    sample_shots = read_dictionary()
    print(sample_shots)
    print()



if __name__ == '__main__':
    main()