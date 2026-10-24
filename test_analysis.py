from analysis import practice_recommendation, performance_summary

def test_empty_data():
    shots = []

    recommendation = practice_recommendation(shots)
    stats = performance_summary(shots)

    assert recommendation is None
    assert stats == {}

    print("Empty data test passed")

def test_insufficient_shots():
    shots = [
        {"club": "Driver", "miss_severity": "severe", "miss_direction": "Left"},
        {"club": "Driver", "miss_severity": "moderate", "miss_direction": "Left"},
        {"club": "Driver", "miss_severity": "severe", "miss_direction": "Right"},
    ]

    recommendation = practice_recommendation(shots)
    assert recommendation is None
    print("Insufficient shots test passed")

def test_practice_priority():
    shots = [
        {"club": "Driver", "miss_severity": "severe", "miss_direction": "Left"},
        {"club": "Driver", "miss_severity": "moderate", "miss_direction": "Left"},
        {"club": "Driver", "miss_severity": "severe", "miss_direction": "Right"},
        {"club": "Driver", "miss_severity": "minor", "miss_direction": "Straight"},
        {"club": "Driver", "miss_severity": "on-target", "miss_direction": "Straight"},

        {"club": "7 Iron", "miss_severity": "moderate", "miss_direction": "Right"},
        {"club": "7 Iron", "miss_severity": "minor", "miss_direction": "Straight"},
        {"club": "7 Iron", "miss_severity": "minor", "miss_direction": "Left"},
        {"club": "7 Iron", "miss_severity": "on-target", "miss_direction": "Straight"},
        {"club": "7 Iron", "miss_severity": "on-target", "miss_direction": "Straight"}
    ]

    recommendation = practice_recommendation(shots)
    assert recommendation is not None
    assert recommendation["club"] == "Driver"
    assert recommendation["major_miss_rate"] == 60.0
    assert recommendation["miss_direction"] == "Left"
    print("Practice priority test passed")



test_empty_data()
test_insufficient_shots()
test_practice_priority()