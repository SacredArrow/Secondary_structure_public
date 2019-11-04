import requests
r = requests.get("https://rnacentral.org/api/v1/rna/?min_length=60&max_length=90")
# r = requests.get("https://rnacentral.org/api/v1/rna/?min_length=1&max_length=4")
# print(r.json()["results"][0]["url"])
# next = r.json()["next"]
# r = requests.get(next)
# if r.json()["previous"]:
#     print("Yes")
# else:
#     print("No")
f_base = open("RNA_CEN.txt", "w")
f_seq = open("central.txt", "w")

while r.json()["next"]:
    for result in r.json()["results"]:
        # print(r.json())
        name = result["rnacentral_id"]
        seq = result["sequence"]
        len = result["length"]
        desc = result["description"]
        type = result["rna_type"]
        # print(result["distinct_databases"])
        base = result["distinct_databases"][0] if result["distinct_databases"] else "?"
        f_base.write("# File " + name + "\n")
        f_base.write("# External source :  " + base + "\n")
        f_base.write("# Type : " + type + "\n")
        f_base.write("# Length : " + str(len) + "\n")
        f_base.write("# Description : " + desc + "\n\n")
        f_base.write(seq + "\n\n")
        f_seq.write(seq + "\n")
        # print(name, seq, len, desc, type, base)
    next = r.json()["next"]
    r = requests.get(next) # переходим на след. страницу
    # print(next)
f_seq.close()
