# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

#Code for JSON
# import os
# script_dir = os.path.dirname(
#     os.path.abspath(__file__)
# )  # Get the directory of the script
# file_path = os.path.join(
#     script_dir, "mbox-short.txt"
# )  # Construct the full path to the file
# handleFile = open(file_path)

nameFile = input("Enter file name:")

if len(nameFile) < 1:
    nameFile = "mbox-short.txt"
    handleFile = open(nameFile)

counts = dict()


for line in handleFile:
    lines = line.split()

    if "From" in lines and len(lines) > 0:
        email = lines[1]
        counts[email] = counts.get(email, 0) + 1

maxEmail = None
maxCount = None

for email, count in counts.items():
    if maxCount is None or count > maxCount:
        maxCount = count
        maxEmail = email

if maxEmail is not None:
    print(maxEmail, maxCount)
