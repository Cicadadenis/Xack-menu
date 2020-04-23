# Tool Name :- Cicada
# Author :- Bednakov-Xack-Live
# Date :- 1/11/2020

import os
import sys
from time import sleep
from modules.logo import *
from modules.system import *

class tool:
  @classmethod
  def install(self):
    while True:
      system=sys()
      os.system("clear")
      logo.ins_tnc()
      inp=input("\033[1;33m 	Вы хотите установить Xack-Menu [Y/n]> \033[00m")
      if inp=="y" or inp=="Y":
        os.system("clear")
        logo.installing()
        if system.sudo is not None:
          #require root permission
          if os.path.exists(system.conf_dir+"/Cicada"):
            pass
          else:
            os.system(system.sudo+" mkdir "+system.conf_dir+"/Cicada")
          os.system(system.sudo+" cp -r modules core Cicada.py "+system.conf_dir+"/Cicada")
          os.system(system.sudo+" cp -r core/Cicada "+system.bin)
          os.system(system.sudo+" cp -r core/cicada "+system.bin)
          os.system(system.sudo+" chmod +x "+system.bin+"/Cicada")
          os.system(system.sudo+" chmod +x "+system.bin+"/cicada")
          os.system("cd .. && "+system.sudo+" rm -rf Cicada")
          if os.path.exists(system.bin+"/Cicada") and os.path.exists(system.conf_dir+"/Cicada"):
            os.system("clear")
            logo.ins_sc()
            tmp=input("\033[1;36m 	##> \033[00m")
            break
          else:
            os.system("clear")
            logo.not_ins()
            tmp=input("\033[1;36m 	##> \033[00m")
            break
        else:
          if os.path.exists(system.conf_dir+"/Cicada"):
            pass
          else:
            os.system("mkdir "+system.conf_dir+"/Cicada")
          os.system("cp -r modules core Cicada.py "+system.conf_dir+"/Cicada")
          os.system("cp -r core/Cicada "+system.bin)
          os.system("cp -r core/cicada "+system.bin)
          os.system("chmod +x "+system.bin+"/Cicada")
          os.system("chmod +x "+system.bin+"/cicada")
          os.system("cd .. && rm -rf Cicada")
          if os.path.exists(system.bin+"/Cicada") and os.path.exists(system.conf_dir+"/Cicada"):
            os.system("clear")
            logo.ins_sc()
            tmp=input("\033[1;36m 	##> \033[00m")
            break
          else:
            os.system("clear")
            logo.not_ins()
            tmp=input("\033[1;36m 	##> \033[00m")
            break
      else:
        break

if __name__=="__main__":
  try:
    tool.install()
  except KeyboardInterrupt:
    os.system("clear")
    logo.exit()
