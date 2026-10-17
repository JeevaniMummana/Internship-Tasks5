if __name__ == '__main__':
    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # Get all unique scores and sort them
    scores = sorted(set(score for name, score in students))

    # Second lowest score
    second_lowest = scores[1]

    # Get names with second lowest score
    names = [name for name, score in students if score == second_lowest]

    # Alphabetical order
    names.sort()

    # Print each name
    for name in names:
        print(name)