import time
import os
os.system("rm -rf /data/data/com.termux/files/home/.termux/termux.properties")
os.system("cp termux.properties /data/data/com.termux/files/home/.termux")
os.system("clear")                                                                              
print("\033[93mtermuxtan", "Çıkış", "Yapıp", "Tekrar", "Giriniz","\033[96m\n(Codded", "by/Strike)", sep=" ")
time.sleep(2)
os.system("termux-open-url https://instagram.com/strike0fficial")

