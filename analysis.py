from sample_data import shot_data

# Iterate through the sample_data shots

def read_dictionary():
    """
    This function prints the list of data found in sample_data.py
    """
    shots = shot_data()
    for shot in shots:
        print(f"Hole: {shot["hole"]}; Club Used: {shot["club"]}; Starting Yardage: {shot["starting_yardage"]}; Current Lie: {shot["current_lie"]}; Ending Yardage: {shot["ending_yardage"]}; Missed Direction (from hole): {shot["miss_direction"]}; Miss Severity: {shot["miss_direction"]}; Penalty: {shot["penalty"]}")


def count_clubs_used():
    """
    This function counts the number of times each club is used, and it returns each club's total usage value.
    """
    club_counts = {}
    shots = shot_data()
    for shot in shots:
        club = shot["club"]
        if club in club_counts:
            club_counts[club] += 1
        else:
            club_counts[club] = 1
    return club_counts

def count_miss_directions():
    """
    This function determines which direction each shot goes relative to the hole, sorted by the club type.
    """
    shots = shot_data()
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

def count_major_misses():
    # Determines how many shots were Moderate/Severe
    shots = shot_data()
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

def count_penalties():
    # Determines how many shots had penalties
    shots = shot_data()
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

def performance_summary():
    """
    Summarize the performance of the player's shot data, sorted by club.
    """
    counts = count_clubs_used()
    misses = count_miss_directions()
    major_misses = count_major_misses()
    penalties = count_penalties()
    for club in counts:
        # Prints the club
        print()
        print(club)
        print("-----------------")
        print(f"Shots: {counts[club]}")
        print(f"Left: {misses[club].get("Left", 0)}")
        print(f"Right: {misses[club].get("Right", 0)}")
        print(f"Straight: {misses[club].get("Straight", 0)}")
        print(f"Moderate/Severe Misses: {major_misses.get(club, 0)}")
        print(f"Penalties: {penalties.get(club, 0)}")
        major_miss_rate = (major_misses.get(club, 0) / counts[club]) * 100
        print(f"Major Miss Rate: {major_miss_rate:.2f}%")