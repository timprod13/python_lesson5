subj = {}
with open('part6.txt', 'r') as part6:
    for line in part6:
        subject, lecture, practice, lab = line.split()
        subj[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Total hours in the subject - \n {subj}')
