from sample_data import shot_data

# Iterate through the sample_data shots

def read_dictionary():
    """
    This function prints the list of data found in sample_data.py
    """
    shots = shot_data()
    for shot in shots:
        print(f"Hole: {shot["hole"]}; Club Used: {shot["club"]}; Starting Yardage: {shot["starting_yardage"]}; Current Lie: {shot["current_lie"]}; Ending Yardage: {shot["ending_yardage"]}; Ending Lie: {shot["ending_lie"]}; Missed Direction (from hole): {shot["miss_direction"]}; Miss Severity: {shot["miss_direction"]}; Penalty: {shot["penalty"]}")


def count_clubs_used(shots):
    """
    This function counts the number of times each club is used, and it returns each club's total usage value.
    """
    club_counts = {}
    for shot in shots:
        club = shot["club"]
        if club in club_counts:
            club_counts[club] += 1
        else:
            club_counts[club] = 1
    return club_counts

def count_miss_directions(shots):
    """
    This function determines which direction each shot goes relative to the hole, sorted by the club type.
    """
    club_misses = {}
    for shot in shots:
        club = shot["club"]
        direction = shot["miss_direction"]
        if club not in club_misses:
            club_misses[club] = {}

        if direction in club_misses[club]:
            club_misses[club][direction] += 1
        else:
            club_misses[club][direction] = 1
    return club_misses

def calculate_distance_progress():
    """
    Calculate the percentage of the original distance to the hole removed by each shot.
    """
    shots = shot_data()
    for shot in shots:
        club = shot["club"]
        starting_yardage = shot["starting_yardage"]
        ending_yardage = shot["ending_yardage"]
        distance_removed = starting_yardage - ending_yardage
        percentage_removed = (distance_removed / starting_yardage) * 100
        print(f"{club}: {starting_yardage} -> {ending_yardage} | {percentage_removed:.2f}%")

def count_major_misses(shots):
    # Determines how many shots were Moderate/Severe
    major_misses = {}
    for shot in shots:
        club = shot["club"]
        severity = shot["miss_severity"]
        if severity == "moderate" or severity == "severe":
            if club not in major_misses:
                major_misses[club] = 1
            else:
                major_misses[club] += 1
    return major_misses

def count_penalties(shots):
    # Determines how many shots had penalties
    p = {}
    for shot in shots:
        club = shot["club"]
        penalty = shot["penalty"]
        if penalty == True:
            if club not in p:
                p[club] = 1
            else:
                p[club] += 1
    return p

def performance_summary(shots):
    """
    Summarize the performance of the player's shot data, sorted by club.
    """
    club_stats = {}

    counts = count_clubs_used(shots)
    misses = count_miss_directions(shots)
    major_misses = count_major_misses(shots)
    penalties = count_penalties(shots)
    for club in counts:
        club_stats[club] = {}
        club_stats[club]["shots"] = counts[club]
        club_stats[club]["major_misses"] = major_misses.get(club, 0)
        club_stats[club]["penalties"] = penalties.get(club, 0)
        club_stats[club]["Left"] = misses[club].get("Left", 0)
        club_stats[club]["Right"] = misses[club].get("Right", 0)
        club_stats[club]["Straight"] = misses[club].get("Straight", 0)
        # Prints the club
        # print()
        # print(club)
        # print("-----------------")
        # print(f"Shots: {counts[club]}")
        # print(f"Left: {misses[club].get("Left", 0)}")
        # print(f"Right: {misses[club].get("Right", 0)}")
        # print(f"Straight: {misses[club].get("Straight", 0)}")
        # print(f"Moderate/Severe Misses: {major_misses.get(club, 0)}")
        # print(f"Penalties: {penalties.get(club, 0)}")
        major_miss_rate = (major_misses.get(club, 0) / counts[club]) * 100
        # print(f"Major Miss Rate: {major_miss_rate:.2f}%")
        club_stats[club]["major_miss_rate"] = major_miss_rate
    return club_stats

def practice_recommendation(shots):
    club_counts = {}
    major_misses = {}
    misses = count_miss_directions(shots)
    for shot in shots:
        club = shot["club"]
        if club in club_counts:
            club_counts[club] += 1
        else:
            club_counts[club] = 1

        if shot["miss_severity"] == "moderate" or shot["miss_severity"] == "severe":
            if club in major_misses:
                major_misses[club] += 1
            else:
                major_misses[club] = 1

    worst_club = None
    highest_miss_rate = 0

    for club, count in club_counts.items():
        if club == "Putter":
            continue
        if count >= 5:
            miss_count = major_misses.get(club, 0)
            major_miss_rate = (miss_count / count) * 100

            if major_miss_rate > highest_miss_rate:
                highest_miss_rate = major_miss_rate
                worst_club = club

        #     print(f"{club}: {major_miss_rate:.2f}%")
        # else:
        #     print(f"{club}: not enough data")

    if worst_club is not None:
        club_directions = misses[worst_club]
        left_count = club_directions.get("Left", 0)
        right_count = club_directions.get("Right", 0)

        if left_count > right_count:
            tendency = "Left"
        elif left_count < right_count:
            tendency = "Right"
        else:
            tendency = "No dominant direction"
    if worst_club is None:
        # print("No practice priority identified from the available data.")
        return None
    else:
        return {
            "club": worst_club,
            "major_miss_rate": highest_miss_rate,
            "miss_direction": tendency
        }
        # print(f"Practice priority: {worst_club}")
        # print(f"Major miss rate {highest_miss_rate:.2f}")
        # print(f"Most common miss direction: {tendency}")