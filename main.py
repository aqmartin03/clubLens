# For lie, the options (in the drop-down menu) should be 'tee, fairway, rough, bunker, and green'.
from analysis import read_dictionary, count_clubs_used, count_miss_directions, calculate_distance_progress, performance_summary, count_major_misses, count_penalties, practice_recommendation
from sample_data import shot_data
from database import create_tables, add_round, get_rounds, add_shot, get_shots, get_all_shots, clear_test_data

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
    # round_id = add_round(
    #     "2026-10-07",
    #     "Eaglecrest National Golf Club"
    # )
    # add_shot (round_id, 1, "Driver", 390, "tee", 105,"rough", "Left", "moderate", False)
    # add_shot (round_id, 2, "7 Iron", 160, "tee", 30, "fairway","Straight", "minor", False)
    # add_shot (round_id, 5, "Pitching Wedge", 122, "fairway", 10, "green","Left", "on-target",  False)
    # add_shot (round_id, 5, "Putter", 10, "green", 2, "green","Right", "minor", False)
    # add_shot (round_id, 5, "Putter", 2, "green", 0, "hole","In", "on-target", False)

    # round_id = add_round(
    #     "2026-10-08",
    #     "Eaglecrest National Golf Club"
    # )
    # add_shot(round_id, 1, "Driver", 405, "tee", 145, "fairway", "Straight", "minor", False)
    # add_shot(round_id, 1, "7 Iron", 145, "fairway", 18, "green", "Left", "minor", False)
    # add_shot(round_id, 1, "Putter", 18, "green", 3, "green", "Right", "minor", False)
    # add_shot(round_id, 1, "Putter", 3, "green", 0, "hole", "In", "on-target", False)
    # add_shot(round_id, 2, "Driver", 380, "tee", 120, "rough", "Left", "moderate", False)
    # add_shot(round_id, 2, "Pitching Wedge", 120, "rough", 12, "green", "Straight", "on-target", False)
    # add_shot(round_id, 2, "Putter", 12, "green", 0, "hole", "In", "on-target", False)

    # round_id = add_round(
    #     "2026-10-10",
    #     "Eaglecrest National Golf Club"
    # )
    # add_shot(round_id, 1, "Driver", 420, "tee", 165, "rough", "Right", "minor", False)
    # add_shot(round_id, 1, "7 Iron", 165, "rough", 25, "green", "Straight", "minor", False)
    # add_shot(round_id, 1, "Putter", 25, "green", 5, "green", "Left", "moderate", False)
    # add_shot(round_id, 1, "Putter", 5, "green", 0, "hole", "In", "on-target", False)
    # add_shot(round_id, 2, "Driver", 395, "tee", 135, "rough", "Left", "severe", True)
    # add_shot(round_id, 2, "9 Iron", 135, "rough", 15, "green", "Right", "minor", False)
    # add_shot(round_id, 2, "Putter", 15, "green", 2, "green", "Straight", "minor", False)
    # add_shot(round_id, 2, "Putter", 2, "green", 0, "hole", "In", "on-target", False)


    # round_id = add_round(
    #     "2026-10-12",
    #     "Eaglecrest National Golf Club"
    # )
    # add_shot(round_id, 1, "Driver", 400, "tee", 130, "fairway", "Straight", "on-target", False)
    # add_shot(round_id, 1, "Pitching Wedge", 130, "fairway", 8, "green", "Straight", "on-target", False)
    # add_shot(round_id, 1, "Putter", 8, "green", 0, "hole", "In", "on-target", False)
    # add_shot(round_id, 2, "Driver", 430, "tee", 175, "rough", "Left", "moderate", False)
    # add_shot(round_id, 2, "7 Iron", 175, "rough", 35, "rough", "Left", "moderate", False)
    # add_shot(round_id, 2, "Pitching Wedge", 35, "rough", 6, "green", "Straight", "on-target", False)
    # add_shot(round_id, 2, "Putter", 6, "green", 0, "hole", "In", "on-target", False)


    # round_id = add_round(
    #     "2026-10-14",
    #     "Eaglecrest National Golf Club"
    # )
    # add_shot(round_id, 1, "Driver", 410, "tee", 155, "rough", "Left", "minor", False)
    # add_shot(round_id, 1, "7 Iron", 155, "rough", 20, "green", "Right", "minor", False)
    # add_shot(round_id, 1, "Putter", 20, "green", 4, "green", "Right", "minor", False)
    # add_shot(round_id, 1, "Putter", 4, "green", 0, "hole", "In", "on-target", False)
    # add_shot(round_id, 2, "Driver", 390, "tee", 115, "fairway", "Straight", "on-target", False)
    # add_shot(round_id, 2, "Pitching Wedge", 115, "fairway", 22, "rough", "Right", "severe", False)
    # add_shot(round_id, 2, "Pitching Wedge", 22, "rough", 5, "green", "Straight", "on-target", False)
    # add_shot(round_id, 2, "Putter", 5, "green", 0, "hole", "In", "on-target", False)

    # print(f"New round ID: {round_id}")
    shots = get_all_shots()
    performance_summary(shots)
    # clear_test_data()
    recommendation = practice_recommendation(shots)
    print(recommendation)

if __name__ == '__main__':
    main()