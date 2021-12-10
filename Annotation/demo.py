import re

# Import {headline-content.txt}, {headline-url.txt}, and {topic annotation.txt}
with open("headline-url.txt", "r") as hu_file:
    h_u = hu_file.readlines()

with open("headline-content.txt", "r") as hc_file:
    h_c = hc_file.readlines()

with open("topic annotation.txt", "r") as annotation_file:
    annotation = annotation_file.readlines()

# Information about the nth news article
n = 20
print(f"There are {len(annotation)} news articles in the dataset.\n")
# single url
url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', h_u[n])
print(f"{url[0]}\n")
# single headline
print(f"{h_u[n].partition('.')[0]} \n")
# single content
print(f"{h_c[n]}\n")
# labels
print(annotation[n])


# Count the occurence of word in an article
def word_count(str):
    # Create an empty dictionary
    counts = dict()
    words = str.split()
    # Loop through each line of the file
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

freq = word_count(h_c[n])
sorted_dict = {}
sorted_keys = sorted(freq, key = freq.get, reverse = True)
for w in sorted_keys:
    sorted_dict[w] = freq[w]
print(sorted_dict, "\n")
