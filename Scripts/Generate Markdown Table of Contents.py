import string
from time import strftime

text = """
"""

for line in text.splitlines():
    if "#" in line:
        
        spaces = " " * ((line.count("#") - 1) * 2)
        md_link, md_anchor = line, line
        
        md_link = md_link.strip("#")
        md_link = md_link.strip()
        
        md_anchor = md_anchor.translate(str.maketrans('', '', string.punctuation))
        md_anchor = md_anchor.strip()
        md_anchor = md_anchor.lower()
        md_anchor = md_anchor.replace(" ", "-")
        
        print("{}- [{}](#{})".format(spaces, md_link, md_anchor))
        
print("\n---\n")
print("**Author:**  Daniel Arapi")
print("**Updated:**", strftime("%m/%d/%Y"))
