def validate_path(expected_path, character_path):
    correct_count = 0
    character_name = character_path[0]

    for i in range(len(expected_path)):
        if expected_path[i] == character_path[i + 1]:
            correct_count += 1

    accuracy_percentage = correct_count / len(expected_path) * 100
    return character_name, accuracy_percentage
