# -*- coding: utf-8 -*-
from YIM.linepy import *
from YIM.akad.ttypes import *
from multiprocessing import Pool, Process
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.request, urllib.parse, urllib.error, urllib.parse,antolib,subprocess,unicodedata,GACSender,pafy, youtube_dl, timeit, atexit, traceback
_session = requests.session()
from gtts import gTTS
from googletrans import Translator
import youtube_dl
#==============================================================================#
botStart = time.time()
#==============================================================================#
#line = LINE()
#line = LINE("เมล","พาส")
line = LINE()
line.log("Auth Token : " + str(line.authToken))
line.log("Timeline Token : " + str(line.tl.channelAccessToken))

print ("Login Succes")

lineMID = line.profile.mid
lineProfile = line.getProfile()
lineSettings = line.getSettings()

oepoll = OEPoll(line)
#call = Call(line)
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
read = json.load(readOpen)
settings = json.load(settingsOpen)
Rfu = [line]
Exc = [line]
lineMID = line.getProfile().mid
bot1 = line.getProfile().mid
RfuBot=[lineMID]
Family=["u1c2a11ba8aa2a0f357f6cb5ae217f1e9",lineMID] 
admin=['u669aa92773d33c22420105d4546fccdd',lineMID] 
RfuFamily = RfuBot + Family

protectname = []
protecturl = []
protection = []
autocancel = {}
autoinvite = []
autoleaveroom = []
targets = []
#==============================================================================#
msg_dict = {}
msg_dict1 = {}
msg_image={}
msg_video={}
msg_sticker={}

settings = {
    "autoAdd": False,
    "autoJoin": False,
    'autoCancel':{"on":True,"members":5},	
    "autoLeave": True,
    "autoRead": False,
    "leaveRoom": False,
    "detectMention": False,
    "checkSticker": False,
    "checkContact": False,
    "checkPost": False,
    "kickMention": False,
    "potoMention": True,
    "delayMention": False,
    "lang":"JP",
    "Wc": True,
    "Lv": True,
    "Nk": True,
    "Api": False,
    "Aip": False,
    "blacklist":{},
    "winvite": False,
    "wblacklist": False,
    "dblacklist": False,
    "gift":False,
    "likeOn":False,
    "timeline":False,
    "commentOn":True,
    "commentBlack":{},
    "wblack": False,
    "dblack": False,
    "clock": False,
    "cName":"",
    "cNames":"",
    "changeGroupPicture": [],
    "changePictureProfile":False,
    "unsendMessage": False,
    "autoJoinTicket": False,
    "welcome":"✧••••••••••❂✧✯✧❂••••••••••✧",
    "kick":"✧••••••••••❂✧✯✧❂•••••••••••✧",
    "bye":"❂•➤➤➤➤➤➤➤➤➤➤➤➤",
    "Respontag":"",
    "eror":"คุณใช้คำสั่งผิด กรุณาศึกษาวิธีใช้ หรือสอบถามกับผู้สร้าง โดยพิมคำสั่ง *.ผส*เพื่อแสดง คท ",
    "spam":{},
    "invite": {},
    "winvite": False,
    "pnharfbot": {},
    "pname": {},
    "server": "VPS",
    "pro_name": {},
    "message1":"",
    "c":"✯͜͡✯┅═हईツ☆❦ℒįℳ❦ツ❈ईह═┅•✯͜͡✯",
    "s":"",
    "message":"✧••••••••••••❂✧✯✧❂•••••••••••••✧\n ➤➤ ֆҽℓƒ-β❂T-┅═हईツ☆❦ℒįℳ❦ツ❈ईह═┅ ➤➤\n✧••••••••••••❂✧✯✧❂•••••••••••••✧\n\n 💀• Aüto Blöck Messagë •💀\n\n☆➣ บัญชีนี้ได้รับการป้องกันคับ\n☆➣ ระบบได้บล็อคคุณอัติโนมัติคับ\n☆➣ ต้องยืนยันกับเจ้าของบัญชีนี้\n☆➣ โดยการพิมคำว่า ไวรัสปีโป้\n☆➣ เราจะปลดบล็อคท่านอัติโนมัติ\n☆➣ ขออภัยที่ไม่ได้รับความสะดวก\n☆➣ เพราะเจ้าของบัญชีเกรียนคับ\n☆➣ ขอบคุณคับ จุ๊ฟป้อก~•▪○\n\n✧••••••••••••❂✧✯✧❂•••••••••••••✧\n ออโต้บล็อค: โดยท่านอัจฉริยะพี่ยิ้ม",
    "comment":"✧••••••••••❂✧✯✧❂••••••••••✧",
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ],
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}     
    }
}

RfuProtect = {
    "protect": False,
    "cancelprotect": False,
    "inviteprotect": False,
    "linkprotect": False,
    "Protectguest": False,
    "Protectjoin": False,
    "autoAdd": True,
}

Setmain = {
    "foto": {},
}

read = {
    "readPoint": {},
    "readMember": {},
    "readTime": {},
    "setTime":{},
    "ROM": {}
}

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }
    
RfuCctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

rfuSet = {
    'setTime':{},
    'ricoinvite':{},
    'winvite':{},
    }

user1 = lineMID
user2 = ""
	
setTime = {}
setTime = rfuSet['setTime']

contact = line.getProfile() 
backup = line.getProfile() 
backup.dispalyName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

mulai = time.time() 

try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")

myProfile["displayName"] = lineProfile.displayName
myProfile["statusMessage"] = lineProfile.statusMessage
myProfile["pictureStatus"] = lineProfile.pictureStatus
#==============================================================================#
#==============================================================================#            
def Rapid1Say(mtosay):
    line.sendText(Rapid1To,mtosay)
    
def sendMessageCustom(to, text, icon, name):
    khieCool = {
        'MSG_SENDER_ICON': icon,
        'MSG_SENDER_NAME':  name,
    }
    line.sendMessage(to, text, contentMetadata=khieCool)
	
def sendContactCustom(to, mid, icon, name):
    khieCool = {
        'mid':mid,
        'MSG_SENDER_ICON': icon,
        'MSG_SENDER_NAME':  name,
    }
    line.sendMessage(to, None, contentMetadata=khieCool, contentType=13)
 
def RhyN_(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@Rh'
        line.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)

def load():
    global images
    global stickers
    with open("image.json","r") as fp:
        images = json.load(fp)
    with open("sticker.json","r") as fp:
        stickers = json.load(fp)
        
def sendSticker(to, version, packageId, stickerId):
    contentMetadata = {
        'STKVER': version,
        'STKPKGID': packageId,
        'STKID': stickerId
    }
    line.sendMessage(to, '', contentMetadata, 7)

def sendImage(to, path, name="image"):
    try:
        if settings["server"] == "VPS":
            line.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)
def backupData():
    try:
        backup1 = Setmain
        f = codecs.open('setting.json','w','utf-8')
        json.dump(backup1, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup2 = settings
        f = codecs.open('settings.json','w','utf-8')
        json.dump(backup2, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup3 = wait
        f = codecs.open('wait.json','w','utf-8')
        json.dump(backup3, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup4 = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup4, f, sort_keys=True, indent=4, ensure_ascii=False)        
        return True
    except Exception as error:
        logError(error)
        return False 
def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"        
def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print ("TAG ALL")
    try:
       line.sendMessage(msg)
    except Exception as error:
       print(error)

def restartBot():
    print ("RESTART SERVER")
    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def logError(text):
    line.log("[ แจ้งเตือน ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))

def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        line.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        line.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
        
def sendMessageWithMention(to, lineMID):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(lineMID)+'}'
        text_ = '@x '
        line.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)

def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')
    
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = line.genOBSParams({'oid': lineMID, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = line.server.postContent('{}/talk/vp/upload.nhn'.format(str(line.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        line.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))
 
def waktu(secs):
	mins, secs = divmod(secs,60)
	hours, mins = divmod(mins,60)
	days,hours = divmod(hours,24)
	return '%02d วัน %02d ชั่วโมง %02d นาที %02d วินาที' % (days, hours, mins, secs)

def delete_log():
    ndt = datetime.datetime.now()
    for data in msg_dict:
        if (datetime.datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]
  
def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "「{}」\nสวัสดี  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = line.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
          #  textx += mention+settings["welcome"]+"\n 􂜁􀅣>􏿿􂘁􀄗w􏿿􂘁􀄅e􏿿􂘁􀄌l􏿿􂜁􀄃c􏿿􂘁􀄏o􏿿􂘁􀄍m􏿿 􂜁􀄅e􏿿􂜁􀅢<􏿿\n\n􀼂􀅝church􏿿􀼂􀅜arbor􏿿﹏􀼂􀅞limo 1􏿿􀼂􀅟limo 2􏿿􀼂􀅠limo 3􏿿﹏􀼂􀅜arbor􏿿􀼂􀅝church􏿿 \n\n􀼂􀆼หงส์􏿿 ยินดีต้อนรับ🌷ᵀᴼ ᴳᴿᴼᵁᴾ🌷􀼂􀆼หงส์􏿿\n"+str(ginfo.name)+"\n􀼂􀆼หงส์􏿿 มาใหม่ แนะนำตัวด้วยนะจ๊ะ 􀼂􀆼หงส์􏿿\n􀔃􀄲ปิดเสียง􏿿ปิดเสียงแจ้งเตือนด้วยจร้า􀔃􀄲ปิดเสียง􏿿\n􀼂􀅝church􏿿􀼂􀅜arbor􏿿﹏􀼂􀅞limo 1􏿿􀼂􀅟limo 2􏿿􀼂􀅠limo 3􏿿﹏􀼂􀅜arbor􏿿􀼂􀅝church􏿿 \n􀐂􀇲เขียน􏿿..ขอบคุณที่สนับสนุนบอทเรา..\n􀔃􀄎ข้อความ􏿿 ID tome2527\n􀼂􀆢โทร􏿿 0928081567\n\nระบบต้อนรับแยกห้องโดย 𝕿𝖔𝖒𝖊💞𝕾𝖊𝖑𝖋𝖇𝖔𝖙💞𝕴𝖓💞𝕷𝖎𝖓𝖊"
            textx += mention+settings["welcome"]+"\n🛐 ชื่อห้อง 🛐  "+str(ginfo.name)+"\n\n🛐 ระบบต้อนรับแยกห้องโดย  By เฮียยิ้ม 🛐"
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(client.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        line.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        line.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "「{}」\n🛐ลาก่อนจ้า 🛐".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = line.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            #textx += mention+settings["leave"]+"\n\n 􀔃􀅇แดง􏿿􂜁􀄇g􏿿􂜁􀄏o􏿿􂜁􀄏o􏿿􂜁􀄄d􏿿􂜁􀅷b􏿿􂜁􀄙y􏿿􂘁􀄅e􏿿􀔃􀅇แดง􏿿􀬁\n         􀼂􀅝church􏿿􀼂􀅜arbor􏿿﹏􀼂􀅞limo 1􏿿􀼂􀅟limo 2􏿿􀼂􀅠limo 3􏿿﹏􀼂􀅜arbor􏿿􀼂􀅝church􏿿\n"+str(ginfo.name)+"\n 􀼂􀆼หงส์􏿿.. แล้วพบกันใหม่นะจ๊ะ..􀼂􀆼หงส์􏿿\n􀐂􀇲เขียน􏿿..ขอบคุณที่สนับสนุนบอท จร้าา.. \n􀼂􀅝church􏿿􀼂􀅜arbor􏿿﹏􀼂􀅞limo 1􏿿􀼂􀅟limo 2􏿿􀼂􀅠limo 3􏿿﹏􀼂􀅜arbor􏿿􀼂􀅝church􏿿 \n􀔃􀄎ข้อความ􏿿https://line.me/ti/p/tome2527\n􀼂􀆢โทร􏿿 0928081567\n\nระบบต้อนรับแยกห้องโดย 𝕿𝖔𝖒𝖊💞𝕾𝖊𝖑𝖋𝖇𝖔𝖙💞𝕴𝖓💞𝕷𝖎𝖓𝖊"
            textx += mention+settings["leave"]+"\n🛐ชื่อห้อง "+str(ginfo.name)+"\n\n🛐ระบบต้อนรับแยกห้องโดย เอียยิ้ม"
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(client.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        line.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        line.sendMessage(to, "[ INFO ] Error :\n" + str(error))        

def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    line.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    
def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "╔══[Mention {} User]\n╠ ".format(str(len(mid)))
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "╠ "
            else:
                try:
                    textx += "╚══[ {} ]".format(str(line.getGroup(to).name))
                except:
                    pass
        line.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        line.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def myhelp():
    myHelp = """✧••••••••••••❂✧✯✧❂•••••••••••••✧
      ✯-[HOTź] JT®67™β❂T-✯
✧••••••••••••❂✧✯✧❂•••••••••••••✧

            ✲•คำสั่งทั่วไปคับ•✲

╭☆•☆•☆•☆•☆•☆•☆•☆•☆•☆•☆
║♡•➤ ยิ้มเช็ค, เช็ค
║♡•➣ คทกู, พี่ยิ้ม 《คท.เรา》
║♡•➤ คุณยิ้ม, ท่านยิ้ม
║♡•➣ สุดหล่อ, ณเดช
║♡•➤ lineid 《ไอดี.เรา》
║♡•➣ ผส, ผู้สร้าง《คทเทพ》
║♡•➤ ข้อมูลกู 《โชว์ข้อมูล》
║♡•➣ ข้อมูล @ 《เพื่อน》
║♡•➤ ยิ้ม1 《โหมดเชลบอท》
║♡•➣ ยิ้ม2 《โหมดในกลุ่ม》
║♡•➤ ยิ้ม3 《โหมดตั้งค่า》
║♡•➣ ยิ้ม4 《โหมดโซเชียล》
║♡•➤ ยิ้ม5 《โหมดฟรุ้งฟริ้ง》
║♡•➣ ยิ้ม6 《โหมดเกรียน》
║♡•➤ โปรโมท 《โปรโมทเรา》
║♡•➣ ไอดี @ 《เพื่อน》
║♡•➤ ชื่อ @ 《ชื่อเพื่อน》
║♡•➣ ตัส @ 《ตัสเพื่อน》
║♡•➤ รูป @ 《รูปเพื่อน》
║♡•➣ ปก @ 《ปกเพื้อน》
║♡•➤ คท @ 《ุ่คทเพื่อน》
║♡•➣ วีดีโอโปร @ 《เพื้อน》
║♡•➤ ไอดีล่อง《IDล่องหน》
║♡•➣ คทล่อง《คท.ล่องหน》
║♡•➤ แทคล่อง《แท็กล่องหน》
║♡•➣ ปฏิทิน,ลาบานูน,กูหลงวัน
║♡•➤ สกืลเลียนแบบ on/off
║♡•➣ ลิสเลียนแบบ《รายชื่อ》
║♡•➤ เลียนแบบ @
║♡•➣ เลิกเลียนแบบ @
║♡•➤ ส่งเสียงกลุ่ม《ข้อความ》
║♡•➣ ส่งเสียงแชท《ข้อความ》
║♡•➤ ประกาศกลุ่ม《ข้อความ》
║♡•➣ ประกาศแชท《ข้อความ》
║♡•➤ ส่งรูปภาพตามแชท
║♡•➣ ยิ้มออน2 《เฟคออน》
║♡•➤ ยิ้มออน 《เช็คออน》
╰☆•☆•☆•☆•☆•☆•☆•☆•☆•☆•☆

✧••••••••••••❂✧✯✧❂•••••••••••••✧
 ♡วิธีใช้ : ไม่ต้องใส่จุดคับเสียเวลา♡"""
    return myHelp

def listgrup():
    listGrup = """✧••••••••••••❂✧✯✧❂•••••••••••••✧
      ✯-[HOTź] JT®67™β❂T-✯
✧••••••••••••❂✧✯✧❂•••••••••••••✧

          ✲•โหมดในกลุ่มคับ•✲

╭☆•☆•☆•☆•☆•☆•☆•☆•☆•☆•☆
║♡•➤ เจ้าบ้าน,ผู้สร้างกลุ่ม
║♡•➣ ชื่อกลุ่ม
║♡•➤ ไอดีกลุ่ม
║♡•➣ เปิดลิ้งกลุ่ม
║♡•➤ ปิดลิ้งกลุ่ม
║♡•➣ ยิ้มยกเชิญ
║♡•➤ ลิ้งกลุ่ม, ขอลิ้ง
║♡•➣ รายการกลุ่ม
║♡•➤ สมาชิกกลุ่ม
║♡•➣ ข้อมูลกลุ่ม
║♡•➤ รูปกลุ่ม
║♡•➣ เปลี่ยนรูปกลุ่ม
║♡•➤ @@@,แทค
║♡•➣ ล้างจาน《ลบรันกลุ่ม》
║♡•➤ เทส, เทสบอท
║♡•➣ รีเจนซี่, รีบอท
║♡•➤ ไอดีล่อง
║♡•➣ คทล่อง
║♡•➤ แทคล่อง
║♡•➣ ตั้งเวลา
║♡•➤ เลิกตั้งเวลา
║♡•➣ ตั้งเวลาใหม่
║♡•➤ สกิลอ่าน
║♡•➣ เปิด/ปิดเอจังเปิดอ่าน
║♡•➤ เปิด/ปิดสแกน
║♡•➣ เปิด/ปิดรับแขก
║♡•➤ เปิด/ปิดส่งแขก
║♡•➣ เปิด/ปิดทักเตะ
║♡•➤ เปิด/ปิดapi
║♡•➣ เปิด/ปิดตรวจสอบ
║♡•➤ ยัดดำ @ 《แบน》
║♡•➣ บัญชีดำ 《ลิสดำ》
║♡•➤ ยัดดำกลุ่ม 《แบนยกห้อง》
║♡•➣ ไฮเตอร์ 《ล้างบช.ดำ》
║♡•➤ ประหารชีวิต 《เตะดำ》
║♡•➣ ยิ้มบิน 《สั่งบินกลุ่ม》
╰☆•☆•☆•☆•☆•☆•☆•☆•☆•☆•☆

✧••••••••••••❂✧✯✧❂•••••••••••••✧
 ♡วิธีใช้ : ไม่ต้องใส่จุดคับเสียเวลา♡"""
    return listGrup

def socmedia():
    socMedia = """✧••••••••••••❂✧✯✧❂•••••••••••••✧
      ✯-[HOTź] JT®67™β❂T-✯
✧••••••••••••❂✧✯✧❂•••••••••••••✧

           ✲•โหมดโซเชียลคับ•✲

╭☆•☆•☆•☆•☆•☆•☆•☆•☆•☆•☆
║♡•➣ github
║♡•➤ ค้นหาไอดี《ไลน์》
║♡•➣ ไอดีไลน์
║♡•➤ พลังจิต《ชื่อ》ข้อความ
║♡•➣ สะกดจิต《ชื่อ》ข้อความ
║♡•➤ ทานข้าวยัง
║♡•➣ ทานข้าวกันไหม
║♡•➤ ขอความในใจ
║♡•➣ ขอเสียงเอฟซี
║♡•➤ ขอเสียงแฟนคลับ
║♡•➣ มาแล้ว
║♡•➤ แสดงความเคารพ
║♡•➣ ชมเค้าหน่อย
║♡•➤ ปฏิทิน, ลาบานูน
║♡•➣ ดูทูป《ชื่อเรื่อง》
║♡•➤ ขอภาพ《ชื่อรูป》
║♡•➣ ขอรูป《ชื่อรูป》
║♡•➤ ขอคลิป《ชื่อเรื่อง》
║♡•➣ ยูทูป《ชื่อเรื่อง》
║♡•➤ มิวสิค《ชื่อเพลง》
║♡•➣ ขอเพลง《ชื่อเพลง》
║♡•➤ เพลย์สโต《ชื่อแอป》
║♡•➣ เฟสบุค《ชื่อเฟส》
║♡•➤ ขอหนัง《ชื่อหนัง》
║♡•➣ ขอวีดีโอ《ชื่อเรื่อง》
║♡•➤ ภาพการ์ตูน《ชื่อรูป》
║♡•➣ รูปการ์ตูน《ชื่อรูป》
║♡•➤ ไอจี 《ชื่อยูส》
║♡•➣ ค้นหา《ข้อความ》
╰☆•☆•☆•☆•☆•☆•☆•☆•☆•☆•☆

✧••••••••••••❂✧✯✧❂•••••••••••••✧
 ♡วิธีใช้ : ไม่ต้องใส่จุดคับเสียเวลา♡"""
    return socMedia

def helpset():
    helpSet = """✧••••••••••••❂✧✯✧❂•••••••••••••✧
      ✯-[HOTź] JT®67™β❂T-✯
✧••••••••••••❂✧✯✧❂•••••••••••••✧

          ✲•โหมดเชลบอทคับ•✲

╭☆•☆•☆•☆•☆•☆•☆•☆•☆•☆•☆
║♡•➤ กู 《คท.เรา》
║♡•➣ เช็คกลุ่ม 《ลิสกลุ่ม》
║♡•➤ เพื่อนเพ 《ลิสเพื่อน》
║♡•➣ สกิล 《เรียกคำสั่ง》
║♡•➤ เปิดพรบฉุกเฉิน
║♡•➣ ปิดพรบฉุกเฉิน
║♡•➤ วัดรอบ, แรงม้า
║♡•➣ Sp, 4g, 8g, 9g
║♡•➤ 10g, 11g, 12g, 13g
║♡•➣ เปิดแอร์
║♡•➤ รันแชท 《@ชื่อ》
║♡•➣ พวกนิโกร 《บชดำ》
║♡•➤ ยิงเป้า 《เตะดำ》
║♡•➣ ล้างขี้ 《ล้างบช.ดำ》
║♡•➤ เปลี่ยนชื่อ《ข้อความ》
║♡•➣ เปลี่ยนตัส《ข้อความ》
║♡•➤ แปลงคท《เลขไอดี》
║♡•➣ เปลี่ยนติส
║♡•➤ เปลี่ยนรูปกลุ่ม
║♡•➣ อัพชื่อ《ข้อความ》
║♡•➤ อัพตัส《ข้อความ》
║♡•➣ โคลนนิ่ง @
║♡•➤ คืนร่าง
║♡•➣ ยิ้มเขียน《ข้อความ》
║♡•➤ ทักเข้า:《ข้อความ》
║♡•➣ ทักออก:《ข้อความ》
║♡•➤ ทักเตะ:《ข้อความ》
║♡•➣ ตั้งแทค:《ข้อความ》
║♡•➤ ตั้งแอด:《ข้อความ》
║♡•➣ คอมเม้น:《ข้อความ》
║♡•➤ ไอดีเพื่อน
║♡•➣ ไอดีไลน์
║♡•➤ ลบแบน @
║♡•➣ บล็อค @
║♡•➤ ลบรัน, ล้างรัน
║♡•➣ ลบแชท, ล้างแชท
║♡•➤ ล้อเล่น @《เตะดึง》
║♡•➣ หวด @《เตะออก》
║♡•➤ สอย @《เตะออก》
║♡•➣ ลาก่อย@《เตะออก》
║♡•➤ ปลิว @《เตะออก》
║♡•➣ ดับไฟ 《คท.ไวรัส》
║♡•➤ เทส, เทสบอท
║♡•➣ ยิ้มมาแล้ว
║♡•➤ ไม่กลัว
║♡•➣ รันคอล 《จำนวน》
╰☆•☆•☆•☆•☆•☆•☆•☆•☆•☆•☆

✧••••••••••••❂✧✯✧❂•••••••••••••✧
 ♡วิธีใช้ : ไม่ต้องใส่จุดคับเสียเวลา♡"""
    return helpSet

def helpsetting():
    helpSetting = """✧••••••••••••❂✧✯✧❂•••••••••••••✧
      ✯-[HOTź] JT®67™β❂T-✯
✧••••••••••••❂✧✯✧❂•••••••••••••✧

            ✲•โหมดตั้งค่าคับ•✲

╭☆•☆•☆•☆•☆•☆•☆•☆•☆•☆•☆
║♡•➤ เปิดกัน/ปิดกัน
║♡•➣ กันยก/ปิดกันยก
║♡•➤ กันเชิญ/ปิดกันเชิญ
║♡•➣ กันลิ้ง/ปิดกันลิ้ง
║♡•➤ กันเข้า/ปิดกันเข้า
║♡•➣ เปิดหมด/ปิดหมด
║♡•➤ เปิดกทม/ปิดกทม
║♡•➣ เปิดเข้า/ปิดเข้า
║♡•➤ เปิดออก/ปิดออก
║♡•➣ เปิดติ๊ก/ปิดติ๊ก
║♡•➤ เปิดบล็อค/ปิดบล็อค
║♡•➣ เปิดมุด/ปิดมุด
║♡•➤ เปิดเสือก/ปิดเสือก
║♡•➣ เปิด/ปิดอ่าน
║♡•➤ เปิด/ปิดapi
║♡•➣ เปิด/ปิดแทค
║♡•➤ เปิด/ปิดแทค2
║♡•➣ เปิด/ปิดแทค3
║♡•➤ เปิด/ปิดเตะแทค
║♡•➣ เปิดคท/ปิดคท
║♡•➤ เปิด/ปิดตรวจสอบ
║♡•➣ เปิด/ปิดเช็คโพส
║♡•➤ เปิดแสกน/ปิดแสกน
║♡•➣ เปิด/ปิดรับแขก
║♡•➤ เปิด/ปิดส่งแขก
║♡•➣ เปิด/ปิดทักเตะ
║♡•➤ เปิด/ปิดข้อความ
╰☆•☆•☆•☆•☆•☆•☆•☆•☆•☆•☆

✧••••••••••••❂✧✯✧❂•••••••••••••✧
 ♡วิธีใช้ : ไม่ต้องใส่จุดคับเสียเวลา♡"""
    return helpSetting

def helptexttospeech():
    helpTextToSpeech =   """✧••••••••••••❂✧✯✧❂•••••••••••••✧
      ✯-[HOTź] JT®67™β❂T-✯
✧••••••••••••❂✧✯✧❂•••••••••••••✧

           ✲•โหมดฟรุ้งฟริ้งคับ•✲

╭☆•☆•☆•☆•☆•☆•☆•☆•☆•☆•☆
║♡•➤ ระเบิดเวลาเอจัง
║♡•➣ เอจังวางระเบิด
║♡•➤ ไวรัส 《Virus》
║♡•➣ ไวรัสเอจัง
║♡•➤ ไวรัสเอจัง2
║♡•➣ ไวรัสเอจัง3
║♡•➤ ไวรัสชิวารี
║♡•➣ ไวรัสปีโป้
║♡•➤ ไวรัสฟรุ้งฟริ้ง
║♡•➣ ไวรัสมุ้งมิ้ง
║♡•➤ ไวรัสคิทตี้
║♡•➣ ไวรัสแมนยู
║♡•➤ ไวรัสฟรุตตี้
║♡•➣ ไวรัสเยลลี่
║♡•➤ ไวรัสสีชมพู
║♡•➣ ไวรัสเจเล่
║♡•➤ ไวรัสป๊อกกี้
║♡•➣ ไวรัสผลไม้
║♡•➤ ไวรัสรวมมิตร
║♡•➣ ไวรัสแห่งความมืด
║♡•➤ ไวรัสแห่งความรัก
║♡•➣ ไวรัสแอ๊บแบ๊ว
║♡•➤ ไวรัสชนบท
║♡•➣ ไวรัสอวตาร
║♡•➤ ปีโป้อร่อยจัง
║♡•➣ Hello Kitty
║♡•➤ ไฮโล, เปิดไฮโล
║♡•➣ เต้าปูปลา
║♡•➤ ด่า
║♡•➣ เศษตังแม่
║♡•➤ ใครเกรียนสุด
║♡•➣ ใครหล่อสุด
║♡•➤ ยิ้มนับ
║♡•➣ นับจีน
║♡•➤ นับไทย
║♡•➣ นับอินโด
║♡•➤ นับไฮโซ
║♡•➣ นับสเปน
║♡•➤ นับอังกฤษ
║♡•➣ ยิ้มปิด
║♡•➤ ยิ้มเปิด
║♡•➣ ผู้สร้างไวรัส
╰☆•☆•☆•☆•☆•☆•☆•☆•☆•☆•☆

✧••••••••••••❂✧✯✧❂•••••••••••••✧
 ♡วิธีใช้ : ไม่ต้องใส่จุดคับเสียเวลา♡"""
    return helpTextToSpeech
    
def helplanguange():
    helpLanguange =    """✧••••••••••••❂✧✯✧❂•••••••••••••✧
      ✯-[HOTź] JT®67™β❂T-✯
✧••••••••••••❂✧✯✧❂•••••••••••••✧

           ✲• โหมดเกรียนคับ •✲

╭☆•☆•☆•☆•☆•☆•☆•☆•☆•☆•☆
║♡•➤ ยิ้มบิน 《บินกลุ่ม》
║♡•➣ ยิ้ม2《เฟคออน》
║♡•➤ ยัดดำ @《แบน》
║♡•➣ กุดหัวมัน 《เตะดำ》
║♡•➤ ไฮเตอร์ 《ล้างบชดำ》
║♡•➣ ไฮสปีด, สปีดไฮ
║♡•➤ 4g 《เกรียนสปีด》
║♡•➣ 8g 《เกรียนสปีด》
║♡•➤ 9g 《เกรียนสปีด》
║♡•➣ 10g 《เกรียนสปีด》
║♡•➤ 11g 《เกรียนสปีด》
║♡•➣ 12g 《เกรียนสปีด》
║♡•➤ 13g 《เกรียนสปีด》
║♡•➣ วัดรอบ, แรงม้า
║♡•➤ Bmx, Bmw,รถเต่า
║♡•➣ .22, .38, .357, .45
║♡•➤ เปิดแอร์《ออโต้บล็อค》
║♡•➣ ปิดแอร์《ออโต้บล็อค》
║♡•➤ ทัก《จำนวน》 สต
║♡•➣ รันแชท @
║♡•➤ ข้อมูลกู
║♡•➣ ชื่อกู 《ชื่อเรา》
║♡•➤ ไอดีกู 《ไอดีเรา》
║♡•➣ ปกกู 《ปกเรา》
║♡•➤ ตัสกู 《ตัสเรา》
║♡•➣ ดิสกู, รูปกู
║♡•➤ เกรียน on ...
║♡•➣ Spam on ...
║♡•➤ ส่งนอน 《จำนวน》 @
║♡•➣ ส่งคลิป ... @
║♡•➤ ส่งหัวใจ ... @
║♡•➣ สแปมแทค ... @
║♡•➤ ส่งของขวัญ .. @
║♡•➣ ส่งความรัก  ... @
║♡•➤ แจกของขวัญ .. @
║♡•➣ ส่งความคิดถึง .. @
║♡•➤ รันคอล 《จำนวน》
║♡•➣ สแปมคอล《จำนวน》
║♡•➤ โคลนนิ่ง @
║♡•➣ เปิดอ่าน
║♡•➤  ปิดอ่าน
║♡•➣ โปรโมท 《ตัวเรา》
║♡•➤ โปรโมท @《เพื่อนเรา》
║♡•➣ คท, .คท《ต้องห้าม》
║♡•➤ Me,me 《ต้องห้าม》
║♡•➣ help 《สุดยอดคำสั่ง》
║♡•➤ Help 《สุดยอดคำสั่ง》
╰☆•☆•☆•☆•☆•☆•☆•☆•☆•☆•☆

✧••••••••••••❂✧✯✧❂•••••••••••••✧
 ♡วิธีใช้ : ไม่ต้องใส่จุดคับเสียเวลา♡"""
    return helpLanguange
#==============================================================================#
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if settings["autoAdd"] == True:
                line.blockContact(op.param1)
        if op.type == 13:
            if lineMID in op.param3:
                G = line.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autoCancel"]["on"] == True:
                        if len(G.members) <= settings["autoCancel"]["members"]:
                            line.rejectGroupInvitation(op.param1)
                        else:
                            line.acceptGroupInvitation(op.param1)
                    else:
                        line.acceptGroupInvitation(op.param1)
                elif settings["autoCancel"]["on"] == True:
                    if len(G.members) <= settings["autoCancel"]["members"]:
                        line.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in settings["blacklist"]:
                    matched_list+=[str for str in InviterX if str == tag]
                if matched_list == []:
                    pass
                else:
                    line.cancelGroupInvitation(op.param1, matched_list)				
#        if op.type == 13:
#            group = line.getGroup(op.param1)
#            if settings["autoJoin"] == True:
#                line.acceptGroupInvitation(op.param1)
        if op.type == 24:
            if settings["autoLeave"] == True:
                line.leaveRoom(op.param1)
                                     
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
            	if settings["winvite"] == True:
                     if msg._from in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = line.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 line.sendMessage(msg.to,"-> " + _name + " \nทำการเชิญสำเร็จ")
                                 break
                             elif invite in settings["blacklist"]:
                                 line.sendMessage(msg.to,"ขออภัย, " + _name + " บุคคนนี้อยู่ในรายการบัญชีดำ")
                                 line.sendMessage(msg.to,"ใช้คำสั่ง!, \n➡ล้างดำ➡ดึง" )
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     line.findAndAddContactsByMid(target)
                                     line.inviteIntoGroup(msg.to,[target])
                                     line.sendMessage(msg.to,"เชิญคนนี้สำเร็จแล้ว : \n➡" + _name)
                                     settings["winvite"] = False
                                     break
                                 except:
                                     try:
                                         line.findAndAddContactsByMid(invite)
                                         line.inviteIntoGroup(op.param1,[invite])
                                         settings["winvite"] = False
                                     except:
                                         line.sendMessage(msg.to,"😧ตรวจพบข้อผิดพลาดที่ไม่ทราบสาเหตุ😩อาจเป็นได้ว่าบัญชีของคุณถูกแบนเชิญ😨")
                                         settings["winvite"] = False
                                         break

        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
               if settings["wblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        line.sendMessage(msg.to,"รับทราบ")
                        settings["wblack"] = False
                    else:
                        settings["commentBlack"][msg.contentMetadata["mid"]] = True
                        settings["wblack"] = False
                        line.sendMessage(msg.to,"decided not to comment")

               elif settings["dblack"] == True:
                   if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        del settings["commentBlack"][msg.contentMetadata["mid"]]
                        line.sendMessage(msg.to,"ลบจากรายการที่ถูกแบนแล้ว")
                        settings["dblack"] = False

                   else:
                        settings["dblack"] = False
                        line.sendMessage(msg.to,"Tidak Ada Dalam Daftar Blacklist")
               elif settings["wblacklist"] == True:
                 if msg._from in admin: 
                   if msg.contentMetadata["mid"] in settings["blacklist"]:
                        line.sendMessage(msg.to,"Sudah Ada")
                        settings["wblacklist"] = False
                   else:
                        settings["blacklist"][msg.contentMetadata["mid"]] = True
                        settings["wblacklist"] = False
                        line.sendMessage(msg.to,"เพิ่มบัญชีนี้ในรายการสีดำเรียบร้อยแล้ว")

               elif settings["dblacklist"] == True:
                 if msg._from in admin: 
                   if msg.contentMetadata["mid"] in settings["blacklist"]:
                        del settings["blacklist"][msg.contentMetadata["mid"]]
                        line.sendMessage(msg.to,"เพิ่มบัญชีนี้ในรายการสีขาวเรียบร้อยแล้ว")
                        settings["dblacklist"] = False

                   else:
                        settings["dblacklist"] = False
                        line.sendMessage(msg.to,"Tidak Ada Dalam Da ftar Blacklist")
                               
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != line.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
#==============================================================================#
                if ".พูด " in msg.text.lower():
                    spl = re.split(".พูด ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        mts = spl[1]
                        mtsl = mts.split()
                        mtsTimeArg = len(mtsl) - 1
                        mtsTime = mtsl[mtsTimeArg]
                        del mtsl[mtsTimeArg]
                        mtosay = " ".join(mtsl)
                        global Rapid1To
                        Rapid1To = msg.to
                        RapidTime = mtsTime
                        rmtosay = []
                        for count in range(0,int(RapidTime)):
                            rmtosay.insert(count,mtosay)
                        p = Pool(20)
                        p.map(Rapid1Say,rmtosay)
                        p.close()
                elif msg.text in ["คำสั่ง","สกิล","ค","h"]:
                    myHelp = myhelp()
                    line.sendMessage(to, str(myHelp))
              #      line.sendMessage(msg.to, None, contentMetadata={"STKID":"8385664","STKPKGID":"1206431","STKVER":"2"}, contentType=7)
                    sendMessageWithMention(to, lineMID)
                    line.sendMessage(to, "🌀 ฟรุ้งฟริ้ง " +datetime.today().strftime('%H:%M:%S')+ "™ 🌀") 
                elif msg.text in ["คำสั่ง1","สกิล1","ค11","h1"]:
                    helpSet = helpset()
                    line.sendMessage(to, str(helpSet))
                    sendMessageWithMention(to, lineMID)
                    line.sendMessage(to, "🌀 ฟรุ้งฟริ้ง " +datetime.today().strftime('%H:%M:%S')+ "™ 🌀") 
              #      line.sendMessage(msg.to, None, contentMetadata={"STKID":"8385664","STKPKGID":"1206431","STKVER":"2"}, contentType=7)
                elif msg.text in ["คำสั่ง2","สกิล2","ค22","h2"]:
                    listGrup = listgrup()
                    line.sendMessage(to, str(listGrup))
                    sendMessageWithMention(to, lineMID)
                    line.sendMessage(to, "🌀 ฟรุ้งฟริ้ง " +datetime.today().strftime('%H:%M:%S')+ "™ 🌀") 
              #      line.sendMessage(msg.to, None, contentMetadata={"STKID":"8385664","STKPKGID":"1206431","STKVER":"2"}, contentType=7)
                elif msg.text in ["คำสั่ง3","สกิล3","ค33","h3"]:
                    helpSetting = helpsetting()
                    line.sendMessage(to, str(helpSetting))
                    sendMessageWithMention(to, lineMID)
                    line.sendMessage(to, "🌀 ฟรุ้งฟริ้ง " +datetime.today().strftime('%H:%M:%S')+ "™ 🌀") 
              #      line.sendMessage(msg.to, None, contentMetadata={"STKID":"8385664","STKPKGID":"1206431","STKVER":"2"}, contentType=7)
                elif msg.text in ["คำสั่ง4","สกิล4","ค44","h4"]:
                    socMedia = socmedia()
                    line.sendMessage(to, str(socMedia))
                    sendMessageWithMention(to, lineMID)
                    line.sendMessage(to, "🌀 ฟรุ้งฟริ้ง " +datetime.today().strftime('%H:%M:%S')+ "™ 🌀") 
              #      line.sendMessage(msg.to, None, contentMetadata={"STKID":"8385664","STKPKGID":"1206431","STKVER":"2"}, contentType=7)
                elif msg.text in ["คำสั่ง5","สกิล5","ค55","h5"]:
                    helpTextToSpeech = helptexttospeech()
                    line.sendMessage(to, str(helpTextToSpeech))
                    sendMessageWithMention(to, lineMID)
                    line.sendMessage(to, "🌀 ฟรุ้งฟริ้ง " +datetime.today().strftime('%H:%M:%S')+ "™ 🌀") 
              #      line.sendMessage(msg.to, None, contentMetadata={"STKID":"8385664","STKPKGID":"1206431","STKVER":"2"}, contentType=7)
                elif msg.text in ["คำสั่ง6","สกิล6","ค66","h6"]:
                    helpLanguange = helplanguange()
                    line.sendMessage(to, str(helpLanguange))
                    sendMessageWithMention(to, lineMID)
                    line.sendMessage(to, "🌀 ฟรุ้งฟริ้ง " +datetime.today().strftime('%H:%M:%S')+ "™ 🌀") 
               #     line.sendMessage(msg.to, None, contentMetadata={"STKID":"8385664","STKPKGID":"1206431","STKVER":"2"}, contentType=
#==============================================================================#
                elif msg.text in ["วัดรอบ","แรงม้า"]:
                    start = time.time()
                    line.sendMessage(to, "✯:::[[[ ®-ความจัดรอบเครื่อง ]]]:::✯")
                    line.sendMessage(msg.to,"❂•••••••••✧แ.ร.ง.ม้.า✧••••••••••❂")
                    elapsed_time = time.time() - start
                    line.sendMessage(msg.to, "[ %s Sec ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
                elif msg.text in ["Sp","sp","speed","Speed"]:
                    start = time.time()
                    line.sendMessage(to, "■•■•♡Spëed Tëst♡•■•■")
                    line.sendMessage(msg.to,"●•➤➤➤➤➤➤➤➤➤➤➤➤")
                    elapsed_time = time.time() - start
                    line.sendMessage(msg.to, "[ %s Sec ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
                elif text.lower() == 'เริ่มใหม่':
                    line.sendMessage(to, "กำลังเริ่มต้นใหม่ ... โปรดรอสักครู่ ..")
                    line.sendMessage(to, "Success Restarting.")
                    restartBot()
                elif msg.text.lower().startswith("พูด "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'th'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("คอล "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = line.getGroup(to)
                    for x in range(jml):
                        members = [mem.mid for mem in group.members]
                        line.acquireGroupCallRoute(to)
                        line.inviteIntoGroupCall(to, contactIds=members)
                    else:
                        line.sendMessage(to, "มาเล่นกันเถอะ ^_^".format(str(jml)))
                elif msg.text in ["เทส","เทสบอท"]:
                    line.sendMessage(to, "   ✯͜͡✯•ֆҽℓƒ-β❂T-ℒįℳ•✯͜͡✯\n─━─━━•≪❂≫•━━─━─")
                    line.sendMessage(to, "กำลังโหลด:▒...0%")
                    line.sendMessage(to, "█▒... 10.0%")
                    line.sendMessage(to, "██▒... 20.0%")
                    line.sendMessage(to, "███▒... 30.0%")
                    line.sendMessage(to, "████▒... 40.0%")
                    line.sendMessage(to, "█████▒... 50.0%")
                    line.sendMessage(to, "██████▒... 60.0%")
                    line.sendMessage(to, "███████▒... 70.0%")
                    line.sendMessage(to, "████████▒... 80.0%")
                    line.sendMessage(to, "█████████▒... 90.0%")
                    line.sendMessage(to, "███████████..100.0%")
                    line.sendMentionFooter(to, '•─ ͜͡✫ѕєʟғвот[ ᴀ̶̲̅ ]κɪcκєʀ ͜͡✫─•\n', sender, "https://line.me/ti/p/~gu.11", "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName);line.sendMessage(to, line.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+line.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~gu.11', 'type': 'mt', 'subText': settings["c"], 'a-installUrl': 'https://line.me/ti/p/~gu.11', 'a-installUrl': ' https://line.me/ti/p/~gu.11', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~gu.11', 'i-linkUri': 'https://line.me/ti/p/~gu.11', 'id': 'mt000000000a6b79f9', 'text': 'Khie', 'linkUri': 'https://line.me/ti/p/~gu.11'}, contentType=19)
                elif msg.text in ["รีเจนซี่","รีบอท"]:
                    line.sendMessage(to, "✯͜͡✯•ֆҽℓƒ-β❂T-ℒįℳ•✯͜͡✯")
                    line.sendMessage(to, "รอสักครู่คับ.................")
                    time.sleep(1)
                    line.sendMessage(to, "💙:::⭐ 3 ⭐:::💙")
                    time.sleep(1)
                    line.sendMessage(to, "💔:::⭐ 2 ⭐:::💔")
                    time.sleep(1)
                    line.sendMessage(to, "💚:::⭐ 1 ⭐:::💚")
                    line.sendMessage(to, "╭➣➣➣➣➣➣➣➣➣➣➣➣\n✯ รีสตาร์ทเรียบร้อยแล้วคับ™\n╰➣➣➣➣➣➣➣➣➣➣➣➣")
                    restartBot()
                    
                elif msg.text in ["บอทออน"]:
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    line.sendMessage(msg.to,"✧•••❂ เวลาทำงานของบอท ❂•••✧")
                    line.sendMessage(msg.to," ❂-ℒįℳ•➣Böt : 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™\n{}".format(str(runtime)))
                elif msg.text in ["เอจังข้อมูล","ข้อมูลเอจัง","ข้อมูล","ข้อมูลกู"]:
                    try:
                        arr = []
                        owner = "u669aa92773d33c22420105d4546fccdd"
                        creator = line.getContact(owner)
                        contact = line.getContact(lineMID)
                        grouplist = line.getGroupIdsJoined()
                        contactlist = line.getAllContactIds()
                        blockedlist = line.getBlockedContactIds()
                        ret_ = "✧•••••❂✧ข้อมูลคนน่ารัก✧❂•••••✧"
                        ret_ += "\n۝ ชื่อ ═ {}".format(contact.displayName)
                        ret_ += "\n۝ กลุ่ม ═ {}".format(str(len(grouplist)))
                        ret_ += "\n۝ เพื่อน ═ {}".format(str(len(contactlist)))
                        ret_ += "\n۝ บล็อค ═ {}".format(str(len(blockedlist)))
                   #   ret_ += "\n╠══[สถานะ] ═ {}".format(contact.statusMessage)
                        ret_ += "\n۝ ผู้สร้าง ═ {}".format(creator.displayName)
                        ret_ += "\n ••••✯🕸ֆҽℓƒ-β❂T-ℒįℳ🕸✯••••"
                        line.sendContact(to, owner)
                        line.sendReplyMessage(msg.id,to, str(ret_))
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
#==============================================================================#
                elif msg.text in ["ยิ้มเช็ค","เช็ค"]:
                    try:
                        ret_ = "✧•••••••••❂✧Â-jańg✧❂••••••••••✧\n    ♡•สถานะที่เปิดอยู่ตอนนี้คับ•♡\n✧••••••••••••❂✧✯✧❂•••••••••••••✧\n\n╭──┅━✥ ======= ✥━┅──"
                        if settings["autoAdd"] == True: ret_ += "\n♡•➤ ออโต้บล็อค✔"
                        else: ret_ += "\n♡•➤ ออโต้บล็อค   ✘ "
                        if settings["autoJoinTicket"] == True: ret_ += "\n♡•➤ มุดลิ้ง✔"
                        else: ret_ += "\n♡•➤ มุดลิ้ง   ✘ "
                        if settings["autoJoin"] == True: ret_ += "\n♡•➤ เข้าห้องออโต้ ✔"
                        else: ret_ += "\n♡•➤ เข้าห้องออโต้    ✘ "
                        if settings["Api"] == True: ret_ += "\n♡•➤ บอทApi✔"                               
                        else: ret_ += "\n♡•➤ บอทApi   ✘ "
                        if settings["Aip"] == True: ret_ += "\n♡•➤ แสกนคำพูด+คำสั่งบิน✔"
                        else: ret_ += "\n♡•➤ แสกนคำพูด+คำสั่งบิน   ✘ "
                        if settings["Wc"] == True: ret_ += "\n♡•➤ ข้อความต้อนรับสมาชิก ✔"
                        else: ret_ += "\n♡•➤ ข้อความต้อนรับสมาชิก    ✘ " 
                        if settings["Lv"] == True: ret_ += "\n♡•➤ ข้อความอำลาสมาชิก ✔"
                        else: ret_ += "\n♡•➤ ข้อความอำลาสมาชิก    ✘ "
                        if settings["Nk"] == True: ret_ += "\n♡•➤ ข้อความแจ้งคนลบ ✔"
                        else: ret_ += "\n♡•➤ ข้อความแจ้งคนลบ    ✘ "
                        if settings["autoCancel"]["on"] == True:ret_+="\n♡•➤ ปฏิเสธกลุ่มที่ > " + str(settings["autoCancel"]["members"]) + " คน ✔"
                        else: ret_ += "\n♡•➤ ปฏิเสธกลุ่มเชิญ    ✘ "
                        if settings["autoLeave"] == True: ret_ += "\n♡•➤ ออกแชทรวม ✔"
                        else: ret_ += "\n♡•➤ ออกแชทรวม ✘ "
                        if settings["autoRead"] == True: ret_ += "\n♡•➤ อ่านออโต้ ✔"
                        else: ret_ += "\n♡•➤ อ่านออโต้   ✘ "
                        if settings["checkContact"] == True: ret_ += "\n♡•➤ อ่านคท ✔"
                        else: ret_ += "\n♡•➤ อ่านคท        ✘ "
                        if settings["checkPost"] == True: ret_ += "\n♡•➤ เช็คโพส ✔"
                        else: ret_ += "\n♡•➤ เช็คโพส        ✘ "
                        if settings["checkSticker"] == True: ret_ += "\n♡•➤ Sticker ✔"
                        else: ret_ += "\n♡•➤ Sticker        ✘ "
                        if settings["detectMention"] == True: ret_ += "\n♡•➤ ตอบกลับคนแทค ✔"
                        else: ret_ += "\n♡•➤ ตอบกลับคนแทค ✘ "
                        if settings["potoMention"] == True: ret_ += "\n♡•➤ แสดงภาพคนแทค ✔"
                        else: ret_ += "\n♡•➤ แสดงภาพคนแทค ✘ "
                        if settings["kickMention"] == True: ret_ += "\n♡•➤ เตะคนแทค ✔"
                        else: ret_ += "\n♡•➤ เตะคนแทค ✘ "
                        if settings["delayMention"] == True: ret_ += "\n♡•➤ แทคกลับคนแทค ✔"
                        else: ret_ += "\n♡•➤ แทคกลับคนแทค ✘ "
                        if RfuProtect["inviteprotect"] == True: ret_ += "\n♡•➤ กันเชิญ ✔"
                        else: ret_ += "\n♡•➤ กันเชิญ ✘ "
                        if RfuProtect["cancelprotect"] == True: ret_ += "\n♡•➤ กันยกเชิญ ✔"
                        else: ret_ += "\n♡•➤ กันยกเชิญ ✘ "
                        if RfuProtect["protect"] == True: ret_ += "\n♡•➤ ป้องกัน ✔"
                        else: ret_ += "\n♡•➤ ป้องกัน ✘ "
                        if RfuProtect["linkprotect"] == True: ret_ += "\n♡•➤ ป้องกันเปิดลิ้ง ✔"
                        else: ret_ += "\n♡•➤ ป้องกันเปิดลิ้ง ✘ "
                        if RfuProtect["Protectguest"] == True: ret_ += "\n♡•➤ ป้องกันสมาชิก ✔"
                        else: ret_ += "\n♡•➤ ป้องกันสมาชิก ✘ "
                        if RfuProtect["Protectjoin"] == True: ret_ += "\n♡•➤ ป้องกันเข้ากลุ่ม ✔"
                        else: ret_ += "\n♡•➤ ป้องกันเข้ากลุ่ม ✘ "
                        ret_ += "\n╰──┅━✥ ======= ✥━┅──\n\n✧••••••••••••❂✧✯✧❂•••••••••••••✧\n      ✯🕸:ֆҽℓƒ-β❂T-ℒįℳ:🕸✯"
                        line.sendMessage(to, str(ret_))
                        sendMessageWithMention(to, lineMID)
                        line.sendMessage(to, "🌀 ฟรุ้งฟริ้ง " +datetime.today().strftime('%H:%M:%S')+ "™ 🌀") 
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
                        
                elif msg.text in ["เปิดบล็อค","เปิดบล็อก","เปิดบล๊อค"]:
                    settings["autoAdd"] = True
                    line.sendMessage(to, "✧••••••••••❂✧✯✧❂•••••••••••✧\n  เปิดระบบ Àutö Blőck: แล้วคับ\n✧••••••••••❂✧✯✧❂•••••••••••✧")
                    sendMessageWithMention(to, lineMID)
                    line.sendMessage(to, "🌀 ฟรุ้งฟริ้ง " +datetime.today().strftime('%H:%M:%S')+ "™ 🌀")
                elif msg.text in ["ปิดบล็อค","ปิดบล็อก","ปิดบล๊อค"]:
                    settings["autoAdd"] = False
                    line.sendMessage(to, "✧••••••••••❂✧✯✧❂•••••••••••✧\n   ปิดระบบ Àutö Blőck: แล้วคับ\n✧••••••••••❂✧✯✧❂•••••••••••✧")
                    sendMessageWithMention(to, lineMID)
                    line.sendMessage(to, "🌀 ฟรุ้งฟริ้ง " +datetime.today().strftime('%H:%M:%S')+ "™ 🌀")
                elif msg.text in ["เปิดแอร์"]:
                    settings["autoAdd"] = True
                    line.sendReplyMessage(msg.id,to, "  ✯͜͡✯•ֆҽℓƒ-β❂T-ℒįℳ•✯͜͡✯\n─━─━━•≪❂≫•━━─━─\n✲••เปิดแอร์อัติโนมัติแล้วคับ••✲\nอุณหภูมิคงที่ 24 องศาเซลเซียส")
                    sendMessageWithMention(to, lineMID)
                    line.sendMessage(to, "🌀 ฟรุ้งฟริ้ง " +datetime.today().strftime('%H:%M:%S')+ "™ 🌀")
                elif msg.text in ["ปิดแอร์"]:
                    settings["autoAdd"] = False
                    line.sendMessage(to, "  ✯͜͡✯•ֆҽℓƒ-β❂T-ℒįℳ•✯͜͡✯\n─━─━━•≪❂≫•━━─━─\n✲•• ปิดแอร์อัติโนมัติแล้วคับ ••✲\nอุณหภูมิคงที่ 29 องศาเซลเซียส")
                    sendMessageWithMention(to, lineMID)
                    line.sendMessage(to, "🌀 ฟรุ้งฟริ้ง " +datetime.today().strftime('%H:%M:%S')+ "™ 🌀")
                elif msg.text in ["เอจังเปิดเข้า","เปิดเข้า"]:
                    settings["autoJoin"] = True
                    line.sendMessage(to, "❂•เปิดเข้ากลุ่มอัติโนมัติแล้วคับ•❂\n A~jańg@Opën: 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")
                elif msg.text in ["เอจังปิดเข้า","ปิดเข้า"]:
                    settings["autoJoin"] = False
                    line.sendMessage(to,"❂•ปิดเข้ากลุ่มอัติโนมัติแล้วคับ•❂\n A~jańg@Clöse 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")
                elif "gcancel:" in msg.text:
                    try:
                        strnum = msg.text.replace("gcancel:","")
                        if strnum == "off":
                                settings["autoCancel"]["on"] = False
                                if settings["lang"] == "JP":
                                    line.sendMessage(msg.to,str(settings["eror"]))
                                else:
                                    line.sendMessage(msg.to,"关了邀请拒绝。要时开请指定人数发送")
                        else:
                                num =  int(strnum)
                                settings["autoCancel"]["on"] = True
                                if settings["lang"] == "JP":
                                    line.sendMessage(msg.to, " สมาชิกในกลุ่มที่ไม่ถึง" + strnum + "จะถูกปฏิเสธคำเชิญโดยอัตโนมัติ")
                                else:
                                    line.sendMessage(msg.to,strnum + "使人以下的小组用自动邀请拒绝")
                    except:
                        if settings["lang"] == "JP":
                                line.sendMessage(msg.to,str(settings["eror"]))
                        else:
                                line.sendMessage(msg.to,"Bizarre ratings")
                elif msg.text in ["เอจังเปิดออก","เปิดออก","เปิดแชทรวม"]:
                    settings["autoLeave"] = True
                    line.sendMessage(to,"❂•เปิดออกแชทรวมอัติโนมัติคับ•❂\n  A~jańg@Opën 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")
                elif msg.text in ["เอจังปิดออก","ปิดออก","ปิดแชทรวม"]:
                    settings["autoLeave"] = False
                    line.sendMessage(to,"❂•ปิดออกแชทรวมอัติโนมัติคับ•❂\n A~jańg@Clöse 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")
                elif msg.text in ["เปิดอ่าน"]:
                    settings["autoRead"] = True
                    line.sendMessage(to, "aütoRead : on •➣➣")
                    line.sendMessage(to, "❂• เปิดอ่านข้อความอัติโนมัติคับ •❂")
                elif msg.text in ["ปิดอ่าน"]:
                    settings["autoRead"] = False
                    line.sendMessage(to, "aütoRead : off •➣➣")
                    line.sendMessage(to, "❂• ปิดอ่านข้อความอัติโนมัติคับ •❂")
                elif msg.text in ["เปิดติ้ก","เปิดติ๊ก","เปิดติก","เอจังเปิดติก"]:
                    settings["checkSticker"] = True
                    line.sendMessage(to, "Sticket Check : on •➣➣")
                    line.sendMessage(to, "✯:: เปิดระบบเช็คสติกเกอร์คับ ::✯")
                elif msg.text in ["ปิดติ้ก","ปิดติ๊ก","ปิดติก","เอจังปิดติก"]:
                    settings["checkSticker"] = False
                    line.sendMessage(to, "Sticket Check : off •➣➣")
                    line.sendMessage(to, "✯:: ปิดระบบเช็คสติกเกอร์คับ ::✯")
                elif text.lower() == 'เปิดมุด':
                    settings["autoJoinTicket"] = True
                    line.sendMessage(to, "✯::Autojoin : Ticket enabled::✯")
                elif text.lower() == 'ปิดมุด':
                    settings["autoJoinTicket"] = False
                    line.sendMessage(to, "✯::Autojoin : Ticket disäbled::✯")
                elif msg.text in ["เปิดเสือก"]:
                    settings["unsendMessage"] = True
                    line.sendReplyMessage(msg.id,to, "✯:: เปิดระบบเสือกเรียบร้อยคับ ::✯")
                    sendMessageWithMention(to, lineMID)
                    line.sendMessage(to, "🌀 ฟรุ้งฟริ้ง " +datetime.today().strftime('%H:%M:%S')+ "™ 🌀")    
                elif msg.text in ["ปิดเสือก"]:
                    settings["unsendMessage"] = False
                    line.sendReplyMessage(msg.id,to, "✯:: ปิดระบบเสือกเรียบร้อยคับ ::✯")
                    sendMessageWithMention(to, lineMID)
                    line.sendMessage(to, "🌀 ฟรุ้งฟริ้ง " +datetime.today().strftime('%H:%M:%S')+ "™ 🌀")           
#==============================================================================#
                elif msg.text.lower() == "โปรโมท":
                    me = line.getContact(lineMID)
                    line.sendMessage(msg.to,"✿👇 ชื่อคนน่ารักเจ้าคับ 👇✿")
                    sendMessageWithMention(to, lineMID)
                    line.sendMessage(msg.to,"✯::: ♡•สเตตัสเจ้าคับ•♡ :::✯\n" + me.statusMessage)
                    line.sendContact(to, lineMID)
                    line.sendMessage(msg.to,"✯::: ♡•รูปคนน่ารักเจ้าคับ•♡ :::✯")
                    line.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                    line.sendMessage(msg.to,"✯::: ♡•ปกคนน่ารักเจ้าคับ•♡ :::✯")
                    cover = line.getProfileCoverURL(lineMID)
                    line.sendImageWithURL(msg.to, cover)
                    line.sendReplyMessage(msg.id,to,str(settings["comment"]) +"\n   ✥✥✥ ประวัติโดยย่อ ✥✥✥ \n✧••••••••••❂✧✯✧❂••••••••••✧\n •➣ สถานะโสดคับ\n •➣ จบโทจากอ็อกฟอร์ด\n •➣ นิสัยดีมากไม่เกรียน\n •➣ ชอบกินปีโป้\n •➣ รถซื้อกับข้าว เฟอรารี่,บีเอ็ม\n •➣ ชอบเล่นเกมเศรษฐี \n✧••••••••••❂✧✯✧❂••••••••••✧")
                elif msg.text in ["พี่ยิ้ม"]:
                    line.sendMentionFooter(to, '「SELF BOT」\n', sender, "https://line.me/ti/p/~yim_cjs", "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName);line.sendMessage(to, line.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+line.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~yim_cjs', 'type': 'mt', 'subText': settings["c"], 'a-installUrl': 'https://line.me/ti/p/~yim_cjs', 'a-installUrl': ' https://line.me/ti/p/~yim_cjs','a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~yim_cjs', 'i-linkUri': 'https://line.me/ti/p/~yim_cjs', 'id': 'mt000000000a6b79f9', 'text': 'Khie', 'linkUri': 'https://line.me/ti/p/~yim_cjs'}, contentType=19)
                elif msg.text in ["ณเดช","สุดหล่อ","หล่อสุด"]:
                    line.sendMentionFooter(to, '「ผู้สร้างเชลบอท」\n', sender, "https://line.me/ti/p/~yim_cjs", "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName);line.sendMessage(to, line.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+line.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~yim_cjs', 'type': 'mt', 'subText': "♡╬╬♡•ຟနุ้७ຟနิ้७•♡╬╬♡", 'a-installUrl': 'https://line.me/ti/p/~yim_cjs', 'a-installUrl': ' https://line.me/ti/p/~yim_cjs','a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~yim_cjs', 'i-linkUri': 'https://line.me/ti/p/~yim_cjs', 'id': 'mt000000000a6b79f9', 'text': 'Khie', 'linkUri': 'https://line.me/ti/p/~yim_cjs'}, contentType=19)       
                elif msg.text in ["คทกู"]:
                    sendMessageWithMention(to, lineMID)
                    line.sendContact(to, lineMID)
                    line.sendMessage(msg.to,"❂➣-ℒįℳ: 🕟 " +datetime.today().strftime('%H:%M:%S')+ "➤")
                elif msg.text in ["ดารา"]:
                    me = line.getContact(lineMID)
                    sendMessageWithMention(to, lineMID)                 
                    line.sendContact(to, lineMID)
                    line.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)             
                elif msg.text in ["ผส","ผู้สร้าง"]:
                    line.sendMessage(msg.to,"ผู้สร้างระบบ•➣➣➣➣➣➣➣➣\n   ❂••• ท่านอัจฉริยะเฮียยิ้ม •••❂\n➣➣➣➣➣➣➣➣• Chiväree™")
                    sendMessageWithMention(to, lineMID)
                    line.sendContact(to, "u669aa92773d33c22420105d4546fccdd")
                    line.sendMessage(msg.to,"👆 •คนนี้คับ• 🕟 " +datetime.today().strftime('%H:%M:%S')+ "➤")
                elif msg.text in ["โคสะนา","โฆษณา","โคนา"]:
                    line.sendReplyMessage(msg.id,to, "╭❂—————————————❂╮\n┃SELF BOT LINE : Jat Hotz67\n╰❂—————————————❂╯\n╭❂─────────────\n┃➣ ลูกเล่นมากกว่า 10,000 คำสั่ง\n┃➣ ราคา 10,000 ต่อปี\n┃➣ ระบบรันกลุ่มความเร็วแสง\n┃➣ ปีต่อไป 30,000\n┃➣ สปีดเทพเจ้า Super VPS™\n┃➣ ทีมบอทซึ่งเต็มไปด้วยอัจฉริยะ\n┃➣ ติดต่อทีมงานได้ 24 ชม.\n┃➣ อัพเดทระบบจากองค์กรนาซ่า\n┃➣ จำหน่ายสคริปบอทระดับโลก\n┃➣ กระโดดถีบหน้าพวกชอบแทค\n┃➣ CPU Core-i9 ยัดคาร์บู KR \n┃➣ ป้องกันการรันทุกรูปแบบ\n┃➣ มีระบบซักอบแห้งอัติโนมัติ\n┃➣ เป็นอมตะ ไม่มีวันตาย\n┃➣ มีดราก้อนบอลให้ฟื้นคืนชีพ\n╰❂─────────────\n╭❂—————————————❂╮\n┃ line.me/ti/p/~yim_cjs\n╰❂—————————————❂╯")
                    sendMessageWithMention(to, lineMID)
                    line.sendMessage(msg.to,"✿✿👇 กรุณาติดต่อ 👇✿✿")
                    line.sendContact(to, "u669aa92773d33c22420105d4546fccdd")
                    line.sendMessage(msg.to,"👆 •คนนี้คับ• 🕟 " +datetime.today().strftime('%H:%M:%S')+ "➤")
                elif msg.text in ["ไอดีกู"]:
                    line.sendReplyMessage(msg.id,to, "✯::: ♡•ไอดีคนน่ารักคับ•♡ ::✯\n" +  lineMID)
                elif msg.text in ["ชื่อกู"]:
                    me = line.getContact(lineMID)
                    line.sendReplyMessage(msg.id,to, "✯::: ♡•ชื่อคนน่ารักคับ•♡ :::✯\n" + me.displayName)
                elif msg.text in ["ตัสกู"]:
                    me = line.getContact(lineMID)
                    line.sendReplyMessage(msg.id,to, "✯::: ♡•สเตตัสคนน่ารักคับ•♡ :::✯\n" + me.statusMessage)
                elif msg.text in ["โปรกู","ดิสกู","รูปกู","ภาพกู"]:
                    line.sendReplyMessage(msg.id,to, "✯::: ♡•รูปคนน่ารักเจ้าคับ•♡ :::✯")
                    me = line.getContact(lineMID)
                    line.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif msg.text in ["วีดีโอกู"]:
                    line.sendReplyMessage(msg.id,to, "✯::: ♡•วีดีโอคนน่ารักคับ•♡ :::✯")
                    me = line.getContact(lineMID)
                    line.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                elif msg.text in ["ปกกู"]:
                    line.sendReplyMessage(msg.id,to, "🌀ปกคนน่ารักคับ " +datetime.today().strftime('%H:%M:%S')+ "™🌀") 
                    me = line.getContact(lineMID)
                    cover = line.getProfileCoverURL(lineMID)   
                    line.sendImageWithURL(msg.to, cover)
                elif text.lower() == 'คอมเม้น':
                    line.sendMessage(msg.to,str(settings["comment"]))
                elif text.lower() == 'ทักเข้า':
                    line.sendMessage(msg.to, str(settings["welcome"]))
                elif text.lower() == 'ทักออก':
                    line.sendMessage(msg.to, str(settings["bye"]))
                elif text.lower() == 'ทักเตะ':
                    line.sendMessage(msg.to, str(settings["kick"]))
                elif text.lower() == 'ข้อความแอด':
                    line.sendMessage(msg.to, str(settings["message"]))
                    sendMessageWithMention(to, lineMID)
                    line.sendMessage(to, "🌀 ฟรุ้งฟริ้ง " +datetime.today().strftime('%H:%M:%S')+ "™ 🌀")
                elif text.lower() == 'ข้อความแทค':
                    line.sendMessage(msg.to, str(settings["Respontag"]))
                elif text.lower() == 'แทคล่อง':
                    gs = line.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        line.sendReplyMessage(msg.id,to, "✯::•ไม่มีคนใส่ล่องหนในกลุ่มคับ•::✯")
                    else:
                        mc = ""
                        for target in targets:
                            mc += sendMessageWithMention(to,target) + "\n"
                        line.sendMessage(to, mc)
                elif text.lower() == 'ไอดีล่อง':
                    gs = line.getGroup(to)
                    lists = []
                    for g in gs.members:
                        if g.displayName in "":
                            lists.append(g.mid)
                    if lists == []:
                        line.sendReplyMessage(msg.id,to, "✯::•ไม่มีคนใส่ล่องหนในกลุ่มคับ•::✯")
                    else:
                        mc = ""
                        for mi_d in lists:
                            mc += "->" + mi_d + "\n"
                        line.sendMessage(to,mc)
                elif text.lower() == 'คทล่อง':
                    gs = line.getGroup(to)
                    lists = []
                    for g in gs.members:
                        if g.displayName in "":
                            lists.append(g.mid)
                    if lists == []:
                        line.sendReplyMessage(msg.id,to, "✯::•ไม่มีคนใส่ล่องหนในกลุ่มคับ•::✯")
                    else:
                        for ls in lists:
                            contact = line.getContact(ls)
                            mi_d = contact.mid
                            line.sendContact(to, mi_d)

#==========================================================                            
                elif msg.text.lower().startswith("คท "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            mi_d = contact.mid
                            line.sendContact(msg.to, mi_d)
                            line.sendMessage(msg.to,"✯::[[[☝คนหน้าม่อคับ☝]]]::✯")
                elif msg.text.lower().startswith("ปก "):
                    if line != None:
                        if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = line.getProfileCoverURL(ls)
                                line.sendImageWithURL(msg.to, str(path))
                                line.sendMessage(msg.to,"🌀ปกคนหน้าม่อคับ " +datetime.today().strftime('%H:%M:%S')+ "™🌀") 
                elif msg.text.lower().startswith("รูป "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + line.getContact(ls).pictureStatus
                            line.sendImageWithURL(msg.to, str(path))
                            line.sendMessage(to, "🌀รูปคนหน้าม่อคับ " +datetime.today().strftime('%H:%M:%S')+ "™🌀") 
                elif msg.text.lower().startswith("ไอดี "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = ""
                        for ls in lists:
                            ret_ += "✯::: ♡•ไอดีคนหน้าม่อคับ•♡ :::✯\n" + ls
                        line.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("ชื่อ "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            line.sendMessage(msg.to, "☆::❂•ชื่อคนหน้าม่อคับ•❂::☆\n" + contact.displayName)
                elif msg.text.lower().startswith("ตัส "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            line.sendMessage(msg.to, "☆::❂•สเตตัสคนหน้าม่อคับ•❂::☆\n{}" + contact.statusMessage)
#==========================================================================
                elif ".โพส " in msg.text:
                    tl_text = msg.text.replace(".โพส ","")
                    line.sendMessage(msg.to,"line://home/post?userMid="+lineMID+"&postId="+line.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
                
                elif "โคลนนิ่ง " in msg.text:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                    for target in targets:
                        try:
                            contact = line.getContact(target)
                            X = contact.displayName
                            profile = line.getProfile()
                            profile.displayName = X
                            line.updateProfile(profile)
                            line.sendMessage(msg.to, "╭➣➣➣➣➣➣➣➣➣➣➣\n✯  เริ่มทำการโคลนนิ่งคับ®\n╰➣➣➣➣➣➣➣➣➣➣➣")
                        #---------------------------------------
                            Y = contact.statusMessage
                            lol = line.getProfile()
                            lol.statusMessage = Y
                            line.updateProfile(lol)
                        #---------------------------------------
                            settings["changePictureProfile"] = True
                            me = line.getContact(target)     
                            line.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                        except Exception as e:
                            line.sendMessage(msg.to, "Failed!")
                            print (e)

                elif "คืนร่าง" in msg.text:
                    if msg._from in admin:
                            try:
                                h = open('mydn.txt',"r")
                                name = h.read()
                                h.close()
                                x = name
                                profile = line.getProfile()
                                profile.displayName = x
                                line.updateProfile(profile)
                                i = open('mysm.txt',"r")
                                sm = i.read()
                                i.close()
                                y = sm
                                cak = line.getProfile()
                                cak.statusMessage = y
                                line.updateProfile(cak)
                                line.sendMessage(msg.to, "คืนได้แค่ชื่อกับตัสนะ😂😂")

                            except Exception as e:
                                line.sendMessage(msg.to,"การคืนร่างล้มเหลว!")
                                print (e)       
#===========================================================================
                elif msg.text in ["Allprotect on","เปิดกทม","เปิดระบบป้องกัน","เปิดพรบฉุกเฉิน"]:
                        settings["kickMention"] = True
                        settings["Aip"] = False
                        RfuProtect["protect"] = True
                        RfuProtect["cancelprotect"] = True
                        RfuProtect["inviteprotect"] = True
                        RfuProtect["linkprotect"] = True
                        RfuProtect["Protectguest"] = True
                        RfuProtect["Protectjoin"] = True
                        line.sendMessage(to,"❂• เปิดระบบป้องกันทั้งหมดคับ •❂\n  A~jańg@Opën 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")

                elif msg.text in ["Allprotect off","ปิดกทม","ปิดระบบป้องกัน","ปิดพรบฉุกเฉิน"]:
                        settings["kickMention"] = False
                        settings["Aip"] = False
                        RfuProtect["protect"] = False
                        RfuProtect["cancelprotect"] = False
                        RfuProtect["inviteprotect"] = False
                        RfuProtect["linkprotect"] = False
                        RfuProtect["Protectguest"] = False
                        RfuProtect["Protectjoin"] = False
                        line.sendMessage(to,"❂• ปิดระบบป้องกันทั้งหมดคับ •❂\n A~jańg@Clöse 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")

                elif msg.text in ["Allmsg on","เปิดข้อความ"]:
                        settings["Wc"] = True
                        settings["Lv"] = True
                        settings["Nk"] = True
                        settings["autoRead"] = True
                        settings["checkSticker"] = True
                        settings["checkContact"] = True
                        settings["checkPost"] = True
                        settings["potoMention"] = True
                        settings["detectMention"] = True
                        settings["delayMention"] = True
                        settings["Api"] = True
                        line.sendMessage(to,"❂• เปิดระบบข้อความทั้งหมดคับ •❂\n   A~jańg@Opën 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")

                elif msg.text in ["Allmsg off","ปิดข้อความ"]:
                        settings["Wc"] = False
                        settings["Lv"] = False
                        settings["Nk"] = False
                        settings["autoRead"] = True
                        settings["checkSticker"] = False
                        settings["checkContact"] = False
                        settings["checkPost"] = False
                        settings["detectMention"] = False
                        settings["potoMention"] = False
                        settings["delayMention"] = False
                        settings["Api"] = False
                        line.sendMessage(to,"❂• ปิดระบบข้อความทั้งหมดคับ •❂\n  A~jańg@Clöse 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")
#==============================================================================#
                elif msg.text.lower().startswith("เลียนแบบ "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            settings["mimic"]["target"][target] = True
                            line.sendMessage(to,"❂•• ระบบเริ่มการเลียนแบบคับ ••❂\n  A~jańg@Opën: 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")
                            break
                        except:
                            line.sendMessage(msg.to,"Added Target Fail !")
                            break
                elif msg.text.lower().startswith("เลิกเลียนแบบ "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del settings["mimic"]["target"][target]
                            line.sendMessage(to,"❂•• ระบบเลิกการเลียนแบบคับ ••❂\n  A~jańg@Clöse 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")
                            break
                        except:
                            line.sendMessage(msg.to,"Deleted Target Fail !")
                            break

                elif text.lower() == 'ลิสเลียนแบบ':
                    if settings["mimic"]["target"] == {}:
                        line.sendMessage(to, "🌀 ฟรุ้งฟริ้ง " +datetime.today().strftime('%H:%M:%S')+ "™ 🌀") 
                    else:
                        mc = "╔══[ Mimic List ]"
                        for mi_d in settings["mimic"]["target"]:
                            mc += "\n╠ "+line.getContact(mi_d).displayName
                        line.sendMessage(msg.to,mc + "\n╚══[ Finish ]")

                elif "สกิลเลียนแบบ" in msg.text.lower():
                    sep = text.split(" ")
                    mic = text.replace(sep[0] + " ","")
                    if mic == "on":
                        if settings["mimic"]["status"] == False:
                            settings["mimic"]["status"] = True
                            line.sendReplyMessage(msg.id,to, "✯::[[[ ®-เปิดสกิลเลียนแบบคับ ]]]::✯")
                    elif mic == "off":
                        if settings["mimic"]["status"] == True:
                            settings["mimic"]["status"] = False
                            line.sendReplyMessage(msg.id,to, "✯::[[[ ®-ปิดสกิลเลียนแบบคับ ]]]::✯")
#---------------------------------------------------------------------------------------------------------------------------------+                     
                elif 'เพลย์สโต ' in msg.text.lower():
                        chivaree = msg.text.lower().replace('เพลย์สโต ',"")
                        line.sendMessage(msg.to,"➤ ֆҽℓƒ-β❂T-ℒįℳ ➤")
                        line.sendMessage(msg.to,"❂➣-รอสักครู่คับ...........")
                        line.sendMessage(msg.to,"ผลจากการค้นหา : "+chivaree+"\nจาก : Google Play\nลิ้งโหลด : https://play.google.com/store/search?q=" + chivaree)
                        line.sendMessage(to, "🌀 ค้นหาสำเร็จคับ " +datetime.today().strftime('%H:%M:%S')+ "™ 🌀")
                elif 'ฟังเพลง ' in msg.text.lower():
                        chivaree = msg.text.lower().replace('ฟังเพลง ',"")
                        line.sendMessage(msg.to,"➤ ֆҽℓƒ-β❂T-ℒįℳ ➤")
                        line.sendMessage(msg.to,"🌀รอสักครู่คับ 🕒 " +datetime.today().strftime('%H:%M:%S')+ "🌀")
                        line.sendMessage(msg.to,"ผลจากการค้นหา : "+chivaree+"\n: https://m.youtube.com/results?search_query=เพลง" + chivaree)
                        line.sendMessage(msg.to,"🎧::รับฟังได้เลยคับ จุ้ฟป้อก::🎧")
                elif 'github ' in msg.text.lower():
                        chivaree = msg.text.lower().replace('github ',"")
                        line.sendMessage(msg.to,"➤ ֆҽℓƒ-β❂T-ℒįℳ ➤")
                        line.sendMessage(msg.to,"❂➣-รอสักครู่คับ...........")
                        line.sendMessage(msg.to,"ผลจากการค้นหา : "+chivaree+"\nจาก : GitHub\nลิ้ง : https://github.com/search?q=" + chivaree)
                        line.sendMessage(to, "🌀 ค้นหาสำเร็จคับ " +datetime.today().strftime('%H:%M:%S')+ "™ 🌀") 
                elif 'เฟสบุค ' in msg.text.lower():
                        chivaree = msg.text.lower().replace('เฟสบุค ',"")
                        line.sendMessage(msg.to,"➤ ֆҽℓƒ-β❂T-ℒįℳ ➤")
                        line.sendMessage(msg.to,"❂➣-รอสักครู่คับ...........")
                        line.sendMessage(msg.to,"ผลจากการค้นหา : "+chivaree+"\nจาก : เฟสบุค\nลิ้ง : https://m.facebook.com/search/top/?q=" + chivaree)
                        line.sendMessage(to, "🌀 ค้นหาสำเร็จคับ " +datetime.today().strftime('%H:%M:%S')+ "™ 🌀") 
#===================================================================
                elif "เกรียน " in msg.text:
                    txt = msg.text.split(" ")
                    jmlh = int(txt[2])
                    teks = msg.text.replace("เกรียน "+str(txt[1])+" "+str(jmlh)+" ","")
                    tulisan = jmlh * (teks+"\n")
                    if txt[1] == "on":
                        if jmlh <= 100000:
                           for x in range(jmlh):
                               line.sendMessage(msg.to, teks)
                        else:
                           line.sendMessage(msg.to, "Out of Range!")
                    elif txt[1] == "off":
                        if jmlh <= 100000:
                            line.sendMessage(msg.to, tulisan)
                        else:
                            line.sendMessage(msg.to, "Out Of Range!")

                elif "Spam " in msg.text:
                    txt = msg.text.split(" ")
                    jmlh = int(txt[2])
                    teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                    tulisan = jmlh * (teks+"\n")
                    if txt[1] == "on":
                        if jmlh <= 100000:
                           for x in range(jmlh):
                               line.sendMessage(msg.to, teks)
                        else:
                           line.sendMessage(msg.to, "Out of Range!")
                    elif txt[1] == "off":
                        if jmlh <= 100000:
                            line.sendMessage(msg.to, tulisan)
                        else:
                            line.sendMessage(msg.to, "Out Of Range!")
                elif "รันคอล" in msg.text.lower():
                    if msg.toType == 2:
                        sep = msg.text.split(" ")
                        resp = msg.text.replace(sep[0] + " ","")
                        num = int(resp)
                        try:
                            line.sendReplyMessage(msg.id,to, "✯͜͡✯•ֆҽℓƒ-β❂T-ℒįℳ•✯͜͡✯")
                            line.sendMessage(msg.to,"☎•ระบบเริ่มรันคอลคับ•☎")
                            line.sendMessage(to, "📞........🔆 " +datetime.today().strftime('%H:%M:%S')+ "™ ") 
                        except:
                            pass
                        for var in range(num):
                            group = line.getGroup(msg.to)
                            members = [mem.mid for mem in group.members]
                            line.acquireGroupCallRoute(msg.to)
                            line.inviteIntoGroupCall(msg.to, contactIds=members)
                        line.sendMessage(msg.to,"🌀•รันคอลเสร็จเรียบร้อยคับ•🌀")
                elif msg.text.lower().startswith("สแปมคอล"):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = line.getGroup(to)
                    for x in range(jml):
                        members = [mem.mid for mem in group.members]
                        line.acquireGroupCallRoute(to)
                        line.inviteIntoGroupCall(to, contactIds=members)
                    else:
                        line.sendMessage(to, "🌀•สแปมคอลเรียบร้อยคับ•🌀".format(str(jml)))
 #==============================================================
                elif msg.text.lower().startswith("ทัก "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    for x in range(jml):
                        name = line.getContact(to)
                        RhyN_(to, name.mid)
#==========================================================
# โหมดคำสั่งเอจังคับ~•💜.💙.💚.💖.💜.💔  จัดทำโดยคุณชิวารี.  •••®©•••
#==========================================================
                elif msg.text in ["กู","คนหล่อ","ใสใส","คนน่ารัก"]:
                    line.sendContact(to, lineMID)
                    line.sendMessage(msg.to,"❂➣ℒįℳ 🕟 " +datetime.today().strftime('%H:%M:%S')+ "➤")
#------------------------------------------------------------------------------------------------------------
                elif msg.text in ["ฉายากู","ฉายาเอจัง","ฉายา"]:
                    line.sendReplyMessage(msg.id,to, "✧••••••••••❂✧✯✧❂••••••••••✧\n\n🔸 ข้าคือเทพแห่งหนังเอ็กซ์\n🔸 ผู้บ้ากามและมีความหื่น\n🔸 ที่แฝงไปด้วยความแอ๊บแบ๊ว\n\n •🐍•🐍•🐍•🐍•🐍•🐍•🐍•🐍•\n✧••••••••••❂✧✯✧❂••••••••••✧")
                    sendMessageWithMention(to, lineMID)
                    line.sendMessage(msg.to, "🌀 ฟรุ้งฟริ้ง " +datetime.today().strftime('%H:%M:%S')+ "™ 🌀")
                elif msg.text in ["ซักอบรีด","ระบบซักผ้า","ระบบซัก","โตชิบา","โตชิบ้า"]:
                    line.sendReplyMessage(msg.id,to, "  ✯͜͡✯•--┅═हईツ☆❦ℒįℳ❦ツ❈ईह═┅ •✯͜͡✯\n─━─━━•≪❂≫•━━─━─\n✲••  ระบบเริ่มซักอบแห้งคับ  ••✲\n🌟•เวลาในการซัก 🕚 : 45 นาที \n🌟•ปั่นแห้งระบบไอน้ำ 15 นาที\n🌟•ตากเองอัติโนมัติรวม 2 ชมคับ")
                    sendMessageWithMention(to, lineMID)
                    line.sendMessage(to, "🌀 ฟรุ้งฟริ้ง " +datetime.today().strftime('%H:%M:%S')+ "™ 🌀")
                elif msg.text in ["ไม่ว่าง","ไม่ว่าง","พี่ไม่ว่าง"]:
                    line.sendReplyMessage(msg.id,to, "    ✯͜͡✯•No•No•No•No•No•✯͜͡✯\n✧•••••••••••❂✧✯✧❂••••••••••••✧\n  ✲ท่านอัจฉริยะเจตต์ไม่ว่างตอบ✲\n\n เนื่องจากติดธุรกิจปลากัด100ล้าน\n  💙•💙• ขออภัยอย่างยิ่ง •💙•💙\n\n🔸งดถ่ายแบบทั่วราชอาณาจักร🔸\n✧•••••••••••❂✧✯✧❂••••••••••••✧")
                    sendMessageWithMention(to, lineMID)
                    line.sendMessage(msg.to, "🌀 ฟรุ้งฟริ้ง " +datetime.today().strftime('%H:%M:%S')+ "™ 🌀")
#------------------------------------------------------------------------------------------------------------
                #แก้ดีๆ ระวังไฟล์พังไม่รุ้นะ. 5555555
#------------------------------------------------------------------------------------------------------------
                elif msg.text in ["ไฮสปีด","สปีดไฮ","สปีด","สปูด","สปาด","สปุด"]:
                    line.sendMessage(msg.to, "♡╬╬♡•ຟနุ้७ຟနิ้७•♡╬╬♡")
                    line.sendMessage(msg.to, "•─ ͜͡✯͜͡S͜͡p͜͡e͜͡e͜͡e͜͡d✯͜͡ѕ͜͡є͜͡ʟ͜͡ғ͜͡в͜͡о͜͡т͜͡✯─•")
                    start = time.time()
                    time.sleep(0.01)
                    elapsed_time = time.time() - start
                    line.sendMessage(msg.to, "%sseconds" % (elapsed_time)) 
#------------------------------------------------------------------------------------------------------------
                elif msg.text in ["4g",".357"]:
                    line.sendMessage(msg.to, "■•■•■•■ O.K. ■•■•■•■")
                    line.sendMessage(msg.to, "✧•••••❂Tëst Speëd❂•••••✧")
                    start = time.time()
                    time.sleep(0.01)
                    elapsed_time = time.time() - start
                    line.sendMessage(msg.to, "%sseconds" % (elapsed_time))
#-------------------------------------------++++++++++++------------------------------------------
                elif msg.text in ["8g","เทสจรวด","Ais","3bb","Dtac"]:
                    line.sendMessage(msg.to, "❂❂❂❂• --┅═हईツ☆❦ℒįℳ❦ツ❈ईह═┅  •❂❂❂❂")
                    line.sendMessage(msg.to, "•••••••• Tëst $peed ••••••••")
                    start = time.time()
                    time.sleep(0.01)
                    elapsed_time = time.time() - start
                    line.sendMessage(msg.to, "%sseconds" % (elapsed_time))
#-------------------------------------------------------------------------------------------------------------
                elif msg.text in ["9g",".45"]:
                    line.sendMessage(msg.to, "❂ℒįℳ•➣➣➣➣➣➣➣")
                    line.sendMessage(msg.to, "❂•➣➣➣ S.p.ë.e.d ➣➣➣➣")
                    start = time.time()
                    time.sleep(0.01)
                    elapsed_time = time.time() - start
                    line.sendMessage(msg.to, "%sseconds" % (elapsed_time))
#--------------------------------------------------------------------------------------------------------------
                elif msg.text in ["10g","M16"]:
                    line.sendMessage(msg.to, "✧•••••••••❂✧✯✧❂••••••••••✧\n     ♡♡ HELLO KITTY ♡♡\n✧•••••••••❂✧✯✧❂••••••••••✧")
                    line.sendMessage(msg.to, "❂•➣➣➣ S.p.ë.e.d ➣➣➣➣")
                    start = time.time()
                    time.sleep(0.002)
                    elapsed_time = time.time() - start
                    line.sendMessage(msg.to, "%sseconds" % (elapsed_time))
#-------------------------------------------------------------------------------------------------------------
                elif msg.text in ["11g","Hk"]:
                    line.sendMessage(msg.to, "✧•••••••••❂✧✯✧❂••••••••••✧\n     Tëst : Prëmium Spëed™\n✧•••••••••❂✧✯✧❂••••••••••✧")
                    line.sendMessage(msg.to, "❂•➣➣➣ S.p.ë.e.d ➣➣➣➣")
                    start = time.time()
                    time.sleep(0.01)
                    elapsed_time = time.time() - start
                    line.sendMessage(msg.to, "%sseconds" % (elapsed_time))
#-------------------------------------------------------------------------------------------------------------
                elif msg.text in ["12g",".38","สปิด","สปีด","สเปด","สแปด","สปัด"]:
                    line.sendMessage(msg.to, "➤➤ ֆҽℓƒ-β❂T-ℒįℳ ➤➤")
                    line.sendMessage(to,"❂•Speed•❂ : 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")
                    start = time.time()
                    time.sleep(0.01)
                    elapsed_time = time.time() - start
                    line.sendMessage(msg.to, "%sseconds" % (elapsed_time))
#--------------------------------------------------------------------------------------------------------------
                elif msg.text in ["13g",".22"]:
                    line.sendMessage(msg.to, "Hî Speëd:•➣➣➣➣➣➣➣➣")
                    line.sendMessage(msg.to, "❂ℒįℳ•➣➣➣➣➣➣➣")
                    start = time.time()
                    time.sleep(0.01)
                    elapsed_time = time.time() - start
                    line.sendMessage(msg.to, "%sseconds" % (elapsed_time))
#------------------------------------------------------------------------------------------------------------
                elif msg.text in ["รถเต่า","Bmx","Bmw","Benz","ปอร์เช่","เบ้นซ์","จากัวร์","เฟอร์รารี่"]:
                    line.sendMessage(msg.to, "■•■•■• 3500cc •■•■•■")
                    line.sendMessage(msg.to, "●•➤➤➤➤➤➤➤➤➤➤")
                    line.sendMessage(msg.to, "●•➤➤➤➤➤➤➤➤➤➤➤➤")
                    start = time.time()
                    time.sleep(0.01)
                    elapsed_time = time.time() - start
                    line.sendMessage(msg.to, "%sseconds" % (elapsed_time))
#-----------------------------------------------------------------------------------------------------------------
##   คำสั้งเกมไฮโล กับเต้าปูปลา เปนคำสั่ง2ชั้น    แก้ดีๆ ระวังไฟล์พังไม่รุ้นะ. 555
#-----------------------------------------------------------------------------------------------------------------
                elif msg.text in ["ไฮโล","เปิดไฮโล","hilo","Hilo"]:
                    try:
                        chivaree = ['💔•💔• เริ่มเขย่าคับ •💔•💔','💙•💙• เริ่มเขย่าคับ •💙•💙','💚•💚• เริ่มเขย่าคับ •💚•💚','💜•💜• เริ่มเขย่าคับ •💜•💜','💛•💛• เริ่มเขย่าคับ •💛•💛','💘•💘• เริ่มเขย่าคับ •💘•💘']
                        chivaree1 = ['•💗•••• 1 ••••💗•','•💙•••• 1 ••••💙•','•💜•••• 1 ••••💜•','•💛•••• 1 ••••💛•','•💚•••• 1 ••••💚•','•💖•••• 1 ••••💖•']
                        chivaree2 = ['•💗•••• 2 ••••💗•','•💙•••• 2 ••••💙•','•💜•••• 2 ••••💜•','•💛•••• 2 ••••💛•','•💚•••• 2 ••••💚•','•💖•••• 2 ••••💖•']
                        chivaree3 = ['•💗•••• 3 ••••💗•','•💙•••• 3 ••••💙•','•💜•••• 3 ••••💜•','•💛•••• 3 ••••💛•','•💚•••• 3 ••••💚•','•💖•••• 3 ••••💖•']
                        chivareeA = ['   •1•1•1•1•','   •2•2•2•2•','   •3•3•3•3•','   •4•4•4•4•','   •5•5•5•5•','   •6•6•6•6•']
                        ret_ = random.choice(chivaree)
                        line.sendMessage(to, str(ret_))
                        ret_ = random.choice(chivaree3)
                        line.sendMessage(to, str(ret_))
                        ret_ = random.choice(chivaree2)
                        line.sendMessage(to, str(ret_))
                        ret_ = random.choice(chivaree1)
                        line.sendMessage(to, str(ret_))
                        line.sendMessage(msg.to, "🌀เปิดคับ🎲 " +datetime.today().strftime('%H:%M:%S')+ "🌀")
                        ret_ = "🎲•🎲•🎲•🎲\n" + random.choice(chivareeA) + "\n🎲•🎲•🎲•🎲"
                        line.sendMessage(to, str(ret_))
                        ret_ = "🎲•🎲•🎲•🎲\n" + random.choice(chivareeA) + "\n🎲•🎲•🎲•🎲"
                        line.sendMessage(to, str(ret_))
                        ret_ = "🎲•🎲•🎲•🎲\n" + random.choice(chivareeA) + "\n🎲•🎲•🎲•🎲"
                        line.sendMessage(to, str(ret_))
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
                elif msg.text in ["กุ้งปลา","เต้าปูปลา"]:
                    try:
                        chivaree = ['💔•💔• เริ่มการสุ่มคับ •💔•💔','💙•💙• เริ่มการสุ่มคับ •💙•💙','💚•💚• เริ่มการสุ่มคับ •💚•💚','💜•💜• เริ่มการสุ่มคับ •💜•💜','💛•💛• เริ่มการสุ่มคับ •💛•💛','💘•💘• เริ่มการสุ่มคับ •💘•💘']
                        chivaree1 = ['•💗•••• 1 ••••💗•','•💙•••• 1 ••••💙•','•💜•••• 1 ••••💜•','•💛•••• 1 ••••💛•','•💚•••• 1 ••••💚•','•💖•••• 1 ••••💖•']
                        chivaree2 = ['•💗•••• 2 ••••💗•','•💙•••• 2 ••••💙•','•💜•••• 2 ••••💜•','•💛•••• 2 ••••💛•','•💚•••• 2 ••••💚•','•💖•••• 2 ••••💖•']
                        chivaree3 = ['•💗•••• 3 ••••💗•','•💙•••• 3 ••••💙•','•💜•••• 3 ••••💜•','•💛•••• 3 ••••💛•','•💚•••• 3 ••••💚•','•💖•••• 3 ••••💖•']
                        chivareeX = ['🎃•🎃•🎃•🎃\n    • น้ำเต้า •\n🎃•🎃•🎃•🎃','🐓•🐓•🐓•🐓\n  •ไก่•ไก่•ไก่•\n🐓•🐓•🐓•🐓','🐯•🐯•🐯•🐯\n   •เสือ•เสือ•\n🐯•🐯•🐯•🐯','🦀•🦀•🦀•🦀\n   •ปู•ปู•ปู•ปู•\n🦀•🦀•🦀•🦀','🐠•🐠•🐠`🐠\n   •ปลา•ปลา•\n🐠•🐠•🐠•🐠','🦐•🦐•🦐•🦐\n  •กุ้ง•กุ้ง•กุ้ง•\n🦐•🦐•🦐•🦐']
                        ret_ = random.choice(chivaree)
                        line.sendMessage(to, str(ret_))
                        ret_ = random.choice(chivaree3)
                        line.sendMessage(to, str(ret_))
                        ret_ = random.choice(chivaree2)
                        line.sendMessage(to, str(ret_))
                        ret_ = random.choice(chivaree1)
                        line.sendMessage(to, str(ret_))
                        line.sendMessage(msg.to, "🌀เปิดคับ " +datetime.today().strftime('%H:%M:%S')+ "🌀")
                        ret_ = random.choice(chivareeX)
                        line.sendMessage(msg.to, str(ret_))
                        ret_ = random.choice(chivareeX)
                        line.sendMessage(msg.to, str(ret_))
                        ret_ = random.choice(chivareeX)
                        line.sendMessage(msg.to, str(ret_))
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
#----------------------------------------------------------------------------------------------------------
                elif msg.text in ["✲•เริ่มทำการเขย่าคับ•✲"]:
                    try:
                        chivaree = ['✯💜•Random•💜✯\n✯💜•Random•💜✯','✯💛•Random•💛✯\n✯💛•Random•💛✯','✯💗•Random•💗✯\n✯💗•Random•💗✯','✯💚•Random•💚✯\n✯💚•Random•💚✯','✯💙•Random•💙✯\n✯💙•Random•💙✯','✯💔•Random•💔✯\n✯💔•Random•💔✯']
                        chivaree8 = ['   •1•1•1•1•','   •2•2•2•2•','   •3•3•3•3•','   •4•4•4•4•','   •5•5•5•5•','   •6•6•6•6•']
                        ret_ = random.choice(chivaree)
                        line.sendMessage(to, str(ret_))
                        line.sendMessage(msg.to, "💘เปิดคับ " +datetime.today().strftime('%H:%M:%S')+ "💘")
                        ret_ = "🎲•🎲•🎲•🎲\n" + random.choice(chivaree8) + "\n🎲•🎲•🎲•🎲"
                        line.sendMessage(to, str(ret_))
                        ret_ = "🎲•🎲•🎲•🎲\n" + random.choice(chivaree8) + "\n🎲•🎲•🎲•🎲"
                        line.sendMessage(to, str(ret_))
                        ret_ = "🎲•🎲•🎲•🎲\n" + random.choice(chivaree8) + "\n🎲•🎲•🎲•🎲"
                        line.sendMessage(to, str(ret_))
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
                elif msg.text in ["✲•เริ่มทำการสุ่มเจ้าคับ•✲"]:
                    try:
                        chivaree = ['✯💜•Random•💜✯\n✯💜•Random•💜✯','✯💛•Random•💛✯\n✯💛•Random•💛✯','✯💗•Random•💗✯\n✯💗•Random•💗✯','✯💚•Random•💚✯\n✯💚•Random•💚✯','✯💙•Random•💙✯\n✯💙•Random•💙✯','✯💔•Random•💔✯\n✯💔•Random•💔✯']
                        chivareeZ = ['🎃•🎃•🎃•🎃\n    • น้ำเต้า •\n🎃•🎃•🎃•🎃','🐓•🐓•🐓•🐓\n  •ไก่•ไก่•ไก่•\n🐓•🐓•🐓•🐓','🐯•🐯•🐯•🐯\n   •เสือ•เสือ•\n🐯•🐯•🐯•🐯','🦀•🦀•🦀•🦀\n   •ปู•ปู•ปู•ปู•\n🦀•🦀•🦀•🦀','🐠•🐠•🐠`🐠\n   •ปลา•ปลา•\n🐠•🐠•🐠•🐠','🦐•🦐•🦐•🦐\n  •กุ้ง•กุ้ง•กุ้ง•\n🦐•🦐•🦐•🦐']
                        ret_ = random.choice(chivaree)
                        line.sendMessage(to, str(ret_))
                        line.sendMessage(msg.to, "💘เปิดคับ " +datetime.today().strftime('%H:%M:%S')+ "💘")
                        ret_ = random.choice(chivareeZ)
                        line.sendMessage(to, str(ret_))
                        ret_ = random.choice(chivareeZ)
                        line.sendMessage(to, str(ret_))
                        ret_ = random.choice(chivareeZ)
                        line.sendMessage(to, str(ret_))
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
#-------------------------------------------------------------------------------------------------------------
#        •••💛•💗•💚 โหมดพลังจิต จัดทำโดยเอจัง 💚•💗•💛•••
#--------------------------------------------------------------------------------------------------------------
                elif msg.text in ["ทานข้าวยัง","ทานข้าวกันไหม"]:
                    if msg.toType == 2:
                        group = line.getGroup(msg.to)
                    else:
                        group = line.getRoom(msg.to)
                    lists = [contact for contact in group.members]
                    for ls in lists:
                        anu = ls
                        mid  = "{}".format(ls)
                        text = "✲ ขอบคุณนะ กินขี้อิ่มแล้วจ้า ✲"
                        icon = "http://dl.profile.line.naver.jp/{}".format(anu.pictureStatus)
                        name = "{}".format(anu.displayName)
                        sendMessageCustom(msg.to, text, icon, name)
                elif msg.text in ["แสดงความเคารพ","ทำความเคารพ"]:
                    if msg.toType == 2:
                        group = line.getGroup(msg.to)
                    else:
                        group = line.getRoom(msg.to)
                    lists = [contact for contact in group.members]
                    for ls in lists:
                        anu = ls
                        mid  = "{}".format(ls)
                        text = "🔹• คาราวะลูกพี่ยิ้ม•🔹"
                        icon = "http://dl.profile.line.naver.jp/{}".format(anu.pictureStatus)
                        name = "{}".format(anu.displayName)
                        sendMessageCustom(msg.to, text, icon, name)
                elif msg.text in ["ขอเสียงเอฟซี","ขอเสียงแฟนคลับ"]:
                    if msg.toType == 2:
                        group = line.getGroup(msg.to)
                    else:
                        group = line.getRoom(msg.to)
                    lists = [contact for contact in group.members]
                    for ls in lists:
                        anu = ls
                        mid  = "{}".format(ls)
                        text = "🔶 F.C. พี่ยิ้มน่ารั้ก กรี๊ดๆๆ 🔶"
                        icon = "http://dl.profile.line.naver.jp/{}".format(anu.pictureStatus)
                        name = "{}".format(anu.displayName)
                        sendMessageCustom(msg.to, text, icon, name)
                elif msg.text in ["ยิ้มมาแล้ว"]:
                    if msg.toType == 2:
                        group = line.getGroup(msg.to)
                    else:
                        group = line.getRoom(msg.to)
                    lists = [contact for contact in group.members]
                    for ls in lists:
                        anu = ls
                        mid  = "{}".format(ls)
                        text = "🌟กรี๊ดไอดอลมา ขอลายเซ็นน่อย🌟"
                        icon = "http://dl.profile.line.naver.jp/{}".format(anu.pictureStatus)
                        name = "{}".format(anu.displayName)
                        sendMessageCustom(msg.to, text, icon, name)
                elif msg.text in ["ชมเค้าหน่อย","ขอความในใจ"]:
                    if msg.toType == 2:
                        group = line.getGroup(msg.to)
                    else:
                        group = line.getRoom(msg.to)
                    lists = [contact for contact in group.members]
                    for ls in lists:
                        anu = ls
                        mid  = "{}".format(ls)
                        text = "✲เฮียยิ้มสุดหล่อเลิศหล้าแห่งปฐพี✲"
                        icon = "http://dl.profile.line.naver.jp/{}".format(anu.pictureStatus)
                        name = "{}".format(anu.displayName)
                        sendMessageCustom(msg.to, text, icon, name)
#---------------------------------------------------------------------------------------------------------
                elif msg.text in ["✲• Aütó Mëssage •✲"]:
                    try:
                        chivaree1 = [' 💜•💜 คุณยิ้มไม่ว่างคับ 💜•💜',' 💚•💚 คุณยิ้มไม่ว่างคับ 💚•💚',' 💙•💙 คุณยิ้มไม่ว่างคับ 💙•💙',' 💔•💔 คุณยิ้มไม่ว่างคับ 💔•💔',' 💛•💛 คุณยิ้มไม่ว่างคับ 💛•💛',' 💘•💘 คุณยิ้มไม่ว่างคับ 💘•💘']
                        chivaree2 = ['   •พี่นั่งสมาธิอยู่..เดี่ยวปืนลั่นคับ•','  •ขับเครื่องบินอยู่อย่ารบกวนคับ•','  •เรียกบ่อยแบบนี้ให้แม่มาขอต่ะ•','   •กำลังเกรียนอยู่อย่ามายุ่งคับ•','  •ให้อาหารว่างไดโนเสาร์อยู่คับ•','      •ติดธุรกิจปลากัด100ล้าน•','   • ปั่นป๊อกเด้งอยู่อย่าเรียกคับ •','  •ติดถ่ายแบบอยู่รอตามคิวน่ะคับ•','  •สร้างแลนมาร์คอยู่รอในเกมคับ•','    •รันไวรัสอยู่..เอาด้วยไหมคับ•']
                        ret_ = "❂———————————————❂\n" + random.choice(chivaree1) + "\n❂———————————————❂\n" + random.choice(chivaree2) + "\n🌀•ขออภัย•ณ.เวลา" +datetime.today().strftime('%H:%M:%S')+ "🌀"
                        line.sendMessage(to, str(ret_))
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
#------------------------------------------------------------------------------------------------------------
                elif msg.text in ["นับ"]:
                    line.sendMessage(msg.to,"➤ ֆҽℓƒ-β❂T-ℒįℳ ➤")
                    line.sendMessage(msg.to,"❂➣-รอสักครู่คับ...........")
                    line.sendMessage(msg.to,"💖:::⭐ 1 ⭐:::💖")
                    line.sendMessage(msg.to,"💚:::⭐ 2 ⭐:::💚")
                    line.sendMessage(msg.to,"💙:::⭐ 3 ⭐:::💙")
                    line.sendMessage(msg.to,"💔:::⭐ 4 ⭐:::💔")
                    line.sendMessage(msg.to,"💖:::⭐ 5 ⭐:::💖")
                    line.sendMessage(msg.to,"💚:::⭐ 6 ⭐:::💚")
                    line.sendMessage(msg.to,"💙:::⭐ 7 ⭐:::💙")
                    line.sendMessage(msg.to,"💔:::⭐ 8 ⭐:::💔")
                    line.sendMessage(msg.to,"💖:::⭐ 9 ⭐:::💖")
                    line.sendMessage(msg.to,"💚:::⭐ 0 ⭐:::💚")
#--------------------------------------------------------------------------------------------------------------
                elif msg.text in ["เอจังนับจีน","นับจีน"]:
                    line.sendMessage(msg.to,"✯͜͡✯•ֆҽℓƒ-β❂T-ℒįℳ•✯͜͡✯")
                    line.sendMessage(msg.to,"❂➣-รอสักครู่คับ...........")
                    line.sendMessage(msg.to,"💖:::⭐ พ่อ ⭐:::💖")
                    line.sendMessage(msg.to,"💚:::⭐ มึง ⭐:::💚")
                    line.sendMessage(msg.to,"💙:::⭐ สิ* ⭐:::💙")
                    line.sendMessage(msg.to,"💔:::⭐ กู* ⭐:::💔")
                    line.sendMessage(msg.to,"💖:::⭐ นับ ⭐:::💖")
                    line.sendMessage(msg.to,"💖:::⭐ จีน ⭐:::💖")
                    line.sendMessage(msg.to,"💚:::⭐ ไม่ ⭐:::💚")
                    line.sendMessage(msg.to,"💙:::⭐ ได้ ⭐:::💙")
                    line.sendMessage(msg.to,"🌀ไอเหี้ย 🕒 " +datetime.today().strftime('%H:%M:%S')+ "🌀")
#------------------------------------------------------------------------------------------------------------------
                elif msg.text in ["เอจังนับไทย","นับไทย"]:
                    line.sendMessage(msg.to,"✥ ֆҽℓƒ-β❂T-ℒįℳ ✥")
                    line.sendMessage(msg.to,"❂➣-รอสักครู่คับ...........")
                    line.sendMessage(msg.to,"💖:::⭐ ๑ ⭐:::💖")
                    line.sendMessage(msg.to,"💚:::⭐ ๒ ⭐:::💚")
                    line.sendMessage(msg.to,"💙:::⭐ ๓ ⭐:::💙")
                    line.sendMessage(msg.to,"💔:::⭐ ๔ ⭐:::💔")                     
                    line.sendMessage(msg.to,"💖:::⭐ ๕ ⭐:::💖")       
                    line.sendMessage(msg.to,"💚:::⭐ ๖ ⭐:::💚")
                    line.sendMessage(msg.to,"💙:::⭐ ๗ ⭐:::💙")     
                    line.sendMessage(msg.to,"💔:::⭐ ๘ ⭐:::💔")
                    line.sendMessage(msg.to,"💖:::⭐ ๙ ⭐:::💖")
                    line.sendMessage(msg.to,"💚:::⭐ 0 ⭐:::💚")
                    line.sendMessage(msg.to,"✥ ขอบพระทัยเพคับ ✥")
#-------------------------------------------------------------------------------------------------------------
                elif msg.text in ["เอจังนับอังกฤษ","นับอังกฤษ"]:
                    line.sendMessage(msg.to,"🎃 ֆҽℓƒ-β❂T-ℒįℳ 🎃")
                    line.sendMessage(msg.to,"❂➣-รอสักครู่คับ...........")
                    line.sendMessage(msg.to,"💖⭐ ••One•• ⭐💖")
                    line.sendMessage(msg.to,"💚⭐ ••Two•• ⭐💚")
                    line.sendMessage(msg.to,"💙⭐ •Three• ⭐💙")
                    line.sendMessage(msg.to,"💔⭐  •Four•  ⭐💔")
                    line.sendMessage(msg.to,"💖⭐ ••Five•• ⭐💖")
                    line.sendMessage(msg.to,"💚⭐ •••Six••• ⭐💚")
                    line.sendMessage(msg.to,"💙⭐ •Seven• ⭐💙")
                    line.sendMessage(msg.to,"💔⭐  •Eight•  ⭐💔")
                    line.sendMessage(msg.to,"💖⭐ ••Nine•• ⭐💖")
                    line.sendMessage(msg.to,"💚⭐ ••Zero•• ⭐💚")
                    line.sendMessage(msg.to,"■•■•■• OK •■•■•■")
#-----------------------------------------------------------------------------------------------------------
                elif msg.text in ["เอจังนับอินโด","นับอินโด"]:
                    line.sendMessage(msg.to,"➤➤ ֆҽℓƒ-β❂T-ℒįℳ ➤➤")
                    line.sendMessage(msg.to,"❂➣-รอสักครู่คับ..................")
                    line.sendMessage(msg.to,"💖⭐1 •••Satu••• 1⭐💖")
                    line.sendMessage(msg.to,"💚⭐2••••Dua••••2⭐💚")
                    line.sendMessage(msg.to,"💙⭐3 •••Tiga••• 3⭐💙")
                    line.sendMessage(msg.to,"💔⭐4 ••Empat••4⭐💔")
                    line.sendMessage(msg.to,"💖⭐5  ••Lima••  5⭐💖")
                    line.sendMessage(msg.to,"💚⭐6•••Enam•••6⭐💚")
                    line.sendMessage(msg.to,"💙⭐7  ••Tujuh•• 7⭐💙")
                    line.sendMessage(msg.to,"💔⭐8 •Delapan•8⭐💔")
                    line.sendMessage(msg.to,"💖⭐9 Sembilan 9⭐💖")
                    line.sendMessage(msg.to,"💚⭐0 ••••Nol•••• 0⭐💚")
                    line.sendMessage(msg.to,"A~jańg@Indo 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")
#------------------------------------------------------------------------------------------------------------
                elif msg.text in ["เอจังนับสเปน","นับสเปน"]:
                    line.sendMessage(msg.to,"🌀 ֆҽℓƒ-β❂T-ℒįℳ 🌀")
                    line.sendMessage(msg.to,"❂➣-รอสักครู่คับ...........")
                    line.sendMessage(msg.to,"1.❂•••  รีลมาดริด")
                    line.sendMessage(msg.to,"2.❂••• บาเซโลน่า")
                    line.sendMessage(msg.to,"3.❂••• บาเลนเซีย")
                    line.sendMessage(msg.to,"4.❂•• แอตมาดริด")
                    line.sendMessage(msg.to,"5.❂•• ลาคอรุนญ่า")
                    line.sendMessage(msg.to,"6.❂••เอสปันญ่อล")
                    line.sendMessage(msg.to,"7.❂•••  โอซาซูน่า")
                    line.sendMessage(msg.to,"8.❂••• ซาราโกซ่า")
                    line.sendMessage(msg.to,"9.❂•••• บียาร์รีลล์")
                    line.sendMessage(msg.to,"0.❂••• เรอัลเบติส")
                    line.sendMessage(msg.to,"💜•⭐ขอบคุณคับ•⭐•💜")
#---------------------------------------------------------------------------------------------------------------
                elif msg.text in ["เอจังนับไฮโซ","นับไฮโซ"]:
                    line.sendMessage(msg.to,"⭐⭐ •ֆҽℓƒ-β❂T-ℒįℳ• ⭐⭐")
                    line.sendMessage(msg.to,"✧••••••❂✯❂••••••✧\n💖💖[[[[[ 1 ]]]]]💖💖\n ••••• " +datetime.today().strftime('%H:%M:%S')+ " •••••")
                    line.sendMessage(msg.to,"✧••••••❂✯❂••••••✧\n💚💚[[[[[ 2 ]]]]]💚💚\n ••••• " +datetime.today().strftime('%H:%M:%S')+ " •••••")
                    line.sendMessage(msg.to,"✧••••••❂✯❂••••••✧\n💙💙[[[[[ 3 ]]]]]💙💙\n ••••• " +datetime.today().strftime('%H:%M:%S')+ " •••••")
                    line.sendMessage(msg.to,"✧••••••❂✯❂••••••✧\n💔💔[[[[[ 4 ]]]]]💔💔\n ••••• " +datetime.today().strftime('%H:%M:%S')+ " •••••")
                    line.sendMessage(msg.to,"✧••••••❂✯❂••••••✧\n💖💖[[[[[ 5 ]]]]]💖💖\n ••••• " +datetime.today().strftime('%H:%M:%S')+ " •••••")
                    line.sendMessage(msg.to,"✧••••••❂✯❂••••••✧\n💚💚[[[[[ 6 ]]]]]💚💚\n ••••• " +datetime.today().strftime('%H:%M:%S')+ " •••••")
                    line.sendMessage(msg.to,"✧••••••❂✯❂••••••✧\n💙💙[[[[[ 7 ]]]]]💙💙\n ••••• " +datetime.today().strftime('%H:%M:%S')+ " •••••")
                    line.sendMessage(msg.to,"✧••••••❂✯❂••••••✧\n💔💔[[[[[ 8 ]]]]]💔์💔\n ••••• " +datetime.today().strftime('%H:%M:%S')+ " •••••")
                    line.sendMessage(msg.to,"✧••••••❂✯❂••••••✧\n💖ั๊💖[[[[[ 9 ]]]]]💖💖\n ••••• " +datetime.today().strftime('%H:%M:%S')+ " •••••")
                    line.sendMessage(msg.to,"✧••••••❂✯❂••••••✧\n💚💚[[[[[ 0 ]]]]]💚💚\n ••••• " +datetime.today().strftime('%H:%M:%S')+ " •••••")
#-----------------------------------------------------------------------------------------------------------------
                elif msg.text in ["ใครสวยสุด","ใครน่ารักสุด","ใครเกรียนสุด","ใครหล่อสุด","ใครเทพสุด"]:
                    line.sendMessage(msg.to,"✥•✥ ֆҽℓƒ-β❂T-ℒįℳ ✥•✥")
                    line.sendMessage(msg.to,"⭐ระบบอัจฉริยะกำลังทำงาน⭐")
                    line.sendMessage(msg.to,"🔍 Search Bot :::::::::::::::::::::")
                    line.sendMessage(msg.to,"Now Loding...............")
                    line.sendMessage(msg.to,"15% ❂•➣➣")
                    line.sendMessage(msg.to,"32% ❂•➣➣➣➣")
                    line.sendMessage(msg.to,"67% ❂•➣➣➣➣➣➣")
                    line.sendMessage(msg.to,"99% ❂•➣➣➣➣➣➣➣➣")
                    line.sendMessage(msg.to,"💖•Mission Complete•💖")
                    line.sendMessage(msg.to,"❂➣-ℒįℳ: 🕟 " +datetime.today().strftime('%H:%M:%S')+ "➤")
                    line.sendContact(to, "u669aa92773d33c22420105d4546fccdd")
                    line.sendMessage(msg.to,"👆• คนนี้เจ้าคับ by : ℒįℳ•👆")
#---------------------------------------------------------------------------------------------------------------
                elif msg.text in ["ยิ้มopen"]:
                    line.sendMessage(msg.to,"✯::[[[ เปิดระบบเรียบร้อยคับ ]]]::✯\n A~jańg@Opën 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")
                elif msg.text in ["ยิ้มclose"]:
                    line.sendMessage(msg.to,"✯::[[[ ปิดระบบเรียบร้อยคับ ]]]::✯\nA~jańg@Clöse 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")
                elif msg.text in ["ยิ้มออน2"]:
                    line.sendMessage(msg.to,"✧•••❂ เวลาทำงานของบอท ❂•••✧")
                    line.sendMessage(msg.to," ❂-ℒįℳ•➣Böt : 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™\n╔•➤➤➤➤➤➤➤➤➤➤➤➤➤\n╠  Ä☆➣   1 ปี\n╠  ••••••Ä☆➣  765 ชั่วโมง\n╠  •••••••••••••Ä☆➣   908   นาที\n╚•➤➤➤➤➤➤➤➤➤➤➤➤➤")
#----------------------------------------------------------------------------------------------------------------
                elif msg.text in ["ด่า"]:
                    line.sendMessage(msg.to,"❂•สักครู่ระบบกำลังประมวลผล•❂\n  A~jang@Open 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")
                    line.sendMessage(msg.to,"Now Loding...........................")
                    line.sendMessage(msg.to,"❂•••• ไอ้ผีฉีกเรียน ••••❂")
                    line.sendMessage(msg.to,"❂••• อีคางคกเห็นผี •••❂")
                    line.sendMessage(msg.to,"❂•• อีจระเข้เดินห้าง ••❂")
                    line.sendMessage(msg.to,"❂••••• ไอ้แกงบูด: •••••❂")
                    line.sendMessage(msg.to,"❂•••  อีสุวรรณมาลี  •••❂")
                    line.sendMessage(msg.to,"❂••• ไอ้ไก่ดุดพรก ••••❂")
                    line.sendMessage(msg.to,"❂•••••ไอ้แตดสีรุ้ง •••••❂")
                    line.sendMessage(msg.to,"❂•••• ไอ้ขี้มูกเขียว ••••❂")
                    line.sendMessage(msg.to,"❂••••• ไอ้ผีขบส้ม •••••❂")
                    line.sendMessage(msg.to,"❂••ไอ้หัวล้านใส่เยล ••❂")
                    line.sendMessage(msg.to,"❂•อีหนังหน้าปลาจวด•❂")
                    line.sendMessage(msg.to,"❂••• อีโกดังเก็บศพ •••❂")
                    line.sendMessage(msg.to,"❂••• อีแย้แดกแห้ว: •••❂")
                    line.sendMessage(msg.to,"❂• อีหลุมดำจักรวาล: •❂")
                    line.sendMessage(msg.to,"❂• ไอ้สะตอโปรตุเกส •❂")
                    line.sendMessage(msg.to,"❂• อีดาวเทียมไทคม: •❂\n💖 แม่งเสือกทุกสถานี 💖\n      จบข่าว จุ้ฟป้อก~⭐")
#--------------------------------------------------------------------------------------------------------------        
                elif msg.text.lower().startswith("สแปมแทค "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = line.getGroup(to)
                    for x in range(jml):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for receiver in lists:
                                contact = line.getContact(receiver)
                                RhyN_(to, contact.mid)
#----------------------------------------------------------------------------------------------------------------------- 
                elif msg.text.lower().startswith("ส่งหัวใจ "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = line.getGroup(to)
                    for x in range(jml):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for receiver in lists:
                                line.sendMessage(receiver,"💖•💗•รั.ก.น่.ะ.ค่.ะ.จุ้.ฟ.ๆ•💗•💖\n💖•💗•รั.ก.น่.ะ.ค่.ะ.จุ้.ฟ.ๆ•💗•💖\n💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                                line.sendMessage(receiver,"💖•💗•รั.ก.น่.ะ.ค่.ะ.จุ้.ฟ.ๆ•💗•💖\n💖•💗•รั.ก.น่.ะ.ค่.ะ.จุ้.ฟ.ๆ•💗•💖\n💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                                line.sendMessage(to, "💗•ส่งในแชทสต.แล้วค่ะ•💗".format(str(jml)))
                            else:
                                pass
                elif msg.text.lower().startswith("ส่งคลิป "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = line.getGroup(to)
                    for x in range(jml):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for receiver in lists:
                                line.sendMessage(receiver, "🌀•คลิปหลุดนักศึกษาเสียวสุดๆ•🌀\n🌀•คลิปหลุดนักศึกษาเสียวสุดๆ•🌀\n💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                                line.sendMessage(receiver, "🌀•คลิปหลุดนักศึกษาเสียวสุดๆ•🌀\n🌀•คลิปหลุดนักศึกษาเสียวสุดๆ•🌀\n💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                                line.sendMessage(to, "🌀ดูคลิปเด็ดในแชท สต.น่ะค่ะ🌀".format(str(jml)))
                                
                elif msg.text.lower().startswith("แจกของขวัญ "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = line.getGroup(to)
                    for x in range(jml):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for receiver in lists:
                                line.sendGift(receiver, '1002077','sticker')
                                line.sendMessage(to, "🎁•รับทางแชทสต.นะค่ะ•🎁".format(str(jml)))
                            else:
                                pass
                
                elif msg.text.lower().startswith("ส่งนอน "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = line.getGroup(to)
                    for x in range(jml):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for receiver in lists:
                                line.sendMessage(receiver,"🌙•หลับฝันดีน่ะค่ะที่รัก จุ๊ฟป้อก•🌙\n🌙•หลับฝันดีน่ะค่ะที่รัก จุ๊ฟป้อก•🌙\n💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                                line.sendMessage(receiver, "🌙•หลับฝันดีน่ะค่ะที่รัก จุ๊ฟป้อก•🌙\n🌙•หลับฝันดีน่ะค่ะที่รัก จุ๊ฟป้อก•🌙\n💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                                line.sendMessage(to, "🌙•ส่งในแชทสต.แล้วค่ะ•🌙".format(str(jml)))
                            else:
                                pass
                                
                elif msg.text.lower().startswith("ส่งความรัก "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = line.getGroup(to)
                    for x in range(jml):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for receiver in lists:
                                line.sendMessage(receiver, "💖.ฉั.น.รั.ก.เ.ธ.อ.ที่.สุ.ด.เ.ล.ย.💖\n💖.ฉั.น.รั.ก.เ.ธ.อ.ที่.สุ.ด.เ.ล.ย.💖\n💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                                line.sendMessage(receiver, "💖.ฉั.น.รั.ก.เ.ธ.อ.ที่.สุ.ด.เ.ล.ย.💖\n💖.ฉั.น.รั.ก.เ.ธ.อ.ที่.สุ.ด.เ.ล.ย.💖\n💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                                line.sendMessage(to, "💗•ส่งในแชทสต.แล้วค่ะ•💗".format(str(jml)))
                            else:
                                pass 
                    
                elif msg.text.lower().startswith("ส่งความคิดถึง "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = line.getGroup(to)
                    for x in range(jml):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for receiver in lists:
                                line.sendMessage(receiver, "💖.คิ.ด.ถึ.ง.เ.ธ.อ.ที่.สุ.ด.เ.ล.ย.💖\n💖.คิ.ด.ถึ.ง.เ.ธ.อ.ที่.สุ.ด.เ.ล.ย.💖\nไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                                line.sendMessage(receiver, "💖.คิ.ด.ถึ.ง.เ.ธ.อ.ที่.สุ.ด.เ.ล.ย.💖\n💖.คิ.ด.ถึ.ง.เ.ธ.อ.ที่.สุ.ด.เ.ล.ย.💖\n💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                                line.sendMessage(to, "💗•ส่งในแชทสต.แล้วค่ะ•💗".format(str(jml)))
                            else:
                                pass                       

                elif msg.text.lower().startswith("ส่งของขวัญ "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = line.getGroup(to)
                    for x in range(jml):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for receiver in lists:
                                line.sendMessage(receiver,"คุ.ณ.ไ.ด้.รั.บ.ข.อ.ง.ข.วั.ญ.ค่.ะ.🎁\nคุ.ณ.ไ.ด้.รั.บ.ข.อ.ง.ข.วั.ญ.ค่.ะ.🎁\n💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                                line.sendMessage(receiver,"คุ.ณ.ไ.ด้.รั.บ.ข.อ.ง.ข.วั.ญ.ค่.ะ.🎁\nคุ.ณ.ไ.ด้.รั.บ.ข.อ.ง.ข.วั.ญ.ค่.ะ.🎁\n💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                                line.sendMessage(to, "🎁•รับทางแชทสต.นะค่ะ•🎁".format(str(jml)))
                            else:
                                pass
#------------------------------------------------------------------------------------------------------------------
                elif msg.text.lower().startswith("ยิ้มเขียน "):
                    sep = msg.text.split(" ")
                    textnya = msg.text.replace(sep[0] + " ","")
                    urlnya = "http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt=" + textnya + "&chts=FFFFFF,70&chf=bg,s,000000"
                    line.sendMessage(msg.to,"✯͜͡✯•ֆҽℓƒ-β❂T-ℒįℳ")
                    line.sendImageWithURL(msg.to, urlnya)
                elif msg.text.lower().startswith("เขียน "):
                    sep = msg.text.split(" ")
                    textnya = msg.text.replace(sep[0] + " ","")
                    urlnya = "http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt=" + textnya + "&chts=FFFFFF,70&chf=bg,s,000000"
                    line.sendMessage(msg.to,"✯͜͡✯•ֆҽℓƒ-β❂T-ℒįℳ•✯͜͡✯")
                    line.sendImageWithURL(msg.to, urlnya)
#===============================================================
#🎃🎃🎃🎃🎃🎃🎃   โหมดไวรัสเอจัง  by.Chivaree   🎃🎃🎃🎃🎃🎃🎃
#    👉👉👉👉   คำเตือน  : เนื่องจากไวรัสเอจังเป็นคำสั่งไวรัสแบบสั่งงาน 2 ชั้น
#     หากท่านแก้ไขหัวคำสั่ง. หรือชือไวรัส อาจทำให้ไวรัสไม่แสดงผล และผิดเพี้ยนไป
#     เพราะคำสั่งจะเป็นแบบผูกกันจะมีตัวแปลซ้อนอีกทีแบบสองชั้นคับ
#  💖 แต่ถ้าท่านมีความเข้าใจในการทำงานสองชั้น เชิญท่านแก้ไขได้ตามสบายคับ จุ้ฟป้อก
              ##           แก้ดีๆ ระวังไฟล์พังไม่รุ้นะ. 5555555 เตือนแล้ว
#----------------------------------------------------------------------------------------------------------------
                elif msg.text in ["ระเบิดเวลาเอจัง","เอจังวางระเบิด","วางระเบิด","ระเบิดเวลา"]:
                    line.sendMessage(msg.to,"✧••••••••❂✧ℒįℳ✧❂••••••••✧\n ✯:::[[[: ֆҽℓƒ-β❂T-ℒįℳ:]]]:::✯")
                    line.sendMessage(msg.to,"💣::โหมดระเบิดเวลาเอจังคับ::💣")
                    line.sendMessage(msg.to,"⏳::เริ่มจุดชนวนระเบิดเวลาคับ::⌛")
                    line.sendMessage(msg.to,"⏰⏳::⭐9⭐::⌛⏰")
                    line.sendMessage(msg.to,"⏰⏳::⭐8⭐::⌛⏰")
                    line.sendMessage(msg.to,"⏰⏳::⭐7⭐::⌛⏰")
                    line.sendMessage(msg.to,"⏰⏳::⭐6⭐::⌛⏰")
                    line.sendMessage(msg.to,"⏰⏳::⭐5⭐::⌛⏰")
                    line.sendMessage(msg.to,"⏰⏳::⭐4⭐::⌛⏰")
                    line.sendMessage(msg.to,"⏰⏳::⭐3⭐่::⌛⏰")
                    line.sendMessage(msg.to,"⏰⏳::⭐2⭐::⌛⏰")
                    line.sendMessage(msg.to,"⏰⏳::⭐1⭐::⌛⏰")
                    line.sendMessage(msg.to,"⏰⏳:: ......................")
                    line.sendMessage(msg.to,"Error... ไม่พบสัญญาน")
                    line.sendMessage(msg.to, "💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣")
                    line.sendMessage(msg.to, "💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣??💣\n💣💣💣??💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣??💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣")
                    line.sendMessage(msg.to, "💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    line.sendMessage(msg.to, "💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.ค่.ะ.💚.💟.💛.🤗.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.ก.า.ดึ๊.บ.ๆ.b.y.เ.อ.จั.ง.💚.💟.💗.🤗...")
                    line.sendMessage(msg.to, "💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    line.sendMessage(msg.to,"💥💥💥💥💥💥💥💥\n   ระเบิดดังตู้มเลยคร้า\n💥💥💥💥💥💥💥💥")
#=======================================================================
                elif msg.text in ["ไวรัสอวตาร","ไวรัสอวตาล"]:
                    line.sendMessage(msg.to,"ไวรัสอวตาร•➣➣➣➣➣➣➣➣\n  ❂••••••✧ℒįℳ✧•••••••❂\n➣➣➣➣➣➣➣➣ •Chiväree™")
                    line.sendMessage(msg.to,"💙:::⭐ 9 ⭐:::💙")
                    line.sendMessage(msg.to,"💚:::⭐ 8 ⭐:::💚")
                    line.sendMessage(msg.to,"💖:::⭐ 7 ⭐:::💖")
                    line.sendMessage(msg.to,"💚:::⭐ 6 ⭐:::💚")
                    line.sendMessage(msg.to,"💖:::⭐ 5 ⭐:::💖")
                    line.sendMessage(msg.to,"💔:::⭐ 4 ⭐:::💔")
                    line.sendMessage(msg.to,"💙:::⭐ 3 ⭐:::💙")
                    line.sendMessage(msg.to,"💚:::⭐ 2 ⭐:::💚")
                    line.sendMessage(msg.to,"💖:::⭐ 1 ⭐:::💖")
                    line.sendMessage(msg.to,"💚:::⭐ 0 ⭐:::💚")
                    line.sendMessage(msg.to,"💖💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚💚\n ขออภัยท่านเอจังยังไม่ใส่โค๊ดคับ\n💚💚💚💚💚💚💚💚💚💚💚💚\n💖💖💖💖💖💖💖💖💖💖💖💖")
#-----------------------------------------------------------------------------------------------------------------------------------------
                elif msg.text in ["ไวรัสแมนยู","ไวรัสผีแดง"]:
                    line.sendMessage(msg.to,"ไวรัสแมนยู•➣➣➣➣➣➣➣➣\n    ❂••••••✧ℒįℳ✧•••••••❂\n➣➣➣➣➣➣➣➣ •Chiväree™")
                    line.sendMessage(msg.to,"😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈")
                    line.sendMessage(msg.to,"😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈")
                    line.sendMessage(msg.to,"😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈")
                    line.sendMessage(msg.to,"😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈")
                    line.sendMessage(msg.to,"😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈")
                    line.sendMessage(msg.to,"😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U ??\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈")
                    line.sendMessage(msg.to,"😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈")
                    line.sendMessage(msg.to,"😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈")
                    line.sendMessage(msg.to,"😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈")
                    line.sendMessage(msg.to,"😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈")
                    line.sendMessage(msg.to,"😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈")
                    line.sendMessage(msg.to,"😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈")
                    line.sendMessage(msg.to,"😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈")
                    line.sendMessage(msg.to,"😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈")
                    line.sendMessage(msg.to,"😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈")
                    line.sendMessage(msg.to,"เกรียน on 7 Man United Fc Club")
#----------------------------------------------------------------------------------------------------------------------------------------------
                elif msg.text in ["ไวรัสชนบท"]:
                    line.sendMessage(msg.to," ╬╬❂•ຟနุ้७ຟနิ้७•❂╬╬")
                    line.sendMessage(msg.to,"💙:::⭐ 9 ⭐:::💙")
                    line.sendMessage(msg.to,"💚:::⭐ 8 ⭐:::💚")
                    line.sendMessage(msg.to,"💖:::⭐ 7 ⭐:::💖")
                    line.sendMessage(msg.to,"💚:::⭐ 6 ⭐:::💚")
                    line.sendMessage(msg.to,"💖:::⭐ 5 ⭐:::💖")
                    line.sendMessage(msg.to,"💔:::⭐ 4 ⭐:::💔")
                    line.sendMessage(msg.to,"💙:::⭐ 3 ⭐:::💙")
                    line.sendMessage(msg.to,"💚:::⭐ 2 ⭐:::💚")
                    line.sendMessage(msg.to,"💖:::⭐ 1 ⭐:::💖")
                    line.sendMessage(msg.to,"💚:::⭐ 0 ⭐:::💚")
                    line.sendMessage(msg.to,"❂•➤➤➤➤➤➤➤➤➤➤➤➤\n • ด้วยความกันดารไร้สัญญาน\n • และสุดแสนชนบทนี้\n • ระบบจึงไม่สามารถรันไวรัสได้\n • ขออภัยอย่างสูงคะ by.เอจัง\n❂•➤➤➤➤➤➤➤➤➤➤➤➤")
#-----------------------------------------------------------------------------------------------------------------------------------------
                elif msg.text in ["สีชมพูคับ"]:
                    line.sendMessage(msg.to, "💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    line.sendMessage(msg.to, "💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                    line.sendMessage(msg.to, "A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    line.sendMessage(msg.to, "💗•💗•💗•Virus Pink•💗•💗•💗")
#----------------------------------------------------------------------------------------------------------------------------------------
                elif msg.text in ["Man United Fc Club"]:
                    line.sendMessage(msg.to,"💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    line.sendMessage(msg.to,"💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                    line.sendMessage(msg.to,"ไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    line.sendMessage(msg.to,"💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    line.sendMessage(msg.to,"ไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    line.sendMessage(msg.to,"💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    line.sendMessage(msg.to,"💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    line.sendMessage(msg.to,"ไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    line.sendMessage(msg.to,"💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    line.sendMessage(msg.to,"💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                    line.sendMessage(msg.to,"ไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    line.sendMessage(msg.to, "💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    line.sendMessage(msg.to,"💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                    line.sendMessage(msg.to,"💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    line.sendMessage(msg.to,"ไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    line.sendMessage(msg.to,"💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    line.sendMessage(msg.to,"   🔅Glory Glory ManUnited🔅\n😈•แมนเชสเตอร์ยูไนเต็ด เอฟซี•😈")
#-------------------------------------------------------------------------------------------------------------------------------------------
                elif msg.text in ["ปีโป้อร่อยจัง"]:
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    line.sendMessage(msg.to, "💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.เ.อ.จั.ง.คุริๆอะจึ๋งๆ~🌟ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Qฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.เอจังคับ")
                    line.sendMessage(msg.to, "💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                    line.sendMessage(msg.to, "ไวรัสเอจังฟรุ้งฟรุ้งมุ้งมิ้ง~☆😍💜💛💚💙💗💖.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.ฟรุ้งฟริ้ง by.เอจัง~☆🤗")
                    line.sendMessage(msg.to, "💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                    line.sendMessage(msg.to, "💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    line.sendMessage(msg.to, "💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    line.sendMessage(msg.to, "💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.??.💚")
                    line.sendMessage(msg.to, "💔.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.ค่.ะ.💚.💟.💛1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.ฟ.รุ้.ง.ฟ.ริ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.💓.💗.💖.")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.เ.อ.จั.ง.คุริๆอะจึ๋งๆ~🌟ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Qฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.เอจังคับ")
                    line.sendMessage(msg.to, "💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.??")
                    line.sendMessage(msg.to, "💛💜💛💜💛💜💛💜💛💜💛\n  ❂••• ปีโป้อร่อยที่สุดเลย •••❂\n💛💜💛💜💛💜💛💜💛💜💛")
#--------------------------------------------------------------------------------------------------------------
                elif msg.text in ["Kitty","kitty","Hello Kitty"]:
                    line.sendMessage(msg.to, "💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.เ.อ.จั.ง.คุริๆอะจึ๋งๆ~🌟ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Qฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.เอจังคับ")
                    line.sendMessage(msg.to, "💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.??.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.เ.อ.จั.ง.น่.า.รั๊.ก.ไ.ล.น์.เ.ขี.ย.ว.~.☆. 🤗.🕸.💙.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.เ.อ.จั.ง.คุริๆอะจึ๋งๆ~🌟ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Qฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.เอจังคับ")
                    line.sendMessage(msg.to, "ไวรัสเอจังฟรุ้งฟรุ้งมุ้งมิ้ง~☆😍💜💛💚💙💗💖.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.ฟรุ้งฟริ้ง by.เอจัง~☆🤗")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    line.sendMessage(msg.to, "💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    line.sendMessage(msg.to, "💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    line.sendMessage(msg.to, "💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.??")
                    line.sendMessage(msg.to, "✧•••••••••❂✧✯✧❂••••••••••✧\n   💖💖 HELLO KITTY 💖💖\n✧•••••••••❂✧✯✧❂••••••••••✧")
#-------------------------------------------------------------------------------------------------------------
                elif msg.text in ["ฟรุ้ตตี้น่ารัก"]:
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.เ.อ.จั.ง.น่.า.รั๊.ก.ไ.ล.น์.เ.ขี.ย.ว.~.☆. 🤗.🕸.💙.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.")
                    line.sendMessage(msg.to, "💔.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.ค่.ะ.💚.💟.💛1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.ฟ.รุ้.ง.ฟ.ริ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.💓.💗.💖.")
                    line.sendMessage(msg.to, "💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.")
                    line.sendMessage(msg.to, "💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    line.sendMessage(msg.to, "💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    line.sendMessage(msg.to, "💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    line.sendMessage(msg.to, "ไวรัสเอจังฟรุ้งฟริ้งมุ้งมิ้ง~☆💜💛💓💟💚💙💗💖🤗1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.")
                    line.sendMessage(msg.to, "ไวรัสเอจังฟรุ้งฟริ้งมุ้งมิ้ง~☆💜💛💓💟💚💙💗💖🤗1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.")
                    line.sendMessage(msg.to, "ไวรัสเอจังฟรุ้งฟริ้งมุ้งมิ้ง~☆💜💛💓💟💚💙💗💖🤗1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.")
                    line.sendMessage(msg.to, "💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    line.sendMessage(msg.to, "💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.เ.อ.จั.ง.คุริๆอะจึ๋งๆ~🌟ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Qฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.เอจังคับ")
                    line.sendMessage(msg.to, "💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    line.sendMessage(msg.to, "✧•••••••••❂✧✯✧❂••••••••••✧\n 🍎🍏🍊🍉 ฟรุตตี้ 🍉🍊🍏🍎\n✧•••••••••❂✧✯✧❂••••••••••✧")
#---------------------------------------------------------------------------------------------------------------
                elif msg.text in ["ไวรัส"]:
                    line.sendMessage(msg.to, "■•■•■• Virus •■•■•■")
                    line.sendMessage(msg.to, "■•■•■• Virus •■•■•■")
                    line.sendMessage(msg.to, "■•■•■• Virus •■•■•■")
                    line.sendMessage(msg.to, "■•■•■• Virus •■•■•■")
                    line.sendMessage(msg.to, "■•■•■• Virus •■•■•■")
                    line.sendMessage(msg.to, "■•■•■• Virus •■•■•■")
                    line.sendMessage(msg.to, "■•■•■• Virus •■•■•■")
                    line.sendMessage(msg.to, "■•■•■• Virus •■•■•■")
                    line.sendMessage(msg.to, "■•■•■• Virus •■•■•■")
                    line.sendMessage(msg.to, "■•■•■• Virus •■•■•■")
                    line.sendMessage(msg.to, "■•■•■• Virus •■•■•■")
                    line.sendMessage(msg.to, "■•■•■• Virus •■•■•■")
                    line.sendMessage(msg.to, "■•■•■• Virus •■•■•■")
                    line.sendMessage(msg.to, "●•➤➤➤➤➤➤➤➤➤➤")
                    line.sendMessage(msg.to, "●•➤➤➤➤➤➤➤➤➤➤")
                    line.sendMessage(msg.to, "💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.เ.อ.จั.ง.คุริๆอะจึ๋งๆ~🌟ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Qฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.เอจังคับ")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    line.sendMessage(msg.to, "💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                    line.sendMessage(msg.to, "💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    line.sendMessage(msg.to, "💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    line.sendMessage(msg.to, "💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    line.sendMessage(msg.to, "■•■•■• Virus •■•■•■")
#-----------------------------------------------------------------------------------------------------------------------------------
                elif msg.text in ["ไวรัสชิวารี","ไวรัสแอ๊บแบ๊ว"]:
                    line.sendMessage(msg.to,"ไวรัสชิวารี• ➣➣➣➣➣➣➣➣\n   ❂••••••✧ℒįℳ✧•••••••❂\n➣➣➣➣➣➣➣➣•Chiväree™")
                    line.sendMessage(msg.to,"💖•ไวรัสแห่งความแอ๊บแบ๊วคับ•💖")
                    line.sendMessage(msg.to,"💙•ไวรัสแห่งความแอ๊บแบ๊วคับ•💙")
                    line.sendMessage(msg.to,"💚•ไวรัสแห่งความแอ๊บแบ๊วคับ•💚")
                    line.sendMessage(msg.to,"💚•ไวรัสแห่งความแอ๊บแบ๊วคับ•💛")
                    line.sendMessage(msg.to,"💜•ไวรัสแห่งความแอ๊บแบ๊วคับ•💜")
                    line.sendMessage(msg.to,"💔•ไวรัสแห่งความแอ๊บแบ๊วคับ•💔")
                    line.sendMessage(msg.to,"💚:::⭐ 6 ⭐:::💚")
                    line.sendMessage(msg.to,"💖:::⭐ 5 ⭐:::💖")
                    line.sendMessage(msg.to,"💔:::⭐ 4 ⭐:::💔")
                    line.sendMessage(msg.to,"💙:::⭐ 3 ⭐:::💙")
                    line.sendMessage(msg.to,"💚:::⭐ 2 ⭐:::💚")
                    line.sendMessage(msg.to,"💖:::⭐ 1 ⭐:::💖")
                    line.sendMessage(msg.to,"💚:::⭐ 0 ⭐:::💚")
                    line.sendMessage(msg.to,"เกรียน on 9 ไวรัสชิวารีแบ๊วไหมคับ")
                    line.sendMessage(msg.to,"💔•ไวรัสแห่งความแอ๊บแบ๊วคับ•💔")
#------------------------------------------------------------------------------------------------------------------------------------
                elif msg.text in ["ไวรัสเอจัง"]:
                    line.sendMessage(msg.to,"ไวรัสเอจัง• ➣➣➣➣➣➣➣➣\n   ❂••••••✧ℒįℳ✧•••••••❂\n➣➣➣➣➣➣➣➣•Chiväree™")
                    line.sendMessage(msg.to,"💖•ไวรัสแห่งความน่ารักคับ•💖")
                    line.sendMessage(msg.to,"💙•ไวรัสแห่งความน่ารักคับ•💙")
                    line.sendMessage(msg.to,"💚•ไวรัสแห่งความน่ารักคับ•💚")
                    line.sendMessage(msg.to,"💛•ไวรัสแห่งความน่ารักคับ•💛")
                    line.sendMessage(msg.to,"💜•ไวรัสแห่งความน่ารักคับ•💜")
                    line.sendMessage(msg.to,"💔•ไวรัสแห่งความน่ารักคับ•💔")
                    line.sendMessage(msg.to,"💚:::⭐ 6 ⭐:::💚")
                    line.sendMessage(msg.to,"💖:::⭐ 5 ⭐:::💖")
                    line.sendMessage(msg.to,"💔:::⭐ 4 ⭐:::💔")
                    line.sendMessage(msg.to,"💙:::⭐ 3 ⭐:::💙")
                    line.sendMessage(msg.to,"💚:::⭐ 2 ⭐:::💚")
                    line.sendMessage(msg.to,"💖:::⭐ 1 ⭐:::💖")
                    line.sendMessage(msg.to,"💚:::⭐ 0 ⭐:::💚")
                    line.sendMessage(msg.to,"เกรียน on 8 ไวรัสเอจังน่ารักไหมคับ")
                    line.sendMessage(msg.to,"💖•ไวรัสเอจังน่ารักฝุดๆเบยคับ•💖")
#----------------------------------------------------------------------------------------------------------------------------
                elif msg.text in ["ไวรัสเอจัง2","ไวรัสแห่งความมืด"]:
                    line.sendMessage(msg.to,"💚💚💚💚💚💚💚💚💚\n    ®Virus ไวรัสเอจัง••••\n💚💚💚💚💚💚💚💚💚")
                    line.sendMessage(msg.to,"❂•➤➤➤➤➤➤➤➤➤➤\n  • ความมืดเริ่มครอบงำคับง\n❂•➤➤➤➤➤➤➤➤➤➤")
                    line.sendMessage(msg.to,"💜•ไวรัสเอจังกับพลังความมืด•💜")
                    line.sendMessage(msg.to,"■■■■■■■■■■■■■■")
                    line.sendMessage(msg.to,"■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■")
                    line.sendMessage(msg.to,"■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■")
                    line.sendMessage(msg.to,"■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■")
                    line.sendMessage(msg.to,"■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■")
                    line.sendMessage(msg.to,"■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■")
                    line.sendMessage(msg.to,"■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■")
                    line.sendMessage(msg.to,"■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■")
                    line.sendMessage(msg.to,"■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■")
                    line.sendMessage(msg.to,"■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■")
                    line.sendMessage(msg.to,"■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■")
                    line.sendMessage(msg.to,"■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■")
                    line.sendMessage(msg.to,"💙:::⭐ 3 ⭐:::💙")
                    line.sendMessage(msg.to,"💚:::⭐ 2 ⭐:::💚")
                    line.sendMessage(msg.to,"💖:::⭐ 1 ⭐:::💖")
                    line.sendMessage(msg.to,"เกรียน on 8 ไวรัสเอจังน่ารักไหมคับ")
                    line.sendMessage(msg.to,"💖•ไวรัสเอจังกับพลังความมืด•💖")
#------------------------------------------------------------------------------------------------------------------------
                elif msg.text in ["ไวรัสเอจัง3","ไวรัสแห่งความรัก"]:
                    line.sendMessage(msg.to,"ไวรัสเอจัง3➣➣➣➣➣➣➣➣\n   ❂••••••✧ℒįℳ✧•••••••❂\n➣➣➣➣➣➣➣•พลังความรัก")
                    line.sendMessage(msg.to,"💖•ไวรัสเอจังกับพลังความรัก•💖")
                    line.sendMessage(msg.to,"💖💖💖💖💖💖💖💖💖💖💖")
                    line.sendMessage(msg.to,"💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙")
                    line.sendMessage(msg.to,"💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙")
                    line.sendMessage(msg.to,"💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙\n💔💔💔💔💔💔💔💔💔💔💔\n💛💛💛💛💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜")
                    line.sendMessage(msg.to,"💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙\n💔💔💔💔💔💔💔💔💔💔💔\n💛💛💛💛💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜")
                    line.sendMessage(msg.to,"💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙\n💔💔💔💔💔💔💔💔💔💔💔\n💛💛💛💛💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜")
                    line.sendMessage(msg.to,"💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙\n💔💔💔💔💔💔💔💔💔💔💔\n💛💛💛💛💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜")
                    line.sendMessage(msg.to,"💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙\n💔💔💔💔💔💔💔💔💔💔💔\n💛💛💛💛💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜")
                    line.sendMessage(msg.to,"💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙\n💔💔💔💔💔💔💔💔💔💔💔\n💛💛💛💛💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙\n💔💔💔💔💔💔💔💔💔💔💔\n💛💛💛💛💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙\n💔💔💔💔💔💔💔💔💔💔💔\n💛💛💛💛💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙\n💔💔💔💔💔💔💔💔💔💔💔\n💛💛💛💛💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙\n💔💔💔💔💔💔💔💔💔💔💔\n💛💛💛💛💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙\n💔💔💔💔💔💔💔💔💔💔💔\n💛💛💛💛💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙\n💔💔💔💔💔💔💔💔💔💔💔\n💛💛💛💛💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙\n💔💔💔💔💔💔💔💔💔💔💔\n💛💛💛💛💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜")
                    line.sendMessage(msg.to,"💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙\n💔💔💔💔💔💔💔💔💔💔💔\n💛💛💛💛💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙\n💔💔💔💔💔💔💔💔??💔💔\n💛💛💛??💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙\n💔💔💔💔💔💔💔💔💔💔💔\n💛💛💛💛💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙\n💔💔💔💔💔💔💔💔💔💔💔\n💛💛💛💛💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙\n💔💔💔💔💔💔💔💔💔💔💔\n💛💛💛💛💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙\n💔💔💔💔💔💔💔💔💔💔💔\n💛💛💛💛💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙\n💔💔💔💔💔💔💔💔💔💔💔\n💛💛💛💛💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙\n💔💔💔💔💔💔💔💔💔💔💔\n💛💛💛💛💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜")
                    line.sendMessage(msg.to,"💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙\n💔💔💔💔💔💔💔💔💔💔💔\n💛💛💛💛💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙\n💔💔💔💔💔💔💔💔💔💔💔\n💛💛💛💛💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙\n💔💔💔💔💔💔💔💔💔💔💔\n💛💛💛💛💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙\n💔💔💔💔💔💔💔💔💔💔💔\n💛💛💛💛💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙\n💔💔💔💔💔💔💔💔💔💔💔\n💛💛💛💛💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙\n💔💔💔💔💔💔💔💔💔💔💔\n💛💛💛💛💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖??💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙\n💔💔💔💔💔💔💔💔💔💔💔\n💛💛💛💛💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙\n💔💔💔💔💔💔💔💔💔💔💔\n💛💛💛💛💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜")
                    line.sendMessage(msg.to,"💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙\n??💔💔💔💔💔💔💔💔💔💔\n💛💛💛💛💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙\n💔💔💔💔💔💔💔💔💔💔💔\n💛💛💛💛💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙\n💔💔💔💔💔💔💔💔💔💔💔\n💛💛💛💛💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙\n💔💔💔💔💔💔💔💔💔💔💔\n💛💛💛💛💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙\n💔💔💔💔💔💔💔💔💔💔💔\n💛💛💛💛💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙\n💔💔💔💔💔💔💔💔💔💔💔\n??💛💛💛💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙\n💔💔💔💔💔💔💔💔💔💔💔\n💛💛💛💛💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙\n💔💔💔💔💔💔💔💔💔💔💔\n💛💛💛💛💛💛💛💛💛💛💛\n💜??💜💜💜💜💜💜💜💜💜")
                    line.sendMessage(msg.to,"💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙\n💔💔💔💔💔💔💔💔💔💔💔\n💛💛💛💛💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙\n💔💔💔💔💔💔💔💔💔💔💔\n💛💛💛💛💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙\n💔💔💔💔💔💔💔💔💔💔💔\n💛💛💛💛💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙\n💔💔💔💔??💔💔💔💔💔💔\n💛💛💛💛💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚??💚💚💚??💚\n💙💙💙💙💙💙💙💙💙💙💙\n💔💔💔💔💔💔💔💔💔💔💔\n💛💛💛💛💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖💖\n💚💚??💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙\n💔💔💔💔💔💔💔💔💔💔💔\n💛💛💛💛💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙??💙💙💙\n💔💔💔💔💔💔💔💔💔💔💔\n💛💛💛💛💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚\n💙💙💙💙💙💙💙💙💙💙💙\n💔💔💔💔💔💔💔💔💔💔💔\n💛💛💛💛💛💛💛💛💛💛💛\n💜💜💜💜💜💜💜💜💜💜💜")
                    line.sendMessage(msg.to,"💙:::⭐ 3 ⭐:::💙")
                    line.sendMessage(msg.to,"💚:::⭐ 2 ⭐:::💚")
                    line.sendMessage(msg.to,"💖:::⭐ 1 ⭐:::💖")
                    line.sendMessage(msg.to,"เกรียน on 9 ไวรัสเอจังน่ารักไหมคับ")
                    line.sendMessage(msg.to,"💖•ไวรัสเอจังน่ารักฝุดๆเบยคับ•💖")
#------------------------------------------------------------------------------------------------------------------------------------------
                elif msg.text in ["คท",".คท","Me","me"]:
                    line.sendMessage(msg.to,"คท.คือไรว่ะ• ➣➣➣➣➣➣➣➣\n   ❂••••••✧A-jáng✧•••••••❂\n➣➣➣➣➣➣➣➣•Me คือไรว่ะ")
                    line.sendMessage(msg.to,"❂•➤➤➤➤➤➤➤➤➤➤➤➤\n  • คท คือไร ควยเทวดาหรอคับ\n  • Me คือไร มีหีกระป๋องหรอคับ\n❂•➤➤➤➤➤➤➤➤➤➤➤➤")
                    line.sendMessage(msg.to,"❂•➤➤➤➤➤➤➤➤➤➤➤➤\n  • คท คือไร ควยเทวดาหรอคับ\n  • Me คือไร มีหีกระป๋องหรอคับ\n❂•➤➤➤➤➤➤➤➤➤➤➤➤")
                    line.sendMessage(msg.to,"❂•➤➤➤➤➤➤➤➤➤➤➤➤\n  • คท คือไร ควยเทวดาหรอคับ\n  • Me คือไร มีหีกระป๋องหรอคับ\n❂•➤➤➤➤➤➤➤➤➤➤➤➤")
                    line.sendMessage(msg.to,"❂•➤➤➤➤➤➤➤➤➤➤➤➤\n  • คท คือไร ควยเทวดาหรอคับ\n  • Me คือไร มีหีกระป๋องหรอคับ\n❂•➤➤➤➤➤➤➤➤➤➤➤➤")
                    line.sendMessage(msg.to,"❂•➤➤➤➤➤➤➤➤➤➤➤➤\n  • คท คือไร ควยเทวดาหรอคับ\n  • Me คือไร มีหีกระป๋องหรอคับ\n❂•➤➤➤➤➤➤➤➤➤➤➤➤")
                    line.sendMessage(msg.to,"❂•➤➤➤➤➤➤➤➤➤➤➤➤\n  • คท คือไร ควยเทวดาหรอคับ\n  • Me คือไร มีหีกระป๋องหรอคับ\n❂•➤➤➤➤➤➤➤➤➤➤➤➤")
                    line.sendMessage(msg.to,"❂•➤➤➤➤➤➤➤➤➤➤➤➤\n  • คท คือไร ควยเทวดาหรอคับ\n  • Me คือไร มีหีกระป๋องหรอคับ\n❂•➤➤➤➤➤➤➤➤➤➤➤➤")
                    line.sendMessage(msg.to,"❂•➤➤➤➤➤➤➤➤➤➤➤➤\n  • คท คือไร ควยเทวดาหรอคับ\n  • Me คือไร มีหีกระป๋องหรอคับ\n❂•➤➤➤➤➤➤➤➤➤➤➤➤")
                    line.sendMessage(msg.to,"❂•➤➤➤➤➤➤➤➤➤➤➤➤\n  • คท คือไร ควยเทวดาหรอคับ\n  • Me คือไร มีหีกระป๋องหรอคับ\n❂•➤➤➤➤➤➤➤➤➤➤➤➤")
                    line.sendMessage(msg.to,"❂•➤➤➤➤➤➤➤➤➤➤➤➤\n  • คท คือไร ควยเทวดาหรอคับ\n  • Me คือไร มีหีกระป๋องหรอคับ\n❂•➤➤➤➤➤➤➤➤➤➤➤➤")
                    line.sendMessage(msg.to,"❂•➤➤➤➤➤➤➤➤➤➤➤➤\n  • คท คือไร ควยเทวดาหรอคับ\n  • Me คือไร มีหีกระป๋องหรอคับ\n❂•➤➤➤➤➤➤➤➤➤➤➤➤")
                    line.sendMessage(msg.to,"❂•➤➤➤➤➤➤➤➤➤➤➤➤\n  • คท คือไร ควยเทวดาหรอคับ\n  • Me คือไร มีหีกระป๋องหรอคับ\n❂•➤➤➤➤➤➤➤➤➤➤➤➤")
                    line.sendMessage(msg.to,"❂•➤➤➤➤➤➤➤➤➤➤➤➤\n  • คท คือไร ควยเทวดาหรอคับ\n  • Me คือไร มีหีกระป๋องหรอคับ\n❂•➤➤➤➤➤➤➤➤➤➤➤➤")
                    line.sendMessage(msg.to,"💚• คท.บ้านพ่อมึงสิคับ •💚")
                    line.sendMessage(msg.to,"💚• Me บ้านพ่อมึงสิคับ •💚")
                    line.sendMessage(msg.to,"เกรียน on 8 ไม่มีคำสั่งนี้นะคับ")
#------------------------------------------------------------------------------------------------------------------------
                elif msg.text in ["ไวรัสเอจัง4"]:
                    line.sendMessage(msg.to,"ไวรัสเอจัง4➣➣➣➣➣➣➣➣\n   ❂••••••✧ℒįℳ✧•••••••❂\n➣➣➣➣➣➣➣•อะจึ๋งๆน่ารัก")
                    line.sendMessage(msg.to, "■•■•■•ไวรัสเอจังอะจึ๋งๆ•■•■•■")
                    line.sendMessage(msg.to, "💔💛💜ไวรัสน่ารัก💜💛💔")
                    line.sendMessage(msg.to, "■•■•■•ไวรัสเอจังอะจึ๋งๆ•■•■•■")
                    line.sendMessage(msg.to, "💔💛💜ไวรัสน่ารัก??💛💔")
                    line.sendMessage(msg.to, "■•■•■•ไวรัสเอจังอะจึ๋งๆ•■•■•■")
                    line.sendMessage(msg.to, "💔💛💜ไวรัสน่ารัก💜💛💔")
                    line.sendMessage(msg.to, "■•■•■•ไวรัสเอจังอะจึ๋งๆ•■•■•■")
                    line.sendMessage(msg.to, "💔💛💜ไวรัสน่ารัก💜💛💔")
                    line.sendMessage(msg.to, "■•■•■•ไวรัสเอจังอะจึ๋งๆ•■•■•■")
                    line.sendMessage(msg.to, "💔💛💜ไวรัสน่ารัก💜💛💔")
                    line.sendMessage(msg.to, "■•■•■•ไวรัสเอจังอะจึ๋งๆ•■•■•■")
                    line.sendMessage(msg.to, "💔💛💜ไวรัสน่ารัก💜💛💔")
                    line.sendMessage(msg.to, "■•■•■•ไวรัสเอจังอะจึ๋งๆ•■•■•■")
                    line.sendMessage(msg.to, "เกรียน on 8 ไวรัสเอจังน่ารักไหมคับ")
                    line.sendMessage(msg.to, "■•■•■•ไวรัสเอจังอะจึ๋งๆ•■•■•■")
#------------------------------------------------------------------------------------------------------------------------------------
                elif msg.text in ["Help","help","Help1","help1","Help2","help2","Help3","help3","Help4","help4","Help5","help5","Help6","help6","Help7","help7"]:
                    line.sendMessage(msg.to, "•💜• Help หาพ่อมึงหราคับ •💜•\n•💜• Help หาพ่อมึงหราคับ •💜•\n•💜• Help หาพ่อมึงหราคับ •💜•")
                    line.sendMessage(msg.to, "•💚• Help หาพ่อมึงหราคับ •💚•\n•💚• Help หาพ่อมึงหราคับ •💚•\n•💚• Help หาพ่อมึงหราคับ •💚•")
                    line.sendMessage(msg.to, "•💖• Help หาพ่อมึงหราคับ •💖•\n•💖• Help หาพ่อมึงหราคับ •💖•\n•💖• Help หาพ่อมึงหราคับ •💖•")
                    line.sendMessage(msg.to, "•💛• Help หาพ่อมึงหราคับ •💛•\n•💛• Help หาพ่อมึงหราคับ •💛•\n•💛• Help หาพ่อมึงหราคับ •💛•")
                    line.sendMessage(msg.to, "•💜• Help หาพ่อมึงหราคับ •💜•\n•💜• Help หาพ่อมึงหราคับ •💜•\n•💜• Help หาพ่อมึงหราคับ •💜•")
                    line.sendMessage(msg.to, "•💚• Help หาพ่อมึงหราคับ •💚•\n•💚• Help หาพ่อมึงหราคับ •💚•\n•💚• Help หาพ่อมึงหราคับ •💚•")
                    line.sendMessage(msg.to, "•💖• Help หาพ่อมึงหราคับ •💖•\n•💖• Help หาพ่อมึงหราคับ •💖•\n•💖• Help หาพ่อมึงหราคับ •💖•")
                    line.sendMessage(msg.to, "•💛• Help หาพ่อมึงหราคับ •💛•\n•💛• Help หาพ่อมึงหราคับ •💛•\n•💛• Help หาพ่อมึงหราคับ •💛•")
                    line.sendMessage(msg.to, "•💜• Help หาพ่อมึงหราคับ •💜•\n•💜• Help หาพ่อมึงหราคับ •💜•\n•💜• Help หาพ่อมึงหราคับ •💜•")
                    line.sendMessage(msg.to, "•💚• Help หาพ่อมึงหราคับ •💚•\n•💚• Help หาพ่อมึงหราคับ •💚•\n•💚• Help หาพ่อมึงหราคับ •💚•")
                    line.sendMessage(msg.to, "•💖• Help หาพ่อมึงหราคับ •💖•\n•💖• Help หาพ่อมึงหราคับ •💖•\n•💖• Help หาพ่อมึงหราคับ •💖•")
                    line.sendMessage(msg.to, "•💛• Help หาพ่อมึงหราคับ •💛•\n•💛• Help หาพ่อมึงหราคับ •💛•\n•💛• Help หาพ่อมึงหราคับ •💛•")
                    line.sendMessage(msg.to, "•💜• Help หาพ่อมึงหราคับ •💜•\n•💜• Help หาพ่อมึงหราคับ •💜•\n•💜• Help หาพ่อมึงหราคับ •💜•")
                    line.sendMessage(msg.to, "•💚• Help หาพ่อมึงหราคับ •💚•\n•💚• Help หาพ่อมึงหราคับ •💚•\n•💚• Help หาพ่อมึงหราคับ •💚•")
                    line.sendMessage(msg.to, "•💖• Help หาพ่อมึงหราคับ •💖•\n•💖• Help หาพ่อมึงหราคับ •💖•\n•💖• Help หาพ่อมึงหราคับ •💖•")
                    line.sendMessage(msg.to, "•💛• Help หาพ่อมึงหราคับ •💛•\n•💛• Help หาพ่อมึงหราคับ •💛•\n•💛• Help หาพ่อมึงหราคับ •💛•")
                    line.sendMessage(msg.to, "•💜• Help หาพ่อมึงหราคับ •💜•\n•💜• Help หาพ่อมึงหราคับ •💜•\n•💜• Help หาพ่อมึงหราคับ •💜•")
                    line.sendMessage(msg.to, "•💚• Help หาพ่อมึงหราคับ •💚•\n•💚• Help หาพ่อมึงหราคับ •💚•\n•💚• Help หาพ่อมึงหราคับ •💚•")
                    line.sendMessage(msg.to, "❂•➤➤➤➤➤➤➤➤➤➤➤➤\n  • 👉 ก็ไปแจ้งความสิคับอีฟาย\n  • 👉 ก็ไปแจ้งความสิคับอีฟาย\n❂•➤➤➤➤➤➤➤➤➤➤➤➤")
                    line.sendMessage(msg.to, "เกรียน on 10 ไม่มีคำสั่งนี้นะคับ")
                    line.sendMessage(msg.to, "❂•➤➤➤➤➤➤➤➤➤➤➤➤\n  • 👉 ก็ไปแจ้งความสิคับอีฟาย\n  • 👉 ก็ไปแจ้งความสิคับอีฟาย\n❂•➤➤➤➤➤➤➤➤➤➤➤➤")
#-----------------------------------------------------------------------------------------------------------------------------------------
                elif msg.text in ["ไวรัสสีชมพู","ไวรัสสีชุมพู"]:
                    line.sendMessage(msg.to, "💗•💗•💗•Virus Pink•💗•💗•💗")
                    line.sendMessage(msg.to, "💗•💗•💗•Virus Pink•💗•💗•💗")
                    line.sendMessage(msg.to, "💗•💗•💗•Virus Pink•💗•💗•💗")
                    line.sendMessage(msg.to, "💗•💗•💗•Virus Pink•💗•💗•💗")
                    line.sendMessage(msg.to, "💗•💗•💗•Virus Pink•💗•💗•💗")
                    line.sendMessage(msg.to, "💗•💗•💗•Virus Pink•💗•💗•💗")
                    line.sendMessage(msg.to, "💗•💗•💗•Virus Pink•💗•💗•💗")
                    line.sendMessage(msg.to, "💗•💗•💗•Virus Pink•💗•💗•💗")
                    line.sendMessage(msg.to, "💗•💗•💗•Virus Pink•💗•💗•💗")
                    line.sendMessage(msg.to, "💗•💗•💗•Virus Pink•💗•💗•💗")
                    line.sendMessage(msg.to, "💗•💗•💗•Virus Pink•💗•💗•💗")
                    line.sendMessage(msg.to, "💗•💗•💗•Virus Pink•💗•💗•💗")
                    line.sendMessage(msg.to, "💗•💗•💗•Virus Pink•💗•💗•💗")
                    line.sendMessage(msg.to, "💗•💗•💗•Virus Pink•💗•💗•💗")
                    line.sendMessage(msg.to, "💗•💗•💗•Virus Pink•💗•💗•💗")
                    line.sendMessage(msg.to, "💗•💗•💗•Virus Pink•💗•💗•💗")
                    line.sendMessage(msg.to, "💗•💗•💗•Virus Pink•💗•💗•💗")
                    line.sendMessage(msg.to, "💗•💗•💗•Virus Pink•💗•💗•💗")
                    line.sendMessage(msg.to, "💗•💗•💗•Virus Pink•💗•💗•💗")
                    line.sendMessage(msg.to, "💗•💗•💗•Virus Pink•💗•💗•💗")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.เ.อ.จั.ง.น่.า.รั๊.ก.ไ.ล.น์.เ.ขี.ย.ว.~.☆. 🤗.🕸.💙.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.")
                    line.sendMessage(msg.to, "💔.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.ค่.ะ.💚.💟.💛1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.ฟ.รุ้.ง.ฟ.ริ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.💓.💗.💖.")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.เ.อ.จั.ง.น่.า.รั๊.ก.ไ.ล.น์.เ.ขี.ย.ว.~.☆. 🤗.🕸.💙.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.")
                    line.sendMessage(msg.to, "💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                    line.sendMessage(msg.to, "เกรียน on 20 สีชมพูคับ")
#------------------------------------------------------------------------------------------------------------------------
                elif msg.text in ["ไวรัสปีโป้","ไวรัสเยลลี่","ไวรัสเจเล่"]:
                    line.sendMessage(msg.to,"✧•••••••••••❂✧✯✧❂••••••••••••✧\n      ✥✥ ֆҽℓƒ-β❂T-ՃิՁণຮี ✥✥ \n✧•••••••••••❂✧✯✧❂••••••••••••✧")
                    line.sendMessage(msg.to,"💖💖💖💖💖💖💖💖💖💖💖💖\n💚💚??💚💚💚💚💚💚💚💚💚\n💜💜💜💜💜💜💜💜💜ิ💜💜ิ💜")
                    line.sendMessage(msg.to,"💛💜💛💜💛💜💛💜💛💜💛💜\n ❂••••••• เอจังชอบกินปีโป้ •••••••❂\n💛💜💛💜💛💜💛💜💛💜💛💜")
                    line.sendMessage(msg.to,"💖💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚💚\n💜💜💜💜💜💜💜💜💜💜💜💜")
                    line.sendMessage(msg.to,"💛💜💛💜💛💜💛💜💛💜💛💜\n ❂••••••• ปีโป้นั้นมีหลากสี •••••••❂\n💛💜💛💜💛💜💛💜💛💜💛💜")
                    line.sendMessage(msg.to,"💖💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚💚\n💜💜💜💜💜💜💜💜💜💜💜💜")
                    line.sendMessage(msg.to,"💛💜💛💜💛💜💛💜💛💜💛💜\n ❂••••• อร่อยทุกสีเลยรู้ไหม •••••❂\n💛💜💛💜💛💜💛💜💛💜💛💜")
                    line.sendMessage(msg.to,"💖💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚💚\n💜💜💜💜💜💜💜💜💜💜💜💜")
                    line.sendMessage(msg.to,"💛💜💛💜💛💜💛💜💛ิ💜💛💜\n ❂•• พวกเรามากินปีโป้กันเถอะ ••❂\n💛💜💛💜💛💜💛💜💛💛💛💜")
                    line.sendMessage(msg.to,"💖💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚💚\n💜💜💜💜💜💜💜💜💜💜💜💜")
                    line.sendMessage(msg.to,"💀💀💀💀💀💀💀💀💀💀💀💀")
                    line.sendMessage(msg.to,"💀💀💀💀💀ุ้💀💀💀💀💀💀💀\n💀💀💀💀💀💀💀💀💀💀💀💀")
                    line.sendMessage(msg.to,"💀💀💀💀💀ุ้💀💀💀💀💀💀💀\n💀💀💀💀💀💀💀💀💀💀💀💀")
                    line.sendMessage(msg.to,"เกรียน on 10 ปีโป้อร่อยจัง")
                    line.sendMessage(msg.to,"💖💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚💚\n💜💜💜💜💜💜ั💜💜💜ิ💜💜💜")
                    line.sendMessage(msg.to,"💛💜💛💜💛💜💛💜💛💜💛💜\n ❂••••••• เอจังชอบกินปีโป้ •••••••❂\n💛💜💛💜💛💜💛💜💛💜💛💜")
                    line.sendMessage(msg.to,"💖💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚💚\n💜💜💜💜💜💜💜💜💜💜💜💜")
                    line.sendMessage(msg.to,"💛💜💛💜💛💜💛💜💛💜💛💜\n ❂•• พวกเรามากินปีโป้กันเถอะ ••❂\n💛💜💛💜💛💜💛💜💛💜💛💜")
                    line.sendMessage(msg.to,"💖💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚💚\n💜💜💜💜💜💜💜💜💜💜💜💜")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                elif msg.text in ["ไวรัสคิทตี้","ไวรัสคิดตี้","ไวรัสคิตตี้","ไวรัสป๊อกกี้"]:
                    line.sendMessage(msg.to,"✧•••••••••••❂✧✯✧❂••••••••••••✧\n      ✥✥ ֆҽℓƒ-β❂T-ℒįℳ ✥✥ \n✧•••••••••••❂✧✯✧❂••••••••••••✧")
                    line.sendMessage(msg.to,"💔💔ไวรัสแห่งความน่ารัก💔💔")                                                                                                                               
                    line.sendMessage(msg.to,"✧•••••••••❂✧✯✧❂•••••••••✧\n   💖💖 HELLO KITTY 💖💖\n✧•••••••••❂✧✯✧❂•••••••••✧")
                    line.sendMessage(msg.to,"•••••••Ħ€ŁŁ❂ ҜÏŦŦ¥✈•••••••\n💕💖💟💗💝💛💙💔💚💗\n💚💛💜💗💟💖💔💙💝💘")
                    line.sendMessage(msg.to,"•••••••Ħ€ŁŁ❂ ҜÏŦŦ¥✈•••••••\n💕💖💟💗💝💛💙💔💚💗\n💚💛💜💗💟💖💔💙💝💘")
                    line.sendMessage(msg.to,"•••••••Ħ€ŁŁ❂ ҜÏŦŦ¥✈•••••••\n💕💖💟💗💝💛💙💔💚💗\n💚💛💜💗💟💖💔💙💝💘")
                    line.sendMessage(msg.to,"💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚\n💗💗💗💗💗💗💗💗💗💗\n╬╬♡ • Ħëłłõ kîttÿ • ♡╬╬\n💗💗💗💗💗💗💗💗💗💗\n💜💜💜💜💜💜💜💜💜💜\n💛💛💛💛💛💛💛💛💛💛")
                    line.sendMessage(msg.to,"💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚\n💗💗💗💗💗💗💗💗💗💗\n╬╬♡ • Ħëłłõ kîttÿ • ♡╬╬\n💗💗💗💗💗💗💗💗💗💗\n💜💜💜💜💜💜💜💜💜💜\n💛💛💛💛💛💛💛💛💛💛")
                    line.sendMessage(msg.to,"💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚\n💗💗💗💗💗💗💗💗💗💗\n╬╬♡ • Ħëłłõ kîttÿ • ♡╬╬\n💗💗💗💗💗💗💗💗💗💗\n💜💜💜💜💜💜💜💜💜💜\n💛💛💛💛💛💛💛💛💛💛")
                    line.sendMessage(msg.to,"💟💟💟💟💟💟💟💟💟💟\n💖💖💖💖💖💖💖💖💖💖\n💜💜💜💜💜💜💜💜💜💜\n💟💟💟💟💟💟💟💟💟💟\n💛💛💛💛💛💛💛💛💛💛\n  💖💖 • Ħëłłõ kîttÿ • 💖💖\n💛💛💛💛💛💛💛💛💛💛\n💟💟💟💟💟💟💟💟💟💟\n💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖\n💟💟💟💟💟💟💟💟💟💟")
                    line.sendMessage(msg.to,"💟💟💟💟💟💟💟💟💟💟\n💖💖💖💖💖💖💖💖💖💖\n💜💜💜💜💜💜💜💜💜💜\n💟💟💟💟💟💟💟💟💟💟\n💛💛💛💛💛💛💛💛💛💛\n  💖💖 • Ħëłłõ kîttÿ • 💖💖\n💛💛💛💛💛💛💛💛💛💛\n💟💟💟💟💟💟💟💟💟💟\n💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖\n💟💟💟💟💟💟💟💟💟💟")
                    line.sendMessage(msg.to,"💟💟💟💟💟💟💟💟💟💟\n💖💖💖💖💖💖💖💖💖💖\n💜💜💜💜💜💜💜💜💜💜\n💟💟💟💟💟💟💟💟💟💟\n💛💛💛💛💛💛💛💛💛💛\n  💖💖 • Ħëłłõ kîttÿ • 💖💖\n💛💛💛💛💛💛💛💛💛💛\n💟💟💟💟💟💟💟💟💟💟\n💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖\n💟💟💟💟💟💟💟💟💟💟")
                    line.sendMessage(msg.to,"💟💟💟💟💟💟💟💟💟💟\n💖💖💖💖💖💖💖💖💖💖\n💜💜💜💜💜💜💜💜💜💜\n💟💟💟💟💟💟💟💟💟💟\n💛💛💛💛💛💛💛💛💛💛\n  💖💖 • Ħëłłõ kîttÿ • 💖💖\n💛💛💛💛💛💛💛💛💛💛\n💟💟💟💟💟💟💟💟💟💟\n💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖\n💟💟💟💟💟💟💟💟💟💟")
                    line.sendMessage(msg.to,"💟💟💟💟💟💟💟💟💟💟\n💖💖💖💖💖💖💖💖💖💖\n💜💜💜💜💜💜💜💜💜💜\n💟💟💟💟💟💟💟💟💟💟\n💛💛💛💛💛💛💛💛💛💛\n  💖💖 • Ħëłłõ kîttÿ • 💖💖\n💛💛💛💛💛💛💛💛💛💛\n💟💟💟💟💟💟💟💟💟💟\n💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖\n💟💟💟💟💟💟💟💟💟💟")
                    line.sendMessage(msg.to,"💟💟💟💟💟💟💟💟💟💟\n💖💖💖💖💖💖💖💖💖💖\n💜💜💜💜💜💜💜💜💜💜\n💟💟💟💟💟💟💟💟💟💟\n💛💛💛💛💛💛💛💛💛💛\n  💖💖 • Ħëłłõ kîttÿ • 💖💖\n💛💛💛💛💛💛💛💛💛💛\n💟💟💟💟💟💟💟💟💟💟\n💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖\n💟💟💟💟💟💟💟💟💟💟")
                    line.sendMessage(msg.to,"💟💟💟💟💟💟💟💟💟💟\n💖💖💖💖💖💖💖💖💖💖\n💜💜💜💜💜💜💜💜💜💜\n💟💟💟💟💟💟💟💟💟💟\n💛💛💛💛💛💛💛💛💛💛\n  💖💖 • Ħëłłõ kîttÿ • 💖💖\n💛💛💛💛💛💛💛💛💛💛\n💟💟💟💟💟💟💟💟💟💟\n💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖\n💟💟💟💟💟💟💟💟💟💟")
                    line.sendMessage(msg.to,"💟💟💟💟💟💟💟💟💟💟\n💖💖💖💖💖💖💖💖💖💖\n💜💜💜💜💜💜💜??💜💜\n💟💟💟💟💟💟💟💟💟💟\n💛💛💛💛💛💛💛💛💛💛\n  💖💖 • Ħëłłõ kîttÿ • 💖💖\n💛💛💛💛💛💛💛💛💛💛\n💟💟💟💟💟💟💟💟💟💟\n💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖\n💟💟💟💟💟💟💟💟💟💟")
                    line.sendMessage(msg.to,"💟💟💟💟💟💟💟💟💟💟\n💖💖💖💖💖💖💖💖💖💖\n💜💜💜💜💜💜💜💜💜💜\n💟💟💟💟💟💟💟💟💟💟\n💛💛💛💛💛💛💛💛💛💛\n  💖💖 • Ħëłłõ kîttÿ • 💖💖\n💛💛💛💛💛💛💛💛💛💛\n💟💟💟💟💟💟💟💟💟💟\n💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖\n💟💟💟💟💟💟💟💟💟💟")
                    line.sendMessage(msg.to, "เกรียน on 10 Hello Kitty")
                    line.sendMessage(msg.to,"💟💟💟💟💟💟💟💟💟💟\n💖💖💖💖💖💖💖💖💖💖\n💜💜💜💜💜💜💜💜💜💜\n💟💟💟💟💟💟💟💟💟💟\n💛💛💛💛💛💛💛💛💛💛\n  💖💖 • Ħëłłõ kîttÿ • 💖💖\n💛💛💛💛💛💛💛💛💛💛\n💟💟💟💟💟💟💟💟💟💟\n💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖\n💟💟💟💟💟💟💟💟💟💟")
                    line.sendMessage(msg.to,"💟💟💟💟💟💟💟💟💟💟\n💖💖💖💖💖💖💖💖💖💖\n💜💜💜💜💜💜💜💜💜💜\n💟💟💟💟💟💟💟💟💟💟\n💛💛💛💛💛💛💛💛💛💛\n  💖💖 • Ħëłłõ kîttÿ • 💖💖\n💛💛💛💛💛💛💛💛💛💛\n💟💟💟💟💟💟💟💟💟💟\n💜💜💜💜💜💜💜💜💜💜\n💖💖💖💖💖💖💖💖💖💖\n??💟💟💟💟💟💟💟💟💟")
                    line.sendMessage(msg.to,"•••••••Ħ€ŁŁ❂ ҜÏŦŦ¥✈•••••••\n💕💖💟💗💝💛💙💔💚💗\n💚💛💜💗💟💖💔💙💝💘")
#-----------------------------------------------------------------------------------------------------------------------------------------------------
                elif msg.text in ["ไวรัสฟรุ้งฟริ้ง","ไวรัสมุ้งมิ้ง"]:
                    line.sendMessage(msg.to,"✧•••••••••••❂✧✯✧❂••••••••••••✧\n      ✥✥ ֆҽℓƒ-β❂T-ℒįℳ✥✥ \n✧•••••••••••❂✧✯✧❂••••••••••••✧")
                    line.sendMessage(msg.to,"💔💔💔•Virus Chivaree•💔💔💔")
                    line.sendMessage(msg.to,"💛💛💛💛💛💛💛💛💛💛💛💛\n  ❂••••• ไวรัสฟรุ้งฟริ้งมุ้งมิ้ง •••••❂\n💛💛💛💛💛💛💛💛💛💛💛💛")
                    line.sendMessage(msg.to,"💖💖💖💖💖💖💖💖💖💖💖💖\n  ❂••••• ไวรัสฟรุ้งฟริ้งมุ้งมิ้ง •••••❂\n💖💖💖💖💖💖💖💖💖💖💖💖")
                    line.sendMessage(msg.to,"💙💙💙💙💙💙💙💙💙💙💙💙\n  ❂••••• ไวรัสฟรุ้งฟริ้งมุ้งมิ้ง •••••❂\n💙💙💙💙💙💙💙💙💙💙💙💙")
                    line.sendMessage(msg.to,"💚💚💚💚💚💚💚💚💚💚💚\n  ❂••••• ไวรัสฟรุ้งฟริ้งมุ้งมิ้ง •••••❂\n💚💚💚💚💚💚💚💚💚💚💚💚")
                    line.sendMessage(msg.to,"💜💜💜💜💜💜💜💜💜💜💜💜\n  ❂••••• ไวรัสฟรุ้งฟริ้งมุ้งมิ้ง •••••❂\n💜💜💜💜💜💜💜💜💜💜💜💜")
                    line.sendMessage(msg.to,"💛💛💛💛💛💛💛💛💛💛💛💛\n💛💛💛💛💛💛💛💛💛💛💛💛\n  ❂••••• ไวรัสฟรุ้งฟริ้งมุ้งมิ้ง •••••❂\n💛💛💛💛💛💛💛💛💛💛💛💛\n💛💛💛💛💛💛💛💛💛💛💛💛")
                    line.sendMessage(msg.to,"💖💖💖💖💖💖💖💖💖💖💖💖\n💖💖💖💖💖💖💖💖💖💖💖💖\n  ❂••••• ไวรัสฟรุ้งฟริ้งมุ้งมิ้ง •••••❂\n💖💖💖💖💖💖💖💖💖💖💖💖\n💖💖💖💖💖💖💖💖💖💖💖💖")
                    line.sendMessage(msg.to,"💙💙💙💙💙💙💙💙💙💙💙💙\n💙💙💙💙💙💙💙💙💙💙💙💙\n  ❂••••• ไวรัสฟรุ้งฟริ้งมุ้งมิ้ง •••••❂\n💙💙💙💙💙💙💙💙💙💙💙💙\n💙💙💙💙💙💙💙💙💙💙💙💙")
                    line.sendMessage(msg.to,"💚💚💚💚💚💚💚💚💚💚💚💚\n💚💚💚💚💚💚💚💚💚💚💚💚\n  ❂••••• ไวรัสฟรุ้งฟริ้งมุ้งมิ้ง •••••❂\n💚💚💚💚💚💚💚💚💚💚💚💚\n💚💚💚💚💚💚💚💚💚💚💚💚")
                    line.sendMessage(msg.to,"💜💜💜💜💜💜💜💜💜💜💜💜\n💜💜💜💜💜💜💜💜💜💜💜💜\n  ❂••••• ไวรัสฟรุ้งฟริ้งมุ้งมิ้ง •••••❂\n💜💜💜💜💜💜💜💜💜💜💜💜\n💜💜💜💜💜💜💜💜💜💜💜💜")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.เ.อ.จั.ง.คุริๆอะจึ๋งๆ~🌟ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Qฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.เอจังคับ")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.เ.อ.จั.ง.คุริๆอะจึ๋งๆ~🌟ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Qฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.เอจังคับ")
                    line.sendMessage(msg.to, "เกรียน on 9 ฟรุ้งฟริ้งสุดตีนคับ")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.เ.อ.จั.ง.คุริๆอะจึ๋งๆ~🌟ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Qฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.เอจังคับ")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.เ.อ.จั.ง.คุริๆอะจึ๋งๆ~🌟ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Qฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.เอจังคับ")
                    line.sendMessage(msg.to,"💖💖💖💖💖💖💖💖💖💖💖💖\n  ❂••••• ไวรัสฟรุ้งฟริ้งมุ้งมิ้ง •••••❂\n💖💖💖💖💖💖💖💖💖💖💖💖")
#----------------------------------------------------------------------------------------------------------------------------------------------------
                elif msg.text in ["ไวรัสรวมมิตร"]:
                    line.sendMessage(msg.to,"•••••••••☆❂-ℒįℳ•➤☆•••••••••\n✯::[[[ ไวรัสรวมมิตรพร้อมคับ ]]]::✯")
                    line.sendMessage(msg.to,"🍡🍡🍙เรื่องกินเรื่องใหญ่🍡ั๊🍡🍡")
                    line.sendMessage(msg.to,"💛💜💀💔🍋🍄🍓🍏⭐⏰💖\n🍏🍇🍎🍆🍅🍄🍋🍊🍡🍙🍚")                                  
                    line.sendMessage(msg.to,"💛💜💀💔🍋🍄🍓🍏⭐ิ⏰💖ึ\n🍏🍇🍎🍆🍅🍄🍋🍊🍓🍙🍚")                                           
                    line.sendMessage(msg.to,"💛💜💀💔🍋🍄🍓🍏⭐ิ⏰💖ึ\n🍏🍇🍎🍆🍅🍄🍋🍊🍡🍙🍚")
                    line.sendMessage(msg.to,"💛💜💀💔ั🍋🍄🍓🍏ั⭐⏰💖\n🍏🍇🍎🍆🍅🍄🍋์🍊ี🍡🍙🍚")
                    line.sendMessage(msg.to,"💛💜💀💔🍋🍄🍓🍏⭐⏰💖\n🍏🍇🍎🍆🍅🍄🍋🍊🍡🍙🍚")
                    line.sendMessage(msg.to,"🍰🌟🥂🍹🍮🍕🍤🍗🍟🍣🍫\n🍓🍒🍑🍅🍄🍉🥝🌴🌳🍍🍈\n🍇🍎🍡🍤🍙🍗🍣🍄🥝🍹🍑")
                    line.sendMessage(msg.to,"🍰🍧🥂🍹🍮🍕🍤🍗🍟🍣🍫\n🍓🍒🍑🍅🍄🍉🥝🌴🌳🍍🍈\n🍇🍎🍡🍤🍙🍗🍣🍄🥝🍹🍑")
                    line.sendMessage(msg.to,"🍰🍧🥂🍹🍮🍕🍤🍗🍟ิ🍣🍫\n🍓🍒🍑🍅🍄🍉🥝🌴🌳🍍🍈\n🍇🍎🍡🍤🍙🍗🍣🍄🥝🍹🍑")
                    line.sendMessage(msg.to,"🍰🍧🥂🍹🍮??🍤🍗🍟🍣🍫\n🍓🍒🍑🍅🍄🍉🥝🌴🌳🍍🍈\n🍇🍎🍡🍤🍙🍗🍣🍄🥝🍹🍑")
                    line.sendMessage(msg.to,"🍰🍧🥂🍹🍮🍕🍤🍗🍟🌟🍫\n🍓🍒🍑🍅🍄🍉??🌴🌳🍍๊🍈่\n🍇🍎🍡🍤🍙🍗🍄💚💚💚🍑")
                    line.sendMessage(msg.to,"🍰🍧🥂🍹🍮🍕🍤🍗🍟🍣🍫\n🍓🍒🍑🍅🍄🍉🥝🌴🌳🍍🍈\n🍇🍎🍡🍤??🍗🍣🍄🥝🍹🍑")
                    line.sendMessage(msg.to,"🍰🍧🥂🍹🍮🍕🍤🍗🍟🍣🍫\n🍓🍒🍑🍅🍄🍉🥝🌴🌳🍍🍈\n🍇🍎🍡🍤🍙🍗🍣🍄🥝🍹🍑")
                    line.sendMessage(msg.to,"เกรียน on 9 ขอให้อิ่มอร่อยทุกคนนะคับ")
                    line.sendMessage(msg.to,"🍰🍧🥂🍹🍮🍕🍤🍗🍟🍣🍫\n🍓🍒🍑🍅🍄🍉🥝🌴🌳🍍🍈\n🍇🍎🍡🍤🍙🍗🍣🍄🥝🍹🍑")
                    line.sendMessage(msg.to,"🍰🍧🥂🍹🍮🍕🍤🍗🍟ิ🍣🍗\n🍓🍒🍑🍅🍄🍉🥝🌴🌳🍍🍈\n🍇🍎🍡🍤🍙🍗🍣🍄🥝🍹🍑")
                    line.sendMessage(msg.to,"🍰🍧🥂🍹🍮🍕🍤🍗🍟🍣🍫\n🍓🍒🍑🍅🍄🍉🥝🌴🌳🍍🍈\n🍇🍎🍡🍤🍙🍗🍣🍄🥝🍹🍑")
                    line.sendMessage(msg.to,"🍰🍧🥂🍹🍮🍕🍤🍗🍟🍣🍫\n🍓🍒🍑🍅🍄🍉🥝🌴🌳🍍๊🍈่\n🍇🍎🍡🍤🍙🍗🍣🍄🥝🍹🍑")
#-------------------------------------------------------------------------------------------------------------------------------------------
                elif msg.text in ["ไวรัสฟรุตตี้","ไวรัสฟรุ้ตตี้","ไวรัสผลไม้"]:
                    line.sendMessage(msg.to,"✧•••••••••••❂✧✯✧❂••••••••••••✧\n      ✥✥ ֆҽℓƒ-β❂T-ℒįℳ ✥✥ \n✧•••••••••••❂✧✯✧❂••••••••••••✧")
                    line.sendMessage(msg.to,"🍌🍎🍏ผลไม้มีวิตามินคับ🍊🍋🍄")
                    line.sendMessage(msg.to,"🍌🍎🍏🍊🍋🍄🍅🍏🍉🍊🍋\n🍇🍈🍉🍐🍑🍒??🍍🥝🍌🌰")
                    line.sendMessage(msg.to,"🍌🍎🍏🍊🍋🍄🍅🍏🍉🍊🍋\n🍇🍈🍉🍐🍑🍒🍓🍍🥝🍌🌰")
                    line.sendMessage(msg.to,"🍌🍎🍏🍊🍋🍄🍅🍏🍉🍊🍒\n🍇🍈🍉🍐🍑🍒🍓🍍🥝🍌🌰")
                    line.sendMessage(msg.to,"🍌🍎🍏🍊🍋🍄🍅🍏🍉🍊🍋\n🍇🍈🍉🍐🍑🍒🍓🍍🥝🍌🌰")
                    line.sendMessage(msg.to,"🍌🍎🍏🍊🍋🍄🍅🍏🍉🍊🍋\n🍇🍈🍉🍐🍑🍒🍓🍍🥝🍌🌰")
                    line.sendMessage(msg.to,"🍌🍎🍏🍊🍋🍄🍅🍏🍉🍊🍋\n🍇🍈🍉🍐🍑🍒🍓🍍🥝🍌🌰")
                    line.sendMessage(msg.to,"🍌🍎🍏🍊🍋🍄🍅🍏🍉🍊🍋\n🍇🍈🍉🍐🍑🍓🍓🍍🥝🍌🌰")
                    line.sendMessage(msg.to,"🍌🍎🍏🍊🍋🍄🍅🍏🍉🍊🍋\n🍇🍈🍉🍐🍑🍒🍓🍍🥝🍌🌰")
                    line.sendMessage(msg.to,"🍌🍎🍏🍊🍋🍄🍅🍏🍉🍊🍋\n💚🍈💚🍐🍑🍒🍓🍍🥝🍌🌰")
                    line.sendMessage(msg.to,"🍌🍎🍏มาทานผลไม้คับ🍊🍋🍄")
                    line.sendMessage(msg.to,"🍌🍎🍏🍊🍋🍄🍅🍏🍉🍊🍋\n🍇🍈🍉🍐🍑🍒🍓🍍🥝🍌🌰")
                    line.sendMessage(msg.to,"🍌🍎🍏🍊🍋🍄🍅🍏🍉🍊🍋\n🍇🍈🍉🍐🍑🍒🍓🍍🥝🍌🌰")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.เ.อ.จั.ง.คุริๆอะจึ๋งๆ~🌟ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Qฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.เอจังคับ")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.เ.อ.จั.ง.น่.า.รั๊.ก.ไ.ล.น์.เ.ขี.ย.ว.~.☆. 🤗.🕸.💙.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.")
                    line.sendMessage(msg.to, "💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                    line.sendMessage(msg.to, "เกรียน on 9 ฟรุ้ตตี้น่ารัก")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.เ.อ.จั.ง.น่.า.รั๊.ก.ไ.ล.น์.เ.ขี.ย.ว.~.☆. 🤗.🕸.💙.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.")
#-------------------------------------------------------------------------------------------------------------------------------------------                    
                elif msg.text in ["ไวรัสชิวารีแบ๊วไหมคับ","ฟรุ้งฟริ้งสุดตีนคับ"]:
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.เ.อ.จั.ง.คุริๆอะจึ๋งๆ~🌟ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Qฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.เอจังคับ")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    line.sendMessage(msg.to, "💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                    line.sendMessage(msg.to, "💔.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.ค่.ะ.💚.💟.💛1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.ฟ.รุ้.ง.ฟ.ริ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.💓.💗.💖.")
                    line.sendMessage(msg.to, "💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    line.sendMessage(msg.to, "ไวรัสเอจังฟรุ้งฟรุ้งมุ้งมิ้ง~☆😍💜💛💚💙💗💖.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.ฟรุ้งฟริ้ง by.เอจัง~☆🤗")
                    line.sendMessage(msg.to, "💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    line.sendMessage(msg.to, "💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.??เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    line.sendMessage(msg.to, "💔.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.ค่.ะ.💚.💟.💛1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.51.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.ฟ.รุ้.ง.ฟ.ริ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.💓.💗.💖.")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.เ.อ.จั.ง.คุริๆอะจึ๋งๆ~🌟ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Qฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.เอจังคับ")
                    line.sendMessage(msg.to, "💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.เ.อ.จั.ง.คุริๆอะจึ๋งๆ~🌟ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Qฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.เอจังคับ")
                    line.sendMessage(msg.to, "💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.เ.อ.จั.ง.น่.า.รั๊.ก.ไ.ล.น์.เ.ขี.ย.ว.~.☆. 🤗.🕸.💙.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.")
                    line.sendMessage(msg.to,"💚•ไวรัสน่ารักแอ๊บแบ๊วมากคับ•💚")
#------------------------------------------------------------------------------------------------------------------------------------------
                elif msg.text in ["ไวรัสเอจังน่ารักไหมคับ"]:
                    line.sendMessage(msg.to, "💔.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.ค่.ะ.💚.💟.💛1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.ฟ.รุ้.ง.ฟ.ริ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.💓.💗.💖.")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.เ.อ.จั.ง.คุริๆอะจึ๋งๆ~🌟ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Qฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.เอจังคับ")
                    line.sendMessage(msg.to, "💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                    line.sendMessage(msg.to, "💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                    line.sendMessage(msg.to, "💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    line.sendMessage(msg.to, "💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.เ.อ.จั.ง.คุริๆอะจึ๋งๆ~🌟ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Qฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.เอจังคับ")
                    line.sendMessage(msg.to, "ไวรัสเอจังฟรุ้งฟรุ้งมุ้งมิ้ง~☆😍💜💛💚💙💗💖.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.ฟรุ้งฟริ้ง by.เอจัง~☆🤗")
                    line.sendMessage(msg.to, "💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.เ.อ.จั.ง.น่.า.รั๊.ก.ไ.ล.น์.เ.ขี.ย.ว.~.☆. 🤗.??.💙.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    line.sendMessage(msg.to,"💖•ไวรัสเอจังน่ารักฝุดๆเบยคับ•💖")
#------------------------------------------------------------------------------------------------------------------------------------------        
                elif msg.text in ["ขอให้อิ่มอร่อยทุกคนนะคับ"]:
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.เ.อ.จั.ง.น่.า.รั๊.ก.ไ.ล.น์.เ.ขี.ย.ว.~.☆. 🤗.🕸.💙.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.")
                    line.sendMessage(msg.to, "💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                    line.sendMessage(msg.to, "💔.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.ค่.ะ.💚.💟.💛1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.ฟ.รุ้.ง.ฟ.ริ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.💓.💗.💖.")
                    line.sendMessage(msg.to, "ไวรัสเอจังฟรุ้งฟรุ้งมุ้งมิ้ง~☆😍💜💛💚💙💗💖.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.ฟรุ้งฟริ้ง by.เอจัง~☆🤗")
                    line.sendMessage(msg.to, "ไวรัสเอจังฟรุ้งฟริ้งมุ้งมิ้ง~☆💜💛💓💟💚💙💗💖🤗1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.1.๑.")
                    line.sendMessage(msg.to, "💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.เ.อ.จั.ง.คุริๆอะจึ๋งๆ~🌟ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Qฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.เอจังคับ")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.เ.อ.จั.ง.คุริๆอะจึ๋งๆ~🌟ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Qฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.เอจังคับ")
                    line.sendMessage(msg.to, "💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    line.sendMessage(msg.to,"🍰🍡🍤🍗🍋🍄🍓🍏🍉🍧🍟\n  อิ่มมากเลย ขอหลับก่อนน๊าคับ\n🍏🍇🍎🍆🍅🍄🍋🍊🍡🍙🍚")
#------------------------------------------------------------------------------------------------------------------------------------------
                elif msg.text in ["ไม่มีคำสั่งนี้นะคับ"]:
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.เ.อ.จั.ง.คุริๆอะจึ๋งๆ~🌟ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Qฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.เอจังคับ")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.เ.อ.จั.ง.คุริๆอะจึ๋งๆ~🌟ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Qฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.เอจังคับ")
                    line.sendMessage(msg.to, "💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                    line.sendMessage(msg.to, "💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    line.sendMessage(msg.to, "💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    line.sendMessage(msg.to, "💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    line.sendMessage(msg.to, "💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.เ.อ.จั.ง.น่.า.รั๊.ก.ไ.ล.น์.เ.ขี.ย.ว.~.☆. 🤗.🕸.💙.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.เ.อ.จั.ง.คุริๆอะจึ๋งๆ~🌟ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Qฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.เอจังคับ")
                    line.sendMessage(msg.to, "💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    line.sendMessage(msg.to,"💜•เป็นห่วงเสมอน่ะคับ จุ้ฟป้อก•💜")
#------------------------------------------------------------------------------------------------------------------------------------------
# 💚💛💜     สุดเขตแดนไวรัสเอจัง  ขอให้เล่นอย่างสนุกสนานนะคับ จุ้ฟป้อก
#------------------------------------------------------------------------------------------------------------------------------------------
                elif msg.text in ["ผู้สร้างไวรัส"]:
                    line.sendMessage(msg.to, "ผู้สร้างไวรัส➣➣➣➣➣➣➣➣\n   ❂••••••✧ℒįℳ✧•••••••❂\n➣➣➣➣➣➣➣➣•Chiväree™")
                    line.sendMessage(msg.to, "💗💗💗💗💗💗💗💗💗💗\n   •ผู้สร้างไวรัสที่แสนน่ารัก•\n💗💗💗💗💗💗💗💗💗💗")
                    line.sendMessage(msg.to, "💚💚💚💚💚💚💚💚💚💚\n   •ผู้สร้างไวรัสที่แสนน่ารัก•\n💚💚💚💚💚💚💚💚💚💚")
                    line.sendMessage(msg.to, "💗💗💗💗💗💗💗💗💗💗\n   •ผู้สร้างไวรัสที่แสนน่ารัก•\n💗💗💗💗💗💗💗💗💗💗")
                    line.sendMessage(msg.to, "💚💚💚💚💚💚💚💚💚💚\n   •ผู้สร้างไวรัสที่แสนน่ารัก•\n💚💚💚💚💚💚💚💚💚💚")
                    line.sendMessage(msg.to, "●•➤➤➤➤➤➤➤➤➤➤\n    \n●•➤➤➤➤➤➤➤➤➤➤")
                    line.sendMessage(msg.to, "💔💔💔 [ คนไหน ] 💔💔💔")
                    line.sendMessage(msg.to, "💚💚💚 [ คนไหน ] 💚💚💚")
                    line.sendMessage(msg.to, "💜💜💜 [ คนไหน ] 💜💜💜")
                    line.sendMessage(msg.to, "💛💛💛 [ คนไหน ] 💛💛💛")
                    line.sendMessage(msg.to, "💖💖💖 [ คนไหน ] 💖💖💖")
                    line.sendMessage(msg.to,"❂➣-ՃิՁণຮี: 🕟 " +datetime.today().strftime('%H:%M:%S')+ "➤")
                    line.sendContact(to, "u669aa92773d33c22420105d4546fccdd")
                    line.sendMessage(msg.to, "👆•Virus A-jang : ผู้สร้าง•👆")
#--------------------------------------------------------------------------------------------------------------------------    
                elif msg.text in ["สมุน7","เจต7","สกิล7"]:
                    line.sendMessage(to, "🌀มึงอ่านบ้างนะคับ " +datetime.today().strftime('%H:%M:%S')+ "🌀")
                    line.sendMessage(msg.to, "✧••••••••••••❂✧✯✧❂•••••••••••••✧\n   ✥✥✥ ֆҽℓƒ-β❂T-ՃิՁণຮี ✥✥✥\n✧••••••••••••❂✧✯✧❂•••••••••••••✧\n\n          ♡•โหมดบ้านพ่อมึงคับ•♡\n\n╭☆•☆•☆•☆•☆•☆•☆•☆•☆•☆•☆\n♡•➣ ไอ้ควายเอ้ย...........\n♡\n♡•➣➣➣ไม่มีสกิล7 ในระบบนี้คับ\n♡\n♡•➣➣➣➣รอให้พ่อมรุงสร้างให้คับ\n♡\n♡  ค.ควาย ค.ควาย ค.ควาย ค.ควาย\n╰☆•☆•☆•☆•☆•☆•☆•☆•☆•☆•☆\n\n✧••••••••••••❂✧✯✧❂•••••••••••••✧\n ♡วิธีใช้ : ไม่ต้องใส่จุดคับเสียเวลา♡")
#------------------------------------------------------------------------------------------------------------------------
                elif msg.text in ["ผู้สร้างกลุ่ม","เจ้าของห้อง","เจ้าของบ้าน","เจ้าบ้าน"]:
                    line.sendMessage(msg.to, "💔💔💔 [ คนไหน ] 💔💔💔")
                    line.sendMessage(msg.to, "💚💚💚 [ คนไหน ] 💚💚💚")
                    line.sendMessage(msg.to, "💜💜💜 [ คนไหน ] 💜💜💜")
                    line.sendMessage(msg.to, "💛💛💛 [ คนไหน ] 💛💛💛")
                    line.sendMessage(msg.to, "💖💖💖 [ คนไหน ] 💖💖💖")
                    group = line.getGroup(to)
                    GS = group.creator.mid
                    line.sendContact(to, GS)
                    line.sendMessage(to,"👆• นี่ไงผู้สร้างหน้าม่อคับ •👆\nBy : ֆҽℓƒ-β❂T-ℒįℳ  🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")
                elif msg.text in ["ไอดีกลุ่ม"]:
                    gid = line.getGroup(to)
                    line.sendMessage(to, "🌀รอสักครู่คับ ⏰ " +datetime.today().strftime('%H:%M:%S')+ "🌀") 
                    line.sendMessage(to, "❂•ไอดีกลุ่มคับ•➣➣➣➣➣\n" + gid.id)
                elif msg.text in ["รูปกลุ่ม"]:
                    line.sendMessage(to, "🌀รอสักครู่คับ ⏰ " +datetime.today().strftime('%H:%M:%S')+ "🌀") 
                    line.sendMessage(to, "✯:::[[[ รูปประจำกลุ่มคับ ]]]:::✯")
                    group = line.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    line.sendImageWithURL(to, path)
                elif msg.text in ["ชื่อกลุ่ม"]:
                    line.sendMessage(to, "🌀รอสักครู่คับ ⏰ " +datetime.today().strftime('%H:%M:%S')+ "🌀") 
                    gid = line.getGroup(to)
                    line.sendMessage(to, "❂•ชื่อกลุ่มคับ•➣➣➣➣➣\n" + gid.name)
                elif msg.text in ["ลิ้งกลุ่ม","เอจังขอลิ้ง","ขอลิ้ง"]:
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            line.sendMessage(to, "ֆҽℓƒ-β❂T-ℒįℳ ")
                            line.sendMessage(to, "🌀รอสักครู่คับ ⏰ " +datetime.today().strftime('%H:%M:%S')+ "🌀") 
                            ticket = line.reissueGroupTicket(to)
                            line.sendMessage(to, "❂•ลิ้งกลุ่มคับ•➣➣➣➣➣\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                elif msg.text in ["เปิดลิ้งกลุ่ม","เอจังเปิดลิ้ง","เปิดลิ้ง"]:
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            line.sendMessage(to, "✯::[[[ เปิดลิ้งกลุ่มเรียบร้อยคับ ]]]::✯")
                        else:
                            group.preventedJoinByTicket = False
                            line.updateGroup(group)
                            line.sendMessage(to, "✯::[[[ เปิดลิ้งกลุ่มเรียบร้อยคับ ]]]::✯")
                elif msg.text in ["ปิดลิ้งกลุ่ม","เอจังปิดลิ้ง","ปิดลิ้ง"]:
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            line.sendMessage(to, "✯::[[[ ปิดลิ้งกลุ่มเรียบร้อยคับ ]]]::✯")
                        else:
                            group.preventedJoinByTicket = True
                            line.updateGroup(group)
                            line.sendMessage(to, "✯::[[[ ปิดลิ้งกลุ่มเรียบร้อยคับ ]]]::✯")
                elif msg.text in ["ข้อมูลกลุ่ม"]:
                    group = line.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "คนนี้คือผู้สร้างกลุ่มนี้"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "ปิด"
                        gTicket = "   รายการลิงค์กลุ่มปิดอยู่คับ"
                    else:
                        gQr = "เปิด"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(line.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "❂ข้อมูลกลุ่ม •➣➣➣➣➣➣➣➣➣"
                    ret_ += "\n•✯• ชื่อกลุ่ม \n     ➤ {}".format(str(group.name))
             #       ret_ += "\n•✯• ผู้สร้างกลุ่ม\n ➤ {}".format(group.id)
                    ret_ += "\n•✯• ผู้สร้างกลุ่ม \n     ➤ {}".format(str(gCreator))
                    ret_ += "\n•✯• จำนวนสมาชิก : {} คน".format(str(len(group.members)))
                    ret_ += "\n•✯• จำนวนค้างเชิญ : {} คน".format(gPending)
                    ret_ += "\n•✯• สถานะกลุ่ม : {}".format(gQr)
                    ret_ += "\n❂Chiväree™•➣➣➣➣➣➣➣➣➣\n\n{}".format(gTicket)
                    ret_ += "\n      ✧•••••❂✧ลิ้งกลุ่มคับ✧❂•••••✧"
                    line.sendMessage(to, str(ret_))
                    line.sendImageWithURL(to, path)
                elif msg.text in ["สมาชิกกลุ่ม"]:
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        ret_ = "       ♡•สมาชิกในกลุ่มนี้คับ•♡\n●•➤➤➤➤➤➤➤➤➤➤➤➤"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n♡ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n●•➤➤➤➤➤➤➤➤➤➤➤➤\n   [ จำนวน {} คน  by : ֆҽℓƒ-β❂T-ℒįℳ  ]".format(str(len(group.members)))
                        line.sendMessage(to, str(ret_))
                elif msg.text in ["เอจังกลุ่ม","กลุ่มเอจัง","เช็คกลุ่ม","อวดกลุ่ม"]:
                        line.sendMessage(msg.to,"🌀รอสักครู่คับ 🕒 " +datetime.today().strftime('%H:%M:%S')+ "🌀")
                        groups = line.groups
                        ret_ = "✧•••••••••••❂✧✯✧❂•••••••••••✧\n      ♡♡ กลุ่มคนน่ารักคับ ♡♡\n✧•••••••••••❂✧✯✧❂•••••••••••✧"
                        no = 0 + 1
                        for gid in groups:
                            group = line.getGroup(gid)
                            ret_ += "\n {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n✧•••••••••••❂✧✯✧❂•••••••••••✧\n   [ จำนวน {} Groups ] By เฮียยิ้ม".format(str(len(groups)))
                        line.sendMessage(to, str(ret_))				
                elif "เชิญคลอ" == msg.text.lower():
                    line.inviteIntoGroupCall(msg.to,[uid.mid for uid in line.getGroup(msg.to).members if uid.mid != line.getProfile().mid])
                    line.sendMessage(msg.to,"เชิญเข้าร่วมการโทรสำเร็จ(｀・ω・´)")
                elif ".sh " in msg.text.lower():
                    spl = re.split(".sh ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        try:
                            line.sendText(msg.to,subprocess.getoutput(spl[1]))
                        except:
                            pass
                elif msg.text.lower() == 'เชิญแอด':
                	if msg.toType == 2:                
                           ginfo = line.getGroup(receiver)
                           try:
                               gcmid = ginfo.creator.mid
                           except:
                               gcmid = "Error"
                           if settings["lang"] == "JP":
                               line.inviteIntoGroup(receiver,[gcmid])
                               line.sendMessage(receiver, "พิมพ์คำเชิญกลุ่มแล้ว")
                           else:
                               line.inviteIntoGroup(receiver,[gcmid])
                               line.sendMessage(receiver, "ผู้สร้างกลุ่มอยู่ในแล้ว")
                               
                elif msg.text.lower() == "getjoined":
                    line.sendText(msg.to,"กรุณารอสักครู่ ใจเย็นๆ")
                    all = line.getGroupIdsJoined()
                    text = ""
                    cnt = 0
                    for i in all:
                        text += line.getGroup(i).name + "\n" + i + "\n\n"
                        cnt += 1
                        if cnt == 10:
                            line.sendText(msg.to,text[:-2])
                            text = ""
                            cnt = 0
                    line.sendText(msg.to,text[:-2])
                    cnt = 0				
                elif "ข้อมูล " in msg.text.lower():
                    spl = re.split("ข้อมูล ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        for i in range(len(prov)):
                            uid = prov[i]["M"]
                            userData = line.getContact(uid)
                            try:
                                line.sendImageWithUrl(msg.to,"http://dl.profile.line-cdn.net{}".format(userData.picturePath))
                            except:
                                pass
                            line.sendMessage(msg.to,"✧•••••••••❂✧✯✧❂••••••••••✧\n   ♡ ข้อมูลคนหน้าม่อเจ้าคับ ♡\n✧•••••••••❂✧✯✧❂••••••••••✧")
                            line.sendMessage(msg.to,"✯::: ♡•ชื่อคนหน้าม่อคับ•♡ :::✯\n❂➣ "+userData.displayName)
                            line.sendMessage(msg.to,"✯::: ♡•ตัสคนหน้าม่อคับ•♡ :::✯\n"+userData.statusMessage)
                            line.sendMessage(msg.to,"✯::: ♡•ไอดีคนหน้าม่อคับ•♡ :::✯\n"+userData.mid)
                
                elif "รับแก้ไฟล์+เพิ่มไฟล์+แก้ภาษา\n💝ราคาดูที่หน้างาน💝\n👉มีบริการให้เช่าบอทSAMURAI\nราคา300บาทต่อเดือน💖\n#เพิ่มคิกเกอร์ตัวละ100👌\n🎀สนใจรีบทัก..บอทpython3ฟังชั่นล้นหลาม🎁กำลังรอให้คุณเป็นเจ้าของ\n(ผมจะอยู่ที่ห้องนี้แค่15นาทีนะจ๊ะ)\nselfbot by:\n╔══════════════┓\n╠™❍✯͜͡RED™ֆҽℓƒ-β❂T-ℒįℳ✯͜͡❂➣ \n╚══════════════┛" in msg.text:
                    spl = msg.text.split("รับแก้ไฟล์+เพิ่มไฟล์+แก้ภาษา\n💝ราคาดูที่หน้างาน💝\n👉มีบริการให้เช่าบอทSAMURAI\nราคา300บาทต่อเดือน💖\n#เพิ่มคิกเกอร์ตัวละ100??\n🎀สนใจรีบทัก..บอทpython3ฟังชั่นล้นหลาม🎁กำลังรอให้คุณเป็นเจ้าของ\n(ผมจะอยู่ที่ห้องนี้แค่15นาทีนะจ๊ะ)\nselfbot by:\n╔══════════════┓\n╠™❍✯͜͡RED™ֆҽℓƒ-β❂T-ℒįℳ ✯͜͡❂➣ \n╚══════════════┛")
                    if spl[len(spl)-1] == "":
                        line.sendText(msg.to,"กดที่นี่เพื่อเขย่าข้อความด้านบน:\nline://nv/chatMsg?chatId="+msg.to+"&messageId="+msg.id)
                elif "เอจังรัน @" in msg.text:
                    print ("[Command]covergroup")
                    _name = msg.text.replace("เอจังรัน @","")
                    _nametarget = _name.rstrip('  ')
                    gs = line.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        line.sendMessage(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                               thisgroup = line.getGroups([msg.to])
                               Mids = [target for contact in thisgroup[0].members]
                               mi_d = Mids[:33]
                               line.createGroup(" ╬╬❂•ຟနุ้७ຟနิ้७•❂╬╬",mi_d)
                               line.sendMessage(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup(" ╬╬❂•ຟနุ้७ຟနิ้७•❂╬╬",mi_d)
                               line.sendMessage(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup(" ╬╬❂•ຟနุ้७ຟနิ้७•❂╬╬",mi_d)
                               line.sendMessage(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup(" ╬╬❂•ຟနุ้७ຟနิ้७•❂╬╬",mi_d)
                               line.sendMessage(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup(" ╬╬❂•ຟနุ้७ຟနิ้७•❂╬╬",mi_d)
                               line.sendMessage(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup(" ╬╬❂•ຟနุ้७ຟနิ้७•❂╬╬",mi_d)
                               line.sendMessage(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup(" ╬╬❂•ຟနุ้७ຟနิ้७•❂╬╬",mi_d)
                               line.sendMessage(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup(" ╬╬❂•ຟနุ้७ຟနิ้७•❂╬╬",mi_d)
                               line.sendMessage(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup(" ╬╬❂•ຟနุ้७ຟနิ้७•❂╬╬",mi_d)
                               line.sendMessage(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup(" ╬╬❂•ຟနุ้७ຟနิ้७•❂╬╬",mi_d)
                               line.sendMessage(msg.to,"??⛷️[จะออกไปแตะขอบฟ้า]")
                               line.sendMessage(msg.to,"เรียบร้อย")
                            except:
                                pass
                    print ("[Command]covergroup]")
                elif "รันแชท @" in msg.text:
                    _name = msg.text.replace("รันแชท @","")
                    _nametarget = _name.rstrip(' ')
                    gs = line.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                           line.sendMessage(msg.to,"✲กำลังดำเนินการคับ.....✲") 
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀??🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀") 
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀") 
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀") 
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀") 
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀??🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀") 
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀") 
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀") 
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀") 
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀") 
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀") 
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀??🌀🌀🌀🌀🌀🌀??")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀??🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀") 
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀") 
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀") 
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀") 
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(g.mid,"🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(msg.to, "🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀\n✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n🌀🌀🌀🌀🌀🌀🌀🌀🌀🌀")
                           line.sendMessage(msg.to, "🌀•รันแชทเสร็จเรียบร้อยคับ•🌀\n Spam@Chät 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")
                           print (" Spammed !")
                elif ".สำรองห้อง" in msg.text:
                    thisgroup = line.getGroups([msg.to])
                    Mids = [contact.mid for contact in thisgroup[0].members]
                    mi_d = Mids[:33]
                    line.createGroup("RED SAMURI SELFBOT", mi_d)
                    line.sendMessage(msg.to,"REDSAMURAI")
                    line.createGroup("RED SAMURI SELFBOT", mi_d)
                    line.sendMessage(msg.to,"REDSAMURAI")
                elif ".รัน: " in msg.text.lower():
                        key = msg.text[-33:]
                        line.findAndAddContactsByMid(key)                   
                        contact = cl.getContact(key)
                        line.createGroup("RED SAMURAI Group",[key])
                        line.sendMessage(msg,to,"┌∩┐(◣_◢)┌∩┐")
                elif ".ไม่รับเชิญ " in msg.text.lower():
                    spl = re.split(".ไม่รับเชิญ ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        spl[1] = spl[1].strip()
                        ag = line.getGroupIdsInvited()
                        txt = "กำลังยกเลิกค้างเชิญจำนวน "+str(len(ag))+" กลุ่ม"
                        if spl[1] != "":
                            txt = txt + " ด้วยข้อความ \""+spl[1]+"\""
                        txt = txt + "\nกรุณารอสักครู่.."
                        line.sendText(msg.to,txt)
                        procLock = len(ag)
                        for gr in ag:
                            try:
                                line.acceptGroupInvitation(gr)
                                if spl[1] != "":
                                    line.sendText(gr,spl[1])
                                line.leaveGroup(gr)
                            except:
                                pass
                        line.sendMessage(msg.to,"สำเร็จแล้ว")	
                elif ".whois " in msg.text.lower():
                    spl = re.split(".whois ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        msg.contentType = 13
                        msg.text = None
                        msg.contentMetadata = {"mid":spl[1]}
                        line.sendMessage(msg)
                elif "หวด" in msg.text.lower():
                    if msg.toType == 2:
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        for i in range(len(prov)):
                            random.choice(Exc).kickoutFromGroup(msg.to,[prov[i]["M"]])
                elif "ล้อเล่น " in msg.text:
                    Ri0 = text.replace("ล้อเล่น ","")
                    Ri1 = Ri0.rstrip()
                    Ri2 = Ri1.replace("@","")
                    Ri3 = Ri2.rstrip()
                    _name = Ri3
                    gs = line.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    line.sendMessage(to, "🔅ทำการเตะแล้วดึงกลับคับ🔅") 
                                    line.kickoutFromGroup(to,[target])
                                    line.findAndAddContactsByMid(target)
                                    line.inviteIntoGroup(to,[target])
                                except:
                                    pass
                elif "ปลิว" in msg.text.lower():
                    if msg.toType == 2:
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        allmid = []
                        for i in range(len(prov)):
                            line.kickoutFromGroup(msg.to,[prov[i]["M"]])
                            allmid.append(prov[i]["M"])
                        line.findAndAddContactsByMids(allmid)
                        line.inviteIntoGroup(msg.to,allmid)
                        line.cancelGroupInvitation(msg.to,allmid)

                elif msg.text.lower() == "mid":
                    line.sendText(msg.to,user1)
                
                elif ".name " in msg.text.lower():
                    spl = re.split(".name ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        prof = line.getProfile()
                        prof.displayName = spl[1]
                        line.updateProfile(prof)
                        line.sendMessage(msg.to,"สำเร็จแล้ว")
                elif ".nmx " in msg.text.lower():
                    spl = re.split(".nmx ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        prof = line.getProfile()
                        prof.displayName = line.nmxstring(spl[1])
                        line.updateProfile(prof)
                        line.sendMessage(msg.to,"สำเร็จแล้ว")
                elif "มุด " in msg.text.lower():
                    spl = re.split(".มุด ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        try:
                            gid = spl[1].split(" ")[0]
                            ticket = spl[1].split(" ")[1].replace("line://ti/g/","") if "line://ti/g/" in spl[1].split(" ")[1] else spl[1].split(" ")[1].replace("http://line.me/R/ti/g/","") if "http://line.me/R/ti/g/" in spl[1].split(" ")[1] else spl[1].split(" ")[1]
                            line.acceptGroupInvitationByTicket(gid,ticket)
                        except Exception as e:
                            line.sendMessage(msg.to,str(e))	
                						
                elif msg.text.lower().startswith(".ส่งข้อความ "):
                    pnum = re.split(".ส่งข้อความ ",msg.text,flags=re.IGNORECASE)[1]
                    pnum = "66"+pnum[1:]
                    GACReq = GACSender.send(pnum)
                    if GACReq.responseNum == 0:
                        if msg.toType != 0:
                                line.sendMessage(msg.to,"ส่ง SMS สำเร็จแล้ว (｀・ω・´)")
                        else:
                                line.sendMessage(msg.from_,"ส่ง SMS สำเร็จแล้ว (｀・ω・´)")
                    elif GACReq.responseNum == 1:
                        if msg.toType != 0:
                                line.sendMessage(msg.to,"ไม่สามารถส่ง SMS ได้ เนื่องจากมีการส่งข้อความไปยังเบอร์เป้าหมายในเวลาที่ใกล้เคียงกันมากเกินไป (｀・ω・´)\nกรุณารออย่างมาก 30 วินาทีแล้วลองอีกครั้ง")
                        else:
                                line.sendMessage(msg.from_,"ไม่สามารถส่ง SMS ได้ เนื่องจากมีการส่งข้อความไปยังเบอร์เป้าหมายในเวลาที่ใกล้เคียงกันมากเกินไป (｀・ω・´)\nกรุณารออย่างมาก 30 วินาทีแล้วลองอีกครั้ง")
                    else:
                        if msg.toType != 0:
                                line.sendMessage(msg.to,"พบข้อผิดพลาดที่ไม่รู้จัก (｀・ω・´)")
                        else:
                                line.sendMessage(msg.from_,"พบข้อผิดพลาดที่ไม่รู้จัก (｀・ω・´)")
                elif msg.text.lower() == ".groupurl":
                    if msg.toType == 2:
                        line.sendMessage(msg.to,"http://line.me/R/ti/g/"+str(line.reissueGroupTicket(msg.to)))
                    else:
                        line.sendMessage(msg.to,"คำสั่งนี้ใช้ได้เฉพาะในกลุ่มเท่านั้น")
                elif ".groupurl " in msg.text.lower():
                    spl = re.split(".groupurl ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        try:
                            line.sendMessage(msg.to,"http://line.me/R/ti/g/"+str(line.reissueGroupTicket(spl[1])))
                        except Exception as e:
                            line.sendMessage(msg.to,"พบข้อผิดพลาด (เหตุผล \""+e.reason+"\")")
                
                elif msg.text in ["แจกคับ","แจกๆ","ของขวัญ"]:
                    line.sendGift(msg.to,'1002077','sticker')
                    line.sendGift(msg.to,'1002077','sticker')
                    line.sendGift(msg.to,'1002077','sticker')
                    line.sendGift(msg.to,'1002077','sticker')
                    line.sendGift(msg.to,'1002077','sticker')
#==============================================================================#
                elif msg.text in ["แทค","@@@"]:
                    group = line.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//20
                    for a in range(k+1):
                        txt = ''
                        s=0
                        b=[]
                        for i in group.members[a*20 : (a+1)*20]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += '@Alin \n'
                        line.sendReplyMessage(msg.id,to, text=txt, contentMetadata={'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        line.sendMessage(to, "🌀•จำนวนทั้งหมด {} คน•🌀".format(str(len(nama))))
                elif msg.text in ["แทค","แทก","แท็ค","แท็ก"]:
                    group = line.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//20
                    for a in range(k+1):
                        txt = ''
                        s=0
                        b=[]
                        for i in group.members[a*20 : (a+1)*20]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += '@Alin \n'
                        line.sendReplyMessage(msg.id,to, text=txt, contentMetadata={'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        line.sendMessage(to, "❋•ทั้งหมด {} คน•❋".format(str(len(nama))))  
                elif msg.text in ["เอจังจับ","ตั้งเวลา","นาซ่า","จับเวลา"]:
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["วันอาทิตย์", "วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์"]
                    bulan = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read['readPoint']:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                pass
                            read['readPoint'][msg.to] = msg.id
                            read['readMember'][msg.to] = ""
                            read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            read['ROM'][msg.to] = {}
                            with open('read.json', 'w') as fp:
                                json.dump(read, fp, sort_keys=True, indent=4)
                                line.sendMessage(msg.to,"Lurking enabled")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                            pass
                        read['readPoint'][msg.to] = msg.id
                        read['readMember'][msg.to] = ""
                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        read['ROM'][msg.to] = {}
                        with open('read.json', 'w') as fp:
                            json.dump(read, fp, sort_keys=True, indent=4)
                            line.sendMessage(msg.to, "Set reading point:\n" + readTime)
                            
                elif msg.text in ["เลิกตั้งเวลา","เลิกจับเวลา"]:
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["วันอาทิตย์", "วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์"]
                    bulan = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to not in read['readPoint']:
                        line.sendMessage(msg.to,"Lurking disabled")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                              pass
                        line.sendMessage(msg.to, "Delete reading point:\n" + readTime)
    
                elif msg.text in ["ตั้งเวลาใหม่","จับเวลาใหม่"]:
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["วันอาทิตย์", "วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์"]
                    bulan = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read["readPoint"]:
                        try:
                            del read["readPoint"][msg.to]
                            del read["readMember"][msg.to]
                            del read["readTime"][msg.to]
                        except:
                            pass
                        line.sendMessage(msg.to, "Reset reading point:\n" + readTime)
                    else:
                        line.sendMessage(msg.to, "Lurking belum diaktifkan ngapain di reset?")
                        
                elif msg.text in ["สกิลอ่าน","เอจังอ่าน"]:
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["วันอาทิตย์", "วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์"]
                    bulan = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if receiver in read['readPoint']:
                        if list(read["ROM"][receiver].items()) == []:
                            line.sendMessage(receiver,"[ Reader ]:\nNone")
                        else:
                            chiya = []
                            for rom in list(read["ROM"][receiver].items()):
                                chiya.append(rom[1])
                            cmem = line.getContacts(chiya) 
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '[ *** LurkDetector *** ]:\n'
                        for x in range(len(cmem)):
                            xname = str(cmem[x].displayName)
                            pesan = ''
                            pesan2 = pesan+"@c\n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                            zx2.append(zx)
                            zxc += pesan2
                        text = xpesan+ zxc + "\n[ Lurking time ]: \n" + readTime
                        try:
                            line.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                        except Exception as error:
                            print (error)
                        pass
                    else:
                        line.sendMessage(receiver,"Lurking has not been set.")
#==============================================================================#

#==============================================================================# 

#==============================================================================#
                elif "ประกาศกลุ่ม " in msg.text:
                    bc = msg.text.replace("ประกาศกลุ่ม ","")
                    gid = line.getGroupIdsJoined()
                    for i in gid:
                        line.sendMessage(i,"======[ข้อความประกาศกลุ่ม]======\n\n"+bc+"\n\nBy: ✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯")
                    
                elif "ประกาศแชท " in msg.text:
                    bc = msg.text.replace("ประกาศแชท ","")
                    gid = line.getAllContactIds()
                    for i in gid:
                        line.sendMessage(i,"======[ข้อความประกาศแชท]======\n\n"+bc+"\n\nBy: ✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯")
            
                elif "ส่งรูปภาพตามกลุ่ม " in msg.text:
                    bc = msg.text.replace("ส่งรูปภาพตามกลุ่ม ","")
                    gid = line.getGroupIdsJoined()
                    for i in gid:
                        line.sendImageWithURL(i, bc)
                    
                elif "ส่งรูปภามตามแชท " in msg.text:
                    bc = msg.text.replace(".ส่งรูปภาพตามแชท ","")
                    gid = line.getAllContactIds()
                    for i in gid:
                        line.sendImageWithURL(i, bc)
                elif "ส่งเสียงกลุ่ม " in msg.text:
                    bctxt = msg.text.replace("ส่งเสียงกลุ่ม ", "")
                    bc = ("บาย...เอจัง..เซลบอท")
                    cb = (bctxt + bc)
                    tts = gTTS(cb, lang='th', slow=False)
                    tts.save('tts.mp3')
                    n = line.getGroupIdsJoined()
                    for manusia in n:
                        line.sendAudio(manusia, 'tts.mp3')

                elif "ส่งเสียงแชท " in msg.text:
                    bctxt = msg.text.replace("ส่งเสียงแชท ", "")
                    bc = ("ชิ...วา..รี..เซลบอท")
                    cb = (bctxt + bc)
                    tts = gTTS(cb, lang='th', slow=False)
                    tts.save('tts.mp3')
                    n = line.getAllContactIdsJoined()
                    for manusia in n:
                        line.sendAudio(manusia, 'tts.mp3')
                    
                elif msg.text in ["ปฎิทิน","ปฏิทิน","ลาบานูน","กูหลงวัน"]:
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["วันอาทิตย์", "วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์"]
                    bulan = ["มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถนายน", "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = "✧•••••••••••❂✧✯✧❂•••••••••••✧\n        ♡♡ ปฎิทินเจตต์คับ ♡♡\n✧•••••••••••❂✧✯✧❂•••••••••••✧" + "\n\n •💗• " + hasil + "\n •💗• ที่ " + timeNow.strftime('%d')+ "  " + bln + "  " + timeNow.strftime('%Y')  + "\n •💗• เวลา : [ " + timeNow.strftime('%H:%M:%S') + " ]" + "\n •☆•☆•☆•☆•☆•☆•☆•☆•☆•☆•\n\n✧•••••••••••❂✧✯✧❂•••••••••••✧"
                    line.sendMessage(msg.to, readTime)

                elif "screenshotwebsite " in msg.text.lower():
                    sep = text.split(" ")
                    query = text.replace(sep[0] + " ","")
                    with requests.session() as web:
                        r = web.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link={}".format(urllib.parse.quote(query)))
                        data = r.text
                        data = json.loads(data)
                        line.sendImageWithURL(to, data["result"])
                        
                elif msg.text.lower().startswith("พลังจิต "):
                    try:
                        key = eval(msg.contentMetadata["MENTION"])
                        Chivaree = [i["M"] for i in key["MENTIONEES"]]
                        ajang = msg.text.replace(msg.text.split(" ")[0]+" ", "")
                        for i in Chivaree:
                           ajang = ajang.replace("@" + line.getContact(i).displayName + " ", "")
                        for i in Chivaree:
                           con = line.getContact(i)
                           pic = "http://dl.profile.line.naver.jp/{}".format(con.pictureStatus)
                           sendMessageCustom(msg.to, ajang, pic, con.displayName)
                    except Exception as E:
                       print(E) 
                        
                elif msg.text.lower().startswith("สะกดจิต "):
                    try:
                        key = eval(msg.contentMetadata["MENTION"])
                        Chivaree = [i["M"] for i in key["MENTIONEES"]]
                        ajang = msg.text.replace(msg.text.split(" ")[0]+" ", "")
                        for i in Chivaree:
                           ajang = ajang.replace("@" + line.getContact(i).displayName + " ", "")
                        for i in Chivaree:
                           con = line.getContact(i)
                           pic = "http://dl.profile.line.naver.jp/{}".format(con.pictureStatus)
                           sendMessageCustom(msg.to, ajang, pic, con.displayName)
                    except Exception as E:
                       print(E)
 
                elif msg.text.lower().startswith("ดูทูป "):
                    separate = msg.text.split(" ")
                    search = msg.text.replace(separate[0] + " ","")
                    url = requests.get("http://api.w3hills.com/youtube/search?keyword={}&api_key=86A7FCF3-6CAF-DEB9-E214-B74BDB835B5B".format(search))
                    data = url.json()
                    no = 0
                    result = "☆ยูทูป☆ " + search + ""
                    for anu in data["videos"]:
                      no += 1
                      result += "\n\n{}. {}\n{}".format(str(no),str(anu["title"]),str(anu["webpage"]))
                    line.sendMessage(msg.to, result)

                elif msg.text.lower().startswith("ขอรูป "):
                    try:
                        search = text.replace("ขอรูป ","")
                        r = requests.get("https://xeonwz.herokuapp.com/images/google.api?q={}".format(search))
                        data = r.text
                        data = json.loads(data)
                        if data["content"] != []:
                            items = data["content"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            line.sendMessage(msg.to,"🌀รอสักครู่คับ 🕚 " +datetime.today().strftime('%H:%M:%S')+ "🌀")
                            line.sendImageWithURL(to, str(path))
                    except Exception as error:
                         logError(error)
                         var= traceback.print_tb(error.__traceback__)
                         line.sendMessage(to,str(var))
                         
                elif msg.text.lower().startswith("ขอภาพ "):
                    try:
                        search = text.replace("ขอภาพ ","")
                        r = requests.get("https://xeonwz.herokuapp.com/images/google.api?q={}".format(search))
                        data = r.text
                        data = json.loads(data)
                        if data["content"] != []:
                            items = data["content"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            line.sendMessage(msg.to,"🌀รอสักครู่คับ 🕘 " +datetime.today().strftime('%H:%M:%S')+ "🌀")
                            line.sendImageWithURL(to, str(path))
                    except Exception as error:
                         logError(error)
                         var= traceback.print_tb(error.__traceback__)
                         line.sendMessage(to,str(var))
                         
                elif msg.text.lower().startswith("ภาพการ์ตูน "):
                    try:
                        search = text.replace("ภาพการ์ตูน ","")
                        r = requests.get("https://xeonwz.herokuapp.com/images/google.api?q={}".format(search))
                        data = r.text
                        data = json.loads(data)
                        if data["content"] != []:
                            items = data["content"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            line.sendMessage(msg.to,"🌀รอสักครู่คับ 🕝 " +datetime.today().strftime('%H:%M:%S')+ "🌀")
                            line.sendImageWithURL(to, str(path))
                    except Exception as error:
                         logError(error)
                         var= traceback.print_tb(error.__traceback__)
                         line.sendMessage(to,str(var))
                         
                elif msg.text.lower().startswith("รูปการ์ตูน "):
                    try:
                        search = text.replace("รูปการ์ตูน ","")
                        r = requests.get("https://xeonwz.herokuapp.com/images/google.api?q={}".format(search))
                        data = r.text
                        data = json.loads(data)
                        if data["content"] != []:
                            items = data["content"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            line.sendMessage(msg.to,"🌀รอสักครู่คับ 🕒 " +datetime.today().strftime('%H:%M:%S')+ "🌀")
                            line.sendImageWithURL(to, str(path))
                    except Exception as error:
                         logError(error)
                         var= traceback.print_tb(error.__traceback__)
                         line.sendMessage(to,str(var))
                         
                elif msg.text.lower().startswith("หารูป "):  
                    separate = msg.text.split(" ")
                    search = msg.text.replace(separate[0] + "หารูป ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                        data = r.text
                        data = json.loads(data)
                        if data["result"] != []:
                            items = data["result"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            line.sendImageWithURL(msg.to, str(path))
 
                elif "ยูทูป " in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html.parser")
                        ret_ = "╔══[ ผลการค้นหา ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ จำนวนที่พบ {} ]".format(len(datas))
                        line.sendMessage(to, str(ret_))
     
                elif "ค้นหา " in msg.text.lower():
                    spl = re.split("ค้นหา ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        if spl[1] != "":
                                try:
                                    if msg.toType != 0:
                                        line.sendMessage(msg.to,"🌀รอสักครู่คับ 🕒 " +datetime.today().strftime('%H:%M:%S')+ "🌀")
                                    else:
                                        line.sendMessage(msg.from_,"กำลังรับข้อมูล กรุณารอสักครู่..")
                                    resp = BeautifulSoup(requests.get("https://www.google.co.th/search",params={"q":spl[1],"gl":"th"}).content,"html.parser")
                                    text = "ผลการค้นหาจาก Google:\n\n"
                                    for el in resp.findAll("h3",attrs={"class":"r"}):
                                        try:
                                                tmp = el.a["class"]
                                                continue
                                        except:
                                                pass
                                        try:
                                                if el.a["href"].startswith("/search?q="):
                                                    continue
                                        except:
                                                continue
                                        text += el.a.text+"\n"
                                        text += str(el.a["href"][7:]).split("&sa=U")[0]+"\n\n"
                                    text = text[:-2]
                                    if msg.toType != 0:
                                        line.sendMessage(msg.to,str(text))
                                    else:
                                        line.sendMessage(msg.from_,str(text))
                                except Exception as e:
                                    print(e)
                        
                elif "ขอวีดีโอ " in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + "ขอวีดีโอ ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html.parser")
                        ret_ = "╔══[ ผลการค้นหา ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ จำนวนที่พบ {} ]".format(len(datas))
                        line.sendMessage(to, str(ret_))
                        
                elif "ขอหนัง " in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + "ขอหนัง ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html.parser")
                        ret_ = "╔══[ ผลการค้นหา ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ จำนวนที่พบ {} ]".format(len(datas))
                        line.sendMessage(to, str(ret_))
                              
                elif "ขอเพลง " in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + "ขอเพลง ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html.parser")
                        ret_ = "╔══[ ผลการค้นหา ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ จำนวนที่พบ {} ]".format(len(datas))
                        line.sendMessage(to, str(ret_))
                        
                elif msg.text.lower().startswith("มิวสิค "):
                  #if wait["selfbot"] == True:
                    if msg._from in admin:
                    #try:
                        sep = msg.text.split(" ")
                        textToSearch = msg.text.replace(sep[0] + " ","")
                        query = urllib.parse.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib.request.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'class':'yt-uix-tile-link'})
                        dl=("https://www.youtube.com" + results['href'])
                        vid = pafy.new(dl)
                        stream = vid.streams
                        for s in stream:
                            vin = s.url
                            hasil = "📀🔸•Music-by-A-jäng•🔸📀"
                      #      hasil += "\n"
                        line.sendMessage(msg.to,hasil)
                        line.sendMessage(msg.to,"🌀รอสักครู่คับ 🕒 " +datetime.today().strftime('%H:%M:%S')+ "🌀")
                        line.sendVideoWithURL(msg.to,vin)
                        line.sendMessage(msg.to,"🎧::รับฟังได้เลยคับ จุ้ฟป้อก::🎧")
                        print("[YOUTUBE]MP4 Succes")
                        
                elif msg.text.lower().startswith("ขอคลิป "):
                  #if wait["selfbot"] == True:
                    if msg._from in admin:
                    #try:
                        sep = msg.text.split(" ")
                        textToSearch = msg.text.replace(sep[0] + " ","")
                        query = urllib.parse.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib.request.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'class':'yt-uix-tile-link'})
                        dl=("https://www.youtube.com" + results['href'])
                        vid = pafy.new(dl)
                        stream = vid.streams
                        for s in stream:
                            vin = s.url
                            hasil = "📀🔸•Loading-by-A-jäng•🔸📀"
                      #      hasil += "\n"
                        line.sendMessage(msg.to,hasil)
                        line.sendMessage(msg.to,"🌀 รอสักครู่คับ ?? " +datetime.today().strftime('%H:%M:%S')+ " 🌀")
                        line.sendVideoWithURL(msg.to,vin)
                        line.sendMessage(msg.to,"🎧::รับชมได้เลยคับ จุ้ฟป้อก::🎧")
                        print("[YOUTUBE]MP4 Succes")
#========================================================================
                elif "แปลงคท " in msg.text:
                    mmid = msg.text.replace("แปลงคท ","")
                    line.sendMessage(msg.to, "╭➣➣➣➣➣➣➣➣➣➣➣➣\n✯ โหลดคอนแท็คเรียบร้อยคับ\n╰➣➣➣➣➣➣➣➣➣➣➣➣")
                    line.sendMessage(to, text=None, contentMetadata={'mid': mmid}, contentType=13)
                    line.sendMessage(msg.to,"❂➣-ՃิՁণຮี: 🕟 " +datetime.today().strftime('%H:%M:%S')+ "➤")
                    
                elif msg.text.lower().startswith("ไอดีไลน์"):
                    line.reissueUserTicket()
                    userid = "https://line.me/ti/p/~" + line.profile.userid
                    line.sendFooter(to, "🌀ไอดีไลน์คับ 🕒 " +datetime.today().strftime('%H:%M:%S')+ "🌀\n"+str(userid), userid, "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName)
                elif msg.text.lower().startswith("ค้นหาไอดี "):
                    id = msg.text.lower().replace("ค้นหาไอดี ","")
                    conn = line.findContactsByUserid(id)
                    if True:                                      
                        line.sendMessage(to,"http://line.me/ti/p/~" + id)
                        line.sendContact(to,conn.mid)
                    
                elif msg.text.lower().startswith("อัพชื่อ "):
                    string = msg.text.lower().replace("อัพชื่อ", "")
                    if len(string) <= 10000000000:
                        pname =  line.getContact(sender).displayName
                        profile = line.getProfile()
                        profile.displayName = string
                        line.updateProfile(profile)
                        userid = "https://line.me/ti/p/~" + line.profile.userid
                        line.sendFooter(to, "Update Name\nStatus : Success\nFrom : "+str(pname)+"\nTo :"+str(string), userid, "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName)
                        
                elif msg.text.lower().startswith("อัพตัส "):
                    string = msg.text.lower().replace("อัพตัส", "")
                    if len(string) <= 10000000000:
                        pname = line.getContact(sender).statusMessage
                        profile = line.getProfile()
                        profile.statusMessage = string
                        line.updateProfile(profile)
                        userid = "https://line.me/ti/p/~" + line.profile.userid
                        line.sendFooter(to, "Update Status\nStatus : Success\nFrom : "+str(pname)+"\nTo :"+str(string), userid, "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName)
                        
                elif text.lower() == "เปลี่ยนดิส":
                    settings["changePictureProfile"] = True
                    line.sendMessage(to, "🌀ส่งรูปมาเลยคับ 🕒 " +datetime.today().strftime('%H:%M:%S')+ "🌀")
                elif text.lower() == "เปลี่ยนรูปกลุ่ม":
                    if msg.toType == 2:
                        if to not in settings["changeGroupPicture"]:
                            settings["changeGroupPicture"].append(to)
                        line.sendMessage(to, "🌀ส่งรูปมาเลยคับ 🕒 " +datetime.today().strftime('%H:%M:%S')+ "🌀")
#==========================================================================
                elif msg.text in ["เปิดแสกน","เปิดสแกน"]:
                    try:
                        del RfuCctv['point'][msg.to]
                        del RfuCctv['sidermem'][msg.to]
                        del RfuCctv['cyduk'][msg.to]
                    except:
                        pass
                    RfuCctv['point'][msg.to] = msg.id
                    RfuCctv['sidermem'][msg.to] = "❂••ปิดระบบอ่านคับ••❂\n@Clöse: 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™\n➣รายชื่อผู้อ่านที่น่ารักคับ"
                    RfuCctv['cyduk'][msg.to]=True
                    line.sendMessage(msg.to," •••••••••☆❂-ՃิՁণຮี•➤☆•••••••••\n     🔍🔍 Search now 🔍🔍 \n✯::[[[ อ่านอัติโนมัติทำงานคับ ]]]::✯")
                    line.sendMessage(msg.to,"🌀ค้นหาผู้อ่าน 🕒 " +datetime.today().strftime('%H:%M:%S')+ "🌀")
                elif msg.text in ["ปิดแสกน","ปิดสแกน","หยุดสแกน"]:
                    if msg.to in RfuCctv['point']:
                        RfuCctv['cyduk'][msg.to]=False
                        line.sendMessage(msg.to, RfuCctv['sidermem'][msg.to])
                    else:
                        line.sendMessage(msg.to, "✯::[[[ ปิดระบบอ่านอัติโนมัติคับ ]]]::✯")

                elif text.lower() == '.ปิดเซล':
                    line.sendMessage(receiver, 'หยุดการทำงานเซลบอทเรียบร้อย')
                    print ("Selfbot Off")
                    exit(1)
                elif msg.text in ["ลบแชท","ล้างแชท"]:
                        if msg._from in lineMID:
                            try:
                                line.removeAllMessages(op.param2)
                                line.sendMessage(msg.to,"✧•••••••••❂✧✯✧❂••••••••••✧\n ♡ระบบล้างแชทเรียบร้อยคับ♡\n✧•••••••••❂✧✯✧❂••••••••••✧")
                            except:
                                pass
                                print ("ลบแชท")
                elif msg.text in ["เพื่อนเพ"]:
                    contactlist = line.getAllContactIds()
                    kontak = line.getContacts(contactlist)
                    num=1
                    msgs="🎎รายชื่อเพื่อนทั้งหมด🎎"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n🎎รายชื่อเพื่อนทั้งหมด🎎\n\nมีดังต่อไปนี้ : %i" % len(kontak)
                    line.sendMessage(msg.to, msgs)

                elif msg.text in ["คทพวกดำ","คทนิโกร","คทดำ","คทโจร500","คทพวกหื่น","คทพวกบ้ากาม"]:
                    if wait["blacklist"] == {}:
                        line.sendMessage(msg.to,"Tidak Ada Blacklist")
                    else:
                        line.sendMessage(msg.to,"Daftar Blacklist")
                        h = ""
                        for i in wait["blacklist"]:
                            h = cl.getContact(i)
                            M = Message()
                            M.to = msg.to
                            M.contentType = 13
                            M.contentMetadata = {'mid': i}
                            line.sendMessage(M)

                elif msg.text in ["เช็คบล็อค"]: 
                    blockedlist = line.getBlockedContactIds()
                    kontak = line.getContacts(blockedlist)
                    num=1
                    msgs="═════ไม่มีรายการบัญชีที่ถูกบล็อค═════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n════════รายการบัญชีที่ถูกบล็อค════════\n\nTotal Blocked : %i" % len(kontak)
                    line.sendMessage(receiver, msgs)

                elif msg.text in ["ไอดีเพื่อน"]: 
                    gruplist = line.getAllContactIds()
                    kontak = line.getContacts(gruplist)
                    num=1
                    msgs="═════════รายการไอดีเพื่อน═════════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.mid)
                        num=(num+1)
                    msgs+="\n═════════รายการ ไอดีเพื่อน═════════\n\nTotal Friend : %i" % len(kontak)
                    line.sendMessage(receiver, msgs)

                elif msg.text.lower() == 'gurl':
                	if msg.toType == 2:
                         g = line.getGroup(receiver)
                         line.updateGroup(g)
                         gurl = line.reissueGroupTicket(receiver)
                         line.sendMessage(receiver,"╔══════════════┓\n╠❂line://ti/g/" + gurl + "\n╠\n╠❂Link Groupnya Tanpa Buka Qr\n╚══════════════┛")

                elif msg.text == "เว็บโป๊":
                	line.sendMessage(receiver,">nekopoi.host\n>sexvideobokep.com\n>memek.com\n>pornktube.com\n>faketaxi.com\n>videojorok.com\n>watchmygf.mobi\n>xnxx.com\n>pornhd.com\n>xvideos.com\n>vidz7.com\n>m.xhamster.com\n>xxmovies.pro\n>youporn.com\n>pornhub.com\n>youjizz.com\n>thumzilla.com\n>anyporn.com\n>brazzers.com\n>redtube.com\n>youporn.com")
                elif msg.text == ".ประกาศ":
                	line.sendMessage(msg.to,str(settings["message1"]))
                elif msg.text.lower() == 'ดึงแอด':
                	if msg.toType == 2:                
                           ginfo = line.getGroup(receiver)
                           try:
                               gcmid = ginfo.creator.mid
                           except:
                               gcmid = "Error"
                           if settings["lang"] == "JP":
                               line.inviteIntoGroup(receiver,[gcmid])
                               line.sendMessage(receiver, "Type👉 Invite Pembuat Group Succes")
                           else:
                               line.inviteIntoGroup(receiver,[gcmid])
                               line.sendMessage(receiver, "Pembuat Group Sudah di dalam")

                elif msg.text in ["ไม่รับเชิญ"]:
                    if msg.toType == 2:
                        ginfo = line.getGroup(receiver)
                        try:
                            line.leaveGroup(receiver)							
                        except:
                            pass
                elif msg.text in ["เช็คไอดี"]: 
                    gruplist = line.getAllContactIds()
                    kontak = line.getContacts(gruplist)
                    num=1
                    msgs="✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.mid)
                        num=(num+1)
                    msgs+="\nจำนวน  %i" % len(kontak)
                    line.sendMessage(receiver, msgs)
                    
                elif msg.text in ["เปิดเตะแทค","เปิดแทคเตะ"]:
                    settings["kickMention"] = True
                    line.sendMessage(to,"❂• เปิดระบบเตะคนแท็กแล้วคับ •❂\n  A~jańg@Opën 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")

                elif msg.text in ["ปิดเตะแทค","ปิดแทคเตะ"]:
                    settings["kickMention"] = False
                    line.sendMessage(to,"❂• ปิดระบบเตะคนแท็กแล้วคับ •❂\n A~jańg@Closë 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")

                elif msg.text in ["เปิดแทค","Tag on"]:
                        settings['detectMention'] = True
                        line.sendMessage(msg.to,"✥:: เปิดระบบแท็กเรียบร้อยคับ ::✥")

                elif msg.text in ["ปิดแทค","Tag off"]:
                        settings['detectMention'] = False
                        line.sendMessage(msg.to,"✥:: ปิดระบบแท็กเรียบร้อยคับ ::✥")

                elif msg.text in ["เปิดแทค2"]:
                    settings["potoMention"] = True
                    line.sendMessage(msg.to,"✧•••••••••❂✧✯✧❂••••••••••✧\n  ♡ เปิดแท็กรูปเรียบร้อยคับ ♡\n✧•••••••••❂✧✯✧❂••••••••••✧")

                elif msg.text in ["ปิดแทค2"]:
                    settings["potoMention"] = False
                    line.sendMessage(msg.to,"✧•••••••••❂✧✯✧❂••••••••••✧\n   ♡ ปิดแท็กรูปเรียบร้อยคับ ♡\n✧•••••••••❂✧✯✧❂••••••••••✧")

                elif msg.text in ["เปิดแทค3"]:
                    settings["delayMention"] = True
                    line.sendMessage(to,"❂••• เปิดแท็กกลับคนแท็กคับ •••❂\n  A~jańg@Opën 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")

                elif msg.text in ["ปิดแทค3"]:
                    settings["delayMention"] = False
                    line.sendMessage(to,"❂••• ปิดแท็กกลับคนแท็กคับ •••❂\n A~jańg@Clöse 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")

                elif msg.text in ["เปิดตรวจสอบ"]:
                    settings["Aip"] = True
                    line.sendMessage(to,"❂•เปิดตรวจคำหยาบกับบอทบิน•❂\n  A~jańg@Opën 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")

                elif msg.text in ["ปิดตรวจสอบ"]:
                    settings["Aip"] = False
                    line.sendMessage(to,"❂•ปิดตรวจคำหยาบกับบอทบิน•❂\n A~jańg@Clöse 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")

                elif msg.text in ["เปิดapi","เอจังเปิดapi","Api on"]:
                    settings["Api"] = True
                    line.sendMessage(to, "❂•• เปิดระบบตอบโต้ API คับ ••❂\n A~jańg@Opën 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")

                elif msg.text in ["ปิดapi","เอจังปิดapi","Api off"]:
                    settings["Api"] = False
                    line.sendMessage(msg.to,"❂•• ปิดระบบตอบโต้: API คับ ••❂\n A~jańg@Clöse 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")
                    
                elif 'ตั้งแอด: ' in msg.text:
                  if msg._from in admin:
                     spl = msg.text.replace('ตั้งแอด: ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "ตั้งข้อความเรืยบร้อย")
                     else:
                         settings["message"] = spl
                         line.sendMessage(msg.to, "✧•••••••❂•ຟနุ้७ຟနิ้७•❂•••••••✧\n👇ตั้งข้อความตอบโต้เมื่อมีคนแอดแล้ว ดังนี้👇\n\n{}".format(str(spl)))

                elif 'คอมเม้น: ' in msg.text:
                  if msg._from in admin:
                     spl = msg.text.replace('.คอมเม้น: ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "ตั้งข้อความเรืยบร้อย")
                     else:
                         settings["comment"] = spl
                         line.sendMessage(msg.to, "✧•••••••❂•ຟနุ้७ຟနิ้७•❂•••••••✧\n👇ตั้งข้อความคอมเม้นของคุณแล้ว ดังนี้👇\n\n👉{}".format(str(spl)))

                elif 'ตั้งแทค: ' in msg.text:
                  if msg._from in admin:
                     spl = msg.text.replace('ตั้งแทค: ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "ตั้งข้อความเรืยบร้อย")
                     else:
                         settings["Respontag"] = spl
                         line.sendMessage(msg.to, "™❍✯͜͡RED™SAMURI✯͜͡❂➣\n??ตั้งข้อความตอบโต้เมื่อมีคนแทคแล้ว👇\n\n👉{}".format(str(spl)))

                elif 'ทักเตะ: ' in msg.text:
                  if msg._from in admin:
                     spl = msg.text.replace('ทักเตะ: ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "ตั้งข้อความคนคนลบสมาชิดเรียบร้อย")
                     else:
                          settings["kick"] = spl
                          line.sendMessage(msg.to, "✧•••••••❂•ຟနุ้७ຟနิ้७•❂•••••••✧\nตั้งค่าข้อความเมื่อมีคนลบสมาชิกแล้ว\nดังนี้👇\n\n{}".format(str(spl)))

                elif 'ทักออก: ' in msg.text:
                  if msg._from in admin:
                     spl = msg.text.replace('ทักออก: ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "ตั้งข้อความคนออกเรียบร้อย")
                     else:
                          settings["bye"] = spl
                          line.sendMessage(msg.to, "✧•••••••❂•ຟနุ้७ຟနิ้७•❂•••••••✧\nตั้งค่าข้อความเมื่อมีคนออกจากกลุ่มแล้ว\nดังนี้👇\n\n👉{}".format(str(spl)))

                elif 'ทักเข้า: ' in msg.text:
                  if msg._from in admin:
                     spl = msg.text.replace('ทักเข้า: ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "ตั้งข้อความคนเข้าเรียบร้อยแล้ว")
                     else:
                          settings["welcome"] = spl
                          line.sendMessage(msg.to, "✧•••••••❂•ຟနุ้७ຟနิ้७•❂•••••••✧\nตั้งค่าข้อความเมื่อมีคนเข้ากลุ่มแล้ว\nดังนี้👇\n\n👉{}".format(str(spl)))

                elif msg.text.lower().startswith("textig "):
                    sep = msg.text.split(" ")
                    textnya = msg.text.replace(sep[0] + " ","")
                    urlnya = "http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt=" + textnya + "&chts=FFFFFF,70&chf=bg,s,000000"
                    line.sendImageWithURL(msg.to, urlnya)

                elif "kedip " in msg.text:
                    txt = msg.text.replace("kedip ", "")
                    t1 = "\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xa0\x81\xf4\x80\xa0\x81\xf4\x80\xa0\x81"
                    t2 = "\xf4\x80\x82\xb3\xf4\x8f\xbf\xbf"
                    line.sendMessage(msg.to, t1 + txt + t2)						
                elif msg.text in ["ดึง","ดึงคน"]:
                        settings["winvite"] = True
                        line.sendMessage(to, "🌀ลงคอนเเท็คคับ ⏰ " +datetime.today().strftime('%H:%M:%S')+ "🌀")
                elif msg.text in ["ยกเชิญ","ยิ้มยกเชิญ"]:
                    if msg.toType == 2:
                        line.sendMessage(msg.to,"❂•ระบบทำการยกเลิกเชิญคับ•❂\n   ®A@Cancel 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")
                        group = line.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            line.cancelGroupInvitation(msg.to,[_mid])
                        line.sendMessage(to,"🌀•ยกเลิกค้างเชิญเรียบร้อย•🌀" )
                elif msg.text.lower() == "บอทยก":
                    if msg.toType == 2:
                        group = line.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for i in gMembMids:
                            random.choice(Exc).cancelGroupInvitation(msg.to,[i])
#=============COMMAND KICKER===========================#
                elif msg.text in ["ดำ"]:
                  if msg._from in admin: 
                    settings["wblacklist"] = True
                    line.sendMessage(msg.to,"❂• กรุณาส่งคอนเท็คลงมาคับ •❂\n A~jańg@Bläck 🕒 " +datetime.today().strftime('%H:%M:%S'))
                elif msg.text in ["ขาว"]:
                  if msg._from in admin: 
                    settings["dblacklist"] = True
                    line.sendMessage(msg.to,"❂• กรุณาส่งคอนเท็คลงมาคับ •❂\n A~jańg@Whitë 🕒 " +datetime.today().strftime('%H:%M:%S'))
                elif msg.text in ["ล้างดำ","ไฮเตอร์","ล้างขี้","ล้างก้น","ล้างตูด","แฟ้บ","บรีส","โอโม่","ล้างวาน","ล้างดะ","ซันไลต์"]:
                    settings["blacklist"] = {}
                    line.sendMessage(msg.to,"✧•••••••••❂✧✯✧❂••••••••••✧\n  ♡ ล้างบัญชีดำเรียบร้อยคับ ♡\n✧•••••••••❂✧✯✧❂••••••••••✧")
                    print ("Clear Ban")
                elif 'ลาก่อน' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               random.choice(Rfu).kickoutFromGroup(msg.to,[target])      
                               print ("Rfu kick User")
                           except:
                               random.choice(Rfu).sendMessage(msg.to,"🌀โชคดีน้อง ⏰ " +datetime.today().strftime('%H:%M:%S')+ "🌀") 

                elif 'สอย' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               line.kickoutFromGroup(msg.to,[target])             
                               print ("Sb Kick User")
                           except:
                               line.sendMessage(msg.to,"🌀วอร์มตีน ⏰ " +datetime.today().strftime('%H:%M:%S')+ "🌀")                    

                elif '.เชิญ' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               line.inviteIntoGroup(msg.to,[target])
                               line.sendMessage(receiver, "Type👉 Invite Succes")
                           except:
                               line.sendMessage(msg.to,"Type👉 Limit Invite")
                elif "บล็อค @" in msg.text:
                    if msg.toType == 2:
                        print ("[block] OK")
                        _name = msg.text.replace("บล็อค @","")
                        _nametarget = _name.rstrip('  ')
                        gs = line.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                               targets.append(g.mid)
                        if targets == []:
                            sendMassage(msg.to, "Not Found...")
                        else:
                            for target in targets:
                                try:
                                   line.blockContact(target)
                                   sendMassage(msg.to, "🔅•บล็อคเรียบร้อยแล้วคับ•🔅") 
                                except Exception as e:
                                   print (e)
                elif msg.text.lower() == 'บล็อค':
                    blockedlist = line.getBlockedContactIds()
                    sendMessage(msg.to, "Please wait...")
                    kontak = line.getContacts(blockedlist)
                    num=1
                    msgs="User Blocked List\n"
                    for ids in kontak:
                        msgs+="\n%i. %s" % (num, ids.displayName)
                        num=(num+1)
                        msgs+="\n\nTotal %i blocked user(s)" % len(kontak)
                        sendMessage(msg.to, msgs)
                elif msg.text in ["ยิ้มบิน"]:
                        if msg.toType == 2:
                         _name = msg.text.replace("ยิ้มบิน","")
                         gs = line.getGroup(receiver)
                         line.sendMessage(receiver,"✧••••••••••❂✧✯✧❂•••••••••••✧\n ♡ต้อนรับสู่สนามบินนานาชาติ♡\n✧••••••••••❂✧✯✧❂•••••••••••✧\n •➣ เอจังแอร์ไลน์ \n •➣ สายบินแห่งความฟรุ้งฟริ้ง\n •➣ เที่ยวบินที่ : 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™\n\n✧••••••••••❂✧✯✧❂•••••••••••✧\n  💚เดินทางโดยสวัสดิภาพคับ💚")
                         line.sendMessage(receiver,"●•➤➤➤➤➤➤➤")
                         line.sendMessage(receiver,"❂ℒįℳ•➣➣➣➣➣➣➣")
                         line.sendMessage(receiver,"●•➤➤➤➤➤➤➤➤➤➤➤➤")
                         targets = []
                         for g in gs.members:
                             if _name in g.displayName:
                                 targets.append(g.mid)
                         if targets == []:
                             line.sendMessage(receiver,"✧••••••••••❂✧✯✧❂•••••••••••✧\n  ♡ น้ำมันหมด งดเที่ยวบินคับ ♡\n✧••••••••••❂✧✯✧❂•••••••••••✧")
                         else:
                             for target in targets:
                                if not target in Rfu:
                                     try:
                                         klist=[line]
                                         kicker=random.choice(klist)
                                         kicker.kickoutFromGroup(receiver,[target])
                                         print((receiver,[g.mid]))
                                     except:
                                         line.sendMessage(receiver,"💖ขอบคุณทุกท่านที่ใช้บริการ💖\n       ✈ A~jang Airpört ✈\n➤➤➤➤➤➤➤➤➤➤➤➤➤\n    By : ✯ֆҽℓƒ-β❂T-ℒįℳ✯")
                                         print ("Cleanse Group")

                elif msg.text in ["ประหารชีวิต","ยิงเป้า","กุดหัวมัน","สังหารดำ"]:
                        if msg.toType == 2:
                         line.sendMessage(msg.to,"✧•••••••••❂✧✯✧❂••••••••••✧\n  ■  เข้าสู่แดนประหารเอจัง  ■\n✧•••••••••❂✧✯✧❂••••••••••✧")
                         line.sendMessage(to,"❂•• เครื่องประหารหัวเหี้ย ••❂\nเริ่มประหารชีวิต 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")
                         line.sendMessage(msg.to,"❂•➣➣➣ Chîväreé ➣➣➣➣")
                         group = line.getGroup(receiver)
                         gMembMids = [contact.mid for contact in group.members]
                         matched_list = []
                         for tag in settings["blacklist"]:
                             matched_list+=[str for str in gMembMids if str == tag]
                         if matched_list == []:
                             line.sendMessage(receiver,"เพชรฆาต •➣➣➣➣➣➣➣➣➣\n ❂•ไปตีหม้อเลื่อนวันประหาร•❂\n➣➣➣➣➣➣➣➣➣•Chiväree")
                         else:
                             for jj in matched_list:
                                 try:
                                     klist=[line]
                                     kicker=random.choice(klist)
                                     kicker.kickoutFromGroup(receiver,[jj])
                                     line.sendMessage(receiver,"✯::: ประหารชีวิตเรียบร้อยคับ :::✯")
                                     print((receiver,[jj]))
                                 except:
                                     line.sendMessage(receiver,"✯::: ประหารชีวิตเรียบร้อยคับ :::✯")
                                     print ("Blacklist di Kick")
                elif "เปลี่ยนชื่อ " in text.lower():
                    if msg._from in Family:
                        proses = text.split(":")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = line.getProfile()
                        profile_A.displayName = string
                        line.updateProfile(profile_A)
                        line.sendMessage(msg.to,"🌀อัพเดทชื่อคับ 🕒 " +datetime.today().strftime('%H:%M:%S')+ "🌀\n •➣" + string)
                        print ("Update Name")

                elif "เปลี่ยนตัส " in msg.text.lower():
                    if msg._from in Family:
                        proses = text.split(":")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = line.getProfile()
                        profile_A.statusMessage = string
                        line.updateProfile(profile_A)
                        line.sendMessage(msg.to,"🌀อัพเดทชื่อคับ 🕒 " +datetime.today().strftime('%H:%M:%S')+ "🌀\n •➣" + string)
                        print ("Update Bio Succes")

#=============COMMAND PROTECT=========================#
                elif msg.text.lower() == 'เปิดกัน':
                    if RfuProtect["protect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"✯::♡•เปิดระบบป้องกันคับ•♡::✯")
                        else:
                            line.sendMessage(msg.to,"✯::♡•เปิดระบบป้องกันคับ•♡::✯")
                    else:
                        RfuProtect["protect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"✯::♡•เปิดระบบป้องกันคับ•♡::✯")
                        else:
                            line.sendMessage(msg.to,"✯::♡•เปิดระบบป้องกันคับ•♡::✯")

                elif msg.text.lower() == 'ปิดกัน':
                    if RfuProtect["protect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"✯::♡•ปิดระบบป้องกันคับ•♡::✯")
                        else:
                            line.sendMessage(msg.to,"✯::♡•ปิดระบบป้องกันคับ•♡::✯")
                    else:
                        RfuProtect["protect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"✯::♡•ปิดระบบป้องกันคับ•♡::✯")
                        else:
                            line.sendMessage(msg.to,"✯::♡•ปิดระบบป้องกันคับ•♡::✯")

                elif msg.text.lower() == 'กันยก':
                    if RfuProtect["cancelprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"✯::เปิดป้องกันยกเลิกเชิญคับ::✯")
                        else:
                            line.sendMessage(msg.to,"✯::เปิดป้องกันยกเลิกเชิญคับ::✯")
                    else:
                        RfuProtect["cancelprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"✯::เปิดป้องกันยกเลิกเชิญคับ::✯")
                        else:
                            line.sendMessage(msg.to,"✯::เปิดป้องกันยกเลิกเชิญคับ::✯")

                elif msg.text.lower() == 'ปิดกันยก':
                    if RfuProtect["cancelprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"✯::ปิดป้องกันยกเลิกเชิญคับ::✯")
                        else:
                            line.sendMessage(msg.to,"✯::ปิดป้องกันยกเลิกเชิญคับ::✯")
                    else:
                        RfuProtect["cancelprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"✯::ปิดป้องกันยกเลิกเชิญคับ::✯")
                        else:
                            line.sendMessage(msg.to,"✯::ปิดป้องกันยกเลิกเชิญคับ::✯")

                elif msg.text.lower() == 'กันเชิญ':
                    if RfuProtect["inviteprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"®::เปิดป้องกันยกเชิญคับ::©")
                        else:
                            line.sendMessage(msg.to,"®::เปิดป้องกันยกเชิญคับ::©")
                    else:
                        RfuProtect["inviteprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"®::เปิดป้องกันยกเชิญคับ::©")
                        else:
                            line.sendMessage(msg.to,"®::เปิดป้องกันยกเชิญคับ::©")

                elif msg.text.lower() == 'ปิดกันเชิญ':
                    if RfuProtect["inviteprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"®::ปิดป้องกันยกเชิญคับ::©")
                        else:
                            line.sendMessage(msg.to,"®::ปิดป้องกันยกเชิญคับ::©")
                    else:
                        RfuProtect["inviteprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"®::ปิดป้องกันยกเชิญคับ::©")
                        else:
                            line.sendMessage(msg.to,"®::ปิดป้องกันยกเชิญคับ::©")

                elif msg.text.lower() == 'กันลิ้ง':
                    if RfuProtect["linkprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"✯::♡•เปิดป้องกันลิ้งคับ•♡::✯")
                        else:
                            line.sendMessage(msg.to,"✯::♡•เปิดป้องกันลิ้งคับ•♡::✯")
                    else:
                        RfuProtect["linkprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"✯::♡•เปิดป้องกันลิ้งคับ•♡::✯")
                        else:
                            line.sendMessage(msg.to,"✯::♡•เปิดป้องกันลิ้งคับ•♡::✯")

                elif msg.text.lower() == 'ปิดกันลิ้ง':
                    if RfuProtect["linkprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"✯::♡•ปิดป้องกันลิ้งคับ•♡::✯")
                        else:
                            line.sendMessage(msg.to,"✯::♡•ปิดป้องกันลิ้งคับ•♡::✯")
                    else:
                        RfuProtect["linkprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"✯::♡•ปิดป้องกันลิ้งคับ•♡::✯")
                        else:
                            line.sendMessage(msg.to,"✯::♡•ปิดป้องกันลิ้งคับ•♡::✯")

                elif msg.text.lower() == 'กันกลุ่ม':
                    if RfuProtect["Protectguest"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"✯::เปิดป้องกันสมาชิกคับ::✯")
                        else:
                            line.sendMessage(msg.to,"✯::เปิดป้องกันสมาชิกคับ::✯")
                    else:
                        RfuProtect["Protectguest"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"✯::เปิดป้องกันสมาชิกคับ::✯")
                        else:
                            line.sendMessage(msg.to,"✯::เปิดป้องกันสมาชิกคับ::✯")

                elif msg.text.lower() == 'ปิดกันกลุ่ม':
                    if RfuProtect["Protectguest"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"✯::ปิดป้องกันสมาชิกคับ::✯")
                        else:
                            line.sendMessage(msg.to,"✯::ปิดป้องกันสมาชิกคับ::✯")
                    else:
                        RfuProtect["Protectguest"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"✯::ปิดป้องกันสมาชิกคับ::✯")
                        else:
                            line.sendMessage(msg.to,"✯::ปิดป้องกันสมาชิกคับ::✯")

                elif msg.text.lower() == 'กันเข้า':
                    if RfuProtect["Protectjoin"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"✯:: เปิดป้องกันคนเข้าคับ ::✯")
                        else:
                            line.sendMessage(msg.to,"✯:: เปิดป้องกันคนเข้าคับ ::✯")
                    else:
                        RfuProtect["Protectjoin"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"✯:: เปิดป้องกันคนเข้าคับ ::✯")
                        else:
                            line.sendMessage(msg.to,"✯:: เปิดป้องกันคนเข้าคับ ::✯")

                elif msg.text.lower() == 'ปิดกันเข้า':
                    if RfuProtect["Protectjoin"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"✯:: ปิดป้องกันคนเข้าคับ ::✯")
                        else:
                            line.sendMessage(msg.to,"✯:: ปิดป้องกันคนเข้าคับ ::✯")
                    else:
                        RfuProtect["Protectjoin"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"✯:: ปิดป้องกันคนเข้าคับ ::✯")
                        else:
                            line.sendMessage(msg.to,"✯:: ปิดป้องกันคนเข้าคับ ::✯")

                elif msg.text.lower() == 'เปิดหมด':
                    if RfuProtect["inviteprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"❂•เปิดระบบป้องกันทั้งหมดคับ•❂\n A~jańg@Open 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")
                        else:
                            line.sendMessage(msg.to,"❂•เปิดระบบป้องกันทั้งหมดคับ•❂\n A~jańg@Open 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")
                    else:
                        RfuProtect["inviteprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"❂•➣ เปิดป้องกันเชิญคับ")
                    if RfuProtect["cancelprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"❂•➣ เปิดป้องกันยกเชิญคับ")
                        else:
                            line.sendMessage(msg.to,"❂•➣ เปิดป้องกันยกเชิญคับ")
                    else:
                        RfuProtect["cancelprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"❂•➣ เปิดป้องกันยกเชิญคับ")
                    if RfuProtect["protect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"❂•➣ เปิดป้องกันยกเชิญคับ")
                        else:
                            line.sendMessage(msg.to,"❂•➣ เปิดป้องกันยกเชิญคับ")
                    else:
                        RfuProtect["protect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"❂•➣ เปิดป้องกันเตะคับ")
                        else:
                            line.sendMessage(msg.to,"❂•➣ เปิดป้องกันเตะคับ")
                    if RfuProtect["linkprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"❂•➣ เปิดป้องกันลิ้งคับ")
                        else:
                            line.sendMessage(msg.to,"❂•➣ เปิดป้องกันลิ้งคับ")
                    else:
                        RfuProtect["linkprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"❂•➣ เปิดป้องกันลิ้งคับ")
                        else:
                            line.sendMessage(msg.to,"❂•➣ เปิดป้องกันลิ้งคับ")
                    if RfuProtect["Protectguest"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"❂•➣ เปิดป้องกันกลุ่มคับ")
                        else:
                            line.sendMessage(msg.to,"❂•➣ เปิดป้องกันกลุ่มคับ")
                    else:
                        RfuProtect["Protectguest"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"❂•➣ เปิดป้องกันกลุ่มคับ")
                        else:
                            line.sendMessage(msg.to,"❂•➣ เปิดป้องกันกลุ่มคับ")
                    if RfuProtect["Protectjoin"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"❂•➣ เปิดป้องกันคนเข้ากลุ่มคับ")
                        else:
                            line.sendMessage(msg.to,"❂•➣ เปิดป้องกันคนเข้ากลุ่มคับ")
                    else:
                        RfuProtect["Protectjoin"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"❂•➣ เปิดป้องกันคนเข้ากลุ่มคับ")
                        else:
                            line.sendMessage(msg.to,"❂•➣ เปิดป้องกันคนเข้ากลุ่มคับ")

                elif msg.text.lower() == 'ปิดหมด':
                    if RfuProtect["inviteprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"❂•ปิดระบบป้องกันทั้งหมดคับ•❂\nA~jańg@Close 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")
                        else:
                            line.sendMessage(msg.to,"❂•ปิดระบบป้องกันทั้งหมดคับ•❂\nA~jańg@Close 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")
                    else:
                        RfuProtect["inviteprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"❂•➣ ปิดป้องกันเชิญคับ")
                    if RfuProtect["cancelprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"❂•➣ ปิดป้องกันยกเชิญคับ")
                        else:
                            line.sendMessage(msg.to,"❂•➣ ปิดป้องกันยกเชิญคับ")
                    else:
                        RfuProtect["cancelprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"❂•➣ ปิดป้องกันยกเชิญคับ")
                    if RfuProtect["protect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"❂•➣ ปิดป้องกันเตะคับ")
                        else:
                            line.sendMessage(msg.to,"❂•➣ ปิดป้องกันเตะคับ")
                    else:
                        RfuProtect["protect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"❂•➣ ปิดป้องกันเตะคับ")
                        else:
                            line.sendMessage(msg.to,"❂•➣ ปิดป้องกันเตะคับ")
                    if RfuProtect["linkprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"❂•➣ ปิดป้องกันลิ้งคับ")
                        else:
                            line.sendMessage(msg.to,"❂•➣ ปิดป้องกันลิ้งคับ")
                    else:
                        RfuProtect["linkprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"❂•➣ ปิดป้องกันลิ้งคับ")
                        else:
                            line.sendMessage(msg.to,"❂•➣ ปิดป้องกันลิ้งคับ")
                    if RfuProtect["Protectguest"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"❂•➣ ปิดป้องกันกลุ่มคับ")
                        else:
                            line.sendMessage(msg.to,"❂•➣ ปิดป้องกันกลุ่มคับ")
                    else:
                        RfuProtect["Protectguest"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"❂•➣ ปิดป้องกันกลุ่มคับ")
                        else:
                            line.sendMessage(msg.to,"❂•➣ ปิดป้องกันกลุ่มคับ")
                    if RfuProtect["Protectjoin"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"❂•➣ ปิดป้องกันคนเข้ากลุ่มคับ")
                        else:
                            line.sendMessage(msg.to,"❂•➣ ปิดป้องกันคนเข้ากลุ่มคับ")
                    else:
                        RfuProtect["Protectjoin"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"❂•➣ ปิดป้องกันคนเข้ากลุ่มคับ")
                        else:
                            line.sendMessage(msg.to,"❂•➣ ปิดป้องกันคนเข้ากลุ่มคับ")

#==============FINNISHING PROTECT========================#
                elif msg.text.lower() == 'เปิดรับแขก':
                        if settings["Wc"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"☆เปิดข้อความ☆ 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™\n❂•ต้อนรับเมื่อมีสมาชิกเข้ากลุ่ม•❂")
                        else:
                            settings["Wc"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"☆เปิดข้อความ☆ 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™\n❂•ต้อนรับเมื่อมีสมาชิกเข้ากลุ่ม•❂")
                elif msg.text.lower() == 'ปิดรับแขก':
                        if settings["Wc"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"☆ปิดข้อความ☆ 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™\n❂•ต้อนรับเมื่อมีสมาชิกเข้ากลุ่ม•❂")
                        else:
                            settings["Wc"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"☆ปิดข้อความ☆ 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™\n❂•ต้อนรับเมื่อมีสมาชิกเข้ากลุ่ม•❂")

                elif msg.text.lower() == 'เปิดทักเตะ':
                        if settings["Nk"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"☆เปิดข้อความ☆ 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™\n❂•แจ้งเตือนเมื่อมีคนเตะกันคับ•❂")
                        else:
                            settings["Nk"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"☆เปิดข้อความ☆ 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™\n❂•แจ้งเตือนเมื่อมีคนเตะกันคับ•❂")

                elif msg.text in ["ปิดทักเตะ"]:
                        if settings["Nk"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"☆ปิดข้อความ☆ 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™\n❂•แจ้งเตือนเมื่อมีคนเตะกันคับ•❂")
                        else:
                            settings["Nk"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"☆ปิดข้อความ☆ 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™\n❂•แจ้งเตือนเมื่อมีคนเตะกันคับ•❂")

                elif msg.text.lower() == 'เปิดส่งแขก':
                        if settings["Lv"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"☆เปิดข้อความ☆ 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™\n❂•อำลาเมื่อสมาชิกออกกลุ่ม•❂")
                        else:
                            settings["Lv"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"☆เปิดข้อความ☆ 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™\n❂•อำลาเมื่อสมาชิกออกกลุ่ม•❂")
                elif msg.text.lower() == 'ปิดส่งแขก':
                        if settings["Lv"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"☆ปิดข้อความ☆ 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™\n❂•อำลาเมื่อสมาชิกออกกลุ่ม•❂")
                        else:
                            settings["Lv"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"☆ปิดข้อความ☆ 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™\n❂•อำลาเมื่อสมาชิกออกกลุ่ม•❂")
                                
                elif msg.text.lower() == 'เปิดคท':
                        if settings["checkContact"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดระบบ•➣➣➣➣➣➣➣➣\n❂•อ่านข้อมูลด้วยคอนแทค•❂\n➣➣➣➣➣➣➣•อยู่แล้วคับ™")
                        else:
                            settings["checkContact"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดระบบ •➣➣➣➣➣➣➣➣\n❂•อ่านข้อมูลด้วยคอนแทค•❂\n➣➣➣➣➣➣➣เรียบร้อยคับ™")
                elif msg.text.lower() == 'ปิดคท':
                        if settings["checkContact"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดระบบ•➣➣➣➣➣➣➣➣\n❂•อ่านข้อมูลด้วยคอนแทค•❂\n➣➣➣➣➣➣➣•อยู่แล้วคับ™")
                        else:
                            settings["checkContact"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดระบบ •➣➣➣➣➣➣➣➣\n❂•อ่านข้อมูลด้วยคอนแทค•❂\n➣➣➣➣➣➣➣เรียบร้อยคับ™")
                elif msg.text.lower() == 'เปิดเช็คโพส':
                        if settings["checkPost"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดระบบ•➣➣➣➣➣➣➣➣\n ❂• เช็คโพสบนทามไลน์ •❂\n➣➣➣➣➣➣➣•อยู่แล้วคับ™")
                        else:
                            settings["checkPost"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดระบบ •➣➣➣➣➣➣➣➣\n ❂• เช็คโพสบนทามไลน์ •❂\n➣➣➣➣➣➣➣เรียบร้อยคับ™")
                elif msg.text.lower() == 'ปิดเช็คโพส':
                        if settings["checkPost"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดระบบ•➣➣➣➣➣➣➣➣\n ❂• เช็คโพสบนทามไลน์ •❂\n➣➣➣➣➣➣➣•อยู่แล้วคับ™")
                        else:
                            settings["checkPost"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดระบบ •➣➣➣➣➣➣➣➣\n ❂• เช็คโพสบนทามไลน์ •❂\n➣➣➣➣➣➣➣เรียบร้อยคับ™")
                elif text.lower() == "ดับไฟ":
                    line.sendMessage(msg.to,"❌•🛑 อันตราย 🛑•❌")
                    line.sendMessage(msg.to,"💙:::⭐ 9 ⭐:::💙")
                    line.sendMessage(msg.to,"💚:::⭐ 8 ⭐:::💚")
                    line.sendMessage(msg.to,"💖:::⭐ 7 ⭐:::💖")
                    line.sendMessage(msg.to,"💚:::⭐ 6 ⭐:::💚")
                    line.sendMessage(msg.to,"💖:::⭐ 5 ⭐:::💖")
                    line.sendMessage(msg.to,"💔:::⭐ 4 ⭐:::💔")
                    line.sendMessage(msg.to,"💙:::⭐ 3 ⭐:::💙")
                    line.sendMessage(msg.to,"💚:::⭐ 2 ⭐:::💚")
                    line.sendMessage(msg.to,"💖:::⭐ 1 ⭐:::💖")
                    line.sendMessage(msg.to,"💚:::⭐ 0 ⭐:::💚")
                    line.sendMessage(msg.to,"🔸•มึงก็เดินไปปิดดิ ไอ้สัด•🔸")

                elif msg.text in ["ลบรัน","เอจังลบรัน","ล้างรัน"]:
                    gid = line.getGroupIdsInvited()
                    start = time.time()
                    for i in gid:
                        line.rejectGroupInvitation(i)
                    elapsed_time = time.time() - start
                    line.sendMessage(to, "✧•••••••••❂✧✯✧❂••••••••••✧\n   ♡ ระบบลบรันเรียบร้อยคับ ♡\n✧•••••••••❂✧✯✧❂••••••••••✧")
                    line.sendMessage(to, "ระยะเวลาที่ใช้: %sวินาที" % (elapsed_time))
                    
                elif msg.text in ["ล้างถ้วย","ไลปอนเอฟ","ล้างจาน"]:
                    gid = line.getGroupIdsInvited()
                    start = time.time()
                    for i in gid:
                        line.rejectGroupInvitation(i)
                    elapsed_time = time.time() - start
                    line.sendReplyMessage(msg.id,to, "     ✯͜͡✯•ֆҽℓƒ-β❂T-ՃิՁণຮี•✯͜͡✯\n✧•••••••••••❂✧✯✧❂••••••••••••✧\n      ✲ ระบบล้างจานอัติโนมัตื ✲\n\n 🔸กวาดเก็บเศษอาหารลงถัง\n 🔸ระบบเริ่มล้างจานอัติโนมัติ...\n 🔸ล้างน้ำสะอาด2ครั้ง\n 🔸เช็ดให้แห้งจัดเก็บเข้าชั้นวาง\n 🔸ล้างจานอัติโนมัติเรียบร้อยคับ\n 🔸จุ้ฟป้อก\n✧•••••••••••❂✧✯✧❂••••••••••••✧")
                    sendMessageWithMention(to, lineMID)
                    line.sendMessage(to, "🌀 ฟรุ้งฟริ้ง " +datetime.today().strftime('%H:%M:%S')+ "™ 🌀")

                elif msg.text in ["ยัดดำกลุ่ม"]:
                  if msg._from in Family:
                      if msg.toType == 2:
                           print ("All Banlist")
                           _name = msg.text.replace("ยัดดำกลุ่ม","")
                           gs = line.getGroup(msg.to)
                           line.sendMessage(msg.to,"●•➤➤➤➤➤➤➤➤➤➤➤➤\n    ■•ยัดดำแม่งยกกลุ่มคับ•■\n●•➤➤➤➤➤➤➤➤➤➤➤➤")
                           targets = []
                           for g in gs.members:
                               if _name in g.displayName:
                                    targets.append(g.mid)
                           if targets == []:
                                line.sendMessage(msg.to,"Maaf")
                           else:
                               for target in targets:
                                   if not target in Family:
                                       try:
                                           settings["blacklist"][target] = True
                                           f=codecs.open('st2__b.json','w','utf-8')
                                           json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                       except:
                                           line.sentMessage(msg.to,"พบข้อผิดพลาดที่ไม่ทราบสาเหตุ")
										   
                elif 'ยัดดำ' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               settings["blacklist"][target] = True
                               f=codecs.open('st2__b.json','w','utf-8')
                               json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                               line.sendMessage(msg.to,"●•➤➤➤➤➤➤➤➤➤➤➤➤\n   ■•ยัดดำเรียบร้อยแล้วคับ•■\n●•➤➤➤➤➤➤➤➤➤➤➤➤")
                               print ("Banned User")
                           except:
                               line.sendMessage(msg.to,"✧•••❂ไม่สามารถยัดดำได้❂•••✧")

                elif 'ล้างแบน' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                             targets.append(x["M"])
                       for target in targets:
                           try:
                               del settings["blacklist"][target]
                               f=codecs.open('st2__b.json','w','utf-8')
                               json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                               line.sendMessage(msg.to,"Succes unban from the blacklist. ")
                               print ("Unbanned User")
                           except:
                               line.sendMessage(msg.to,"Contact Not Found")
                
                elif msg.text in ["เช็คดำ","บัญชีดำ","พวกนิโกร","พวกบ้ากาม","พวกหื่น","พวกโจร500","พวกดำ","พวกโรคจิต"]:
                  if msg._from in Family:
                    if settings["blacklist"] == {}:
                        line.sendMessage(msg.to,"●•➤➤➤➤➤➤➤➤➤➤➤➤\n     ■•ไม่มีลิสในบัญชีดำคับ•■\n●•➤➤➤➤➤➤➤➤➤➤➤➤")
                    else:
                        line.sendMessage(msg.to,"รายชื่อบัญชีดำ 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")
                        mc = "✧•••••••••❂✧✯✧❂••••••••••✧\n ✯💀<[[•• Blacklist ••]]>💀✯\n✧•••••••••❂✧✯✧❂••••••••••✧\n" 
                        for mi_d in settings["blacklist"]:
                              mc += "[√] " + line.getContact(mi_d).displayName + " \n"
                        line.sendMessage(msg.to, mc + "")

                elif msg.text.lower().startswith("urban "):
                    sep = msg.text.split(" ")
                    judul = msg.text.replace(sep[0] + " ","")
                    url = "http://api.urbandictionary.com/v0/define?term="+str(judul)
                    with requests.session() as s:
                        s.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = s.get(url)
                        data = r.text
                        data = json.loads(data)
                        y = "[ Result Urban ]"
                        y += "\nTags: "+ data["tags"][0]
                        y += ","+ data["tags"][1]
                        y += ","+ data["tags"][2]
                        y += ","+ data["tags"][3]
                        y += ","+ data["tags"][4]
                        y += ","+ data["tags"][5]
                        y += ","+ data["tags"][6]
                        y += ","+ data["tags"][7]
                        y += "\n[1]\nAuthor: "+str(data["list"][0]["author"])
                        y += "\nWord: "+str(data["list"][0]["word"])
                        y += "\nLink: "+str(data["list"][0]["permalink"])
                        y += "\nDefinition: "+str(data["list"][0]["definition"])
                        y += "\nExample: "+str(data["list"][0]["example"])
                        line.sendMessage(to, str(y))

            elif msg.contentType == 13:
                if settings["checkContact"] == True:
                    try:
                        contact = line.getContact(msg.contentMetadata["mid"])
                        if line != None:
                            cover = line.getProfileCoverURL(msg.contentMetadata["mid"])
                        else:
                            cover = "Tidak dapat masuk di line channel"
                        path = "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                        try:
                            line.sendImageWithURL(to, str(path))
                        except:
                            pass
                        ret_ = "[ รายการทั้งหมดจากการสำรวจด้วย คท ]"
                        ret_ += "\n ชื่อ : {}".format(str(contact.displayName))
                        ret_ += "\n ไอดี : {}".format(str(msg.contentMetadata["mid"]))
                        ret_ += "\n ตัส : {}".format(str(contact.statusMessage))
                        ret_ += "\n รูปโปรไฟล : http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                        ret_ += "\n  รูปปก : {}".format(str(cover))
                        ret_ += "\n[ สิ้นสุดการสำรวจ ]"
                        line.sendMessage(to, str(ret_))
                    except:
                        line.sendMessage(to, "เกิดข้อผิดพลาดในการสำรวจ")
            elif msg.contentType == 1:
                if settings["changePictureProfile"] == True:
                    path = line.downloadObjectMsg(msg_id)
                    settings["changePictureProfile"] = False
                    line.updateProfilePicture(path)
                    line.sendMessage(to, "ทำการแปลงโฉมเสร็จเรียบร้อย")
                if msg.toType == 2:
                    if to in settings["changeGroupPicture"]:
                        path = line.downloadObjectMsg(msg_id)
                        settings["changeGroupPicture"].remove(to)
                        line.updateGroupPicture(to, path)
                        line.sendMessage(to, "เปลี่ยนรูปภาพกลุ่มเรียบร้อยแล้ว")
            elif msg.contentType == 7:
                if settings["checkSticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    ret_ = " 🔷 ระบบเช็คสติ๊กเกอร์เราคับ 🔷\n✧••••••••••❂✧✯✧❂••••••••••✧"
                    ret_ += "\n🌟STK IĐ ::: {}".format(stk_id)
                    ret_ += "\n🌟PKG IĐ ::: {}".format(pkg_id)
                    ret_ += "\n🌟STK Vër ::: {}".format(stk_ver)
                    ret_ += "\n✧••••••••••❂✧✯✧❂••••••••••✧\n  line://shop/detail/{}".format(pkg_id)
                    line.sendReplyMessage(msg.id,to, str(ret_))
              
#==============================================================================#
        if op.type == 19:
            if lineMID in op.param3:
                settings["blacklist"][op.param2] = True
        if op.type == 22:
            if settings['leaveRoom'] == True:
                line.leaveRoom(op.param1)              
        if op.type == 24:
            if settings['leaveRoom'] == True:
                line.leaveRoom(op.param1)             
#==============================================================================#
#==============================================================================#
        if op.type == 17:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
            if RfuProtect["protect"] == True:
                if settings["blacklist"][op.param2] == True:
                    try:
                        line.kickoutFromGroup(op.param1,[op.param2])
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        line.updateGroup(G)
                    except:
                        try:
                            line.kickoutFromGroup(op.param1,[op.param2])
                            G = line.getGroup(op.param1)
                            G.preventedJoinByTicket = True
                            line.updateGroup(G)
                        except:
                            pass
        if op.type == 19:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
                elif RfuProtect["protect"] == True:
                    settings ["blacklist"][op.param2] = True
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(Rfu).inviteIntoGroup(op.param1,[op.param2])
        
        if op.type == 13:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
                elif RfuProtect["inviteprotect"] == True:
                    settings ["blacklist"][op.param2] = True
                    random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Family:
                        if op.param2 in Family:
                            pass
                        elif RfuProtect["inviteprotect"] == True:
                            settings ["blacklist"][op.param2] = True
                            random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])
                            random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                            if op.param2 not in Family:
                                if op.param2 in Family:
                                    pass
                                elif RfuProtect["cancelprotect"] == True:
                                    settings ["blacklist"][op.param2] = True
                                    random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])

        if op.type == 11:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
                elif RfuProtect["linkprotect"] == True:
                    settings ["blacklist"][op.param2] = True
                    G = line.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    line.updateGroup(G)
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
        if op.type == 5:
            if RfuProtect["autoAdd"] == True:
                if (settings["message"] in [""," ","\n",None]):
                    pass
                else:
                    line.sendMessage(op.param1,str(settings["message"]))                    

        if op.type == 11:
            if RfuProtect["linkprotect"] == True:
                if op.param2 not in Family:
                    G = line.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    random.choice(Rfu).updateGroup(G)
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param3])                    

        if op.type == 13:
           if RfuProtect["Protectguest"] == True:
               if op.param2 not in Family:
                  random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
        if op.type == 17:
            if op.param2 in settings["blacklist"] == {}:
                line.kickoutFromGroup(op.param1,[op.param2])
                now2 = datetime.datetime.now()
                nowT = datetime.datetime.strftime(now2,"%H")
                nowM = datetime.datetime.strftime(now2,"%M")
                nowS = datetime.datetime.strftime(now2,"%S")
                tm = "\n\n"+nowT+":"+nowM+":"+nowS
                line.sendText(op.param1,"สมาชิกที่ถูกแบนไม่ได้รับอนุญาตให้เข้าร่วมกลุ่ม （´・ω・｀）"+tm)
        if op.type == 17:
           if RfuProtect["Protectjoin"] == True:
               if op.param2 not in Family:
                   random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 1:
            if sender in Setmain["foto"]:
                path = line.downloadObjectMsg(msg_id)
                del Setmain["foto"][sender]
                line.updateProfilePicture(path)
                line.sendMessage(to,"Foto berhasil dirubah")
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if settings ["Aip"] == True:
                if msg.text in ["cleanse","group cleansed.","mulai",".winebot",".kickall","mayhem","kick on","Kick","!kickall","nuke","บิน","Kick","กระเด็น","หวด","เซลกากจัง","เตะ",".","ปลิว"]:
                    random.choice(Rfu).kickoutFromGroup(receiver,[sender])
                    random.choice(Rfu).sendText(msg.to,"ตรวจพบคำสั่งของบอทลบกลุ่ม จำเป็นต้องนำออกเพื่อความปลอดภัยของสมาชิก (｀・ω・´)")
            if settings ["Aip"] == True:
                if msg.text in ["ควย","หี","แตด","เย็ดแม่","เย็ดเข้","ค.วย","สัส","เหี้ย","ไอ้เหี้ย","พ่อมึงตาย","ไอ้เลว","ระยำ","ชาติหมา","หน้าหี","เซลกาก","ไอ้เรส","ไอ้เหี้ยเรส","ไอ่เรส","พ่องตาย","ส้นตีน","แม่มึงอ่ะ","แม่มึงดิ","พ่อมึงดิ"]:
                    random.choice(Rfu).kickoutFromGroup(receiver,[sender])
                    random.choice(Rfu).sendText(msg.to,"ตรวจพบคำพูดหยาบคายไม่สุภาพ จำเป็นต้องนำออกเพื่อความสงบสุขของสมาชิก (｀・ω・´)")
            if settings ["Api"] == True:
                if msg.text in ["ไอ้ยิ้ม","ไอยิ้ม","ยิ้ม","พี่ยิ้ม","อียิ้ม","น้องยิ้ม","ลุงยิ้ม","ทวดยิ้ม","เชี้ยยิ้ม","เหี้ยยิ้ม","นังยิ้ม","หมายิ้ม"]:
                    line.sendMessage(msg.to, "✲• Aütó Mëssage •✲")
            if settings ["Api"] == True:
                if msg.text in ["help","ค22","ค33","ค44","ค55","ค66","ค77","คำสั่ง","ค","คำสั่ง1","คำสั่ง2","คำสั่ง3","คำสั่ง4","คำสั่ง5","h1","h2","h3","h4","h5","h6","h7","คำสั่ง6"]:
                    line.sendMessage(msg.to,"✧•••••❂✧ֆҽℓƒ-β❂T-ℒįℳ ✧❂•••••✧\n ♡ความจำสั้นหรอคับ Helpทั้งวัน♡\n✧•••••••••••❂✧✯✧❂••••••••••••✧")
                 #   line.sendMessage(msg.to, None, contentMetadata={"STKID":"14134793","STKPKGID":"1356533","STKVER":"2"}, contentType=7)
            if settings ["Api"] == True:
                if msg.text in ["ปิดเว้น","ปิดเว้นท์","ปิดอีเว้น","ปิดอีเว้นท์","ปิดอีเวร","ปิดเวร","ปิดจ๊อบ","ปิดเวน","ปิดอีเวน"]:
                    line.sendMessage(msg.to,"❂•เพิ่งปิดหราคะ เต่าล้านปีเอ้ย•❂\n   ֆҽℓƒ-β❂T-ℒįℳ  🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")
          #          line.sendMessage(msg.to, None, contentMetadata={"STKID":"","STKPKGID":"1356533","STKVER":"2"}, contentType=7)
            if settings ["Api"] == True:
                if msg.text in ["sp","Sp","Speed","วัดรอบ","speed",".วัดรอบ"]:
                    line.sendMessage(msg.to,"Hî Speëd •➣➣➣➣➣➣➣➣\n❂•สปีดหริอเต่าคับ เช็คอยู่ได้•❂\n➣➣➣➣➣➣➣➣•Chiväree™")
            if settings ["Api"] == True:
                if msg.text in ["คท","me","Me",".โย่ว","โย่ว","เวลออน",".เวลออน","บอทออน",".บอทออน",".เช็ค","เช็ค","เวลาออน","กู","นช","Runtime","runtime",".ข้อมูล","ข้อมูล",".ออน","ออน",".เชค","เชค","ผส",".ผส","ข้อมูลกลุ่ม",".ข้อมูลกลุ่ม","Status","status","Set","set","Mybot"]:
                    line.sendMessage(msg.to,"เช็คไรหนักหนาคับ เช็คสมองบ้าง\n  ֆҽℓƒ-β❂T-ℒįℳ  🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")
             #       line.sendMessage(msg.to, None, contentMetadata={"STKID":"14134793","STKPKGID":"1356533","STKVER":"2"}, contentType=7)
            if settings ["Api"] == True:
                if msg.text in [".ไฮโล","เปิดไฮโล","แทงโล","แทงไฮโล","เปิดโล",".Hilo",".hilo"]:
                    line.sendMessage(msg.to, "✲•เริ่มทำการเขย่าคับ•✲")
            if settings ["Api"] == True:
                if msg.text in [".เต้าปูปลา",".กุ้งปลา","น้ำเต้าปูปลา","แทงกุ้งปลา","เปิดกุ้งปลา"]:
                    line.sendMessage(msg.to, "✲•เริ่มทำการสุ่มเจ้าคับ•✲")
            if settings ["Api"] == True:
                if msg.text in ["สต","สต.","ส.ต."]:
                    line.sendMessage(msg.to," ✥✥✥ ส้นตีนหรอคับ ✥✥✥\nֆҽℓƒ-β❂T-ℒįℳ  🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")
            if settings ["Api"] == True:
                if msg.text in ["ปฎิทิน","ปฏิทิน","แพ้ทาง","191","ยาม","ปะติทิน","ปติทิน",".ปฎิทิน",".ปฏิทิน"]:
                    line.sendMessage(msg.to,"❂•เป็นเพลงของวงลาบานูนคับ•❂\nֆҽℓƒ-β❂T-ℒįℳ  🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")
            if settings ["Api"] == True:
                if msg.text in ["กินข้าว","ทานข้าว","กินข้าวกัน","ทานข้าวกัน","กินขนมหวาน","กินขนมจีน","กินกล้วยทอด","มาม่า","กินมาม่า","กินขนม","ขนมจีน","กล้วยทอด","ตีน","กินตีน","เมากัน","กินเหล้ากัน","เหล้ากัน","ส้นตีน","ขี้","ขี้หมา","ขี้วัว","ขี้ไก่","กินขี้"]:
                    line.sendMessage(msg.to,"❂•➣➣➣➣➣➣➣➣➣➣➣➣\n   กินมา 20กว่าปีล่ะ ไม่เบื่อหรา\n❂•➣➣➣➣➣➣➣➣➣➣➣➣")
            if settings ["Api"] == True:
                if msg.text in ["ทำได้ไง","คิดได้ไง","เก่งมาก","ทำไมเก่งจัง","จบได้ไง","เล่นได้ไง"]:
                    line.sendMessage(msg.to,"✧•••••••••❂✧✯✧❂••••••••••✧\n    ♡♡ เพราะกูฉลาดคับ ♡♡\n✧•••••••••❂✧✯✧❂••••••••••✧")
            if settings ["Api"] == True:
                if msg.text in ["คิดตี้","คิตตี้","คิทตี้"]:
                    line.sendMessage(msg.to,"✧•••••••••❂✧✯✧❂••••••••••✧\n     ♡♡ HELLO KITTY ♡♡\n✧•••••••••❂✧✯✧❂••••••••••✧")
            if settings ["Api"] == True:
                if msg.text in ["ลบแชท",".ลบแชท","ลบรัน",".ลบรัน","ลบกลุ่ม","ลบเพื่อน","ลบข้อความ","ลบดำ",".ลบดำ"]:
                    line.sendMessage(msg.to,"💔ขอลบเทอออกจากใจบ้างนะ💔\n    ֆҽℓƒ-β❂T-ℒįℳ  ?? " +datetime.today().strftime('%H:%M:%S')+ "™")
            if settings ["Api"] == True:
                if msg.text in ["ล้างแชท",".ล้างแชท","ล้างรัน"".ล้างรัน","ล้างเพื่อน","ล้างดำ",".ล้างดำ"]:
                    line.sendMessage(msg.to,"❂•ไปล้างที่คาร์แคร์ดิ อีเบื๊อก•❂\n  ֆҽℓƒ-β❂T-ℒįℳ  🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")
            if settings ["Api"] == True:
                if msg.text in ["น่าน"]:
                    line.sendMessage(msg.to,"🌀น่าน คือจ.ในภาคเหนือคับ🌀\n ֆҽℓƒ-β❂T-ℒįℳ  🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")
            if settings ["Api"] == True:
                if msg.text in ["ขอบคุนค่ะ","ขอบคุนคับ","ขอบคุนคร้า","ขอบคุนคะ","ขอบคุณ","ขอบคุน","ขอบใจ","ขอบคุณคับ","ขอบคุณคะ","ขอบคุณค่ะ","ใจจ้า","ดีคับ","ดีค่ะ","ดีคะ","ดีคร้า","ดีค้าบ","ดีค้าฟ","มอนิ้ง","มอนิ่ง","ขอบคุณมาก","ขอบคุนมาก","ดียามเช้า","อรุณสวัสดิ์"," ดีจ้า","สวัสดี","สวัสดีคร้า","สวัสดีคะ","สวัสดีค่ะ","สวัสดีคับ","สวีดัด","สวัสดีปีใหม่"]:
                    line.sendMessage(msg.to,"❂•• กองไว้ตรงนั้นคับ ••❂\n  Auto® 🕞 " +datetime.today().strftime('%H:%M:%S')+ "™")
            if settings ["Api"] == True:
                if msg.text in ["หลาบ","หลาบขี้","หรอย","หรอยแรง","หรอยคาด","หรอยหนัด","ทำพือ","ว่าพือ","ไม่พือ"]:
                    line.sendMessage(msg.to,"❂• แหลงใต้กันหล่าวโหม๋โส •❂\n ֆҽℓƒ-β❂T-ℒįℳ  🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")
            if settings ["Api"] == True:
                if msg.text in ["เยส","เยสสส","เยสส","เยสสสสส","เยสสสส","เงี่ยน","เงี่ยนชิบ","เงี่ยนโว้ย","เงี่ยนโว้ยยย","เงี่ยนวะ","กูเงี่ยน","เงี่ยนเว้ย"]:
                    line.sendMessage(msg.to,"❂❂•ก็ไปเยสกับรถถังสิคับ•❂❂\n ֆҽℓƒ-β❂T-ℒįℳ  🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")
            if settings ["Api"] == True:
                if msg.text in ["บอท","Bot","bot","คนหรือบอท","บอทหรอ","คนหรอบอท","บอทป่าว","บอทป่ะ","เชล","เชลบอท","บอทตาย"]:
                    line.sendMessage(msg.to,"❂•เรื่องบอทณเดชจะไม่ยุ่งคับ•❂\n ֆҽℓƒ-β❂T-ℒįℳ  🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")
            if settings ["Api"] == True:
                if msg.text in ["ดึง","ฝากดึง","ดึงที","ฝากดึงที","ดึงหน่อย"]:
                    line.sendMessage(msg.to,"❂•ไม่ดึงนะคับ ไม่อยากรู้จัก•❂\n ֆҽℓƒ-β❂T-ℒįℳ  🕒 " +datetime.today().strftime('%H:%M:%S'))
            if settings ["Api"] == True:
                if msg.text in ["รอ","รอๆ","รอนะ","จะรอ","รออยู่","รอยู่","แปป","รอแปป","แปปปป","แปปป","แปปนึงคับ","แปปนึง","รอแปปคับ","แปปคับ","แปปคับ","แปปคะ","แปปคับ","แปปๆ","แป๊ป","แปปนะ","แปปน่ะ"]:
                    line.sendMessage(msg.to,"❂•ไม่นานคร้า แค่8ชั่วโมงเอง•❂\n  ֆҽℓƒ-β❂T-ℒįℳ  🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")
            if settings ["Api"] == True:
                if msg.text in ["เปิดเสือก",".เปิดเสือก","เปิดเผือก",".เปิดเผือก"]:
                    line.sendMessage(msg.to,"❂•คุณคือแชมป์เสือกประจำปีคับ•❂\n ֆҽℓƒ-β❂T-ℒįℳ  🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")
            if settings ["Api"] == True:
                if msg.text in ["หลุด"]:
                    line.sendMessage(msg.to,"✥•✥ กางเกงหลุดหราคับ ✥•✥\n ֆҽℓƒ-β❂T-ℒįℳ  🕒 " +datetime.today().strftime('%H:%M:%S')+ "™")

        if op.type in [25,26]:
            msg = op.message
            if msg.contentType == 16:
                if settings["checkPost"] == True:
                        try:
                            ret_ = "[ ข้อมูลของโพสนี้ ]"
                            if msg.contentMetadata["serviceType"] == "GB":
                                contact = line.getContact(sender)
                                auth = "\n  ผู้เขียนโพส : {}".format(str(contact.displayName))
                            else:
                                auth = "\n  ผู้เขียนโพส : {}".format(str(msg.contentMetadata["serviceName"]))
                            purl = "\n  ลิ้งโพส : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                            ret_ += auth
                            ret_ += purl
                            if "mediaOid" in msg.contentMetadata:
                                object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                if msg.contentMetadata["mediaType"] == "V":
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n  Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        murl = "\n  Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n  Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        murl = "\n  Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                        ret_ += murl
                                else:
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                ret_ += ourl
                            if "stickerId" in msg.contentMetadata:
                                stck = "\n  Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                ret_ += stck
                            if "text" in msg.contentMetadata:
                                text = "\n ข้อความโดยย่อ : {}".format(str(msg.contentMetadata["text"]))
                                ret_ += text
                            ret_ += "\n[ สิ้นสุดการเช็คโพส ]"
                            line.sendMessage(to, str(ret_))
                        except:
                            line.sendMessage(to, "เกิดข้อผิดะลาดในการเช็คโพสนี้")

        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != line.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if settings["autoRead"] == True:
                    line.sendChatChecked(to, msg_id)				
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                    text = msg.text
                    if text is not None:
                        line.sendMessage(msg.to,text)
                elif msg.contentType == 7:
                    if settings["checkSticker"] == True:
                        try:
                            stk_id = msg.contentMetadata['STKID']
                            stk_ver = msg.contentMetadata['STKVER']
                            pkg_id = msg.contentMetadata['STKPKGID']
                            ret_ = "🔶ระบบเช็คสติ๊กเกอร์เพื่อนคับ🔶\n✧••••••••••❂✧✯✧❂••••••••••✧"
                            ret_ += "\n🌟STK IĐ ::: {}".format(stk_id)
                            ret_ += "\n🌟PKG IĐ ::: {}".format(pkg_id)
                            ret_ += "\n🌟STK Vër ::: {}".format(stk_ver)
                            ret_ += "\n✧••••••••••❂✧✯✧❂••••••••••✧\n  line://shop/detail/{}".format(pkg_id)
                            print(msg)
                            line.sendImageWithURL(to, "http://dl.stickershop.line.naver.jp/products/0/0/"+msg.contentMetadata["STKVER"]+"/"+msg.contentMetadata["STKPKGID"]+"/WindowsPhone/stickers/"+msg.contentMetadata["STKID"]+".png")
                            line.sendReplyMessage(msg.id,to, str(ret_))                            
                        except Exception as error:
                            line.sendMessage(to, str(error))
                if settings["unsendMessage"] == True:
                    try:
                        msg = op.message
                        if msg.toType == 0:
                            line.log("[{} : {}]".format(str(msg._from), str(msg.text)))
                        else:
                            line.log("[{} : {}]".format(str(msg.to), str(msg.text)))
                            msg_dict[msg.id] = {"text": msg.text, "from": msg._from, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                    except Exception as error:
                        logError(error)
                if msg.contentType == 0:
                    if text is None:
                        return
                    if "/ti/g/" in msg.text.lower():
                        if settings["autoJoinTicket"] == True:
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(text)
                            n_links = []
                            for l in links:
                                if l not in n_links:
                                    n_links.append(l)
                            for ticket_id in n_links:
                                group = line.findGroupByTicket(ticket_id)
                                line.acceptGroupInvitationByTicket(group.id,ticket_id)
                                line.sendMessage(to, "มุดลิ้งเข้าไปในกลุ่ม👉 %s 👈 เรียบร้อยแล้ว" % str(group.name))
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in msg.contentMetadata.keys() != None:
        	             if settings['kickMention'] == True:
        		             contact = line.getContact(msg._from)
        		             cName = contact.displayName
        		             balas = ["เนื่องจากตอนนี้ผมเปิดระบบเตะคนแทคไว้ " + "\n👉" + cName + "\n🙏ต้องขออภัยด้วยจริงๆ🙏Bye!!!"]
        		             ret_ = "" + random.choice(balas)                     
        		             name = re.findall(r'@(\w+)', msg.text)
        		             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
        		             mentionees = mention["MENTIONEES"]
        		             for mention in mentionees:
        			               if mention['M'] in admin:
        				                  line.sendText(msg.to,ret_)
        				                  random.choice(Rfu).kickoutFromGroup(msg.to,[msg._from])
        				                  break                                  
        			               if mention['M'] in lineMID:
        				                  line.sendText(msg.to,ret_)
        				                  random.choice(Rfu).kickoutFromGroup(msg.to,[msg._from])
        				                  break
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys())!= None:
                         if settings['potoMention'] == True:
                             contact = line.getContact(msg._from)
                             cName = contact.pictureStatus
                             mi_d = contact.mid
                             balas = ["http://dl.profile.line-cdn.net/" + cName]
                             ret_ = random.choice(balas)
                             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                             mentionees = mention["MENTIONEES"]
                             for mention in mentionees:
                                   if mention["M"] in lineMID:
                                          line.sendImageWithURL(to,ret_)
                        #                  line.sendContact(msg.to, mi_d)
                        #                  line.sendMessage(msg.to, None, contentMetadata={"STKID":"2654757","STKPKGID":"1064185","STKVER":"2"}, contentType=7)
                                          break  
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys()) != None:
                         if settings['detectMention'] == True:
                             contact = line.getContact(msg._from)
                             cName = contact.displayName
                             chivareeZ = [' 💔💔💔- ว่างหรอคับ -💔💔💔',' 💚💚💚- ว่างหรอคับ -💚💚💚',' 💜💜💜- ว่างหรอคับ -💜💜💜',' 💙💙💙- ว่างหรอคับ -💙💙💙',' 💛💛💛- ว่างหรอคับ -💛💛💛',' 🔶🔶🔶- ว่างหรอคับ -🔶🔶🔶',' 🔷🔷🔷- ว่างหรอคับ -🔷🔷🔷',' 🌟🌟🌟- ว่างหรอคับ -🌟🌟🌟',' 💗💗💗- ว่างหรอคับ -💗💗💗',' 💘💘💘- ว่างหรอคับ -💘💘💘']
                             chivareeV = [' น้องไปเล่นดีดลูกแก้วตรงโน้นน่ะ',' น้องไปเล่นกะโดดยางตรงโน้นน่ะ',' พี่ไม่ว่างนะคับขับเครื่องบินอยู่คับ',' น้องไปเล่นขี้ตรงโน้นน่ะพี่ไม่ว่าง',' ไปเล่นขี้พลางๆนะคับพี่ยังไม่ว่าง',' พี่ขับเครื่องบินอยู่คับไม่ว่างตอบ',' ไม่ว่างคับให้อาหารไดโนเสาร์อยู่',' สร้างแลนมาร์คอยู่ไม่ว่างตอบคับ',' ไม่ว่างเล่นด้วยนะขัดสนิมปืนอยู่',' พี่ขัดปืนอยู่ ไว้ยิงพวกชอบแทค',' มีไรคับเตะหน้าพวกชอบแทคอยู่',' น้องไปเล่นหมากเก็บตรงโน้นน่ะ']
                             ret_ = "✧••••••••••❂✧✯✧❂••••••••••✧\n" + random.choice(chivareeZ) + "\n✧••••••••••❂✧✯✧❂••••••••••✧\n" + random.choice(chivareeV) + "\n ➤ " + cName
                             name = re.findall(r'@(\w+)', msg.text)
                             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                             mentionees = mention['MENTIONEES']
                             for mention in mentionees:
                                   if mention['M'] in lineMID:
                                          line.sendMessage(to,ret_)
                                          line.sendMessage(to,str(settings["Respontag"]))
                                          break
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys()) != None:
                         if settings['delayMention'] == True:
                             contact = line.getContact(msg._from)
                             cName = contact.displayName
                             name = re.findall(r'@(\w+)', msg.text)
                             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                             mentionees = mention['MENTIONEES']
                             for mention in mentionees:
                                   if mention['M'] in lineMID:
                                          sendMessageWithMention(to, contact.mid)
                                          sendMessageWithMention(to, contact.mid)
                                          sendMessageWithMention(to, contact.mid)
                                          sendMessageWithMention(to, contact.mid)
                                          sendMessageWithMention(to, contact.mid)
                                          sendMessageWithMention(to, contact.mid)
                                          sendMessageWithMention(to, contact.mid)
                                          sendMessageWithMention(to, contact.mid)
                                          sendMessageWithMention(to, contact.mid)
                                          sendMessageWithMention(to, contact.mid)
                                          break 
                                          
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = sender
                elif msg.toType == 2:
                    to = receiver
                if msg.contentType == 0:
                    if settings["unsendMessage"] == True:
                        try:
                            if msg.location != None:
                                unsendmsg = time.time()
                                msg_dict[msg.id] = {"lokasi":msg.location,"from":msg._from,"waktu":unsendmsg}
                            else:
                                unsendmsg = time.time()
                                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"waktu":unsendmsg}
                        except Exception as e:
                            print (e)
                if msg.contentType == 1:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg1 = time.time()
                            path = line.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"image":path,"waktu":unsendmsg1}
                        except Exception as e:
                            print (e)
                if msg.contentType == 2:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg2 = time.time()
                            path = line.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"video":path,"waktu":unsendmsg2}
                        except Exception as e:
                            print (e)
                if msg.contentType == 3:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg3 = time.time()
                            path = line.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"audio":path,"waktu":unsendmsg3}
                        except Exception as e:
                            print (e)
                if msg.contentType == 7:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg7 = time.time()
                            sticker = msg.contentMetadata["STKID"]
                            link = "http://dl.stickershop.line.naver.jp/stickershop/v1/sticker/{}/android/sticker.png".format(sticker)
                            msg_dict[msg.id] = {"from":msg._from,"sticker":link,"waktu":unsendmsg7}
                        except Exception as e:
                            print (e)
                if msg.contentType == 13:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg13 = time.time()
                            mid = msg.contentMetadata["mid"]
                            msg_dict[msg.id] = {"from":msg._from,"mid":mid,"waktu":unsendmsg13}
                        except Exception as e:
                            print (e)
                if msg.contentType == 14:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg14 = time.time()
                            path = line.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"file":path,"waktu":unsendmsg14}
                        except Exception as e:
                            print (e)
#==============================================================================#
        if op.type == 65:
            print ("[ 65 ] NOTIFIED DESTROY MESSAGE")
            if settings["unsendMessage"] == True:
                at = op.param1
                msg_id = op.param2
                if msg_id in msg_dict:
                    ah = time.time()
                    ikkeh = line.getContact(msg_dict[msg_id]["from"])
                    if "text" in msg_dict[msg_id]:
                        waktumsg = ah - msg_dict[msg_id]["waktu"]
                        waktumsg = format_timespan(waktumsg)
                        rat_ = "\n🔶• Sp {}".format(waktumsg)
                        rat_ += "\n🔷• ➤ {}".format(msg_dict[msg_id]["text"])
                        rat_ += "\n🌀• เวลา 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™ Timë🌀"
                        line.sendMessage(at, "✧•••••••••••❂✧✯✧❂•••••••••••✧\n  💔พบการยกเลิกข้อความคับ💔\n✧•••••••••••❂✧✯✧❂•••••••••••✧\n🔷• ชื่อ {}".format(str(ikkeh.displayName) + str(rat_)))
                   #     sendMention(at, ikkeh.mid, "** ตรวจพบการยกเลิกข้อความ **\n\nMaker :\n", str(rat_))
                        del msg_dict[msg_id]
                    else:
                        if "image" in msg_dict[msg_id]:
                            waktumsg = ah - msg_dict[msg_id]["waktu"]
                            waktumsg = format_timespan(waktumsg)
                            rat_ = "\n🔶• Sp {}".format(waktumsg)
                            rat_ += "\n🌀• เวลา 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™ Timë🌀"
                            line.sendMessage(at, "✧•••••••••••❂✧✯✧❂•••••••••••✧\n   💙พบการยกเลิกรูปภาพคับ💙\n✧•••••••••••❂✧✯✧❂•••••••••••✧\n🔷• ชื่อ {}".format(str(ikkeh.displayName) + str(rat_)))
                            line.sendImage(at, msg_dict[msg_id]["image"])
                            del msg_dict[msg_id]
                        else:
                            if "video" in msg_dict[msg_id]:
                                waktumsg = ah - msg_dict[msg_id]["waktu"]
                                waktumsg = format_timespan(waktumsg)
                                rat_ = "\n🔶• Sp {}".format(waktumsg)
                                rat_ += "\n🌀• เวลา 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™ Timë🌀"
                                line.sendMessage(at, "✧•••••••••••❂✧✯✧❂•••••••••••✧\n    💗 พบการยกเลิกวีดีโอคับ 💗\n✧•••••••••••❂✧✯✧❂•••••••••••✧\n🔷• ชื่อ {}".format(str(ikkeh.displayName) + str(rat_)))
                                line.sendVideo(at, msg_dict[msg_id]["video"])
                                del msg_dict[msg_id]
                            else:
                                if "audio" in msg_dict[msg_id]:
                                    waktumsg = ah - msg_dict[msg_id]["waktu"]
                                    waktumsg = format_timespan(waktumsg)
                                    rat_ = "\n🔶• Sp {}".format(waktumsg)
                                    rat_ += "\n🌀• เวลา 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™ Timë🌀"
                                    line.sendMessage(at, "✧•••••••••••❂✧✯✧❂•••••••••••✧\n 🎧พบการยกเลิกไฟล์เสียงคับ🎧\n✧•••••••••••❂✧✯✧❂•••••••••••✧\n🔷• ชื่อ {}".format(str(ikkeh.displayName) + str(rat_)))
                                    line.sendAudio(at, msg_dict[msg_id]["audio"])
                                    del msg_dict[msg_id]
                                else:
                                    if "sticker" in msg_dict[msg_id]:
                                        waktumsg = ah - msg_dict[msg_id]["waktu"]
                                        waktumsg = format_timespan(waktumsg)
                                        rat_ = "\n🔶• Sp {}".format(waktumsg)
                                        rat_ += "\n🌀• เวลา 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™ Timë🌀"
                                        line.sendMessage(at, "✧•••••••••••❂✧✯✧❂•••••••••••✧\n  💛พบการยกเลิกสติ๊กเกอร์คับ💛\n✧•••••••••••❂✧✯✧❂•••••••••••✧\n🔷• ชื่อ {}".format(str(ikkeh.displayName) + str(rat_)))
                                        line.sendImageWithURL(at, msg_dict[msg_id]["sticker"])
                                        del msg_dict[msg_id]
                                    else:
                                        if "mid" in msg_dict[msg_id]:
                                            waktumsg = ah - msg_dict[msg_id]["waktu"]
                                            waktumsg = format_timespan(waktumsg)
                                            rat_ = "\n🔶• Sp {}".format(waktumsg)
                                            rat_ += "\n🌀• เวลา 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™ Timë🌀"
                                            line.sendMessage(at, "✧•••••••••••❂✧✯✧❂•••••••••••✧\n  💚พบการยกเลิกคอนเท็คคับ💚\n✧•••••••••••❂✧✯✧❂•••••••••••✧\n🔷• ชื่อ {}".format(str(ikkeh.displayName) + str(rat_)))
                                            line.sendContact(at, msg_dict[msg_id]["mid"])
                                            del msg_dict[msg_id]
                                        else:
                                            if "lokasi" in msg_dict[msg_id]:
                                                waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                waktumsg = format_timespan(waktumsg)
                                                rat_ = "\n🔶• Sp {}".format(waktumsg)
                                                rat_ += "\n🌀• เวลา 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™ Timë🌀"
                                                line.sendMessage(at, "✧•••••••••••❂✧✯✧❂•••••••••••✧\n 💜 พบการยกเลิกโลเคชั่นคับ 💜\n✧•••••••••••❂✧✯✧❂•••••••••••✧\n🔷• ชื่อ {}".format(str(ikkeh.displayName) + str(rat_)))
                                                line.sendLocation(at, msg_dict[msg_id]["lokasi"])
                                                del msg_dict[msg_id]
                                            else:
                                                if "file" in msg_dict[msg_id]:
                                                    waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                    waktumsg = format_timespan(waktumsg)
                                                    rat_ = "\n🔶• Sp {}".format(waktumsg)
                                                    rat_ += "\n🌀• เวลา 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™ Timë🌀"
                                                    line.sendMessage(at, "✧•••••••••••❂✧✯✧❂•••••••••••✧\n 🌟 พบการยกเลิกไฟล์งานคับ 🌟\n✧•••••••••••❂✧✯✧❂•••••••••••✧\n🔷• ชื่อ {}".format(str(ikkeh.displayName) + str(rat_)))
                                                    line.sendFile(at, msg_dict[msg_id]["file"])
                                                    del msg_dict[msg_id]
                else:
                    line.sendMessage(at, "✧•••••••••••❂✧✯✧❂•••••••••••✧\n   🔶พบการยกเลิกข้อความคับ🔶\n    ✯͜͡✯•ֆҽℓƒ-β❂T-┅═हईツ☆❦ℒįℳ❦ツ❈ईह═┅• ✯͜͡✯\n✧•••••••••••❂✧✯✧❂•••••••••••✧")

        if op.type == 17:
           print ("MEMBER JOIN TO GROUP")
           if settings["Wc"] == True:
             if op.param2 in lineMID:
                 return
             dan = line.getContact(op.param2)
             tgb = line.getGroup(op.param1)
             chivaree = ['      💛💛 ยินดีต้อนรับ 💛💛','      💔💔 ยินดีต้อนรับ 💔💔','      💜💜 ยินดีต้อนรับ 💜💜','      💙💙 ยินดีต้อนรับ 💙💙','      💚💚 ยินดีต้อนรับ 💚💚']
             ajang = ['💕💕 •ֆҽℓƒ-β❂T-┅═हईツ☆❦ℒįℳ❦ツ❈ईह═┅• 💕💕','💓💓 •ֆҽℓƒ-β❂T-┅═हईツ☆❦ℒįℳ❦ツ❈ईह═┅• 💓💓','💗💗•ֆҽℓƒ-β❂T-┅═हईツ☆❦ℒįℳ❦ツ❈ईह═┅•  💗💗','💞💞•ֆҽℓƒ-β❂T-┅═हईツ☆❦ℒįℳ❦ツ❈ईह═┅• 💞💞','💘💘 •ֆҽℓƒ-β❂T-┅═हईツ☆❦ℒįℳ❦ツ❈ईह═┅• 💘💘']
             line.sendMessage(op.param1, str(settings["welcome"]) + "\n" + str(random.choice(chivaree)) +"\n✧••••••••••❂✧✯✧❂••••••••••✧\n •➣ {}\n •➣ {}".format(str(dan.displayName),str(tgb.name)))
             line.sendContact(op.param1, op.param2)
          #   line.sendMessage(op.param1,"สเตตัส\n{}".format(str(dan.statusMessage)))
             line.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
             line.sendMessage(op.param1, str(random.choice(ajang)))
        if op.type == 19:
           print ("MEMBER KICKOUT TO GROUP")
           if settings["Nk"] == True:
             if op.param2 in lineMID:
                 return
             dan = line.getContact(op.param2)
             tgb = line.getGroup(op.param1)
             line.sendMessage(op.param1,str(settings["kick"]) + "\n    -Auto Kick:- 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™\n✧••••••••••❂✧✯✧❂•••••••••••✧\n      เป็นฟรีคิกที่งดงามมากคับ\n 🏆🏆🏆✯ดาวซัลโว✯🏆🏆🏆\n •➤ {}".format(str(dan.displayName)))
        #     line.sendContact(op.param1, op.param2)
         #    line.sendMessage(op.param1,"สเตตัส\n{}".format(str(dan.statusMessage)))
             line.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
        if op.type == 15:
           print ("MEMBER LEAVE TO GROUP")
           if settings["Lv"] == True:
             if op.param2 in lineMID:
                 return
             dan = line.getContact(op.param2)
             tgb = line.getGroup(op.param1)
             line.sendMessage(op.param1,str(settings["bye"]) + "\n   B.Y.Ë. ณ. เวลา 🕟 " +datetime.today().strftime('%H:%M:%S')+ "™\n❂•➤➤➤➤➤➤➤➤➤➤➤➤\n 😂บ๊ะบาย แล้วเจอกันใหม่น๊ะ😂\n •➣ {}\n •➣ {}".format(str(dan.displayName),str(tgb.name)))
             line.sendContact(op.param1, op.param2)
             line.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
        if op.type == 55:
            try:
                if RfuCctv['cyduk'][op.param1]==True:
                    if op.param1 in RfuCctv['point']:
                        Name = line.getContact(op.param2).displayName
                        if Name in RfuCctv['sidermem'][op.param1]:
                            pass
                        else:
                            RfuCctv['sidermem'][op.param1] += "\n🔰" + Name
                            pref=['   🍺ไวนะเทอ อ่านคนแรกเลย','     🔍: เทพเจ้าแห่งการอ่าน','   🎖แชมป์อ่าน 8 สมัยมาแว้ว','      👉  ฮั่นแน่..เค้ารู้ทันนะ','   🌀อ่านอย่างเดียวเลยนะคับ','    👉: อ๊ะอ๊ะ!! ตาวิเศษเห็นน่ะ..','    🕣:ออกมาคุยกันหน่อย อิอิ']
                            chivaree = ['  💛💛 HEŁŁO KITTY 💛💛','  💘💘 HEŁŁO KITTY 💘💘','  💔💔 HEŁŁO KITTY 💔💔','  💜💜 HEŁŁO KITTY 💜💜','  💙💙 HEŁŁO KITTY 💙💙','  💚💚 HEŁŁO KITTY 💚💚','    ♡♡ HEŁŁO KITTY ♡♡','  💗💗 HEŁŁO KITTY 💗💗']
                            sendMessageWithMention(op.param1, op.param2)
                            line.sendMessage(op.param1,"✧••••••••••❂✧✯✧❂••••••••••✧\n" + str(random.choice(chivaree)) + "\n✧••••••••••❂✧✯✧❂••••••••••✧\n" + str(random.choice(pref)))
                            line.sendContact(op.param1, op.param2)
                    else:
                        pass
                else:
                    pass
            except:
                pass

        if op.type == 55:
            try:
                if RfuCctv['cyduk'][op.param1]==True:
                    if op.param1 in RfuCctv['point']:
                        Name = line.getContact(op.param2).displayName
                        if Name in RfuCctv['sidermem'][op.param1]:
                            pass
                        else:
                            RfuCctv['sidermem'][op.param1] += "\n⌬ " + Name + "\n╚════════════════┛"
                            if " " in Name:
                            	nick = Name.split(' ')
                            if len(nick) == 2:
                            	line.sendMessage(op.param1, "Nah " +nick[0])
                            summon(op.param1, [op.param2])
                    else:
                        pass
                else:
                    pass
            except:
                pass
        if op.type == 55:
            print (" ╬╬♡•ຟနุ้७ຟနิ้७•♡╬╬ ")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
    except Exception as error:
        logError(error)
#==============================================================================#
def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
        

while True:
    try:
        ops = oepoll.singleTrace(count=5)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
atexit.register(atend)
