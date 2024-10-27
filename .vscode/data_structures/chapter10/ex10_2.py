# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

nameFile = input("Enter file name:")
if len(nameFile) < 1:
    nameFile = "mbox-short.txt"
handleFile = open(nameFile)

counts = dict()

for line in handleFile:
    if line.startswith("From"):
        lines = line.split()

        if len(lines) > 5:
            time = lines[5]
            hour = time.split(":")[0]
            counts[hour] = counts.get(hour, 0) + 1

for hour in sorted(counts):
    print(hour, counts[hour])
