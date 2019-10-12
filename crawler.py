import requests
from bs4 import BeautifulSoup
cnt = 1
type = "NDB"
f = open('RNA_' + type + '.txt', 'w')
while cnt<=72:
    url = "http://www.rnasoft.ca/strand/show_file.php?format=Dot-parentheses&molecule_ID=" + type + "_" +str(cnt).zfill(5) + "&check_out_the=View+the+RNA+sequence+and+secondary+structure+for+molecule+" + type + "_" +str(cnt).zfill(5)
    r = requests.get(url)
    # print(r.text)
    soup = BeautifulSoup(r.content, features="html5lib")
    tmp = soup.find("textarea")
    if not (tmp):
        cnt+=1
        continue
    s = tmp.string
    if(s):
        f.write(s)
    else:
        print(soup.prettify(formatter = None))
    print(cnt)
    cnt+=1
f.close()
