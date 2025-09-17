import requests
import json
from pybtex.database.input import bibtex

token = 'J3drlJH13gH0dJZUz2FwhrSvNK4gqW7khI5rWAy1'

# get the data for the REACH library
results = requests.get("https://api.adsabs.harvard.edu/v1/biblib/libraries/QFTpllppSgS1zK9Z6lTVPQ?fl=bibcode,alternate_bibcode,title,author,abstract,date,pub,pubdate,first_author,issue,keyword,doi&rows=2000",
                       headers={'Authorization': 'Bearer ' + token})

with open("reach_papers_list/results.json", "w") as f:
    f.write(json.dumps(results.json()))

# Read bib file and format as json file
parser = bibtex.Parser()
bib_data = parser.parse_file("reach_papers_list/reach_conference_proceedings.bib")

# Create JSON object
proceedings_dict = {"proceedings":[]}

for key in bib_data.entries:
    entry = bib_data.entries[key]

    authors = []

    for author in entry.persons["author"]:
        authors.append(str(author))

    proceedings_dict["proceedings"].append({
        "title": entry.fields["title"],
        "author": authors,
        "year": entry.fields["year"],
        "doi": entry.fields["doi"],
        "pub": entry.fields["booktitle"]
    })

# Sort dict by year
proceedings_dict["proceedings"] = sorted(proceedings_dict["proceedings"], key=lambda x: x["year"], reverse=True)

# Write JSON object to file
with open("reach_papers_list/reach_conference_proceedings.json", "w") as f:
    f.write(json.dumps(proceedings_dict))