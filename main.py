# For lie, the options (in the drop-down menu) should be 'tee, fairway, rough, bunker, and green'.
from analysis import read_dictionary, count_clubs_used, count_miss_directions, calculate_distance_progress, performance_summary, count_major_misses, count_penalties
from sample_data import shot_data
from database import create_tables, add_round, get_rounds, add_shot, get_shots

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
    # print("Here is the performance summary of your round, sorted by club:")
    # performance = performance_summary()
    # create_tables()
    # rounds = get_rounds()
    # for golf_round in rounds:
    #     print(golf_round)
    # add_round("2026-10-04", "Test Golf Course")
    # add_shot(
    #     1,
    #     1,
    #     "Driver",
    #     390,
    #     "Tee",
    #     105,
    #     "Fairway",
    #     "Left",
    #     "moderate",
    #     False
    # )
    # shots = get_shots(1)
    # for shot in shots:
    #     print(shot["club"], shot["miss_severity"], shot["penalty"])
    # performance_summary(shots)
    round_id = add_round(
        "2026-10-07",
        "Eaglecrest National Golf Club"
    )
    add_shot (
        round_id,
        1, 
        "Driver", 
        390, 
        "tee", 
        105,
        "rough", 
        "Left", 
        "moderate", 
        False
    )
    add_shot (
        round_id,
        2, 
        "7 Iron", 
        160, 
        "tee", 
        30, 
        "fairway",
        "Straight", 
        "minor", 
        False
    )
    add_shot (
        round_id,
        5, 
        "Pitching Wedge", 
        122, 
        "fairway", 
        10, 
        "green",
        "Left", 
        "on-target", 
         False
    )
    add_shot (
        round_id,
        5, 
        "Putter", 
        10, 
        "green", 
        2, 
        "green",
        "Right", 
        "minor", 
        False
    )
    add_shot (
        round_id,
        5, 
        "Putter", 
        2, 
        "green", 
        0, 
        "hole",
        "In", 
        "on-target", 
        False
    )
    print(f"New round ID: {round_id}")
    shots = get_shots(round_id)
    performance_summary(shots)


if __name__ == '__main__':
    main()