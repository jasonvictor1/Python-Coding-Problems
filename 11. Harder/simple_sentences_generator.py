
# Define lists of subjects, verbs, and objects
subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Hockey", "Football"]

# Use nested loops to generate all possible sentences
for i in range(len(subjects)):
    for j in range(len(verbs)):
        for k in range(len(objects)):
            # Print each generated sentence
            print(subjects[i], verbs[j], objects[k])
