import os
import time
import sys
import random

def jalan(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.02)

jalan("\t\t\033[1;91m____________     ___  ______________")
jalan("\t\t\033[1;91m|  ___| ___ \    |  \/  |  _  |  _  |")
jalan("\t\t\033[1;91m| |_  | |_/ /_  _| .  . | | | | | | |")
jalan("\t\t\033[0m|  _| | ___ \ \/ / |\/| | | | | | | |")
jalan("\t\t\033[0m| |   | |_/ />  <| |  | \ \_/ / |/ /")
jalan("\t\t\033[0m\_|   \____//_/\_\_|  |_/\___/|___/")

jalan("Pilih Server\n")
print(" [1] Server Indonesia")
print(" [2] Server Pakistan")
print(" [3] Server Bangladesh\n")
pilih = raw_input('Silahkan Di Pilih: ')
if pilih == "1":
        os.system('cd VNM && python2 FBxMOD.VNM')





