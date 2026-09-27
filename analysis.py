from sample_data import shot_data

# Iterate through the sample_data shots

def read_dictionary():
    shots = shot_data()
    for shot in shots:
        print(f"Hole: {shot["hole"]}; Club Used: {shot["club"]}; Starting Yardage: {shot["starting_yardage"]}; Current Lie: {shot["current_lie"]}; Ending Yardage: {shot["ending_yardage"]}; Missed Direction (from hole): {shot["miss_direction"]}; Penalty: {shot["penalty"]}")


def count_clubs_used():
    club_counts = {}
    shots = shot_data()
    for shot in shots:
        club = shot["club"]
        if club in club_counts:
            