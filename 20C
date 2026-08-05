if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # Find the second lowest grade
    grades = sorted(list(set([s[1] for s in students])))
    second_lowest_grade = grades[1]

    # Collect names of students with that grade
    second_lowest_students = [s[0] for s in students if s[1] == second_lowest_grade]

    # Sort names alphabetically and print
    for name in sorted(second_lowest_students):
        print(name)
