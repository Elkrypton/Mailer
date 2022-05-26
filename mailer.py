import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64
import easyimap
import sys, os, csv
from sentiment import SentimentAnalyzer
from getpass import getpass
from email.mime.image import MIMEImage
from sentiment import SentimentAnalyzer



class Email():

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.msg = MIMEMultipart()
        self.msg_mass = MIMEMultipart()
        self.context = ssl.create_default_context()

    def SendMail(self):
        print("""
_______             _______
|@|@|@|@|           |@|@|@|@|       <#> YOU HAVE CHOSEN TO SEND AN EMAIL!
|@|@|@|@|   _____   |@|@|@|@|       <#> OKAY, GO AHEAD AND DO YOUR NASTY THING!
|@|@|@|@| /\_T_T_/\ |@|@|@|@|
|@|@|@|@||/\ T T /\||@|@|@|@|
 ~/T~~T~||~\/~T~\/~||~T~~T\~
  \|__|_| \(-(O)-)/ |_|__|/
  _| _|    ||8_8//    |_ |_
|(@)]   /~~[_____]~~\   [(@)|
  ~    (  |       |  )    ~
      [~` ]       [ '~]
      |~~|         |~~|
      |  |         |  |
     _<\/>_       _<\/>_
    /_====_\     /_====_|

        """)
        #self.sender = self.username
        self.receiver = input("\n[+] To :")
        self.msg['From'] = self.username
        self.msg['To'] = self.receiver
        self.msg['Subject'] = input("[+] Subject:")
        text = input("<#> Message:")
        self.msg.attach(MIMEText(text))
        self.Evoke()
        #self.context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com",465,context=self.context) as smtpObj:
            smtpObj.ehlo()
            #smtpObj.starttls()
            smtpObj.login(self.username,self.password)
            print("[==>] Sending to : {}".format(self.receiver))
            smtpObj.sendmail(self.username,self.receiver,self.msg.as_string())

        print("[^_^] Email(s) Sent!")
       

    def MassSender(self):
        print("""

MASS DESTRUCTION 
   _                        _______                      _
  _dMMMb._              .adOOOOOOOOOba.              _,dMMMb_
 dP'  ~YMMb            dOOOOOOOOOOOOOOOb            aMMP~  `Yb
 V      ~"Mb          dOOOOOOOOOOOOOOOOOb          dM"~      V
          `Mb.       dOOOOOOOOOOOOOOOOOOOb       ,dM'
           `YMb._   |OOOOOOOOOOOOOOOOOOOOO|   _,dMP'
      __     `YMMM| OP'~"YOOOOOOOOOOOP"~`YO |MMMP'     __
    ,dMMMb.     ~~' OO     `YOOOOOP'     OO `~~     ,dMMMb.
 _,dP~  `YMba_      OOb      `OOO'      dOO      _aMMP'  ~Yb._

             `YMMMMMMOOOo     OOO     oOOO'/MMMMP'
     ,aa.     `~YMMb `OOOb._,dOOOb._,dOOO'dMMP~'       ,aa.
   ,dMYYMba._         `OOOOOOOOOOOOOOOOO'          _,adMYYMb.
  ,MP'   `YMMba._      OOOOOOOOOOOOOOOOO       _,adMMP'   `YM.
  MP'        ~YMMMba._ YOOOOPVVVVVYOOOOP  _,adMMMMP~       `YM
  YMb           ~YMMMMMMOOOOI`````IOOOOO'/MMMMP~           dMP
   `Mb.           `YMMMb`OOOI,,,,,IOOOO'dMMMP'           ,dM'
     `'                  `OObNNNNNdOO'                   `'
                           `~OOOOO~'   --  BEWARE OF ME

            """)
        csv_file = input("\n>> Please Specify the file:")
        #self.mass_sender = input("[+] Sender:")
        self.msg_mass['From'] = self.username
        self.msg_mass['Subject'] = input("[+] Subject:")
        self.mass_message = input("<<Message>>:")
        self.msg_mass.attach(MIMEText(self.mass_message))
        #fp = open("image.jpg",'rb')
        #msgImage = MIMEImage(fp.read())
        #fp.close()
        #msgImage.add_header('Content-ID', '<image1>')
        #self.msg_mass.attach(msgImage)
        self.Evoke()
        with open(csv_file) as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for name, email in reader:

                self.msg_mass['To'] = email
                with smtplib.SMTP_SSL("smtp.gmail.com",465,context=self.context) as smtpObj2:
                    smtpObj2.ehlo()
                    smtpObj2.login(self.username, self.password)
                    print("\n>> Sending to : {} : {}".format(name,email))
                    smtpObj2.sendmail(self.username,email,self.msg_mass.as_string())




    def ReadMail(self):
        print("""

 <#> LET'S READ THAT NASTY INBOX

        .-|=====-.
        | | mail |
     ___|________|
            ||
            ||
            ||   www
     ,;,    ||   )_(,;;;,
     <_>  \ ||   \|/ \_/
     \|/  \\||  \\|   |//
_jgs_\|//_\\|///_\V/_\|//__
        """)
        imapper = easyimap.connect('imap.gmail.com', self.username, self.password)
        number = input("<#> The Number of Messages:")
        for mail_id in imapper.listids(limit=int(number)):
            mail = imapper.mail(mail_id)
            print("[+] From :{}".format(mail.from_addr))
            print("\n[+] To : {}".format(mail.to))
            print("\n[+] CC : {}".format(mail.cc))
            print("\n[+] Subject : {}".format(mail.title))
            print("\n[+] Message:\n{}".format(mail.body))
            print("\n")
            senti = input(">> Would you like to Analyze the sentiment of the email [y/n]\n:")
            if senti.lower() == "yes":
                print("\n")
                SentObj = SentimentAnalyzer(str(mail.body))
                SentObj.AdvancedAnalyzer()
            else:
                pass
            
            if mail.attachments:
                print("\n[+] Attachments:\n".format(mail.attachments))
                choice = input("\n>> WOULD LIKE TO SAVE ATTACHMENTS:[y/n]?")
                if choice.lower() == "yes" or "y":
                    for attachment in mail.attachments:
                        f = open("attachments/" + attachment[0], "wb")
                        f.write(attachment[1])
                        f.close()
                        break

    def Evoke(self):
        print("""
\|/
-o------.
/|\     |'
 |      '-|
 |        |
 |        |
 |        |
 |        |
 |    file|
 '--------'

        """)
        print("\n[+] Do Want to add a file?\n")
        choice = input("[Yes/No] :")
        if choice.lower() == "yes":
            filenames = input(">> Filenames:")
            try:

                for attachment in filenames.split(','):
                    self.part = MIMEBase('application','octet-stream')
                    self.part.set_payload(open(attachment,'rb').read())
                    encode_base64(self.part)
                    self.part.add_header('Content-Disposition','attachment; filename="%s"'%os.path.basename(attachment))
                    self.msg.attach(self.part)
                    self.msg_mass.attach(self.part)
                    break
            except:
                print("[!] File Does not exist")
        else:
            pass

def main():
    print("""

███╗   ███╗ █████╗ ██╗██╗     ███████╗██████╗
████╗ ████║██╔══██╗██║██║     ██╔════╝██╔══██╗
██╔████╔██║███████║██║██║     █████╗  ██████╔╝
██║╚██╔╝██║██╔══██║██║██║     ██╔══╝  ██╔══██╗
██║ ╚═╝ ██║██║  ██║██║███████╗███████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═╝  ╚═╝ -- Made By Krypton

    |oooo|        |oooo|
    |oooo| .----. |oooo|
    |Oooo|/\_||_/\|oooO|
    `----' / __ \ `----'
    ,/ |#|/\/__\/\|#| \,
   /  \|#|| |/\| ||#|/
  / \_/|_|| |/\| ||_|\_/
 |_\/    o\=----=/o    \/_|
 <_>      |=\__/=|      <_>
 <_>      |------|      <_>
 | |   ___|======|___   | |
//||  / |O|======|O| \  | |
|  |  | |O+------+O| |  |  |
|\/|  \_+/        \+_/  |\/|
\__/  _|||        |||_  \__/
      | ||        || |
     [==|]        [|==]
     [===]        [===]
      >_<          >_<
     || ||        || ||
     || ||        || ||
     || ||        || ||    -- Destructive Mailing
   __|\_/|__    __|\_/|__
  /___n_n___\  /___n_n___|



 >>>> Changing the code won't make you the programmer of the script.
 >>>> I am not responsible for any misuses of this program.""")
    email = input("\n\n[+] Email: ")
    password = getpass("[+] Password:")
    EmailObj = Email(email,password)
    state = True
    while state:

        print("""\n\t.----------------------------------------------------.
        | Welcome to Krypton Mailer, Choose Your Weapon:     |
        '----------------------------------------------------'""")
        print("""
            |oooo|        |oooo|
            |oooo| .----. |oooo|
            |Oooo|/\_||_/\|oooO|
            `----' / __ \ `----'
            ,/ |#|/\/__\/\|#| \,
           /  \|#|| |/\| ||#|/
          / \_/|_|| |/\| ||_|\_/            1 - One Time Killer
         |_\/    o\=----=/o    \/_|
         <_>      |=\__/=|      <_>         2 - Read Mail
         <_>      |------|      <_>
         | |   ___|======|___   | |         3 - Mass Killer
        //||  / |O|======|O| \  | |
        |  |  | |O+------+O| |  |  |        4 - Exit
        |\/|  \_+/        \+_/  |\/|
        \__/  _|||        |||_  \__/
              | ||        || |
             [==|]        [|==]
             [===]        [===]
              >_<          >_<
             || ||        || ||
             || ||        || ||
             || ||        || ||
           __|\_/|__    __|\_/|__
          /___n_n___\  /___n_n___|  #Malicious Mailer

            """)
        choice = int(input("<#>:"))
        if choice == 1:
            EmailObj.SendMail()
        elif choice == 2:
            EmailObj.ReadMail()
        elif choice == 3:
            EmailObj.MassSender()
        elif choice == 4:
            sys.exit(">> Exiting...")

        else:
            print("[!] Unknown Option!")

if __name__ == "__main__":
    main()
