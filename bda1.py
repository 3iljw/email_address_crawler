import re
import urllib

url1 = 'http://www.csie.kuas.edu.tw/teacher.php'
url2 = 'http://www.csie.ncku.edu.tw/ncku_csie/depmember/teacher'

web1 = urllib.urlopen(url1).read()
web2 = urllib.urlopen(url2).read()

def getmail():
    email1 = re.compile(r"[a-zA-Z0-9._%+]+@[a-zA-Z0-9.+]+\.[a-zA-Z]{2,4}", re.IGNORECASE)
    mails1 = re.findall(email1,web1)
    print(url1 + ":")
    for i in range (0,len(mails1)) :
        print(mails1[i])
    print("Sorry to Mr.wang because your e-mail address is \"ccwang@ nkust.edu.tw\" .")
    print("")
    email2 = re.compile(r"[a-zA-Z0-9._%+]+@[a-zA-Z0-9.+]+\.[a-zA-Z]{2,4}", re.IGNORECASE)
#    mails2 = re.findall(email2,web2("td",{ "class" : "teacherInfo"}))
    mails2 = re.findall(email2,web2)
    print(url2 + ":")
    for j in range (0,len(mails2)) :
        print(mails2[j])
    print(len(mails2))

def main():
    getmail()

if __name__ == '__main__':
    main()
