# -*- coding: utf-8 -*-
#thanks to allfams
#from LineAPI import *
from LineAPI.linepy import *
from LineAPI.akad.ttypes import Message
from LineAPI.akad.ttypes import ContentType as Type
import json, requests, sys
from akad.ttypes import ContentType as Type
from akad.ttypes import Message
from multiprocessing import Pool, Process
from time import sleep
import pytz, datetime, pafy, time, timeit, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, urllib3, wikipedia, html5lib
from datetime import timedelta, date
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from datetime import datetime
from bs4 import BeautifulSoup
from googletrans import Translator
from gtts_token.gtts_token import Token
_session = requests.session()
from gtts import gTTS
import youtube_dl
from ffmpy import FFmpeg
import traceback

#client = LINE("EBwJ9QsSogP3EF00X3H0.Ql1GwYBgPq4bD8CfwL22qa.sKZkOTP5t/Kbz4GoC1pglLwmSZyNWe00v4UqDDndO38=")
client = LINE("ECyLm91h4WevclhvruK0.Ql1GwYBgPq4bD8CfwL22qa.M+ygfn6M+1kpO6kgsJOYR+06m3QYEHAelQpEJtpZWcU=")
 #TEMP_ID = "1623679774"
#channel = Channel(client, TEMP_ID)
#client.log(str(channel.getChannelResult()))
client.log("Timeline Token : " + str(client.tl.channelAccessToken))
clientMid = client.profile.mid
clientProfile = client.getProfile()
clientSettings = client.getSettings()
clientPoll = OEPoll(client)
botStart = time.time()
admin = ["ua8bd605b26c6a50e0177c7055a5db640","u6723125e7f53d6758acb4aaa613605d0"]
msg_dict = {}
msg_dict1 = {}


settings = {
    "autoAdd": True,
    "autoJoin": True,
    "autolike": True,
    "comment": "auto comment by:\n   ⚛️ ID BOTS ⚛️ \n\n⚛️ Open order bot protect ⚛️\n⚛️.Protect room smule\n⚛️.Protect room event\n⚛️.Protect room chat\n⚛️.Protect room olshop\n Dilengkapi dengan anti JS\nSedia juga selfbot Only\n\nAnda minat\nsilahkan hubungi id line di bawah\nhttps://line.me/ti/p/~id_bots",
    "autoBlock": True,
    "autoLeave": True,
    "autoRead": False,
    "autoRespon": False,
    "welcome": False,
    "leave": False,
    "Respontag":"ada apa tag aku\nkangen ya sama aku ",
    "stickerOn": False,
    "autoJoinTicket": False,
    "checkContact": False,
    "checkPost": False,
    "checkSticker": False,
    "changePictureProfile": False,
    "changeGroupPicture": [],
    "keyCommand": "",
    "AddstickerTag": {
        "sid": "",
        "spkg": "",
        "status": False
            },
    "Addsticker":{
            "name": "",
            "status":False
            },
    "stk":{},
    "selfbot":True,
    "Images":{},
    "Img":{},
    "Addimage":{
            "name": "",
            "status":False
            },
    "Videos":{},
    "Addaudio":{
            "name": "",
            "status":False
            },
    "Addvideo":{
            "name": "",
            "status":False
            },
    "myProfile": {
        "displayName": "",
        "coverId": "",
        "pictureStatus": "",
        "statusMessage": ""
    },
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
    },
    "setKey": False,
    "sider": True,
    "unsendMessage": False
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

read = {
    "ROM": {},
    "readPoint": {},
    "readMember": {},
    "readTime": {}
}

list_language = {
    "list_textToSpeech": {
        "id": "Indonesia",
        "af" : "Afrikaans",
        "sq" : "Albanian",
        "ar" : "Arabic",
        "hy" : "Armenian",
        "bn" : "Bengali",
        "ca" : "Catalan",
        "zh" : "Chinese",
        "zh-cn" : "Chinese (Mandarin/China)",
        "zh-tw" : "Chinese (Mandarin/Taiwan)",
        "zh-yue" : "Chinese (Cantonese)",
        "hr" : "Croatian",
        "cs" : "Czech",
        "da" : "Danish",
        "nl" : "Dutch",
        "en" : "English",
        "en-au" : "English (Australia)",
        "en-uk" : "English (United Kingdom)",
        "en-us" : "English (United States)",
        "eo" : "Esperanto",
        "fi" : "Finnish",
        "fr" : "French",
        "de" : "German",
        "el" : "Greek",
        "hi" : "Hindi",
        "hu" : "Hungarian",
        "is" : "Icelandic",
        "id" : "Indonesian",
        "it" : "Italian",
        "ja" : "Japanese",
        "km" : "Khmer (Cambodian)",
        "ko" : "Korean",
        "la" : "Latin",
        "lv" : "Latvian",
        "mk" : "Macedonian",
        "no" : "Norwegian",
        "pl" : "Polish",
        "pt" : "Portuguese",
        "ro" : "Romanian",
        "ru" : "Russian",
        "sr" : "Serbian",
        "si" : "Sinhala",
        "sk" : "Slovak",
        "es" : "Spanish",
        "es-es" : "Spanish (Spain)",
        "es-us" : "Spanish (United States)",
        "sw" : "Swahili",
        "sv" : "Swedish",
        "ta" : "Tamil",
        "th" : "Thai",
        "tr" : "Turkish",
        "uk" : "Ukrainian",
        "vi" : "Vietnamese",
        "cy" : "Welsh"
    },
    "list_translate": {    
        "af": "afrikaans",
        "sq": "albanian",
        "am": "amharic",
        "ar": "arabic",
        "hy": "armenian",
        "az": "azerbaijani",
        "eu": "basque",
        "be": "belarusian",
        "bn": "bengali",
        "bs": "bosnian",
        "bg": "bulgarian",
        "ca": "catalan",
        "ceb": "cebuano",
        "ny": "chichewa",
        "zh-cn": "chinese (simplified)",
        "zh-tw": "chinese (traditional)",
        "co": "corsican",
        "hr": "croatian",
        "cs": "czech",
        "da": "danish",
        "nl": "dutch",
        "en": "english",
        "eo": "esperanto",
        "et": "estonian",
        "tl": "filipino",
        "fi": "finnish",
        "fr": "french",
        "fy": "frisian",
        "gl": "galician",
        "ka": "georgian",
        "de": "german",
        "el": "greek",
        "gu": "gujarati",
        "ht": "haitian creole",
        "ha": "hausa",
        "haw": "hawaiian",
        "iw": "hebrew",
        "hi": "hindi",
        "hmn": "hmong",
        "hu": "hungarian",
        "is": "icelandic",
        "ig": "igbo",
        "id": "indonesian",
        "ga": "irish",
        "it": "italian",
        "ja": "japanese",
        "jw": "javanese",
        "kn": "kannada",
        "kk": "kazakh",
        "km": "khmer",
        "ko": "korean",
        "ku": "kurdish (kurmanji)",
        "ky": "kyrgyz",
        "lo": "lao",
        "la": "latin",
        "lv": "latvian",
        "lt": "lithuanian",
        "lb": "luxembourgish",
        "mk": "macedonian",
        "mg": "malagasy",
        "ms": "malay",
        "ml": "malayalam",
        "mt": "maltese",
        "mi": "maori",
        "mr": "marathi",
        "mn": "mongolian",
        "my": "myanmar (burmese)",
        "ne": "nepali",
        "no": "norwegian",
        "ps": "pashto",
        "fa": "persian",
        "pl": "polish",
        "pt": "portuguese",
        "pa": "punjabi",
        "ro": "romanian",
        "ru": "russian",
        "sm": "samoan",
        "gd": "scots gaelic",
        "sr": "serbian",
        "st": "sesotho",
        "sn": "shona",
        "sd": "sindhi",
        "si": "sinhala",
        "sk": "slovak",
        "sl": "slovenian",
        "so": "somali",
        "es": "spanish",
        "su": "sundanese",
        "sw": "swahili",
        "sv": "swedish",
        "tg": "tajik",
        "ta": "tamil",
        "te": "telugu",
        "th": "thai",
        "tr": "turkish",
        "uk": "ukrainian",
        "ur": "urdu",
        "uz": "uzbek",
        "vi": "vietnamese",
        "cy": "welsh",
        "xh": "xhosa",
        "yi": "yiddish",
        "yo": "yoruba",
        "zu": "zulu",
        "fil": "Filipino",
        "he": "Hebrew"
    }
}

try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")
    
settings["myProfile"]["displayName"] = clientProfile.displayName
settings["myProfile"]["statusMessage"] = clientProfile.statusMessage
settings["myProfile"]["pictureStatus"] = clientProfile.pictureStatus
coverId = client.getProfileDetail()["result"]["objectId"]
settings["myProfile"]["coverId"] = coverId

main = codecs.open("dataku.json","r","utf-8")
imagesOpen = codecs.open("image.json","r","utf-8")
videosOpen = codecs.open("video.json","r","utf-8")
waitOpen = codecs.open("wait.json","r","utf-8")
audiosOpen = codecs.open("audio.json","r","utf-8")
images = json.load(imagesOpen)
videos = json.load(videosOpen)
wait = json.load(waitOpen)
audios = json.load(audiosOpen)
setting = json.load(main)

mulai = time.time()

def restartBot():
    print ("[ INFO ] BOT RESTART")
    python = sys.executable
    os.execl(python, python, *sys.argv)

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE") 

def logError(text):
    client.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))
def flexWel(to, text1):
#    group = client.getGroup(op.param1)
    contact = client.getContact(clientMid)
    data = {
      "messages": [
                                        {
                                            "type": "flex",
                                            "altText": "Brocast by: team ID BOTS",
                                            "contents": 
                                                {
                                                "type": "bubble",
                                                "styles": {
                                                        "body": {
                                                            "backgroundColor": "#000000",
                                                        },
                                                        "footer": {
                                                            "backgroundColor": "#000000",
                                                            "separator": True,
                                                            "separatorColor": "#6F00FF",
                                                        }
                                                    },
                                                "body": {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "contents": [
                                                        {
                                                            "type": "box",
                                                            "layout": "horizontal",
                                                            "contents": [
                                                                {
                                                                    "type": "separator",
                                                                    "color": "#7CFC00"
                                                                },
                                                                {
                                                                    "type": "image",
                                                                    "url": "https://obs.line-scdn.net/{}".format(contact.picturePath),
                                                                    "aspectRatio": "3:4",
                                                                    "aspectMode": "cover",
                                                                    "size": "lg",
                                                                    "flex": 0,
                                                                    "align": "start"
                                                                },
                                                                {
                                                                    "type": "separator",
                                                                    "color": "#7CFC00"
                                                                },
                                                                {
                                                                    "type": "text",
                                                                    "text": "╭────────────\n│   ᴾᴱᴺᴳᴵᴿᴵᴹ\n╰────────────\n     {}".format(contact.displayName),
                                                                    "wrap": True,
                                                                    "color": "#FFFF00",
                                                                    "flex": 0
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "type": "box",
                                                            "layout": "vertical",
                                                            "contents": [
                                                                {
                                                                    "type": "separator",
                                                                    "color": "#7CFC00"
                                                                },
                                                                {
                                                                    "type": "text",
                                                                    "text": "          ⚛️ ʙʀᴏᴀᴅᴄᴀsᴛ ⚛️",
                                                                    "wrap": True,
                                                                    "color": "#00FFFF",
                                                                    "size": "lg",
                                                                    "flex": 1,
                                                                    "gravity": "top"
                                                                },
                                                                {
                                                                   "type": "separator",
                                                                   "color": "#7CFC00"
                                                                },
                                                                {
                                                                   "type": "text",
                                                                   "text": text1,
                                                                   "wrap": True,
                                                                   "flex": 1,
                                                                   "color": "#00FF7F",
                                                                   "gravity": "bottom"
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                },
                                                "footer": {
                                                    "type": "box",
                                                    "layout": "horizontal",
                                                    "spacing": "none",
                                                    "contents": [
                                                        {
                                                            "type": "button",
                                                            "style": "link",
                                                            "color": "#FF4500",
                                                            "height": "sm",
                                                            "action": {
                                                              "type": "uri",
                                                              "label": "OᵂᴺᴱR",
                                                              "uri": "https://line.me/ti/p/~lovedewi1"
                                                            }
                                                        },
                                                        {
                                                            "type": "separator",
                                                            "color": "#7CFC00"
                                                         },
                                                         {
                                                            "type": "button",
                                                            "style": "link",
                                                            "height": "sm",
                                                            "color": "#EE82EE",
                                                            "action": {
                                                              "type": "uri",
                                                              "label": "cᴿᴱᴬᵀᴼR",
                                                              "uri": "https://line.me/ti/p/~id_bots"
                                                            }
                                                        },
                                                        {
                                                            "type": "spacer",
                                                            "size": "sm"
                                                        }
                                                    ],
                                                    "flex": 0
                                                }
                                            }
                                        }
        ]
    }
    sendTemplate(to, data)

def flexHelp(to, text1):
    data = {
      "messages": [
                                        {
                                            "type": "flex",
                                            "altText": "ID҉ ᴮᵒᵗˢ",
                                            "contents":
                                                {
                                                "type": "bubble",
                                                "styles": {
                                                        "header": {
                                                            "backgroundColor": "#aaffaa",
                                                        },
                                                        "body": {
                                                            "backgroundColor": "#0000ff",
                                                            "separator": True,
                                                            "separatorColor": "#ff0000"
                                                        },
                                                        "footer": {
                                                            "backgroundColor": "#FF4500",
                                                            "separator": True
                                                        }
                                                    },
                                                "header": {
                                                    "type": "box",
                                                    "layout": "horizontal",
                                                    "spacing": "xs",
                                                    "contents": [
                                                        {
                                                            "type": "text",
                                                            "align": "center",
                                                            "text": "☯ ID BOTS ☯",
                                                            "weight": "bold",
                                                            "color": "#ff0000",
                                                            "size": "xl", 
                                "action" : {
                               "type" : "uri", "uri" : "https://line.me/ti/p/~id_bots"} 
                                                        }
                                                    ]
                                                },
                                                "body": {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "contents": [
                                                        {
                                                            "type": "box",
                                                            "layout": "vertical",
                                                            "margin": "lg",
                                                            "spacing": "sm",
                                                            "contents": [
                                                                {
                                                                    "type": "box",
                                                                    "layout": "baseline",
                                                                    "spacing": "sm",
                                                                    "contents": [
                                                                        {
                                                                            "type": "text",
                                                                            "text": text1,
                                                                            "color": "#00ff00",
                                                                            "wrap": True,
                                                                            "size": "sm",
                                                                        },
                                                                    ]
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                },
                                                "footer": {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "spacing": "sm",
                                                    "contents": [
                                                                        {
                                                                            "type": "text",
                                                                            "align": "center",
                                                                            "text": "ID BOTS",
                                                                            "color": "#F0F8FF",
                                                                            "wrap": True,
                                                                            "size": "sm"
                                                                        },
                                                        {
                                                            "type": "spacer",
                                                            "size": "sm",
                                                        }
                                                    ],
                                                    "flex": 0
                                                }
                                            }
                                        }
        ],
    }
    sendTemplate(to, data)       
   
def footer(to, text):
    data = {
        "messages": [
            {
                "type": "text",
                "text": text,
                "sentBy":{"label":"ID BOTS",
                "iconUrl":'http://dl.profile.line-cdn.net/0hZpCOqIpFBV9-Ni8ohtZ6CEJzCzIJGAMXBldMOlk2WGsHABUNQAVNP18_Cz0AAxJZEldKO1w3XzpS',
                "linkUrl":"https://line.me/ti/p/~id_bots"
                }
             }
       ]
    }
    sendTemplate(to, data)       
def footersider(to, text):
    contact = client.getContact(op.param2)
    data = {
        "messages": [
            {
                "type": "text",
                "text": text,
                "sentBy":{"label":"{}".format(contact.displayName),
                "iconUrl":'http://dl.profile.line-cdn.net/{}'.format(contact.picturePath),
                "linkUrl":"https://line.me/ti/p/~id_bots"
                }
             }
       ]
    }
    sendTemplate(to, data)       


def flexWelx(to, text1):
    group = client.getGroup(op.param1)
    contact = client.getContact(op.param2)
    data = {
      "messages": [
                                        {
                                            "type": "flex",
                                            "altText": "ID BOTS",
                                            "contents": 
                                                {
                                                "type": "bubble",
                                                "styles": {
                                                        "header": {
                                                            "backgroundColor": "#FFC0CB",
                                                        }, 
                                                        "body": {
                                                            "backgroundColor": "#8F00FF",
                                                            "separator": True,
                                                            "separatorColor": "#0000FF"
                                                        }, 
                                                        "footer": {
                                                            "backgroundColor": "#6F00FF",
                                                            "separator": True
                                                        }
                                                    },
                                                "header": {
                                                    "type": "box",
                                                    "layout": "horizontal",
                                                    "contents": [
                                                        {
                                                            "type": "text",
                                                            "align": "center",
                                                            "text": "Nama: {}".format(contact.displayName),
                                                            "weight": "bold",
                                                            "color": "#BF00FF",
                                                            "size": "sm", 
                                "action" : {
                               "type" : "uri", "uri" : "https://line.me/ti/p/~id_bots"} 
                                                        }
                                                    ]
                                                },
                                                "body": {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "contents": [
                                                        {
                                                            "type": "box",
                                                            "layout": "vertical",
                                                            "margin": "lg",
                                                            "spacing": "sm",
                                                            "contents": [
                                                                {
                                                                    "type": "box",
                                                                    "layout": "baseline",
                                                                    "spacing": "sm",
                                                                    "contents": [
                                                                        {
                                                                            "type": "text",
                                                                            "text": text1,
                                                                            "color": "#00ff00",
                                                                            "wrap": True,
                                                                            "size": "sm",
                                                                        },
                                                                    ]
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                },
                                                "footer": {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "spacing": "sm",
                                                    "contents": [
                                                                        {
                                                                            "type": "text",
                                                                            "align": "center",
                                                                            "text": "Group: {}".format(str(group.name)),
                                                                            "color": "#F0F8FF",
                                                                            "wrap": True,
                                                                            "size": "sm"
                                                                        },
                                                        {
                                                            "type": "spacer",
                                                            "size": "sm",
                                                        }
                                                    ],
                                                    "flex": 0
                                                }
                                            }
                                        }
        ],
    }
    sendTemplate(to, data)
    
def flexLev(to, text1):
    group = client.getGroup(op.param1)
    contact = client.getContact(op.param2)
    data = {
      "messages": [
                                        {
                                            "type": "flex",
                                            "altText": "ID BOTS",
                                            "contents": 
                                                {
                                                "type": "bubble",
                                                "styles": {
                                                        "header": {
                                                            "backgroundColor": "#FFFF00",
                                                        }, 
                                                        "body": {
                                                            "backgroundColor": "#1C1C1C",
                                                            "separator": True,
                                                            "separatorColor": "#0000FF"
                                                        }, 
                                                        "footer": {
                                                            "backgroundColor": "#FF4500",
                                                            "separator": True
                                                        }
                                                    },
                                                "header": {
                                                    "type": "box",
                                                    "layout": "horizontal",
                                                    "contents": [
                                                        {
                                                            "type": "text",
                                                            "align": "center",
                                                            "text": "Nama: {}".format(contact.displayName),
                                                            "weight": "bold",
                                                            "color": "#FF0000",
                                                            "size": "sm", 
                                "action" : {
                               "type" : "uri", "uri" : "https://line.me/ti/p/~id_bots"} 
                                                        }
                                                    ]
                                                },
                                                "body": {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "contents": [
                                                        {
                                                            "type": "box",
                                                            "layout": "vertical",
                                                            "margin": "lg",
                                                            "spacing": "sm",
                                                            "contents": [
                                                                {
                                                                    "type": "box",
                                                                    "layout": "baseline",
                                                                    "spacing": "sm",
                                                                    "contents": [
                                                                        {
                                                                            "type": "text",
                                                                            "text": text1,
                                                                            "color": "#00ff00",
                                                                            "wrap": True,
                                                                            "size": "sm",
                                                                        },
                                                                    ]
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                },
                                                "footer": {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "spacing": "sm",
                                                    "contents": [
                                                                        {
                                                                            "type": "text",
                                                                            "align": "center",
                                                                            "text": "Group: {}".format(str(group.name)),
                                                                            "color": "#F0F8FF",
                                                                            "wrap": True,
                                                                            "size": "sm"
                                                                        },
                                                        {
                                                            "type": "spacer",
                                                            "size": "sm",
                                                        }
                                                    ],
                                                    "flex": 0
                                                }
                                            }
                                        }
        ],
    }
    sendTemplate(to, data)

def flexSmule(to, text1):
    data = {
      "messages": [
                                        {
                                            "type": "flex",
                                            "altText": "ID BOTS",
                                            "contents":
                                                {
                                                "type": "bubble",
                                                "styles": {
                                                        "header": {
                                                            "backgroundColor": "#FF4500",
                                                        },
                                                        "body": {
                                                            "backgroundColor": "#1C1C1C",
                                                            "separator": True,
                                                            "separatorColor": "#0000FF"
                                                        },
                                                        "footer": {
                                                            "backgroundColor": "#FF4500",
                                                            "separator": True
                                                        }
                                                    },
                                                "header": {
                                                    "type": "box",
                                                    "layout": "horizontal",
                                                    "contents": [
                                                        {
                                                            "type": "text",
                                                            "align": "center",
                                                            "text": "Record smule",
                                                            "weight": "bold",
                                                            "color": "#F0F8FF",
                                                            "size": "sm", 
                                "action" : {
                               "type" : "uri", "uri" : "https://line.me/ti/p/~id_bots"} 
                                                        }
                                                    ]
                                                },
                                                "body": {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "contents": [
                                                        {
                                                            "type": "box",
                                                            "layout": "vertical",
                                                            "margin": "lg",
                                                            "spacing": "sm",
                                                            "contents": [
                                                                {
                                                                    "type": "box",
                                                                    "layout": "baseline",
                                                                    "spacing": "sm",
                                                                    "contents": [
                                                                        {
                                                                            "type": "text",
                                                                            "text": text1,
                                                                            "color": "#00ff00",
                                                                            "wrap": True,
                                                                            "size": "sm",
                                                                        },
                                                                    ]
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                },
                                                "footer": {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "spacing": "sm",
                                                    "contents": [
                                                                        {
                                                                            "type": "text",
                                                                            "align": "center",
                                                                            "text": "selanjutnya ketik:\nrecord [id smule]|[nomer urut]",
                                                                            "color": "#F0F8FF",
                                                                            "wrap": True,
                                                                            "size": "sm"
                                                                        },
                                                        {
                                                            "type": "spacer",
                                                            "size": "sm",
                                                        }
                                                    ],
                                                    "flex": 0
                                                }
                                            }
                                        }
        ],
    }
    sendTemplate(to, data) 

def flexSmule1(to, text1):
    data = {
      "messages": [
                                        {
                                            "type": "flex",
                                            "altText": "ID BOTS",
                                            "contents":
                                                {
                                                "type": "bubble",
                                                "styles": {
                                                        "header": {
                                                            "backgroundColor": "#FF4500",
                                                        },
                                                        "body": {
                                                            "backgroundColor": "#1C1C1C",
                                                            "separator": True,
                                                            "separatorColor": "#0000FF"
                                                        },
                                                        "footer": {
                                                            "backgroundColor": "#FF4500",
                                                            "separator": True
                                                        }
                                                    },
                                                "header": {
                                                    "type": "box",
                                                    "layout": "horizontal",
                                                    "contents": [
                                                        {
                                                            "type": "text",
                                                            "align": "center",
                                                            "text": "D E T A I L  R E C O R D",
                                                            "weight": "bold",
                                                            "color": "#F0F8FF",
                                                            "size": "sm", 
                                "action" : {
                               "type" : "uri", "uri" : "https://line.me/ti/p/~id_bots"} 
                                                        }
                                                    ]
                                                },
                                                "body": {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "contents": [
                                                        {
                                                            "type": "box",
                                                            "layout": "vertical",
                                                            "margin": "lg",
                                                            "spacing": "sm",
                                                            "contents": [
                                                                {
                                                                    "type": "box",
                                                                    "layout": "baseline",
                                                                    "spacing": "sm",
                                                                    "contents": [
                                                                        {
                                                                            "type": "text",
                                                                            "text": text1,
                                                                            "color": "#00ff00",
                                                                            "wrap": True,
                                                                            "size": "sm",
                                                                        },
                                                                    ]
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                },
                                                "footer": {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "spacing": "sm",
                                                    "contents": [
                                                                        {
                                                                            "type": "text",
                                                                            "align": "center",
                                                                            "text": "silahkan tunggu permintaan\nsedang di proses",
                                                                            "color": "#F0F8FF",
                                                                            "wrap": True,
                                                                            "size": "sm"
                                                                        },
                                                        {
                                                            "type": "spacer",
                                                            "size": "sm",
                                                        }
                                                    ],
                                                    "flex": 0
                                                }
                                            }
                                        }
        ],
    }
    sendTemplate(to, data) 


def flexAdd(to, text1):
    data = {
      "messages": [
                                        {
                                            "type": "flex",
                                            "altText": "ID BOTS",
                                            "contents":
                                                {
                                                "type": "bubble",
                                                "styles": {
                                                        "header": {
                                                            "backgroundColor": "#FF4500",
                                                        },
                                                        "body": {
                                                            "backgroundColor": "#1C1C1C",
                                                            "separator": True,
                                                            "separatorColor": "#0000FF"
                                                        },
                                                        "footer": {
                                                            "backgroundColor": "#FF4500",
                                                            "separator": True
                                                        }
                                                    },
                                                "header": {
                                                    "type": "box",
                                                    "layout": "horizontal",
                                                    "contents": [
                                                        {
                                                            "type": "text",
                                                            "align": "center",
                                                            "text": "KLIK DISINI BUAT ORDER",
                                                            "weight": "bold",
                                                            "color": "#F0F8FF",
                                                            "size": "sm", 
                                "action" : {
                               "type" : "uri", "uri" : "https://line.me/ti/p/~id_bots"} 
                                                        }
                                                    ]
                                                },
                                                "body": {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "contents": [
                                                        {
                                                            "type": "box",
                                                            "layout": "vertical",
                                                            "margin": "lg",
                                                            "spacing": "sm",
                                                            "contents": [
                                                                {
                                                                    "type": "box",
                                                                    "layout": "baseline",
                                                                    "spacing": "sm",
                                                                    "contents": [
                                                                        {
                                                                            "type": "text",
                                                                            "text": text1,
                                                                            "color": "#00ff00",
                                                                            "wrap": True,
                                                                            "size": "sm",
                                                                        },
                                                                    ]
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                },
                                                "footer": {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "spacing": "sm",
                                                    "contents": [
                                                                        {
                                                                            "type": "text",
                                                                            "align": "center",
                                                                            "text": "ID BOTS",
                                                                            "color": "#F0F8FF",
                                                                            "wrap": True,
                                                                            "size": "sm"
                                                                        },
                                                        {
                                                            "type": "spacer",
                                                            "size": "sm",
                                                        }
                                                    ],
                                                    "flex": 0
                                                }
                                            }
                                        }
        ],
    }
    sendTemplate(to, data) 
    
def flexBro(to, text1):
#    group = client.getGroup(op.param1)
    contact = client.getContact(clientMid)
    data = {
      "messages": [
                                        {
                                            "type": "flex",
                                            "altText": "Brocast by: team ID BOTS",
                                            "contents": 
                                                {
                                                "type": "bubble",
                                                "styles": {
                                                        "body": {
                                                            "backgroundColor": "#000000",
                                                        },
                                                        "footer": {
                                                            "backgroundColor": "#000000",
                                                            "separator": True,
                                                            "separatorColor": "#6F00FF",
                                                        }
                                                    },
                                                "body": {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "contents": [
                                                        {
                                                            "type": "box",
                                                            "layout": "horizontal",
                                                            "contents": [
                                                                {
                                                                    "type": "separator",
                                                                    "color": "#7CFC00"
                                                                },
                                                                {
                                                                    "type": "image",
                                                                    "url": "https://obs.line-scdn.net/{}".format(contact.picturePath),
                                                                    "aspectRatio": "3:4",
                                                                    "aspectMode": "cover",
                                                                    "size": "lg",
                                                                    "flex": 0,
                                                                    "align": "start"
                                                                },
                                                                {
                                                                    "type": "separator",
                                                                    "color": "#7CFC00"
                                                                },
                                                                {
                                                                    "type": "text",
                                                                    "text": "╭────────────\n│   ᴾᴱᴺᴳᴵᴿᴵᴹ\n╰────────────\n     {}".format(contact.displayName),
                                                                    "wrap": True,
                                                                    "color": "#FFFF00",
                                                                    "flex": 0
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "type": "box",
                                                            "layout": "vertical",
                                                            "contents": [
                                                                {
                                                                    "type": "separator",
                                                                    "color": "#7CFC00"
                                                                },
                                                                {
                                                                    "type": "text",
                                                                    "text": "          ⚛️ ʙʀᴏᴀᴅᴄᴀsᴛ ⚛️",
                                                                    "wrap": True,
                                                                    "color": "#00FFFF",
                                                                    "size": "lg",
                                                                    "flex": 1,
                                                                    "gravity": "top"
                                                                },
                                                                {
                                                                   "type": "separator",
                                                                   "color": "#7CFC00"
                                                                },
                                                                {
                                                                   "type": "text",
                                                                   "text": text1,
                                                                   "wrap": True,
                                                                   "flex": 1,
                                                                   "color": "#00FF7F",
                                                                   "gravity": "bottom"
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                },
                                                "footer": {
                                                    "type": "box",
                                                    "layout": "horizontal",
                                                    "spacing": "none",
                                                    "contents": [
                                                        {
                                                            "type": "button",
                                                            "style": "link",
                                                            "color": "#FF4500",
                                                            "height": "sm",
                                                            "action": {
                                                              "type": "uri",
                                                              "label": "OᵂᴺᴱR",
                                                              "uri": "https://line.me/ti/p/~lovedewi1"
                                                            }
                                                        },
                                                        {
                                                            "type": "separator",
                                                            "color": "#7CFC00"
                                                         },
                                                         {
                                                            "type": "button",
                                                            "style": "link",
                                                            "height": "sm",
                                                            "color": "#EE82EE",
                                                            "action": {
                                                              "type": "uri",
                                                              "label": "cᴿᴱᴬᵀᴼR",
                                                              "uri": "https://line.me/ti/p/~id_bots"
                                                            }
                                                        },
                                                        {
                                                            "type": "spacer",
                                                            "size": "sm"
                                                        }
                                                    ],
                                                    "flex": 0
                                                }
                                            }
                                        }
        ]
    }
    sendTemplate(to, data)
def flexSid1(to, text1):
#    group = client.getGroup(op.param1)
    contact = client.getContact(op.param2)
    data = {
      "messages": [
                                        {
                                            "type": "flex",
                                            "altText": "ID BOTS",
                                            "contents": 
                                                {
                                                "type": "bubble",
                                                "styles": {
                                                        "body": {
                                                            "backgroundColor": "#40E0D0",
                                                        }
                                                    },
                                                "body": {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "contents": [
                                                        {
                                                            "type": "text",
                                                            "text": "{}".format(contact.displayName),
                                                            "color": "#EE82EE",
                                                            "wrap": True,
                                                            "flex": 1,
                                                            "gravity": "top",
                                                            "size": "sm",
                                                            "weight": "bold"
						        },
						        {
                                                            "type": "separator",
                                                            "color": "#DC143C"
                                                        },
                                                        {
                                                            "type": "text",
                                                            "text": text1,
                                                            "color": "#6A5ACD",
                                                            "wrap": True,
                                                            "flex": 1,
                                                            "gravity": "bottom",
                                                            "size": "sm",
                                                            "weight": "bold"
                                                        }
                                                    ],
                                                }
                                            }
                                        }
        ],
    }
    sendTemplate(to, data)

def flexSid2(to, text1):
#    group = client.getGroup(op.param1)
    contact = client.getContact(op.param2)
    data = {
      "messages": [
                                        {
                                            "type": "flex",
                                            "altText": "ID BOTS",
                                            "contents": 
                                                {
                                                "type": "bubble",
                                                "styles": {
                                                        "body": {
                                                            "backgroundColor": "#BC8F8F",
                                                        }
                                                    },
                                                "body": {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "contents": [
                                                        {
                                                            "type": "text",
                                                            "text": "{}".format(contact.displayName),
                                                            "color": "#FFA500",
                                                            "wrap": True,
                                                            "flex": 1,
                                                            "gravity": "top",
                                                            "size": "sm",
                                                            "weight": "bold"
						        },
						        {
                                                            "type": "separator",
                                                            "color": "#7CFC00"
                                                        },
                                                        {
                                                            "type": "text",
                                                            "text": text1,
                                                            "color": "#7B68EE",
                                                            "wrap": True,
                                                            "flex": 1,
                                                            "gravity": "bottom",
                                                            "size": "sm",
                                                            "weight": "bold"
                                                        }
                                                    ],
                                                }
                                            }
                                        }
        ],
    }
    sendTemplate(to, data)

def flexSid3(to, text1):
#    group = client.getGroup(op.param1)
    contact = client.getContact(op.param2)
    data = {
      "messages": [
                                        {
                                            "type": "flex",
                                            "altText": "ID BOTS",
                                            "contents": 
                                                {
                                                "type": "bubble",
                                                "styles": {
                                                        "body": {
                                                            "backgroundColor": "#E6E6FA",
                                                        }
                                                    },
                                                "body": {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "contents": [
                                                        {
                                                            "type": "text",
                                                            "text": "{}".format(contact.displayName),
                                                            "color": "#0000CD",
                                                            "wrap": True,
                                                            "flex": 1,
                                                            "gravity": "top",
                                                            "size": "sm",
                                                            "weight": "bold"
						        },
						        {
                                                            "type": "separator",
                                                            "color": "#7CFC00"
                                                        },
                                                        {
                                                            "type": "text",
                                                            "text": text1,
                                                            "color": "#FF0000",
                                                            "wrap": True,
                                                            "flex": 1,
                                                            "gravity": "bottom",
                                                            "size": "sm",
                                                            "weight": "bold"
                                                        }
                                                    ],
                                                }
                                            }
                                        }
        ],
    }
    sendTemplate(to, data)

def flexOff(to, text1):
#    group = client.getGroup(op.param1)
    contact = client.getContact(clientMid)
    data = {
      "messages": [
                                        {
                                            "type": "flex",
                                            "altText": "ID Bots",
                                            "contents": 
                                                {
                                                "type": "bubble",
                                                "styles": {
                                                        "body": {
                                                            "backgroundColor": "#708090",
                                                        }
                                                    },
                                                "body": {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "contents": [
                                                        {
                                                            "type": "box",
                                                            "layout": "baseline",
                                                            "contents": [
                                                                {
                                                                    "type": "icon",
                                                                    "url": "https://obs.line-scdn.net/{}".format(contact.picturePath),
                                                                    "size": "lg"
                                                                },
                                                                {
                                                                    "type": "text",
                                                                    "text": text1,
                                                                    "color": "#FFFF00",
                                                                   # "sparator": True,
                                                                    "size": "sm",
                                                                    "weight": "bold"
                                                                }
                                                            ]
                                                        }
                                                    ],
                                                }
                                            }
                                        }
        ],
    }
    sendTemplate(to, data)
 
def flexOn(to, text1):
#    group = client.getGroup(op.param1)
    contact = client.getContact(clientMid)
    data = {
      "messages": [
                                        {
                                            "type": "flex",
                                            "altText": "ID Bots",
                                            "contents": 
                                                {
                                                "type": "bubble",
                                                "styles": {
                                                        "body": {
                                                            "backgroundColor": "#008080",
                                                        }
                                                    },
                                                "body": {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "contents": [
                                                        {
                                                            "type": "box",
                                                            "layout": "baseline",
                                                            "contents": [
                                                                {
                                                                    "type": "icon",
                                                                    "url": "https://obs.line-scdn.net/{}".format(contact.picturePath),
                                                                    "size": "lg"
                                                                },
                                                                {
                                                                    "type": "text",
                                                                    "text": text1,
                                                                    "color": "#FF4500",
                                                                   # "sparator": True,
                                                                    "size": "sm",
                                                                    "weight": "bold"
                                                                }
                                                            ]
                                                        }
                                                    ],
                                                }
                                            }
                                        }
        ],
    }
    sendTemplate(to, data)

def flexCek(to, text1):
    data = {
      "messages": [
                                        {
                                            "type": "flex",
                                            "altText": "ID BOTS",
                                            "contents": 
                                                {
                                                "type": "bubble",
                                                "styles": {
                                                        "body": {
                                                            "backgroundColor": "#00FF00",
                                                        }
                                                    },
                                                "body": {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "contents": [
                                                        {
                                                            "type": "text",
                                                            "text": text1,
                                                            "color": "#FF00FF",
                                                            "size": "sm",
                                                            "wrap": True
                                                        }
                                                    ],
                                                }
                                            }
                                        }
        ],
    }
    sendTemplate(to, data)

def flexSet(to, text1):
    data = {
      "messages": [
                                        {
                                            "type": "flex",
                                            "altText": "ID BOTS",
                                            "contents": 
                                                {
                                                "type": "bubble",
                                                "styles": {
                                                        "body": {
                                                            "backgroundColor": "#0000FF",
                                                        }
                                                    },
                                                "body": {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "contents": [
                                                        {
                                                            "type": "text",
                                                            "text": text1,
                                                            "color": "#FFFFFF",
                                                            "size": "sm",
                                                            "wrap": True
                                                        }
                                                    ],
                                                }
                                            }
                                        }
        ],
    }
    sendTemplate(to, data)

def sendTemplate(to, data):
    xyzz = LiffContext(chat=LiffChatContext(to))
    view = LiffViewRequest('1562242036-RW04okm', context = xyzz)
    token = client.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Line/8.14.0',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    return _session.post(url=url, data=json.dumps(data), headers=headers)
    
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                client.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]
            
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
    

def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@airi "
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
    client.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def sendMention1(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@imamdewi "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        client.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        client.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        client.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)

def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
    
def helpmessage():
    num = 1
    if settings["setKey"] == True:
        key = settings["keyCommand"]
    else:
        key = ''
    helpMessage = "█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀\n"
    helpMessage += "▉ " + "\n"
    helpMessage += "▉" + " ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n"
    helpMessage += "▉" + " ▒ 0%i│" % num + key + " Restart\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ 0%i│" % num + key + " Runtime\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ 0%i│" % num + key + " Speed\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ 0%i│" % num + key + " About\n"
    num = (num+1)
    helpMessage += "▉" + " ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n"
    helpMessage += "▉" + " ▒ 0%i│" % num + key + " AutoAdd on/off\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ 0%i│" % num + key + " AutoJoin on/off\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ 0%i│" % num + key + " AutoLeave on/off\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ 0%i│" % num + key + " Autoread on/off\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ 0%i│" % num + key + " Respon on/off\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " welcome on/off\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " Sticker on/off\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " Unsendmsg on/off\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " Autoblock on/off\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " Leavemsg on/off\n"
    num = (num+1)
    helpMessage += "▉" + " ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n"
    helpMessage += "▉" + " ▒ %i│" % num + key + " record [id smule]\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " fs [text]\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " MyName\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " Mybio\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " Mypicture\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " Myprofilevideo\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " Mycover\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " Getcontact @\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " Getmid @\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " Getname @\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " Getbio @\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " Getpict @\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " Getprofilvideo @\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " Getcover\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " CloneProfile\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " RestoreProfile\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " Addimg text\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " Addvideo text\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " Addmp3 text\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " +sticker text\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " Dellimg text\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " Dellvideo text\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " Dellmp3 text\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " +sticker text\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " Listimage\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " Listvideo\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " Listmp3\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " daftarsticker\n"
    num = (num+1)
    helpMessage += "▉" + " ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n"
    helpMessage += "▉" + " ▒ %i│" % num + key + " GroupCreator\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " GroupId\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " GroupName\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " GroupPicture\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " GroupTicket\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " GroupTicket on/off\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " GroupList\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " GroupMemberList\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " GroupInfo\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " sepi\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " Lurking On/Off/Reset\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " Kalender\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " ngintip on/off\n"
    num = (num+1)
    helpMessage += "▉" + " ▒ %i│" % num + key + " Musik\n"
    num = (num+1)
    helpMessage += "▉ " + "▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n"
    helpMessage += "▉ " + " \n"
    helpMessage += "█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄"
    return helpMessage

def helpmessag():
    num = 1
    if settings["setKey"] == True:
        key = settings["keyCommand"]
    else:
        key = ''
    helpMessag = "█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀\n"
    helpMessag += "▉ " + "\n"
    helpMessag += "▉" + " ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n"
    helpMessag += "▉" + " ▒ 0%i│" % num + key + " setwelcome [text]\n"
    num = (num+1)
    helpMessag += "▉" + " ▒ 0%i│" % num + key + " setleave [text]\n"
    num = (num+1)
    helpMessag += "▉" + " ▒ 0%i│" % num + key + " setrespon [text]\n"
    num = (num+1)
    helpMessag += "▉" + " ▒ 0%i│" % num + key + " setsider1 [text]\n"
    num = (num+1)
    helpMessag += "▉" + " ▒ 0%i│" % num + key + " setsider2 [text]\n"
    num = (num+1)
    helpMessag += "▉" + " ▒ 0%i│" % num + key + " setsider3 text\n"
    num = (num+1)
    helpMessag += "▉" + " ▒ 0%i│" % num + key + " cek welcome\n"
    num = (num+1)
    helpMessag += "▉" + " ▒ 0%i│" % num + key + " cek leave\n"
    num = (num+1)
    helpMessag += "▉" + " ▒ 0%i│" % num + key + " cek sider1\n"
    num = (num+1)
    helpMessag += "▉" + " ▒ %i│" % num + key + " cek sider3\n"
    num = (num+1)
    helpMessag += "▉" + " ▒ %i│" % num + key + " cek respon\n"
    num = (num+1)
    helpMessag += "▉ " + "▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n"
    helpMessag += "▉ " + " \n"
    helpMessag += "█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄"
    return helpMessag
#==============================================================================#
def clientBot(op):
    try:
        if op.type == 0:
            print ("[ 0 ] END OF OPERATION")
            return

        if op.type == 5:
            print ("[ 5 ] NOTIFIED ADD CONTACT")
            if settings["autoAdd"] == True:
                aku = "u6723125e7f53d6758acb4aaa613605d0"
                client.sendMessage(op.param1, "Cie ketahuan add ya" ,contentMetadata={'MSG_SENDER_ICON': "http://dl.profile.line-cdn.net"+client.getContact(aku).picturePath,'MSG_SENDER_NAME':  '{}'.format(str(client.getContact(aku).displayName))} )
               # flexAdd(op.param1, "ID BOTS\n\nopen order bot protect\n1.protect room smule\n2.protect room chat\nprotect room event\nPLUS ANTI JS\n4.SEDIA JUGA SELFBOT ONLY\nFITUR TERUPDATE DILENGKAPI JUGA DENGAN TEMPLATE")
              #  client.sendMessage(op.param1, "http://line.me/ti/p/~id_bots" ,contentMetadata={'MSG_SENDER_ICON': "http://dl.profile.line-cdn.net"+client.getContact(op.param1).picturePath,'MSG_SENDER_NAME':  '{}'.format(str(client.getContact(op.param1).displayName))} )

        if op.type == 5:
            print ("[ 5 ] NOTIFIED AUTO BLOCK CONTACT")
            if settings["autoBlock"] == True:
                client.blockContact(op.param1)
                client.sendMessage(op.param1,"Tapi Maaf Auto Block Saya Aktif........")

        if op.type == 13:
            print ("[ 13 ] NOTIFIED INVITE INTO GROUP")
            if clientMid in op.param3:
                if settings["autoJoin"] == True:
                    client.rejectGroupInvitation(op.param1)
                   # sendMention(op.param1, "@!, group apa ini ya")

        if op.type in [22, 24]:
            print ("[ 22 And 24 ] NOTIFIED INVITE INTO ROOM & NOTIFIED LEAVE ROOM")
            if settings["autoLeave"] == True:
#                sendMention(op.param1, "maaf @!, auto leave aktif")
                client.leaveRoom(op.param1)
                
        if op.type == 15:
            print ("[ 15 ] NOTIFIED LEAVE INTO GROUP")
            if setting["leave"] == True:
                flexLev(op.param1, setting["leavemsg"])
                #client.sendContact(op.param1, op.param2)
                #client.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
        	
        if op.type == 17:
            print ("[ 17 ] NOTIFIED WELCOME INTO GROUP")
            if setting["welcome"] == True:
                #dan = client.getContact(op.param2)
                #tgb = client.getGroup(op.param1)
                flexWel(op.param1, setting["welcomemsg"])
               # client.sendContact(op.param1, op.param2)
                #client.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
#========================================================================
                if msg.contentType == 0:
                    msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                if msg.contentType == 1:
                    path = client.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
                if msg.contentType == 7:
                    stk_id = msg.contentMetadata["STKID"]
                    stk_ver = msg.contentMetadata["STKVER"]
                    pkg_id = msg.contentMetadata["STKPKGID"]
                    ret_ = "\n\n? Sticker Info ?"
                    ret_ += "\n? Sticker ID : {}".format(stk_id)
                    ret_ += "\n? Sticker Version : {}".format(stk_ver)
                    ret_ += "\n? Sticker Package : {}".format(pkg_id)
                    ret_ += "\n? Sticker Url : line://shop/detail/{}".format(pkg_id)
                    query = int(stk_id)
                    if type(query) == int:
                             data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                             path = client.downloadFileURL(data)
                             msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
                if msg.contentType == 7:
                 if settings["stickerOn"] == True:
                     stk_id = msg.contentMetadata['STKID']
                     stk_ver = msg.contentMetadata['STKVER']
                     pkg_id = msg.contentMetadata['STKPKGID']
                     with requests.session() as s:
                         s.headers['user-agent'] = 'Mozilla/5.0'
                         r = s.get("https://store.line.me/stickershop/product/{}/id".format(urllib.parse.quote(pkg_id)))
                         soup = BeautifulSoup(r.content, 'html5lib')
                         data = soup.select("[class~=mdBtn01Txt]")[0].text
                         if data == 'Lihat Produk Lain':
                             ret_ = "? Sticker Info ?"
                             ret_ += "\n? STICKER ID : {}".format(stk_id)
                             ret_ += "\n? STICKER PACKAGES ID : {}".format(pkg_id)
                             ret_ += "\n? STICKER VERSION : {}".format(stk_ver)
                             ret_ += "\n? STICKER URL : line://shop/detail/{}".format(pkg_id)
                             client.sendMessage(msg.to, str(ret_))
                             query = int(stk_id)
                             if type(query) == int:
                                data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                                path = client.downloadFileURL(data)
                                client.sendImage(msg.to,path)
                         else:
                             ret_ = "? Sticker Info ?"
                             ret_ += "\n? PRICE : "+soup.findAll('p', attrs={'class':'mdCMN08Price'})[0].text
                             ret_ += "\n? AUTHOR : "+soup.select("a[href*=/stickershop/author]")[0].text
                             ret_ += "\n? STICKER ID : {}".format(str(stk_id))
                             ret_ += "\n? STICKER PACKAGES ID : {}".format(str(pkg_id))
                             ret_ += "\n? STICKER VERSION : {}".format(str(stk_ver))
                             ret_ += "\n? STICKER URL : line://shop/detail/{}".format(str(pkg_id))
                             ret_ += "\n? DESCRIPTION :\n"+soup.findAll('p', attrs={'class':'mdCMN08Desc'})[0].text
                             client.sendMessage(msg.to, str(ret_))
                             query = int(stk_id)
                             if type(query) == int:
                                data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                                path = client.downloadFileURL(data)
                                client.sendImage(msg.to,path)
                if msg.contentType == 16:
                    if settings["autolike"]==True:
                        url_post = msg.contentMetadata['postEndUrl']
                        pliter = url_post.replace('line://home/post?userMid=','')
                        pliter = pliter.split('&postId=')
                        client.likePost(mid=pliter[0],postId=pliter[1])
                        client.createComment(mid=pliter[0],postId=pliter[1],text=settings["comment"])
                        flexOff(to,'Like Success')
                if msg.contentType == 7:
                    if msg._from in clientMid:
                        try:
                            if wait["tstiker"] == True:
                                wait["chulltikel"][wait["memproses"]] = msg.contentMetadata
                                wait["memproses"] = {}
                                wait["tstiker"] = False
                                f=codecs.open("wait.json","w","utf-8")
                                json.dump(wait, f, sort_keys=True, indent=4,ensure_ascii=False)
                                flexOff(msg.to,"Tersimpan")
                        except Exception as e:
                            client.sendMessage(msg.to,"{}".format(str(e)))
                if msg.contentType == 7:
                  if msg._from in clientMid:
                     if settings["AddstickerTag"]["status"] == True:
                         settings["AddstickerTag"]["sid"] = msg.contentMetadata["STKID"]
                         settings["AddstickerTag"]["spkg"] = msg.contentMetadata["STKPKGID"]
                         client.sendAiri(msg.id,msg.to, "Sticker respon telah di ganti")
                         settings["AddstickerTag"]["status"] = False
                if msg.contentType == 1:
                  if msg._from in clientMid:
                     if settings["Addimage"]["status"] == True:
                         path = client.downloadObjectMsg(msg.id)
                         images[settings["Addimage"]["name"]] = str(path)
                         f = codecs.open("image.json","w","utf-8")
                         json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                         client.sendAiri(msg.id,msg.to, "Berhasil menambahkan gambar {}".format(str(settings["Addimage"]["name"])))
                         settings["Addimage"]["status"] = False
                         settings["Addimage"]["name"] = ""
                if msg.contentType == 2:
                  if msg._from in clientMid:
                     if settings["Addvideo"]["status"] == True:
                         path = client.downloadObjectMsg(msg.id)
                         videos[settings["Addvideo"]["name"]] = str(path)
                         f = codecs.open("video.json","w","utf-8")
                         json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                         client.sendAiri(msg.id,msg.to, "Berhasil menambahkan video {}".format(str(settings["Addvideo"]["name"])))
                         settings["Addvideo"]["status"] = False
                         settings["Addvideo"]["name"] = ""
                if msg.contentType == 7:
                  if msg._from in clientMid:
                     if settings["Addsticker"]["status"] == True:
                         stickers[settings["Addsticker"]["name"]] = {"STKID":msg.contentMetadata["STKID"],"STKPKGID":msg.contentMetadata["STKPKGID"]}
                         f = codecs.open("sticker.json","w","utf-8")
                         json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                         client.sendAiri(msg.id,msg.to, "Berhasil menambahkan sticker {}".format(str(settings["Addsticker"]["name"])))
                         settings["Addsticker"]["status"] = False
                         settings["Addsticker"]["name"] = ""
                if msg.contentType == 3:
                  if msg._from in clientMid:
                     if settings["Addaudio"]["status"] == True:
                         path = client.downloadObjectMsg(msg.id)
                         audios[settings["Addaudio"]["name"]] = str(path)
                         f = codecs.open("audio.json","w","utf-8")
                         json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                         client.sendAiri(msg.id,msg.to, "Berhasil menambahkan mp3 {}".format(str(settings["Addaudio"]["name"])))
                         settings["Addaudio"]["status"] = False
                         settings["Addaudio"]["name"] = ""
                if msg.contentType == 0:
                  if settings["autoRead"] == True:
                      client.sendChatChecked(msg.to, msg_id)
                      print ("Read")
                  if text is None:
                      return
                  else:
                  #       for sticker in wait["chulltikel"]:
                   #       if msg._from in clientMid:
                    #        if text.lower() == sticker:
                     #          sid = stickers[text.lower()]["STKID"]
                      #         spkg = stickers[text.lower()]["STKPKGID"]
                       #        client.sendSticker(to, spkg, sid)
                         for image in images:
                          if msg._from in clientMid:
                            if text.lower() == image:
                               client.sendImage(msg.to, images[image])
                         for audio in audios:
                          if msg._from in clientMid:
                            if text.lower() == audio:
                               client.sendAudio(msg.to, audios[audio])
                         for video in videos:
                          if msg._from in clientMid:
                            if text.lower() == video:
                               client.sendVideo(msg.to, videos[video])

        if op.type in [26,25]:
            try:
                print ("[ 25 ] SEND MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                setKey = settings["keyCommand"].title()
                if settings["setKey"] == False:
                    setKey = ''
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != client.profile.mid:
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
                        else:
                            cmd = command(text)
                            if cmd == "help":
                              if msg._from in admin:
                                  helpMessage = helpmessage()
                                  flexHelp(msg.to, str(helpMessage))

                            elif cmd == "help2":
                              if msg._from in admin:
                                  helpMessag = helpmessag()
                                  flexHelp(msg.to, str(helpMessag))
                            elif cmd.startswith("changekey:"):
                              if msg._from in admin:
                                sep = text.split(" ")
                                key = text.replace(sep[0] + " ","")
                                if " " in key:
                                    client.sendAiri(msg.id,to, "Key tidak bisa menggunakan spasi")
                                else:
                                    settings["keyCommand"] = str(key).lower()
                                    client.sendAiri(msg.id,to, "Berhasil mengubah key command menjadi [ {} ]".format(str(key).lower()))
                            elif cmd == "speed" or cmd == "sp":
                              if msg._from in admin:
                                start = time.time()
                                flexOff(to, "lambat")
                                elapsed_time = time.time() - start
                                flexOn(msg.to, "{} sec".format(str(elapsed_time)))
                            elif cmd == "runtime":
                              if msg._from in admin:
                                timeNow = time.time()
                                runtime = timeNow - botStart
                                runtime = format_timestart(runtime)
                                footer(msg.to, "Bot sudah berjalan selama {}".format(str(runtime)))
                            elif cmd == "restart":
                              if msg._from in admin:
                                flexOn(msg.to, "Reboot")
                                flexOff(msg.to, "Bot has ben active")
                                restartBot()
#=====================================================================================================================================
                            elif cmd == "me":
                               contact = client.getContact(msg._from)
                               data = {
                                   "messages": [
                                      {
                                           "type": "flex",
                                           "altText": "ID BOTS",
                                           "contents": {
                                               "type": "bubble",
                                               "styles": {
                                                       "header": {
                                                           "backgroundColor": "#000000",
                                                       },
                                                       "body": {
                                                           "backgroundColor": "#000000",
                                                       },
                                                       "footer": {
                                                           "backgroundColor": "#000000",
                                                           "separator": True
                                                       }
                                                   },
                                               "header": {
                                                 "type": "box",
                                                 "layout": "vertical",
                                                 "contents": [
                                                   {
                                                     "type": "text",
                                                     "text": "{}".format(contact.displayName),
                                                     "weight": "bold",
                                                     "color": "#7CFC00",
                                                     "size": "sm",
						   }
						 ]
                                               },
                                               "hero": {
                                                       "type": "image",
                                                       "url": "https://obs.line-scdn.net/{}".format(contact.picturePath),
                                                       "size": "full",
                                                       "aspectRatio": "1.51:1",
                                                       "aspectMode": "cover",
                                               },
                                               "body": {
                                                       "type": "box",
                                                       "layout": "vertical",
                                                       "contents": [
                                                          {
                                                            "type": "box",
                                                            "layout": "vertical",
                                                            "contents": [
                                                               {
                                                                 "type": "box",
                                                                 "layout": "baseline",
                                                                 "contents": [
                                                                    {
                                                                      "type": "text",
                                                                      "text": "Dᴇᴛᴀɪʟ Pʀᴏғɪʟᴇ",
                                                                      "color": "#0000ff",
                                                                      "weight": "bold"
                                                                    }
                                                                 ]
                                                               }
                                                            ]
                                                          },
                                                          {
                                                            "type": "box",
                                                            "layout": "vertical",
                                                            "spacing": "xs",
                                                            "contents": [
                                                               {
                                                                 "type": "box",
                                                                 "layout": "horizontal",
                                                                 "contents": [
                                                                    {
                                                                      "type": "text",
                                                                      "text": "NAMA:",
                                                                      "color": "#228B22",
                                                                      "size": "xxs",
                                                                      "weight": "bold",
                                                                      "flex": 1
                                                                    },
                                                                    {
                                                                      "type": "text",
                                                                      "text": "{}".format(contact.displayName),
                                                                      "color": "#FF4500",
                                                                      "size": "sm",
                                                                      "wrap": True,
                                                                      "flex": 3
                                                                    }
                                                                 ]
                                                               }
                                                            ]
                                                          },
                                                          {
                                                            "type": "box",
                                                            "layout": "vertical",
                                                            "spacing": "xs",
                                                            "contents": [
                                                               {
                                                                 "type": "box",
                                                                 "layout": "horizontal",
                                                                 "contents": [
                                                                    {
                                                                      "type": "text",
                                                                      "text": "BIO:",
                                                                      "color": "#ff0000",
                                                                      "size": "xxs",
                                                                      "weight": "bold",
                                                                      "flex": 1
                                                                    },
                                                                    {
                                                                      "type": "text",
                                                                      "text": "{}".format(contact.statusMessage),
                                                                      "color": "#4B0082",
                                                                      "size": "sm",
                                                                      "wrap": True,
                                                                      "flex": 3
                                                                    }
                                                                 ]
                                                               }
                                                            ]
                                                          }
                                                       ]
                                               },
                                               "footer": {
                                                       "type": "box",
                                                       "layout": "horizontal",
                                                       "spacing": "none",
                                                       "contents": [
                                                           {
                                                               "type": "button",
			                                       "style": "link",
		                                               "color": "#FF4500",
							       "height": "sm",
                                                               "action": {
                                                                 "type": "uri",
                                                                 "label": "OʷᶰᵉR",
                                                                 "uri": "http://line.me/ti/p/~lovedewi1"
                                                               }
                                                           },
							   {
						               "type": "separator",
					                       "color": "#7CFC00"
						           },
							   {
							       "type": "button",
                                                               "style": "link",
                                                               "height": "sm",
                                                               "color": "#EE82EE",
                                                               "action": {
                                                                 "type": "uri",
                                                                 "label": "CʳᵉᵃᵗᵒR",
                                                                 "uri": "https://line.me/ti/p/~id_bots"
							       }
						           },
							   {
						               "type": "spacer",
						               "size": "sm"
							   }
                                                       ],
						       "flex": 0
                                               }
                                           }
                                      }
                                   ]
                               }
                               sendTemplate(to, data)
#====================================================================================================================================
                            elif cmd == "autoadd on":
                              if msg._from in admin:
                                settings["autoAdd"] = True
                                flexOn(msg.to, "auto add di aktifkan")
                            elif cmd == "autoadd off":
                              if msg._from in admin:
                                settings["autoAdd"] = False
                                flexOff(msg.to, "Berhasil menonaktifkan auto add")
                            elif cmd == "autojoin on":
                              if msg._from in admin:
                                settings["autoJoin"] = True
                                flexOn(msg.to, "Berhasil mengaktifkan auto join")
                            elif cmd == "autojoin off":
                              if msg._from in admin:
                                settings["autoJoin"] = False
                                flexOff(msg.to, "Berhasil menonaktifkan auto join")
                            elif cmd == "autoblock on":
                              if msg._from in admin:
                                settings["autoBlock"] = True
                                flexOn(msg.to, "Berhasil mengaktifkan auto Block")
                            elif cmd == "autoblock off":
                              if msg._from in admin:
                                settings["autoBlock"] = False
                                flexOff(msg.to, "Berhasil menonaktifkan auto Block")
                            elif cmd == "autoleave on":
                              if msg._from in admin:
                                settings["autoLeave"] = True
                                flexOn(msg.to, "Berhasil mengaktifkan auto leave")
                            elif cmd == "autoleave off":
                              if msg._from in admin:
                                settings["autoLeave"] = False
                                flexOff(msg.id,to, "Berhasil menonaktifkan auto leave")
                            elif cmd == "welcome on":
                              if msg._from in admin:
                                setting["welcome"] = True
                                flexOn(msg.to, "Berhasil mengaktifkan welcome")
                            elif cmd == "welcome off":
                              if msg._from in admin:
                                setting["welcome"] = False
                                flexOff(msg.to, "Berhasil menonaktifkan welcome")
                            elif cmd == "leavemsg on":
                              if msg._from in admin:
                                setting["leave"] = True
                                flexOn(msg.to, "Berhasil mengaktifkan leavemsg")
                            elif cmd == "leavemsg off":
                              if msg._from in admin:
                                setting["leave"] = False
                                flexOff(msg.to, "Berhasil menonaktifkan leavemsg")
                            elif cmd == "respon on":
                              if msg._from in admin:
                                setting["autorespon"] = True
                                footer(msg.to, "Berhasil mengaktifkan auto respon")
                            elif cmd == "respon off":
                              if msg._from in admin:
                                setting["autorespon"] = False
                                footer(msg.to, "Berhasil menonaktifkan auto respon")
                            elif cmd == "autoread on":
                              if msg._from in admin:
                                settings["autoRead"] = True
                                flexOn(msg.to, "Berhasil mengaktifkan auto read")
                            elif cmd == "autoread off":
                              if msg._from in admin:
                                settings["autoRead"] = False
                                flexOff(msg.to, "Berhasil menonaktifkan auto read")
                            elif cmd == "autojointicket on":
                              if msg._from in admin:
                                settings["autoJoinTicket"] = True
                                flexOn(msg.to, "Berhasil mengaktifkan auto join by ticket")
                            elif cmd == "autojointicket off":
                              if msg._from in admin:
                                settings["autoJoinTicket"] = False
                                flexOff(msg.id,to, "Berhasil menonaktifkan auto join by ticket")
                            elif cmd == "checkcontact on":
                              if msg._from in admin:
                                settings["checkContact"] = True
                                flexOn(msg.to, "Berhasil mengaktifkan check details contact")
                            elif cmd == "checkcontact off":
                              if msg._from in admin:
                                settings["checkContact"] = False
                                flexOff(msg.to, "Berhasil menonaktifkan check details contact")
                            elif cmd == "checkpost on":
                              if msg._from in admin:
                                settings["checkPost"] = True
                                flexOn(msg.to, "Berhasil mengaktifkan check details post")
                            elif cmd == "checkpost off":
                              if msg._from in admin:
                                settings["checkPost"] = False
                                flexOff(msg.to, "Berhasil menonaktifkan check details post")
                            elif cmd == "checksticker on":
                              if msg._from in admin:
                                settings["checkSticker"] = True
                                flexOn(msg.to, "Berhasil mengaktifkan check details sticker")
                            elif cmd == "checksticker off":
                              if msg._from in admin:
                                settings["checkSticker"] = False
                                flexOff(msg.to, "Berhasil menonaktifkan check details sticker")
                            elif cmd == "unsendmsg on":
                              if msg._from in admin:
                                settings["unsendMessage"] = True
                                flexOff(msg.to, "Berhasil mengaktifkan unsend message")
                            elif cmd == "unsendmsg off":
                              if msg._from in admin:
                                settings["unsendMessage"] = False
                                flexOn(msg.to, "Berhasil menonaktifkan unsend message")
                            elif cmd == "stickerku on":
                              if msg._from in admin:
                                setting["stickerku"] = True
                                flexOn(msg.to, "sticker di aktifkan")
                            elif cmd == "stickerku off":
                              if msg._from in admin:
                                setting["stickerku"] = False
                                flexOff(msg.to, "sticker di nonaktifkan")
                            elif cmd == "settings":
                              if msg._from in admin:
                                try:
                                    ret_ = "\n▄▄▄▄▄▄▄▄▄▄\n\n"
                                    if settings["autoAdd"] == True: ret_ += "ꗃ Autoadd\n"
                                    else: ret_ += "🔒 Autoadd\n"
                                    if settings["autoBlock"] == True: ret_ += "ꗃ Autoblock\n"
                                    else: ret_ += "🔒 Autoblock\n"
                                    if settings["autoJoin"] == True: ret_ += "ꗃ Autojoin\n"
                                    else: ret_ += "🔒 Autojoin\n"
                                    if settings["autoLeave"] == True: ret_ += "ꗃ Autoleave\n"
                                    else: ret_ += "🔒 Autoleave\n"
                                    if setting["welcome"] == True: ret_ += "ꗃ Welcome\n"
                                    else: ret_ += "🔒 Welcome\n"
                                    if setting["leave"] == True: ret_ += "ꗃ Leavemsg\n"
                                    else: ret_ += "🔒 Leavemsg\n"
                                    if settings["autoJoinTicket"] == True: ret_ += "ꗃ Autojointicket\n"
                                    else: ret_ += "🔒 Autojointicket\n"
                                    if settings["autoRead"] == True: ret_ += "ꗃ Autoread\n"
                                    else: ret_ += "🔒 Autoread\n"
                                    if setting["autorespon"] == True: ret_ += "ꗃ Respon\n"
                                    else: ret_ += "🔒 Respon\n"
                                    if settings["checkContact"] == True: ret_ += "ꗃ Checkcontact\n"
                                    else: ret_ += "🔒 Checkcontact\n"
                                    if settings["checkPost"] == True: ret_ += "ꗃ Checkpost\n"
                                    else: ret_ += "🔒 Checkpost\n"
                                    if settings["checkSticker"] == True: ret_ += "ꗃ Sticker\n"
                                    else: ret_ += "🔒 Sticker\n"
                                    if settings["setKey"] == True: ret_ += "ꗃ Setkey\n"
                                    else: ret_ += "🔒 Setkey\n"
                                    if settings["unsendMessage"] == True: ret_ += "ꗃ Unsendmsg\n"
                                    else: ret_ += " Unsendmsg\n"
                                    ret_ += "\n\n▄▄▄▄▄▄▄▄▄▄"
                                    flexHelp(msg.to, str(ret_))
                                except Exception as e:
                                    client.sendMessage(msg.to, str(e))
#=====================================================================================================================================
#=====================================================================================================================================
                           # elif cmd == "cs":
                                #client.sendContact(to, "ube187443474747c3ec352e7efeb48c1b',")
                            elif cmd.startswith("changename:"):
                              if msg._from in admin:
                                sep = text.split(" ")
                                string = text.replace(sep[0] + " ","")
                                if len(string) <= 1000:
                                    profile = client.getProfile()
                                    profile.displayName = string
                                    client.updateProfile(profile)
                                    flexOn(msg.to,"Succes change to {}".format(str(string)))
                            elif cmd.startswith("changebio:"):
                              if msg._from in admin:
                                sep = text.split(" ")
                                string = text.replace(sep[0] + " ","")
                                if len(string) <= 500:
                                    profile = client.getProfile()
                                    profile.statusMessage = string
                                    client.updateProfile(profile)
                                    client.sendAiri(msg.id,to,"Succes change to {}".format(str(string)))
                            elif cmd.startswith("addimg"):
                              if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in images:
                                    settings["Addimage"]["status"] = True
                                    settings["Addimage"]["name"] = str(name.lower())
                                    images[str(name.lower())] = ""
                                    f = codecs.open("image.json","w","utf-8")
                                    json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    client.sendAiri(msg.id,to, "Silahkan kirim fotonya...")
                                else:
                                    client.sendAiri(msg.id,to, "Foto itu sudah dalam list")

                            elif cmd.startswith("dellimg"):
                              if msg._from in admin:
                               sep = text.split(" ")
                               name = text.replace(sep[0] + " ","")
                               name = name.lower()
                               if name in images:
                                   client.deleteFile(images[str(name.lower())])
                                   del images[str(name.lower())]
                                   f = codecs.open("image.json","w","utf-8")
                                   json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                   client.sendAiri(msg.id,to, "Berhasil menghapus {}".format( str(name.lower())))
                               else:
                                   client.sendAiri(msg.id,to, "Foto itu tidak ada dalam list")

                            elif cmd == "listimage":
                              if msg._from in admin:
                                no = 0
                                ret_ = "Daftar Image\n\n"
                                for image in images:
                                    no += 1
                                    ret_ += str(no) + ". " + image.title() + "\n"
                                ret_ += "\nTotal {} Images".format(str(len(images)))
                                client.sendAiri(msg.id,to, ret_)
#=========== [ Add Video ] ============#                               
                            elif cmd.startswith("addvideo "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in videos:
                                    settings["Addvideo"]["status"] = True
                                    settings["Addvideo"]["name"] = str(name.lower())
                                    videos[str(name.lower())] = ""
                                    f = codecs.open("video.json","w","utf-8")
                                    json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    client.sendAiri(msg.id,to, "Silahkan kirim videonya...") 
                                else:
                                    client.sendAiri(msg.id,to, "Video itu sudah dalam list") 
                                
                            elif cmd.startswith("dellvideo "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name in videos:
                                    client.deleteFile(videos[str(name.lower())])
                                    del videos[str(name.lower())]
                                    f = codecs.open("video.json","w","utf-8")
                                    json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    client.sendAiri(msg.id,to, "Berhasil menghapus video {}".format( str(name.lower())))
                                else:
                                    client.sendAiri(msg.id,to, "Video itu tidak ada dalam list") 
                                 
                            elif cmd == "listvideo":
                              if msg._from in admin:
                                no = 0
                                ret_ = " Daftar Video \n\n"
                                for video in videos:
                                    no += 1
                                    ret_ += str(no) + ". " + video.title() + "\n"
                                ret_ += "\nTotal {} Videos".format(str(len(videos)))
                                client.sendAiri(msg.id,to, ret_)
#=========== [ Add Video ] ============#                               
                            elif cmd.startswith("addmp3 "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in audios:
                                    settings["Addaudio"]["status"] = True
                                    settings["Addaudio"]["name"] = str(name.lower())
                                    audios[str(name.lower())] = ""
                                    f = codecs.open("audio.json","w","utf-8")
                                    json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    flexOn(msg.to, "Silahkan kirim mp3 nya...") 
                                else:
                                    flexOff(msg.to, "Mp3 itu sudah dalam list") 
                                
                            elif cmd.startswith("dellmp3 "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name in audios:
                                    client.deleteFile(audios[str(name.lower())])
                                    del audios[str(name.lower())]
                                    f = codecs.open("audio.json","w","utf-8")
                                    json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    flexOn(msg.to, "Berhasil menghapus mp3 {}".format( str(name.lower())))
                                else:
                                    flexOff(msg.to, "Mp3 itu tidak ada dalam list") 
                                 
                            elif cmd == "listmp3":
                              if msg._from in admin:
                                no = 0
                                ret_ = " Daftar Lagu \n\n"
                                for audio in audios:
                                    no += 1
                                    ret_ += str(no) + ". " + audio.title() + "\n"
                                ret_ += "\nTotal {} Lagu".format(str(len(audios)))
                                client.sendAiri(msg.id,to, ret_)
#=========== [ Add Sticker ] ============#                                            
                            elif cmd.startswith("+sticker "):
                              if msg._from in admin:
                                proses = text.split(" ")
                                nama = text.replace(proses[0] + " ","")
                                try:
                                    if nama in wait["chulltikel"]:
                                        flexOn(msg.to,"Nama tersebut sudah ada")
                                    else:
                                        wait["memproses"] = nama
                                        wait["tstiker"] = True
                                        f=codecs.open("wait.json","w","utf-8")
                                        json.dump(wait, f, sort_keys=True, indent=4,ensure_ascii=False)
                                        flexOn(msg.to,"Kirim stikernya")
                                except Exception as e:
                                    flexOff(msg.to,"{}".format(str(e)))
                                    
                            elif cmd.startswith("-sticker "):
                              if msg._from in admin:
                                proses = text.split(" ")
                                nama = text.replace(proses[0] + " ","")
                                try:
                                    if nama not in wait["chulltikel"]:
                                        flexOn(msg.to,"Nama tersebut tidak ada")
                                    else:
                                        del wait["chulltikel"][nama]
                                        f=codecs.open("wait.json","w","utf-8")
                                        json.dump(wait, f, sort_keys=True, indent=4,ensure_ascii=False)
                                        flexOn(msg.to,"Stiker terhapus")
                                except Exception as e:
                                    flexOff(msg.id,to,"{}".format(str(e)))
                                    
                            elif cmd.startswith("daftarsticker"):
                              if msg._from in admin:
                                if wait["chulltikel"] == {}:
                                    footer(msg.to,"Stiker belum ada")
                                else:
                                    no = 0
                                    hasil = "List\n"
                                    for a in wait["chulltikel"]:
                                        no += 1
                                        hasil += "\n" +str(no)+". " +str(a)
                                        hasil += "\n\nTotal %i Stiker" % len(wait["chulltikel"])
                                    flexHelp(msg.to, hasil)
                            elif text.lower() in wait["chulltikel"]:
                             #   if msg._from in admin:
                                    query = wait["chulltikel"][text.lower()]["STKID"]
                                    spkg = wait["chulltikel"][text.lower()]["STKPKGID"]
                                    sticker = requests.get('https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/IOS/sticker_animation@2x.png').text
                                    if sticker == "404 Not Found":
                                       data = {
                                          "messages": [{
                                              "type": "template",
                                              "altText": "{} menghapus anda dari group".format(client.getContact(msg._from).displayName),
                                              "baseSize": {
                                                  "height": 1040, 
                                                  "width": 1040 
                                              }, 
                                              "template": {
                                                  "type": "image_carousel",
                                                  "imageAspectRatio": "square",
                                                  "imageSize": "cover",
                                                  "columns": [{
                                                      "imageUrl": 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png',
                                                      "action": {
                                                          "type": "uri",
                                                          "uri": "line://shop/detail/{}".format(spkg),
                                                          "area": {
                                                              "x": 520,
                                                              "y": 0,
                                                              "width": 520,
                                                              "height": 1040
                                                          }
                                                      }
                                                  }]
                                              }
                                          }]
                                       }
                                       sendTemplate(to, data)
                                    else:
                                       data = {
                                          "messages": [{
                                              "type": "template",
                                              "altText": "{} menghapus anda dari group".format(client.getContact(msg._from).displayName),
                                              "baseSize": {
                                                  "height": 1040, 
                                                  "width": 1040 
                                              }, 
                                              "template": {
                                                  "type": "image_carousel",
                                                  "imageAspectRatio": "square",
                                                  "imageSize": "cover",
                                                  "columns": [{
                                                      "imageUrl": 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/IOS/sticker_animation@2x.png',
                                                      "action": {
                                                          "type": "uri",
                                                          "uri": "line://shop/detail/{}".format(spkg),
                                                          "area": {
                                                              "x": 520,
                                                              "y": 0,
                                                              "width": 520,
                                                              "height": 1040
                                                          }
                                                      }
                                                  }]
                                              }
                                          }]
                                       }
                                       sendTemplate(to, data)
#=============Add/Del File==================
                            elif cmd == "refresh" or text.lower() == 'refresh':
                              if msg._from in admin:
                                settings["AddstickerTag"] = False
                                settings["Addsticker"] = False
                                settings["Addaudio"] = False
                                settings["Addimage"] = False
                                settings["Addvideo"] = False
                                settings["AddstickerTag"] = False
                                client.sendAiri(msg.id,to, "All refresh")

                           # elif cmd == "me":
                            #    client.sendAiri(msg.i)
                             #   client.sendContact(to, sender)

                            elif cmd == "mid":
                                footer(msg.to, "{}".format(sender))
                            elif cmd == "myname":
                              if msg._from in admin:
                                contact = client.getContact(sender)
                                client.sendMessage(to, "Name :{}".format(contact.displayName))
                            elif cmd == "mybio":
                              if msg._from in admin:
                                contact = client.getContact(sender)
                                client.sendMessage(to, "Status :{}".format(contact.statusMessage))
                            elif cmd == "mypicture":
                              if msg._from in admin:
                                contact = client.getContact(sender)
                                client.sendImageWithURL(to,"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                            elif cmd == "myvideoprofile":
                              if msg._from in admin:
                                contact = client.getContact(sender)
                                client.sendVideoWithURL(to,"http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))
                            elif cmd == "mycover":
                              if msg._from in admin:
                                channel = client.getProfileCoverURL(sender)          
                                path = str(channel)
                                client.sendImageWithURL(to, path)
                            elif cmd == "responsticker":
                              if msg._from in admin:
                                settings["AddstickerTag"]["status"] = True
                                settings["AddstickerTag"]["sid"] = ""
                                settings["AddstickerTag"]["spkg"] = ""
                                settings["AddstickerTag"]["sver"] = ""
                                client.sendAiri(msg.id,to, "please send a sticker if you want to add")
                            elif cmd.startswith("cloneprofile "):
                              if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        client.cloneContactProfile(ls)
                                        client.sendAiri(msg.id,to, "Berhasil mengclone profile {}".format(contact.displayName))
                            elif cmd == "restoreprofile":
                              if msg._from in admin:
                                try:
                                    clientProfile = client.getProfile()
                                    clientProfile.displayName = str(settings["myProfile"]["displayName"])
                                    clientProfile.statusMessage = str(settings["myProfile"]["statusMessage"])
                                    clientProfile.pictureStatus = str(settings["myProfile"]["pictureStatus"])
                                    client.updateProfileAttribute(8, clientProfile.pictureStatus)
                                    client.updateProfile(clientProfile)
                                    coverId = str(settings["myProfile"]["coverId"])
                                    client.updateProfileCoverById(coverId)
                                    client.sendAiri(msg.id,to, "Berhasil restore profile tunggu beberapa saat sampai profile berubah")
                                except Exception as e:
                                    client.sendAiri(msg.id,to, "Gagal restore profile")
                                    logError(error)
                            elif cmd == "backupprofile":
                              if msg._from in admin:
                                try:
                                    profile = client.getProfile()
                                    settings["myProfile"]["displayName"] = str(profile.displayName)
                                    settings["myProfile"]["statusMessage"] = str(profile.statusMessage)
                                    settings["myProfile"]["pictureStatus"] = str(profile.pictureStatus)
                                    coverId = client.getProfileDetail()["result"]["objectId"]
                                    settings["myProfile"]["coverId"] = str(coverId)
                                    client.sendAiri(msg.id,to, "Berhasil backup profile")
                                except Exception as e:
                                    client.sendAiri(msg.id,to, "Gagal backup profile")
                                    logError(error)
                            elif cmd.startswith("stealmid "):
                              if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    ret_ = "[ Mid User ]"
                                    for ls in lists:
                                        ret_ += "\n{}".format(str(ls))
                                    client.sendAiri(msg.id,to, str(ret_))
                            elif cmd.startswith("stealname "):
                              if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        client.sendMessage(to, "[ Display Name ]\n{}".format(str(contact.displayName)))
                            elif cmd.startswith("stealbio "):
                              if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        client.sendMessage(to, "[ Status Message ]\n{}".format(str(contact.statusMessage)))
                            elif cmd.startswith("stealpicture"):
                              if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        path = "http://dl.profile.line.naver.jp/{}".format(contact.pictureStatus)
                                        client.sendImageWithURL(to, str(path))
                            elif cmd.startswith("stealvideoprofile "):
                              if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        path = "http://dl.profile.line.naver.jp/{}/vp".format(contact.pictureStatus)
                                        client.sendVideoWithURL(to, str(path))
                            elif cmd.startswith("stealcover "):
                              if msg._from in admin:
                                if client != None:
                                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for ls in lists:
                                            channel = client.getProfileCoverURL(ls)
                                            path = str(channel)
                                            client.sendImageWithURL(to, str(path))
#=====================================================================================================================================
#=====================================================================================================================================
                            elif cmd == 'groupcreator':
                              if msg._from in admin:
                                group = client.getGroup(to)
                                GS = group.creator.mid
                                client.sendContact(to, GS)
                            elif cmd == 'groupid':
                              if msg._from in admin:
                                gid = client.getGroup(to)
                                client.sendAiri(msg.id,to, "[ID Group : ]\n" + gid.id)
                            elif cmd == 'grouppicture':
                              if msg._from in admin:
                                group = client.getGroup(to)
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                client.sendImageWithURL(to, path)
                            elif cmd == 'groupname':
                              if msg._from in admin:
                                gid = client.getGroup(to)
                                client.sendMessage(to, "[Nama Group : ]\n" + gid.name)
                            elif cmd == 'groupticket':
                              if msg._from in admin:
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    if group.preventedJoinByTicket == False:
                                        ticket = client.reissueGroupTicket(to)
                                        client.sendMessage(to, "[ Group Ticket ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                                    else:
                                        client.sendMessage(to, "Grup qr tidak terbuka silahkan buka terlebih dahulu dengan perintah {}openqr".format(str(settings["keyCommand"])))
                            elif cmd == 'groupticket on':
                              if msg._from in admin:
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    if group.preventedJoinByTicket == False:
                                        client.sendMessage(to, "Grup qr sudah terbuka")
                                    else:
                                        group.preventedJoinByTicket = False
                                        client.updateGroup(group)
                                        client.sendMessage(to, "Berhasil membuka grup qr")
                            elif cmd == 'groupticket off':
                              if msg._from in admin:
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    if group.preventedJoinByTicket == True:
                                        client.sendMessage(to, "Grup qr sudah tertutup")
                                    else:
                                        group.preventedJoinByTicket = True
                                        client.updateGroup(group)
                                        client.sendMessage(to, "Berhasil menutup grup qr")
                            elif cmd == 'groupinfo':
                              if msg._from in admin:
                                group = client.getGroup(to)
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if group.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(client.reissueGroupTicket(group.id)))
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                ret_ = "╔══[ Group Info ]"
                                ret_ += "\n╠ Nama Group : {}".format(str(group.name))
                                ret_ += "\n╠ ID Group : {}".format(group.id)
                                ret_ += "\n╠ Pembuat : {}".format(str(gCreator))
                                ret_ += "\n╠ Jumlah Member : {}".format(str(len(group.members)))
                                ret_ += "\n╠ Jumlah Pending : {}".format(gPending)
                                ret_ += "\n╠ Group Qr : {}".format(gQr)
                                ret_ += "\n╠ Group Ticket : {}".format(gTicket)
                                ret_ += "\n╚══[ Finish ]"
                                client.sendAiri(msg.id,to, str(ret_))
                                client.sendImageWithURL(to, path)
                            elif cmd == 'groupmemberlist':
                              if msg._from in admin:
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    ret_ = "╔══[ Member List ]"
                                    no = 0 + 1
                                    for mem in group.members:
                                        ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                                        no += 1
                                    ret_ += "\n╚══[ Total {} ]".format(str(len(group.members)))
                                    flexCek(msg.id,to, str(ret_))
                            elif cmd == 'grouplist':
                              if msg._from in admin:
                                    groups = client.groups
                                    ret_ = "╔══[ Group List ]"
                                    no = 0 + 1
                                    for gid in groups:
                                        group = client.getGroup(gid)
                                        ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                                        no += 1
                                    ret_ += "\n╚══[ Total {} Groups ]".format(str(len(groups)))
                                    flexCek(msg.id,to, str(ret_))
                            elif cmd.startswith ('call '):
                            	if msg.toType == 2:
                            		sep = text.split(" ")
                            		strnum = text.replace(sep[0] + " ","")
                            		num = int(strnum)
                            		group = client.getGroup(to)
                            		path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                            		gTicket = "https://line.me/R/ti/g/{}".format(str(client.reissueGroupTicket(group.id)))
                                  #  client.sendAiri(msg.id,to, "Sukses Boss")
                            		for var in range(0,num):
                            			members = [mem.mid for mem in group.members]
                            			client.inviteIntoGroupCall(to, contactIds=members)
                                    
#=====================================================================================================================================
#=====================================================================================================================================
                            elif cmd == "changepictureprofile":
                              if msg._from in admin:
                                settings["changePictureProfile"] = True
                                client.sendAiri(msg.id,to, "Silahkan kirim gambarnya")
                            elif cmd == "changegrouppicture.":
                                if msg.toType == 2:
                                    if to not in settings["changeGroupPicture"]:
                                        settings["changeGroupPicture"].append(to)
                                    client.sendAiri(msg.id,to, "Silahkan kirim gambarnya")
                            elif cmd == 'sepi':
                              if msg._from in admin:
                                group = client.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                k = len(nama)//20
                                for a in range(k+1):
                                    txt = u''
                                    s=0
                                    b=[]
                                    for i in group.members[a*20 : (a+1)*20]:
                                        b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                        s += 7
                                        txt += u'@airi \n'
                                      #  anu = text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0))
                                   # client.sendAiri(msg.id,to, anu)
                                    client.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                                  #i  client.sendMessage(to, "Total {} Mention".format(str(len(nama))))  
                            elif cmd == "lurking on":
                              if msg._from in admin:
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if receiver in read['readPoint']:
                                    try:
                                        del read['readPoint'][receiver]
                                        del read['readMember'][receiver]
                                        del read['readTime'][receiver]
                                    except:
                                        pass
                                    read['readPoint'][receiver] = msg_id
                                    read['readMember'][receiver] = ""
                                    read['readTime'][receiver] = readTime
                                    read['ROM'][receiver] = {}
                                    client.sendMessage(receiver,"Lurking telah diaktifkan")
                                else:
                                    try:
                                        del read['readPoint'][receiver]
                                        del read['readMember'][receiver]
                                        del read['readTime'][receiver]
                                    except:
                                        pass
                                    read['readPoint'][receiver] = msg_id
                                    read['readMember'][receiver] = ""
                                    read['readTime'][receiver] = readTime
                                    read['ROM'][receiver] = {}
                                    client.sendMessage(receiver,"Set reading point : \n" + readTime)
                            elif cmd == "lurking off":
                              if msg._from in admin:
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if receiver not in read['readPoint']:
                                    client.sendMessage(receiver,"Lurking telah dinonaktifkan")
                                else:
                                    try:
                                        del read['readPoint'][receiver]
                                        del read['readMember'][receiver]
                                        del read['readTime'][receiver]
                                    except:
                                        pass
                                    client.sendMessage(receiver,"Delete reading point : \n" + readTime)
        
                            elif cmd == "lurking reset":
                              if msg._from in admin:
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
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
                                        del read["ROM"][msg.to]
                                    except:
                                        pass
                                    read['readPoint'][receiver] = msg_id
                                    read['readMember'][receiver] = ""
                                    read['readTime'][receiver] = readTime
                                    read['ROM'][receiver] = {}
                                    client.sendMessage(msg.to, "Reset reading point : \n" + readTime)
                                else:
                                    client.sendMessage(msg.to, "Lurking belum diaktifkan ngapain di reset?")
                                    
                            elif cmd == "lurking":
                              if msg._from in admin:
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if receiver in read['readPoint']:
                                    if read["ROM"][receiver].items() == []:
                                        client.sendMessage(receiver,"Tidak Ada Sider")
                                    else:
                                        chiya = []
                                        for rom in read["ROM"][receiver].items():
                                            chiya.append(rom[1])
                                        cmem = client.getContacts(chiya) 
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = '[tukang ngintip ]\n'
                                    for x in range(len(cmem)):
                                        xname = str(cmem[x].displayName)
                                        pesan = ''
                                        pesan2 = pesan+"@c\n"
                                        xlen = str(len(zxc)+len(xpesan))
                                        xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                        zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                    text = xpesan+ zxc + "\n" + readTime
                                    try:
                                        client.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    except Exception as error:
                                        print (error)
                                    pass
                                else:
                                    client.sendMessage(receiver,"Lurking belum diaktifkan")
                            elif cmd.startswith("mimicadd"):
                              if msg._from in admin:
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:
                                        settings["mimic"]["target"][target] = True
                                        client.sendAiri(msg.id,msg.to,"Target ditambahkan!")
                                        break
                                    except:
                                        client.sendAiri(msg.id,msg.to,"Gagal menambahkan target")
                                        break
                            elif cmd.startswith("mimicdel"):
                              if msg._from in admin:
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:
                                        del settings["mimic"]["target"][target]
                                        client.sendAiri(msg.id,msg.to,"Target dihapuskan!")
                                        break
                                    except:
                                        client.sendAiri(msg.id,msg.to,"Gagal menghapus target")
                                        break
                                    
                            elif cmd == "mimiclist":
                              if msg._from in admin:
                                if settings["mimic"]["target"] == {}:
                                    client.sendMessage(msg.to,"Tidak Ada Target")
                                else:
                                    mc = "╔══[ Mimic List ]"
                                    for mi_d in settings["mimic"]["target"]:
                                        mc += "\n╠ "+client.getContact(mi_d).displayName
                                    mc += "\n╚══[ Finish ]"
                                    client.sendAiri(msg.id,msg.to,mc)
                                
                            elif cmd.startswith("mimic"):
                              if msg._from in admin:
                                sep = text.split(" ")
                                mic = text.replace(sep[0] + " ","")
                                if mic == "on":
                                    if settings["mimic"]["status"] == False:
                                        settings["mimic"]["status"] = True
                                        client.sendAiri(msg.id,msg.to,"Reply Message on")
                                elif mic == "off":
                                    if settings["mimic"]["status"] == True:
                                        settings["mimic"]["status"] = False
                                        client.sendAiri(msg.id,msg.to,"Reply Message off")
                            elif cmd == "ngintip on":
                              if msg._from in admin:
                                try:
                                    del cctv['point'][msg.to]
                                    del cctv['sidermem'][msg.to]
                                    del cctv['cyduk'][msg.to]
                                except:
                                    pass
                                cctv['point'][msg.to] = msg.id
                                cctv['sidermem'][msg.to] = ""
                                cctv['cyduk'][msg.to]=True
                                flexOn(msg.to,"tukang ngintip masuklah ")

                            elif cmd == "ngintip off":
                              if msg._from in admin:
                                if msg.to in cctv['point']:
                                    cctv['cyduk'][msg.to]=False
                                    flexOff(msg.to, "cctv di off kan")
                                else:
                                    flexOn(msg.to," Sider Belum On ")
                            

#=====================================================================================================================================
#===================================================================================================================================
                            elif cmd.startswith("checkwebsite"):
                              if msg._from in admin:
                                try:
                                    sep = text.split(" ")
                                    query = text.replace(sep[0] + " ","")
                                    r = requests.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link={}".format(urllib.parse.quote(query)))
                                    data = r.text
                                    data = json.loads(data)
                                    client.sendImageWithURL(to, data["result"])
                                except Exception as error:
                                    logError(error)

                            elif cmd.startswith("spekandro "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","+")
                                cond = query.split("|")
                                search = str(cond[0])
                                with requests.session() as s:
                                    s.headers['user-agent'] = random.choice(settings["userAgent"])
                                    r = s.get("https://www.gsmarena.com/res.php3?sSearch={}".format(str(search)))
                                    soup = BeautifulSoup(r.content, 'html5lib')
                                    data = soup.select("div.makers")[0]
                                    b = data.findAll('a', href=True)
                                    if len(cond) == 1:
                                        num = 0
                                        ret_ = "Spesifikasi Android\n"
                                        for anu in b:
                                            num += 1
                                            c = "https://www.gsmarena.com/"+anu['href']
                                            ret_ += "\n {}. {}".format(str(num), str(anu.get_text()))
                                        ret_ += "\n\n Total {} Tipe Android".format(str(len(b)))
                                        client.sendMessage(to, str(ret_))
                                    elif len(cond) == 2:
                                        num = int(cond[1])
                                        if num <= len(b):
                                            anu = b[num - 1]
                                            with requests.session() as s:
                                                s.headers['user-agent'] = random.choice(settings["userAgent"])
                                                r = s.get("https://www.gsmarena.com/{}".format(str(anu['href'])))
                                                soup = BeautifulSoup(r.content, 'html5lib')
                                                data = soup.findAll('div', attrs={'class':'center-stage light nobg specs-accent'})
                                                for pict in soup.findAll('div', attrs={'class':'specs-photo-main'}):
                                                    url = pict.find('img')['src']
                                                    atitle = pict.find('img')['alt']
                                                    title = atitle.replace("MORE PICTURES","")
                                                    client.sendImageWithURL(msg.to, url)
                                                    ret = title
                                                for spec in data:
                                                    ret += "\nDate :\n"+spec.findAll('span')[0].text
                                                    ret += "\nWeight :\n"+spec.findAll('span')[3].text
                                                    ret += "\nOperation System :\n"+spec.findAll('span')[4].text
                                                    ret += "\nInternal :\n"+spec.findAll('span')[6].text
                                                    ret += "\nDisplay size & resolution :\n"+spec.findAll('span')[11].text+" "+spec.findAll('div', attrs={'data-spec':'displayres-hl'})[0].text
                                                    ret += "\nCamera photo & video :\n"+spec.findAll('span')[12].text+"MP "+spec.findAll('div', attrs={'data-spec':'videopixels-hl'})[0].text
                                                    ret += "\nRAM & chipset :\n"+spec.findAll('span')[14].text+"GB RAM "+spec.findAll('div', attrs={'data-spec':'chipset-hl'})[0].text
                                                    ret += "\nBattery capacity & tech :\n"+spec.findAll('span')[16].text+"mAh "+spec.findAll('div', attrs={'data-spec':'battype-hl'})[0].text
                                                    client.sendMessage(msg.to, ret)
                            elif cmd.startswith("tafsirquran "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","+")
                                cond = query.split("|")
                                search = str(cond[0])
                                with requests.session() as s:
                                    s.headers['user-agent'] = random.choice(settings["userAgent"])
                                    r = s.get("https://tafsirq.com/topik/{}".format(str(search)))
                                    soup = BeautifulSoup(r.content, 'html5lib')
                                    data = soup.findAll('div', attrs={'class':'col-md-12'})
                                    tit = soup.findAll('h1')[0].text
                                    if len(cond) == 1:
                                        num = 0
                                        ret_ = tit+"\n"
                                        for get in data:
                                            num += 1
                                            tip = get.find('span').text
                                            isi = tip+': '+get.find('a').text
                                            link = get.find('a')['href']
                                            ret_ += "\n {}. {}".format(str(num), str(isi))
                                        ret_ += "\n\n Total {} Result".format(str(len(data)))
                                        client.sendMessage(to, str(ret_))
                                    elif len(cond) == 2:
                                        num = int(cond[1])
                                        if num <= len(data):
                                            get = data[num - 1]
                                            with requests.session() as s:
                                                s.headers['user-agent'] = random.choice(settings["userAgent"])
                                                r = s.get(get.find('a')['href'])
                                                soup = BeautifulSoup(r.content, 'html5lib')
                                                data = soup.findAll('div', attrs={'class':'panel-body'})[0]
                                                try:
                                                    ret = get.find('a').text+"\n"
                                                    ret += data.findAll('p')[0].text
                                                    ret += "\n\n"+data.findAll('p')[1].text
                                                    client.sendMessage(to, str(ret))
                                                except:
                                                    client.sendMessage(to, "Gagal mengambil data.")
                            elif cmd.startswith("togel"):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                search = str(cond[0])
                                with requests.session() as s:
                                    s.headers['user-agent'] = random.choice(settings["userAgent"])
                                    r = s.get("https://wazetoto.com/wap")
                                    soup = BeautifulSoup(r.content, 'html5lib')
                                    data = soup.findAll('table', attrs={'class':'table'})[0]
                                    hasil = data.select('td > a')
                                    if len(cond) == 1:
                                        num = 0
                                        ret_ = 'Result Pasaran\n'
                                        for anu in hasil:
                                            num += 1
                                            isi = anu.get_text()
                                            link = anu['href']
                                            ret_ += "\n {}. {}".format(str(num), str(isi))
                                        ret_ += "\n\n Total {} Result".format(str(len(hasil)))
                                        client.sendMessage(to, str(ret_))
                                    elif len(cond) == 2:
                                        num = int(cond[1])
                                        if num <= len(hasil):
                                            anu = hasil[num - 1]
                                            with requests.session() as s:
                                                s.headers['user-agent'] = random.choice(settings["userAgent"])
                                                r = s.get(anu['href'])
                                                soup = BeautifulSoup(r.content, 'html5lib')
                                                title = soup.select('h4')[0].text
                                                data = soup.findAll('table', attrs={'class':'table table-hover table-mc-light-blue'})
                                                for res in data:
                                                    try:
                                                        ret = title+"\n"
                                                        ret +="\n "+ res.findAll('td')[0].text+" Periode "+res.findAll('td')[1].text+" Result "+res.findAll('td')[2].text
                                                        ret +="\n "+ res.findAll('td')[3].text+" Periode "+res.findAll('td')[4].text+" Result "+res.findAll('td')[5].text
                                                        ret +="\n "+ res.findAll('td')[6].text+" Periode "+res.findAll('td')[7].text+" Result "+res.findAll('td')[8].text
                                                        ret +="\n "+ res.findAll('td')[9].text+" Periode "+res.findAll('td')[10].text+" Result "+res.findAll('td')[11].text
                                                        ret +="\n "+ res.findAll('td')[12].text+" Periode "+res.findAll('td')[13].text+" Result "+res.findAll('td')[14].text
                                                        ret +="\n "+ res.findAll('td')[15].text+" Periode "+res.findAll('td')[16].text+" Result "+res.findAll('td')[17].text
                                                        ret +="\n "+ res.findAll('td')[18].text+" Periode "+res.findAll('td')[19].text+" Result "+res.findAll('td')[20].text
                                                        client.sendMessage(to, str(ret))
                                                    except:
                                                        client.sendMessage(to, "Gagal mengambil data.")
                            elif cmd.startswith("checkdate"):
                              if msg._from in admin:
                                try:
                                    sep = msg.text.split(" ")
                                    tanggal = msg.text.replace(sep[0] + " ","")
                                    r = requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                                    data=r.text
                                    data=json.loads(data)
                                    ret_ = "[ D A T E ]"
                                    ret_ += "\nDate Of Birth : {}".format(str(data["data"]["lahir"]))
                                    ret_ += "\nAge : {}".format(str(data["data"]["usia"]))
                                    ret_ += "\nBirthday : {}".format(str(data["data"]["ultah"]))
                                    ret_ += "\nZodiak : {}".format(str(data["data"]["zodiak"]))
                                    client.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("checkpraytime "):
                              if msg._from in admin:
                                separate = msg.text.split(" ")
                                location = msg.text.replace(separate[0] + " ","")
                                r = requests.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(location))
                                data = r.text
                                data = json.loads(data)
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashar : " and data[4] != "Maghrib : " and data[5] != "Isya : ":
                                    ret_ = "╔══[ Jadwal Sholat Sekitar " + data[0] + " ]"
                                    ret_ += "\n╠ Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                    ret_ += "\n╠ Jam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                    ret_ += "\n╠ " + data[1]
                                    ret_ += "\n╠ " + data[2]
                                    ret_ += "\n╠ " + data[3]
                                    ret_ += "\n╠ " + data[4]
                                    ret_ += "\n╠ " + data[5]
                                    ret_ += "\n╚══[ Success ]"
                                    client.sendMessage(msg.to, str(ret_))
                            elif cmd.startswith("checkweather "):
                              if msg._from in admin:
                                try:
                                    sep = text.split(" ")
                                    location = text.replace(sep[0] + " ","")
                                    r = requests.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(location))
                                    data = r.text
                                    data = json.loads(data)
                                    tz = pytz.timezone("Asia/Makassar")
                                    timeNow = datetime.now(tz=tz)
                                    if "result" not in data:
                                        ret_ = "╔══[ Weather Status ]"
                                        ret_ += "\n╠ Location : " + data[0].replace("Temperatur di kota ","")
                                        ret_ += "\n╠ Suhu : " + data[1].replace("Suhu : ","") + "°C"
                                        ret_ += "\n╠ Kelembaban : " + data[2].replace("Kelembaban : ","") + "%"
                                        ret_ += "\n╠ Tekanan udara : " + data[3].replace("Tekanan udara : ","") + "HPa"
                                        ret_ += "\n╠ Kecepatan angin : " + data[4].replace("Kecepatan angin : ","") + "m/s"
                                        ret_ += "\n╠══[ Time Status ]"
                                        ret_ += "\n╠ Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                        ret_ += "\n╠ Jam : " + datetime.strftime(timeNow,'%H:%M:%S') + " WIB"
                                        ret_ += "\n╚══[ Success ]"
                                        client.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("checklocation "):
                              if msg._from in admin:
                                try:
                                    sep = text.split(" ")
                                    location = text.replace(sep[0] + " ","")
                                    r = requests.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(location))
                                    data = r.text
                                    data = json.loads(data)
                                    if data[0] != "" and data[1] != "" and data[2] != "":
                                        link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                        ret_ = "╔══[ Location Status ]"
                                        ret_ += "\n╠ Location : " + data[0]
                                        ret_ += "\n╠ Google Maps : " + link
                                        ret_ += "\n╚══[ Success ]"
                                        client.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("instainfo"):
                              if msg._from in admin:
                                try:
                                    sep = text.split(" ")
                                    search = text.replace(sep[0] + " ","")
                                    r = requests.get("https://www.instagram.com/{}/?__a=1".format(search))
                                    data = r.text
                                    data = json.loads(data)
                                    if data != []:
                                        ret_ = "╔══[ Profile Instagram ]"
                                        ret_ += "\n╠ Nama : {}".format(str(data["graphql"]["user"]["full_name"]))
                                        ret_ += "\n╠ Username : {}".format(str(data["graphql"]["user"]["username"]))
                                        ret_ += "\n╠ Bio : {}".format(str(data["graphql"]["user"]["biography"]))
                                        ret_ += "\n╠ Pengikut : {}".format(str(data["graphql"]["user"]["edge_followed_by"]["count"]))
                                        ret_ += "\n╠ Diikuti : {}".format(str(data["graphql"]["user"]["edge_follow"]["count"]))
                                        if data["graphql"]["user"]["is_verified"] == True:
                                            ret_ += "\n╠ Verifikasi : Sudah"
                                        else:
                                            ret_ += "\n╠ Verifikasi : Belum"
                                        if data["graphql"]["user"]["is_private"] == True:
                                            ret_ += "\n╠ Akun Pribadi : Iya"
                                        else:
                                            ret_ += "\n╠ Akun Pribadi : Tidak"
                                        ret_ += "\n╠ Total Post : {}".format(str(data["graphql"]["user"]["edge_owner_to_timeline_media"]["count"]))
                                        ret_ += "\n╚══[ https://www.instagram.com/{} ]".format(search)
                                        path = data["graphql"]["user"]["profile_pic_url_hd"]
                                        client.sendImageWithURL(to, str(path))
                                        client.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("instapost"):
                              if msg._from in admin:
                                try:
                                    sep = text.split(" ")
                                    text = text.replace(sep[0] + " ","")   
                                    cond = text.split("|")
                                    username = cond[0]
                                    no = cond[1] 
                                    r = requests.get("http://rahandiapi.herokuapp.com/instapost/{}/{}?key=betakey".format(str(username), str(no)))
                                    data = r.text
                                    data = json.loads(data)
                                    if data["find"] == True:
                                        if data["media"]["mediatype"] == 1:
                                            client.sendImageWithURL(msg.to, str(data["media"]["url"]))
                                        if data["media"]["mediatype"] == 2:
                                            client.sendVideoWithURL(msg.to, str(data["media"]["url"]))
                                        ret_ = "╔══[ Info Post ]"
                                        ret_ += "\n╠ Jumlah Like : {}".format(str(data["media"]["like_count"]))
                                        ret_ += "\n╠ Jumlah Comment : {}".format(str(data["media"]["comment_count"]))
                                        ret_ += "\n╚══[ Caption ]\n{}".format(str(data["media"]["caption"]))
                                        client.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)

                            elif cmd.startswith("smule "):
                                sep = msg.text.split(" ")
                                smule = msg.text.replace(sep[0] + " ","")
                                with requests.session() as s:
                                    s.headers['user-agent'] = 'Mozilla/5.0'
                                    r = s.get("https://sing.salon/smule-downloader/?url={}".format(urllib.parse.quote(smule)))
                                    data = BeautifulSoup(r.content, 'html5lib')
                                    get = data.select("a[href*=https://www.smule.com/redir?]")[0]
                                    title = data.findAll('h2')[0].text
                                    imag = data.select("img[src*=https://www.smule.com/redir?]")[0]
                                    if 'Smule.m4a' in get['download']:
                                        client.sendImageWithURL(msg.to, imag['src'])
                                        client.sendMessage(to,"Type: Audio\nTitle :\n"+title+"\n\nWait for media uploading..!")
                                        client.sendAudioWithURL(msg.to, get['href'])
                                    else:
                                        client.sendImageWithURL(msg.to, imag['src'])
                                        client.sendMessage(to,"Type: Video\nTitle :\n"+title+"\n\nWait for media uploading..!")
                                        client.sendVideoWithURL(msg.to, get['href'])

                            elif cmd.startswith("\smule "):
                                if '/' in text:
                                    sep = text.split("/")
                                    x = len(sep)
                                    smule = sep[x - 1]
                                else:
                                    smule == text.split(" ")[1]               
                                with requests.session() as s:
                                    s.headers['user-agent'] = random.choice(settings["userAgent"])
                                    r = s.get("http://www.singsmule.net//p/{}.html".format(str(smule)))
                                    data = BeautifulSoup(r.content, 'html5lib')
                                    note = data.findAll('div', attrs={'class':'col-md-4'})[3].text
                                    x = data.title.string
                                    title = x.replace('| SingSmule.Net','')
                                    tumb = data.select("img.img-thumbnail")[0]
                                    pict = tumb['src']
                                    if 'Not Available' in note:
                                        aud = data.select('a[href*=https://y-ash.smule.com/]')[0]
                                        m4a = aud['href']
                                        client.sendMessage(msg.to,"Title :\n"+title)
                                        client.sendImageWithURL(msg.to, pict)
                                        client.sendMessage(msg.to,"Type : Audio\nWait for media uploading..!")
                                        client.sendAudioWithURL(msg.to, m4a)
                                    else:
                                        vid = data.select('a[href*=https://y-ash.smule.com/]')[1]
                                        mp4 = vid['href']
                                        client.sendMessage(msg.to,"Title :\n"+title)
                                        client.sendImageWithURL(msg.to, pict)
                                        client.sendMessage(msg.to,"Type : Video\nWait for media uploading..!")
                                        client.sendVideoWithURL(msg.to, mp4)
                            elif cmd.startswith("instastory"):
                              if msg._from in admin:
                                try:
                                    sep = text.split(" ")
                                    text = text.replace(sep[0] + " ","")
                                    cond = text.split("|")
                                    search = str(cond[0])
                                    if len(cond) == 2:
                                        r = requests.get("http://rahandiapi.herokuapp.com/instastory/{}?key=betakey".format(search))
                                        data = r.text
                                        data = json.loads(data)
                                        if data["url"] != []:
                                            num = int(cond[1])
                                            if num <= len(data["url"]):
                                                search = data["url"][num - 1]
                                                if search["tipe"] == 1:
                                                    client.sendImageWithURL(to, str(search["link"]))
                                                if search["tipe"] == 2:
                                                    client.sendVideoWithURL(to, str(search["link"]))
                                except Exception as error:
                                    logError(error)
                                    
                            elif cmd.startswith("say-"):
                              if msg._from in admin:
                                sep = text.split("-")
                                sep = sep[1].split(" ")
                                lang = sep[0]
                                say = text.replace("say-" + lang + " ","")
                                if lang not in list_language["list_textToSpeech"]:
                                    return client.sendMessage(to, "Language not found")
                                tts = gTTS(text=say, lang=lang)
                                tts.save("hasil.mp3")
                                client.sendAudio(to,"hasil.mp3")
                                
                            elif cmd.startswith("searchimage"):
                              if msg._from in admin:
                                try:
                                    separate = msg.text.split(" ")
                                    search = msg.text.replace(separate[0] + " ","")
                                    r = requests.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(search))
                                    data = r.text
                                    data = json.loads(data)
                                    if data["result"] != []:
                                        items = data["result"]
                                        path = random.choice(items)
                                        a = items.index(path)
                                        b = len(items)
                                        client.sendImageWithURL(to, str(path))
                                except Exception as error:
                                    logError(error)
				

                            elif cmd == "cek welcome":
                               if msg._from in admin:
                                  flexCek(msg.to, str(setting["welcomemsg"]))
					
                            elif cmd == "cek leave":
                               if msg._from in admin:
                                  flexCek(msg.to, str(setting["leavemsg"]))
					
                            elif cmd == "cek sider1":
                               if msg._from in admin:
                                  flexCek(msg.to, str(setting["sider1"]))
					
                            elif cmd == "cek sider2":
                               if msg._from in admin:
                                  flexCek(msg.to, str(setting["sider2"]))
					
                            elif cmd == "cek sider3":
                               if msg._from in admin:
                                  flexCek(msg.to, str(setting["sider3"]))
					
                            elif cmd == "cek respon":
                               if msg._from in admin:
                                  flexCek(msg.to, str(setting["respontag"]))

                            elif 'setleave ' in msg.text:
                               if msg._from in admin:
                                  spl = msg.text.replace('setleave ','')
                                  if spl in [""," ","\n",None]:
                                      client.sendMessage(msg.to, "Gagal mengganti leave Msg")
                                  else:
                                      setting["leavemsg"] = spl
                                      f = codecs.open("dataku.json","w","utf-8")
                                      json.dump(setting, f, sort_keys=True, indent=4,ensure_ascii=False)
                                      flexSet(msg.to, "leavemsg di ganti\n {}".format(str(spl)))
                            elif 'setwelcome ' in msg.text:
                               if msg._from in admin:
                                  spl = msg.text.replace('setwelcome ','')
                                  if spl in [""," ","\n",None]:
                                      flexSet(msg.to, "Gagal mengganti Welcome Msg")
                                  else:
                                      setting["welcomemsg"] = spl
                                      f = codecs.open("dataku.json","w","utf-8")
                                      json.dump(setting, f, sort_keys=True, indent=4,ensure_ascii=False)
                                      flexSet(msg.to, "welcomemsg di ganti\n {}".format(str(spl)))

                            elif 'setsider1 ' in msg.text:
                               if msg._from in admin:
                                  spl = msg.text.replace('setsider1 ','')
                                  if spl in [""," ","\n",None]:
                                      flexSet(msg.to, "Gagal mengganti sider1")
                                  else:
                                      setting["sider1"] = spl
                                      f = codecs.open("dataku.json","w","utf-8")
                                      json.dump(setting, f, sort_keys=True, indent=4,ensure_ascii=False)
                                      flexSet(msg.to, "sider1 di ganti\n {}".format(str(spl)))
					
                            elif 'setsider2 ' in msg.text:
                               if msg._from in admin:
                                  spl = msg.text.replace('setsider2 ','')
                                  if spl in [""," ","\n",None]:
                                      flexSet(msg.to, "Gagal mengganti sider2")
                                  else:
                                      setting["sider2"] = spl
                                      f = codecs.open("dataku.json","w","utf-8")
                                      json.dump(setting, f, sort_keys=True, indent=4,ensure_ascii=False)
                                      flexSet(msg.to, "sider2 di ganti\n {}".format(str(spl)))
                            elif 'setsider3 ' in msg.text:
                               if msg._from in admin:
                                  spl = msg.text.replace('setsider3 ','')
                                  if spl in [""," ","\n",None]:
                                      flexSet(msg.to, "Gagal mengganti sider3")
                                  else:
                                      setting["sider3"] = spl
                                      f = codecs.open("dataku.json","w","utf-8")
                                      json.dump(setting, f, sort_keys=True, indent=4,ensure_ascii=False)
                                      flexSet(msg.to, "sider3 di ganti\n {}".format(str(spl)))
					
                            elif 'setrespon ' in msg.text:
                               if msg._from in admin:
                                  spl = msg.text.replace('setrespon ','')
                                  if spl in [""," ","\n",None]:
                                      flexSet(msg.to, "Gagal mengganti respon")
                                  else:
                                      setting["respontag"] = spl
                                      f = codecs.open("dataku.json","w","utf-8")
                                      json.dump(setting, f, sort_keys=True, indent=4,ensure_ascii=False)
                                      flexSet(msg.to, "respontag di ganti\n {}".format(str(spl)))




                            elif "/musik" in msg.text.lower():
                              if msg._from in admin:
                                try:
                                    search = text.lower().replace("/musik ","")
                                    r = requests.get("https://rest.farzain.com/api/joox.php?apikey=rambu&id={}".format(urllib.parse.quote(search))) #untuk api key bisa requests ke web http://www.farzain.xyz/requests.php
                                    data = r.text
                                    data = json.loads(data)
                                    info = data["info"]
                                    audio = data["audio"]
                                    hasil = "? Hasil Musik ?\n"
                                    hasil += "\nPenyanyi : {}".format(str(info["penyanyi"]))
                                    hasil += "\nJudul : {}".format(str(info["judul"]))
                                    hasil += "\nAlbum : {}".format(str(info["album"]))
                                    hasil += "\n\nLink : \n1. Image : {}".format(str(data["gambar"]))
                                    hasil += "\n\nLink : \n2. MP3 : {}".format(str(audio["mp3"]))
                                    client.sendImageWithURL(msg.to, str(data["gambar"]))
                                    client.sendMessage(msg.to, str(hasil))
                                    client.sendAudioWithURL(msg.to, str(audio["mp3"]))
                                    client.sendMessage(msg.to, "Selamat Menikmati Musicnya kk...")
                                except Exception as error:
                                    client.sendMessage(msg.to, "? Result Error ?\n" + str(error))
                            elif cmd.startswith("led "):
                              if msg._from in admin:
                                separate = text.split(" ")
                                teks = text.replace(separate[0] + " ","")
                                url = "https://ari-api.herokuapp.com/led?text="+teks+"&sign=PB"
                                client.sendImageWithURL(to, url)
                                
                            elif cmd.startswith("musik "):
                               if msg._from in admin:
                                 query = msg.text.replace("musik","")
                                 search = query.replace(" ","+")
                                 result = requests.get("https://api.zicor.ooo/joox.php?song={}".format(str(search)))
                                 datu = result.text
                                 datu = json.loads(datu)
                                 ret_ = "\n- ʲᵘᵈᵘˡ : {}".format(datu["title"])
                                 ret_ += "\n- ᵃʳᵗᶤᶳ : {}".format(datu["singer"])
                                 data = {
                                   "messages": [
                                                                     {
                                                                         "type": "flex",
                                                                         "altText": "musik",
                                                                         "contents": 
                                                                             {
                                                                             "type": "bubble",
                                                                             "styles": {
                                                                                     "body": {
                                                                                         "backgroundColor": "#000000",
                                                                                     },
                                                                                     "footer": {
                                                                                         "backgroundColor": "#000000",
                                                                                         "separator": True,
                                                                                         "separatorColor": "#6F00FF",
                                                                                     }
                                                                                 },
                                                                             "body": {
                                                                                 "type": "box",
                                                                                 "layout": "vertical",
                                                                                 "contents": [
                                                                                     {
                                                                                         "type": "box",
                                                                                         "layout": "horizontal",
                                                                                         "contents": [
                                                                                             {
                                                                                                 "type": "separator",
                                                                                                 "color": "#7CFC00"
                                                                                             },
                                                                                             {
                                                                                                 "type": "image",
                                                                                                 "url": datu["image"],
                                                                                                 "aspectRatio": "3:4",
                                                                                                 "aspectMode": "cover",
                                                                                                 "size": "lg",
                                                                                                 "flex": 0,
                                                                                                 "align": "start"
                                                                                             },
                                                                                             {
                                                                                                 "type": "separator",
                                                                                                 "color": "#7CFC00"
                                                                                             },
                                                                                             {
                                                                                                 "type": "text",
                                                                                                 "text": "          ⏫\n     ⏪⏹️⏩\n          ⏬\n   ────────\n     🔂 🔁 🔀",
                                                                                                 "wrap": True,
                                                                                                 "color": "#FFFF00",
                                                                                                 "flex": 0
                                                                                             }
                                                                                         ]
                                                                                     },
                                                                                     {
                                                                                         "type": "box",
                                                                                         "layout": "vertical",
                                                                                         "contents": [
                                                                                             {
                                                                                                 "type": "separator",
                                                                                                 "color": "#7CFC00"
                                                                                             },
                                                                                             {
                                                                                                 "type": "text",
                                                                                                 "text": "          🔈🔉🔊",
                                                                                                 "wrap": True,
                                                                                                 "color": "#00FFFF",
                                                                                                 "size": "lg",
                                                                                                 "flex": 1,
                                                                                                 "gravity": "top"
                                                                                             },
                                                                                             {
                                                                                                "type": "separator",
                                                                                                "color": "#7CFC00"
                                                                                             },
                                                                                             {
                                                                                                "type": "text",
                                                                                                "text": ret_,
                                                                                                "wrap": True,
                                                                                                "flex": 1,
                                                                                                "color": "#00FF7F",
                                                                                                "gravity": "bottom"
                                                                                             }
                                                                                         ]
                                                                                     }
                                                                                 ],
                                                                             }
                                                                         }
                                                                     }
                                     ]
                                 }
                                 sendTemplate(to, data)
                                # client.sendImageWithURL(to, data["image"])
                                # footer(to, ret_)
                                 client.sendAudioWithURL(to, datu["url"])
                            elif cmd.startswith("ceksmule "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                search = text.replace(sep[0] + " ","")
                                with requests.session() as web:
                                    web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                    r = web.get("https://www.smule.com/{}".format(urllib.parse.quote(search)))
                                    gunakan = BeautifulSoup(r.content, 'html5lib')
                                for getinfosmule in gunakan.findAll('script',{'type':'text/javascript'})[1]:
                                    getJsonSmule = re.search(r'DataStore.Pages.Profile\s*=\s*(\{.+\})\s*;', getinfosmule).group(1)
                                    dati = json.loads(getJsonSmule)
                                for smuleProfile in dati:
                                    ret_ = "PROFILE:\n"
                                    ret_ += "\n• Id Smule: @{}".format(str(dati["user"]["handle"]))
                                    ret_ += "\n• Total Rekaman: {} record".format(str(dati["user"]["num_performances"]))
                                    ret_ += "\n• Pengikut: {} orang".format(str(dati["user"]["followers"]))
                                    ret_ += "\n• Mengikuti: {} orang".format(str(dati["user"]["followees"]))
                                    ret_ += "\n• Bio: {}".format(str(dati["user"]["blurb"]))
                                    if dati["user"]["is_verified"] == True:
                                        ret_ += "\n• Verifikasi: Sudah"
                                    else:
                                        ret_ += "\n• Verifikasi: Belum"
                                    if dati["user"]["is_vip"] == True:
                                        ret_ += "\n• Akun VIP: Iya"
                                    else:
                                        ret_ += "\n• Akun VIP: Tidak"
                                    
                                    path = dati["user"]["pic_url"]
                                    name = "INFO PROFILE SMULE"
                                    url = "https://www.smule.com/{}".format(search)
                                    iconlink = dati["user"]["pic_url"]
                                data = {
                                    "messages": [
                                       {
                                            "type": "flex",
                                            "altText": "ID BOTS",
                                            "contents": {
                                                "type": "bubble",
                                                "styles": {
                                                        "header": {
                                                            "backgroundColor": "#4169E1",
                                                        },
                                                        "footer": {
                                                            "backgroundColor": "#4169E1",
                                                            "separator": True
                                                        }
                                                    },
                                                "header": {
                                                  "type": "box",
                                                  "layout": "vertical",
                                                  "contents": [
                                                    {
                                                      "type": "text",
                                                      "text": "INFO SMULE",
                                                      "weight": "bold",
                                                      "color": "#7CFC00",
                                                      "size": "xl",
                                                    }
                                                  ]
                                                },
                                                "hero": {
                                                        "type": "image",
                                                        "url": str(path),
                                                        "size": "full",
                                                        "aspectRatio": "1.51:1",
                                                        "aspectMode": "cover",
                                                },
                                                "body": {
                                                        "type": "box",
                                                        "layout": "vertical",
                                                        "contents": [
                                                           {
                                                             "type": "box",
                                                             "layout": "vertical",
                                                             "contents": [
                                                                {
                                                                  "type": "box",
                                                                  "layout": "baseline",
                                                                  "contents": [
                                                                     {
                                                                       "type": "text",
                                                                       "text": "INFO PROFILE SMULE",
                                                                       "color": "#0000ff",
                                                                       "weight": "bold"
                                                                     }
                                                                  ]
                                                                }
                                                             ]
                                                           },
                                                           {
                                                             "type": "box",
                                                             "layout": "vertical",
                                                             "spacing": "xs",
                                                             "contents": [
                                                                {
                                                                  "type": "box",
                                                                  "layout": "horizontal",
                                                                  "contents": [
                                                                     {
                                                                       "type": "text",
                                                                       "text": "NAMA:",
                                                                       "color": "#228B22",
                                                                       "size": "xxs",
                                                                       "weight": "bold",
                                                                       "flex": 1
                                                                    },
                                                                    {
                                                                       "type": "text",
                                                                       "text": "@{}".format(str(dati["user"]["handle"])),
                                                                       "color": "#FF4500",
                                                                       "size": "sm",
                                                                       "wrap": True,
                                                                       "flex": 3
                                                                     }
                                                                   ]
                                                                }
                                                             ]
                                                           },
                                                           {
                                                             "type": "box",
                                                             "layout": "vertical",
                                                             "spacing": "xs",
                                                             "contents": [
                                                                {
                                                                  "type": "box",
                                                                  "layout": "horizontal",
                                                                  "contents": [
                                                                     {
                                                                       "type": "text",
                                                                       "text": "BIO:",
                                                                       "color": "#ff0000",
                                                                       "size": "xxs",
                                                                       "weight": "bold",
                                                                       "flex": 1
                                                                     },
                                                                     {
                                                                       "type": "text",
                                                                       "text": str(ret_),
                                                                       "color": "#FF00FF",
                                                                       "size": "sm",
                                                                       "wrap": True,
                                                                       "flex": 3
                                                                    }
                                                                  ]
                                                                }
                                                             ]
                                                           }
                                                        ]
                                                },
                                                "footer": {
                                                        "type": "box",
                                                        "layout": "vertical",
                                                        "spacing": "lg",
                                                        "contents": [
                                                           {
                                                             "type": "button",
                                                             "style": "primary",
                                                             "action": {
                                                                 "type": "uri",
                                                                 "label": "follow",
                                                                 "uri": "https://www.smule.com/Mase_Nis"
                                                              }
                                                           }
                                                        ]
                                                }
                                            }
                                       }
                                    ]
                                }
                                sendTemplate(to, data)
                               # client.sendMessage(to, str(ret_))
                               # client.sendImageWithURL(msg.to, str(path))				
                            elif cmd.startswith("searchlyric"):
                              if msg._from in admin:
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                search = cond[0]
                                api = requests.get("http://api.secold.com/joox/cari/{}".format(str(search)))
                                data = api.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "╔══[ Result Lyric ]"
                                    for lyric in data["results"]:
                                        num += 1
                                        ret_ += "\n╠ {}. {}".format(str(num), str(lyric["single"]))
                                    ret_ += "\n╚══[ Total {} Music ]".format(str(len(data["results"])))
                                    ret_ += "\n\nUntuk Melihat Details Lyric, silahkan gunakan command {}SearchLyric {}|「number」".format(str(setKey), str(search))
                                    client.sendMessage(to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["results"]):
                                        lyric = data["results"][num - 1]
                                        api = requests.get("http://api.secold.com/joox/sid/{}".format(str(lyric["songid"])))
                                        data = api.text
                                        data = json.loads(data)
                                        lyrics = data["results"]["lyric"]
                                        lyric = lyrics.replace('ti:','Title - ')
                                        lyric = lyric.replace('ar:','Artist - ')
                                        lyric = lyric.replace('al:','Album - ')
                                        removeString = "[1234567890.:]"
                                        for char in removeString:
                                            lyric = lyric.replace(char,'')
                                        client.sendMessage(msg.to, str(lyric))
                            elif "Cekik " in msg.text:
                              if msg._from in admin:
                                _name = text.replace("Cekik ","")
                                gs = client.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    if _name in g.displayName:
                                        targets.append(g.mid)
                                if targets == []:
                                    pass
                                else:
                                    for target in targets:
                                        if target in clientMid:
                                            pass
                                        else:
                                            try:
                                                client.kickoutFromGroup(msg.to,[target])
                                            except:
                                                pass

                            elif cmd.startswith("music: "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("=")
                                search = str(cond[0])
                                result = requests.get("http://api-jooxtt.sanook.com/web-fcgi-bin/web_search?country=id&lang=id&search_input={}&sin=1&ein=30".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    citl = "╭━━[ Result Music ]━━"
                                    for music in data['itemlist']:
                                        num += 1
                                        citl += "\n│▶ {}. {}".format(str(num), base64.b64decode(music['info1']).decode('utf-8'))
                                    citl += "\n╰━━[ Total {} Music ]━━".format(str(len(music)))
                                    client.sendMessageWithMention(msg.to,msg._from, "「✨ᶜⁱᵗˡsᴇʟғʙᴏᴛ」\nUser: ","\n\n{}\n⏺Untuk melihat Play music, silahkan gunakan command Music: {}=「number」".format(str(citl), str(search)))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data['itemlist']):
                                        music = data['itemlist'][num - 1]
                                        result = requests.get("http://api-jooxtt.sanook.com/web-fcgi-bin/web_get_songinfo?country=id&lang=id&songid={}".format(music['songid']))
                                        data = result.text
                                        data = json.loads(data)
                                        print(data)
                                        citl = "╭━━━「 Music 」━━━━"
                                        citl += "\n│ Penyanyi : {}".format(data["msinger"])
                                        citl += "\n│ Judul : {}".format(data["msong"])
                                        citl += "\n│ Album : {}".format(data["malbum"])
                                        citl += "\n╰━━━「Done」━━━━"
                                        client.sendImageWithURL(msg.to, str(data["imgSrc"]))
                                        client.sendMessageWithMention(msg.to, msg._from, "","\n{}\n\n??Audio masih dalam proses".format(str(citl)))
                                        client.sendAudioWithURL(msg.to, str(data["mp3Url"]))     
                            elif cmd.startswith("record "):
                              if msg._from in admin:
                                proses = text.split(" ")
                                urutan = text.replace(proses[0] + " ","")
                                count = urutan.split("|")
                                search = str(count[0])
                                r = requests.get("https://www.smule.com/"+search+"/performances/json")
                                data = json.loads(r.text)
                                if len(count) == 1:
                                    no = 0
                                    ret_ = " "
                                    for aa in data["list"]:
                                        no += 1
                                        ret_ += "\n" + str(no) + ". " + str(aa["title"])
                                    ret_ += "\n\nCONTOH:\nrecord {}|1".format(str(search))
                                    flexSmule(msg.to,ret_)
                                elif len(count) == 2:
                                    try:
                                        num = int(count[1])
                                        b = data["list"][num - 1]
                                        smule = str(b["web_url"])
                                        c = " Judul Oc: "+str(b["title"])
                                        c += "\n Pembuat: "+str(b["owner"]["handle"])
                                        c += "\n Total like: "+str(b["stats"]["total_loves"])+" like"
                                        c += "\n Total comment: "+str(b["stats"]["total_comments"])+" comment"
                                        c += "\n Status VIP: "+str(b["owner"]["is_vip"])
                                        c += "\n Status Oc: "+str(b["message"])
                                        c += "\n Created Oc: {}".format(b["created_at"][:10])
                                        c += "\n Didengarkan: {}".format(b["stats"]["total_listens"])+" orang"
                                        hasil = "\n\n"+str(c)
                                        dl = str(b["cover_url"])
                                      #  client.sendImageWithURL(msg.to,dl)
                                        flexSmule1(msg.to, hasil)
                                        with requests.session() as s:
                                            s.headers['user-agent'] = 'Mozilla/5.0'
                                            r = s.get("https://sing.salon/smule-downloader/?url=https://www.smule.com{}".format(urllib.parse.quote(smule)))
                                            data = BeautifulSoup(r.content, 'html5lib')
                                            get = data.select("a[href*=https://www.smule.com/redir?]")[0]
                                            title = data.findAll('h2')[0].text
                                            imag = data.select("img[src*=https://www.smule.com/redir?]")[0]
                                            if 'Smule.m4a' in get['download']:
                                                #client.sendMessage(to,"Type: Audio\n\nWait for media uploading..!")
                                                client.sendAudioWithURL(msg.to, get['href'])
                                            else:
                                                #client.sendMessage(to,"Type: Video\n\nWait for media uploading..!")
                                                client.sendVideoWithURL(msg.to, get['href'])
                                    except Exception as e:
                                        client.sendAiri(msg.id,msg.to,"「 Result Error 」\n"+str(e))

                            elif cmd.startswith("poster "):
                              if msg._from in admin:
                                separate = text.split(" ")
                                teks = text.replace(separate[0] + " ","")
                                url = "https://ari-api.herokuapp.com/neon?text="+teks+"&color=blue"
                                client.sendImageWithURL(to, url)
				
                            elif cmd.startswith("bcast "):
                                if msg._from in admin:
                                   sep = text.split(" ")
                                   pesan = text.replace(sep[0] + " ","")
                                   saya = client.getGroupIdsJoined()
                                   for group in saya:
                                       flexBro(group, str(pesan))
                                   

                            elif cmd.startswith("fs2 "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = "https://rest.farzain.com/api/special/fansign/cosplay/cosplay.php?apikey=nda123&text={}".format(txt)
                                client.sendImageWithURL(to, url)

                            elif cmd.startswith("cool "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = "https://rest.farzain.com/api/cooltext.php?text={}&apikey=nda123".format(txt)
                                client.sendImageWithURL(to, url)

                            elif cmd.startswith("fs3 "):
                              if msg._from in admin:
                                txt = text.replace("fs3 ","")
                                url = "https://rest.farzain.com/api/special/fansign/indo/viloid.php?apikey=nda123&text={}".format(txt)
                                client.sendImageWithURL(to, url)
                   	
                            elif cmd.startswith("fs "):
                              if msg._from in admin:
                                separate = msg.text.split(" ")
                                nama = msg.text.replace(separate[0] + " ","")
                                url = ("http://api.farzain.com/special/fansign/cosplay/cosplay.php?apikey=sb_apikey&text="+nama)
                                client.sendImageWithURL(msg.to, url)				
                            #except Exception as error:
                               # client.sendMessage(msg.to, str(error))
                         #  else:
                           #    client.sendMessage(msg.to, "Khusus member premium!")
					
                            elif cmd.startswith("/ "):
                              if msg._from in admin:
                                ardian = text.replace("/ ","")
                                client.sendMessage(msg.to, None, contentMetadata={'mid': ardian}, contentType=13)
                                contact = client.getContact(ardian)
                                ganteng = client.getProfileCoverURL(ardian)
                                path = str(ganteng)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                try:
                                    client.sendMessage(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                                    client.sendMessage(msg.to,"Profile Picture " + contact.displayName)
                                    client.sendImageWithURL(msg.to,image)
                                    client.sendMessage(msg.to,"Cover Picture " + contact.displayName)
                                    client.sendImageWithURL(msg.to,path)
                                except:
                                    pass
                            elif cmd.startswith("searchyoutube"):
                              if msg._from in admin:
                                sep = text.split(" ")
                                search = text.replace(sep[0] + " ","")
                                params = {"search_query": search}
                                r = requests.get("https://www.youtube.com/results", params = params)
                                soup = BeautifulSoup(r.content, "html5lib")
                                ret_ = "╔══[ Youtube Result ]"
                                datas = []
                                for data in soup.select(".yt-lockup-title > a[title]"):
                                    if "&lists" not in data["href"]:
                                        datas.append(data)
                                for data in datas:
                                    ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                                    ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                                ret_ += "\n╚══[ Total {} ]".format(len(datas))
                                client.sendAiri(msg.id,to, str(ret_))
                            elif cmd.startswith("tr-"):
                              if msg._from in admin:
                                sep = text.split("-")
                                sep = sep[1].split(" ")
                                lang = sep[0]
                                say = text.replace("tr-" + lang + " ","")
                                if lang not in list_language["list_translate"]:
                                    return client.sendMessage(to, "Language not found")
                                translator = Translator()
                                hasil = translator.translate(say, dest=lang)
                                A = hasil.text
                                client.sendMessage(to, str(A))
#=====================================================================================================================================
#=====================================================================================================================================
                        if text.lower() == "mykey":
                          if msg._from in admin:
                            client.sendAiri(msg.id,to, "KeyCommand Saat ini adalah [ {} ]".format(str(settings["keyCommand"])))
                        elif text.lower() == "setkey on":
                          if msg._from in admin:
                            settings["setKey"] = True
                            client.sendAiri(msg.id,to, "Berhasil mengaktifkan setkey")
                        elif text.lower() == "setkey off":
                          if msg._from in admin:
                            settings["setKey"] = False
                            client.sendAiri(msg.id,to, "Berhasil menonaktifkan setkey")
#=====================================================================================================================================
#=====================================================================================================================================
                    elif msg.contentType == 1:
                        if settings["changePictureProfile"] == True:
                            path = client.downloadObjectMsg(msg_id)
                            settings["changePictureProfile"] = False
                            client.updateProfilePicture(path)
                            client.sendAiri(msg.id,to, "Berhasil mengubah foto profile")
                        if msg.toType == 2:
                            if to in settings["changeGroupPicture"]:
                                path = client.downloadObjectMsg(msg_id)
                                settings["changeGroupPicture"].remove(to)
                                client.updateGroupPicture(to, path)
                                client.sendAiri(msg.id,to, "Berhasil mengubah foto group")
                    elif msg.contentType == 7:
                        if settings["checkSticker"] == True:
                            stk_id = msg.contentMetadata['STKID']
                            stk_ver = msg.contentMetadata['STKVER']
                            pkg_id = msg.contentMetadata['STKPKGID']
                            ret_ = "╔══[ Sticker Info ]"
                            ret_ += "\n╠ STICKER ID : {}".format(stk_id)
                            ret_ += "\n╠ STICKER PACKAGES ID : {}".format(pkg_id)
                            ret_ += "\n╠ STICKER VERSION : {}".format(stk_ver)
                            ret_ += "\n╠ STICKER URL : line://shop/detail/{}".format(pkg_id)
                            ret_ += "\n╚══[ Finish ]"
                            client.sendMessage(to, str(ret_))
                    elif msg.contentType == 13:
                        if settings["checkContact"] == True:
                            try:
                                contact = client.getContact(msg.contentMetadata["mid"])
                                if client != None:
                                    cover = client.getProfileCoverURL(msg.contentMetadata["mid"])
                                else:
                                    cover = "Tidak dapat masuk di line channel"
                                path = "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                                try:
                                    client.sendImageWithURL(to, str(path))
                                except:
                                    pass
                                ret_ = "╔══[ Details Contact ]"
                                ret_ += "\n╠ Nama : {}".format(str(contact.displayName))
                                ret_ += "\n╠ MID : {}".format(str(msg.contentMetadata["mid"]))
                                ret_ += "\n╠ Bio : {}".format(str(contact.statusMessage))
                                ret_ += "\n╠ Gambar Profile : http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                                ret_ += "\n╠ Gambar Cover : {}".format(str(cover))
                                ret_ += "\n╚══[ Finish ]"
                                client.sendMessage(to, str(ret_))
                            except:
                                client.sendAiri(msg.id,to, "Kontak tidak valid")
                    elif msg.contentType == 16:
                        if settings["checkPost"] == True:
                            try:
                                ret_ = "╔══[ Details Post ]"
                                if msg.contentMetadata["serviceType"] == "GB":
                                    contact = client.getContact(sender)
                                    auth = "\n╠ Penulis : {}".format(str(contact.displayName))
                                else:
                                    auth = "\n╠ Penulis : {}".format(str(msg.contentMetadata["serviceName"]))
                                purl = "\n╠ URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                ret_ += auth
                                ret_ += purl
                                if "mediaOid" in msg.contentMetadata:
                                    object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                    if msg.contentMetadata["mediaType"] == "V":
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                            murl = "\n╠ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                            murl = "\n╠ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                        ret_ += murl
                                    else:
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                    ret_ += ourl
                                if "stickerId" in msg.contentMetadata:
                                    stck = "\n╠ Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                    ret_ += stck
                                if "text" in msg.contentMetadata:
                                    text = "\n╠ Tulisan : {}".format(str(msg.contentMetadata["text"]))
                                    ret_ += text
                                ret_ += "\n╚══[ Finish ]"
                                client.sendAiri(msg.id,to, str(ret_))
                            except:
                                client.sendMessage(to, "Post tidak valid")
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
                
        if op.type == 26:
            try:
                print ("[ 26 ] RECIEVE MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != client.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if settings["autoRead"] == True:
                        client.sendChatChecked(to, msg_id)
                    if to in read["readPoint"]:
                        if sender not in read["ROM"][to]:
                            read["ROM"][to][sender] = True
                    if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                        text = msg.text
                        if text is not None:
                            client.sendAiri(msg.id,msg.to,text)
 
                    if settings["unsendMessage"] == True:
                        try:
                            msg = op.message
                            if msg.toType == 0:
                                client.log("[{} : {}]".format(str(msg._from), str(msg.text)))
                            else:
                                client.log("[{} : {}]".format(str(msg.to), str(msg.text)))
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
                                    group = client.findGroupByTicket(ticket_id)
                                    client.acceptGroupInvitationByTicket(group.id,ticket_id)
                                    client.sendAiri(msg.id,to, "Berhasil masuk ke group %s" % str(group.name))
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if clientMid in mention["M"]:
                                    if setting["autorespon"] == True:
                                        contact = client.getContact(msg._from)
                                        data = {
                                            "messages": [
                                               {
                                                   "type": "flex",
                                                   "altText": "ID BOTS",
                                                   "contents": 
                                                       {
                                                       "type": "bubble",
                                                       "styles": {
                                                               "body": {
                                                                   "backgroundColor": "#E6E6FA",
                                                               }
                                                           },
                                                       "body": {
                                                           "type": "box",
                                                           "layout": "vertical",
                                                           "contents": [
                                                               {
                                                                   "type": "text",
                                                                   "text": "{}".format(contact.displayName),
                                                                   "color": "#0000CD",
                                                                   "wrap": True,
                                                                   "flex": 1,
                                                                   "gravity": "top",
                                                                   "size": "sm",
                                                                   "weight": "bold"
						               },
						               {
                                                                   "type": "separator",
                                                                   "color": "#7CFC00"
                                                               },
                                                               {
                                                                   "type": "text",
                                                                   "text": setting["respontag"],
                                                                   "color": "#FF0000",
                                                                   "wrap": True,
                                                                   "flex": 1,
                                                                   "gravity": "bottom",
                                                                   "size": "sm",
                                                                   "weight": "bold"
                                                               }
                                                           ],
                                                       }
                                                   }
                                               }
                                           ],
                                        }
                                        sendTemplate(to, data)

                                       # sendMessage(msg.to, setting["respontag"])
                                        #client.sendMessage(msg.to, "iya nih kangen\nhabisnyaa kamu tu ngangenin sih" ,contentMetadata={'MSG_SENDER_ICON': "http://dl.profile.line-cdn.net"+client.getContact(msg._from).picturePath,'MSG_SENDER_NAME':  '{}'.format(str(client.getContact(msg._from).displayName))} )
                             #           sid = str(settings["AddstickerTag"]["sid"])
                              #          spkg = str(settings["AddstickerTag"]["spkg"])
                               #         client.sendSticker(msg.to, spkg, sid)
                                    break
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
        if op.type == 65:
            print ("[ 65 ] NOTIFIED DESTROY MESSAGE")
            if settings["unsendMessage"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                            contact = client.getContact(msg_dict[msg_id]["from"])
                            if contact.displayNameOverridden != None:
                                name_ = contact.displayNameOverridden
                            else:
                                name_ = contact.displayName
                                ret_ = "\nUnsend"
                                ret_ += "\nPengirim : @!"
                                ret_ += "\nWaktu : {}".format(str(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"]))))
                                ret_ += "\nType : {}".format(str(Type._VALUES_TO_NAMES[msg_dict[msg_id]["contentType"]]))
                                ret_ += "\nText : {}".format(str(msg_dict[msg_id]["text"]))
                                sendMention(at, str(ret_), [contact.mid])
                            del msg_dict[msg_id]
                        else:
                            client.sendAiri(msg.id,at,"SentMessage cancelled,But I didn't have log data.\nSorry > <")
                except Exception as error:
                    logError(error)
                    traceback.print_tb(error.__traceback__)
			
 
        if op.type == 55:
        	try:
        		group_id = op.param1
        		user_id=op.param2
        	except Exception as e:
        		print(e)
			
                    
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = client.getContact(op.param2).displayName
                            dan = client.getContact(op.param2).picturePath
                            tgb = client.getGroup(op.param1)
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        flexSid1(op.param1, setting["sider1"])
                                       # client.sendContact(op.param1, op.param2)
                                        #client.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan))
                                    else:
                                        flexSid2(op.param1, setting["sider2"])
                                       # client.sendContact(op.param1, op.param2)
                                        #client.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan))
                                else:
                                    flexSid3(op.param1, setting["sider3"])
                                    #client.sendContact(op.param1, op.param2)
                                    #client.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan))
                        else:
                            pass #client.sendMessage(op.param1, "mumpung sepi ngintip ahh" ,contentMetadata={'MSG_SENDER_ICON': "http://dl.profile.line-cdn.net"+client.getContact(op.param2).picturePath,'MSG_SENDER_NAME':  '{}'.format(str(client.getContact(op.param2).displayName))} )
                    else:
                        pass #client.sendMessage(op.param1, "minggir woy aku mau ngintip" ,contentMetadata={'MSG_SENDER_ICON': "http://dl.profile.line-cdn.net"+client.getContact(op.param2).picturePath,'MSG_SENDER_NAME':  '{}'.format(str(client.getContact(op.param2).displayName))} )
                except:
                    pass
        else:
            pass


        if op.type == 55:
            print ("[ 55 ]NOTIFIED READ MESSAGE")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                else:
                   pass

            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)

    except Exception as error:
        logError(error)
        traceback.print_tb(error.__traceback__)


while True:
    try:
        delete_log()
        ops = clientPoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                clientBot(op)
                clientPoll.setRevision(op.revision)
    except Exception as error:
        logError(error)
        
def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
atexit.register(atend)
