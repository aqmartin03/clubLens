# For lie, the options (in the drop-down menu) should be 'tee, fairway, rough, bunker, and green'.
from analysis import read_dictionary, count_clubs_used, count_miss_directions, calculate_distance_progress, performance_summary, count_major_misses, count_penalties
from sample_data import shot_data

def main():
    # sample_shots = read_dictionary()
    # print(sample_shots)
    # print()
    # club_counts = count_clubs_used()
    # print(club_counts)
    # print()
    # misses = count_miss_directions()
    # print(misses)
    # print()
    # progress = calculate_distance_progress()
    # print(progress)
    print("Here is the performance summary of your round, sorted by club:")
    performance = performance_summary()



if __name__ == '__main__':
    main()