# Crawler, that uses RNAcentral API
import requests
r = requests.get("https://rnacentral.org/api/v1/rna/?min_length=60&max_length=90")

f_base = open("RNA_CEN.txt", "w") # Full information goes here
f_seq = open("central.txt", "w") # Here go only sequences

while r.json()["next"]:
    for result in r.json()["results"]:
        name = result["rnacentral_id"]
        seq = result["sequence"]
        len = result["length"]
        desc = result["description"]
        type = result["rna_type"]
        base = result["distinct_databases"][0] if result["distinct_databases"] else "?"
        f_base.write("# File " + name + "\n")
        f_base.write("# External source :  " + base + "\n")
        f_base.write("# Type : " + type + "\n")
        f_base.write("# Length : " + str(len) + "\n")
        f_base.write("# Description : " + desc + "\n\n")
        f_base.write(seq + "\n\n")
        f_seq.write(seq + "\n")
    next = r.json()["next"]
    r = requests.get(next) # fetch next page
f_seq.close()
