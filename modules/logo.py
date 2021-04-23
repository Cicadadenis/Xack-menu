class logo:
  def tool_footer(self):
    print('''\033[1;36m        _______________________________________________
        ===============================================\033[00m''')


  @classmethod
  def not_ins(self):
    self.tool_header()
    print ('''
        \033[1;31m  [ + ]  \033[1;31mXack-Menu успешно установлен.\033[1;m
        \033[1;31m  [ + ]  \033[1;31mЗапустить Xack-Menu.\033[1;m
        \033[1;31m  [ + ]  \033[1;31mВведите cicada в вашем терминале.\033[1;m''')
    self.tool_footer()

  @classmethod
  def ins_tnc(self):
    self.tool_header()
    print ('''
        \033[1;33m  [ + ] \033[1;32mИспользуйте его на свой страх и риск.
        \033[1;33m  [ + ] \033[1;32mНет гарантии.
        \033[1;33m  [ + ] \033[1;32mИспользуйте это только в законных целях.
        \033[1;33m  [ + ] \033[1;32mЯ не несу ответственности за ваши действия.
        \033[1;33m  [ + ] \033[1;32mНе делайте то, что запрещено.

        \033[1;31m Если вы устанавливаете этот инструмент.
        это означает, что вы согласны со всеми условиями.''')
    self.tool_footer()

  @classmethod
  def ins_sc(self):
    self.tool_header()
    print ('''
        \033[1;33m    [ + ] \033[1;32mXack-Menu  успешно установлен.
        \033[1;33m    [ + ] \033[1;32mЗапустить Xack-Menu .
        \033[1;33m    [ + ] \033[1;32mВведите cicada в вашем терминале.''')
    self.tool_footer()

  @classmethod
  def update(self):
    self.tool_header()
    print ('''
        \033[1;33m  [ 1 ] \033[1;32mОбновите ваш Xack-Menu
        \033[1;33m  [ 0 ] \033[1;32mВернуться.\033[00m''')
    self.tool_footer()

  @classmethod
  def updated(self):
    self.tool_header()
    print ('''
        \033[1;33m      [ + ] \033[1;32mXack-Menu  успешно обновлен.
        \033[1;33m      [ + ] \033[1;32mНажмите Enter, чтобы продолжить.\033[00m''')
    self.tool_footer()

  @classmethod
  def nonet(self):
    self.tool_header()
    print ('''
        \033[1;31m  [ + ]  \033[1;31mНет сетевого подключения?\033[1;m
        \033[1;31m  [ + ]  \033[1;31mВы в автономном режиме?\033[1;m
        \033[1;31m  [ + ]  \033[1;31mПожалуйста, попробуйте еще раз через некоторое время.\033[00m''')
    self.tool_footer()

  @classmethod
  def update_error(self):
    self.tool_header()
    print ('''
        \033[1;31m  [ + ]  \033[1;31mУстановленна последняя версия Xack-Menu .\033[1;m
        \033[1;31m  [ + ]  \033[1;31mПожалуйста, попробуйте еще раз через некоторое время.\033[00m''')
    self.tool_footer()


  @classmethod
  def about(self,total):
    self.tool_header()
    print (f'''
        \033[1;33m       [+] Название :- \033[1;32mXack-Menu
        \033[1;33m       [+] Разроботчик :- \033[1;32mBednakov Denis
        \033[1;33m       [+] GitHub :- \033[1;32mhttp://github.com/bednakovdenis
        \033[1;33m       [+] facebook :- \033[1;32mhttps://www.facebook.com/cicada3301denis/
        \033[1;33m       [+] Обновление :- \033[1;32m19/01/2021.\033[1;m
        \033[1;33m       [+] инструменты :- \033[1;32mвсего {total} инструментов.\033[1;m

        \033[1;33m [+] \033[1;32mЭто автоматический установщик программ.
        \033[1;33m [+] \033[1;32mСделано для системы на основе termux и linux.
        \033[1;31m [+] Используйте этот инструмент на свой страх и риск.''')
    self.tool_footer()


  @classmethod
  def install_tools(self):
    print ("""\033[01;33m       =============================================
\033[01;32m      |__________ Выберите свой инструмент _________|
 \033[01;33m      =============================================\033[00m""")

  @classmethod
  def already_installed(self,name):
    self.tool_header()
    print(f'''
        \033[1;33m  [ + ] \033[1;32mИзвените ??
        \033[1;33m  [ + ] \033[1;37m'{name}'\033[01;32m уже установлено !!
        ''')
    self.tool_footer()

  @classmethod
  def installed(self,name):
    self.tool_header()
    print(f'''
        \033[1;33m  [ + ] \033[1;32mУспешно установлено!!
        \033[1;33m  [ + ] \033[1;37m'{name}'\033[01;32m успешно установлен!!
        ''')
    self.tool_footer()

  @classmethod
  def not_installed(self,name):
    self.tool_header()
    print(f'''
        \033[1;33m  [ + ] \033[1;31mИзвини ??
        \033[1;33m  [ + ] \033[1;37m'{name}'\033[01;31m не установлено !!
        ''')
    self.tool_footer()

  @classmethod
  def back(self):
    print ("""\033[01;36m        =============================================
\033[01;33m       |  00) Назад                                  |
 \033[01;36m       =============================================\033[00m""")

  @classmethod
  def updating(self):
    print ("""\033[01;33m =============================================
\033[01;32m|______________ обновление ______________|
 \033[01;33m=============================================\033[00m""")

  @classmethod
  def installing(self):
    print ("""\033[01;33m =============================================
\033[01;32m|________________ Установка _________________|
 \033[01;33m=============================================\033[00m""")

  @classmethod
  def menu(self,total):
    self.tool_header()
    print (f'''
        \033[1;33m  [ 1 ] \033[1;32mВсе инструменты.\033[1;33m [ \033[1;91mВсего {total} инструментов\033[1;33m ]
        \033[1;33m  [ 2 ] \033[1;32mКатегории
        \033[1;33m  [ 3 ] \033[1;32mОбновление
        \033[1;33m  [ 4 ] \033[1;32mПро Меня
        \033[1;33m  [ x ] \033[1;32mВыход.''')
    self.tool_footer()

  @classmethod
  def exit(self):
    self.tool_header()
    print ('''
        \033[1;33m         [ + ] \033[1;32mСпасибо за использование Xack-Menu
        \033[1;33m         [ + ] \033[1;32mПока.....:)\033[00m''')
    self.tool_footer()
