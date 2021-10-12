import speech_recognition as sr
from random import randint
import time
import playsound
from gtts import gTTS, lang
import os
import display
from importlib import reload

class thong_tin():
    def __init__(self,mau,ki_nang):
        self.mau = mau
        self.ki_nang = ki_nang
def lua_skill():
    skill1 = "thăng cấp"
    skill2 = "giảm cấp"
    skill3 = "hoán đổi"
    skill4 = "ăn trộm"
    skill5 = "hút máu"
    choose_skill = randint(1,5)
    if choose_skill == 1:
            choose_skill = skill1
    elif choose_skill == 2:
            choose_skill = skill2
    elif choose_skill == 3:
            choose_skill = skill3
    elif choose_skill == 4:
            choose_skill = skill4
    elif choose_skill == 5:
            choose_skill = skill5
    return choose_skill
def handle():
    playsound.playsound('audio/ok.mp3')
    r = sr.Recognizer()
    with sr.Microphone() as mic:
        print("bot đang nghe")
        audio = r.record(mic, duration=5)
    try:
        text = r.recognize_google(audio, language='vi-VN')
        print(text)
    except:
        print(".....")
    text = input()
    if "ok" or "sẵn sàng" or "rồi" in text:
        playsound.playsound('audio/ok2.mp3')
        chon_skill()
    else:
        display.choose_1()
    

kien = thong_tin(5,lua_skill())
toan = thong_tin(5,lua_skill())
thanh = thong_tin(5,lua_skill())
dong = thong_tin(5,lua_skill())
dat = thong_tin(5,lua_skill())
#tạo đường dẫn tới các file skill

def chon_skill():
    playsound.playsound('audio/choose_skill.mp3')
    time.sleep(1)
    playsound.playsound('audio/goi1.mp3')
    time.sleep(2)
    tts = gTTS(str(kien.ki_nang),lang='vi',slow=False)
    tts.save("audio/skill_kien.mp3")
    playsound.playsound("audio/skill_kien.mp3")
    print(" Đỗ Trung Kiên \n Máu : %d\n Kĩ năng : %s"%(kien.mau,kien.ki_nang))
    
    playsound.playsound('audio/goi2.mp3')
    tts = gTTS(str(toan.ki_nang),lang='vi',slow=False)
    tts.save("audio/skill_toan.mp3")
    playsound.playsound("audio/skill_toan.mp3")
    print(" Đỗ Mạnh Toàn \n Máu : %d\n Kĩ năng : %s"%(toan.mau,toan.ki_nang))

    playsound.playsound('audio/goi3.mp3')
    tts = gTTS(str(thanh.ki_nang),lang='vi',slow=False)
    tts.save("audio/skill_thanh.mp3")
    playsound.playsound("audio/skill_thanh.mp3")
    print(" Nguyễn Danh Thành \n Máu : %d \n Kĩ năng : %s"%(thanh.mau,thanh.ki_nang))
    
    playsound.playsound('audio/goi4.mp3')
    tts = gTTS(str(dong.ki_nang),lang='vi',slow=False)
    tts.save("audio/skill_dong.mp3")
    playsound.playsound("audio/skill_dong.mp3")
    print(" Nguyễn Tiến Đồng \n Máu : %d \n Kĩ năng : %s"%(dong.mau,dong.ki_nang))
    
    playsound.playsound('audio/goi5.mp3')
    tts = gTTS(str(dat.ki_nang),lang='vi',slow=False)
    tts.save("audio/skill_dat.mp3")
    playsound.playsound("audio/skill_dat.mp3")
    print(" Trương Quốc Đạt \n Máu : %d \n Kĩ năng : %s"%(dat.mau,dat.ki_nang))
    
    time.sleep(1)
    playsound.playsound('audio/enter.mp3')

def kien_player():

    if kien.mau < 1:
        playsound.playsound('audio/kien_die.mp3')
        toan_player()
    else:
        playsound.playsound('audio/hoi2.mp3')
        # chuyển giọng nói thành văn bản
        r = sr.Recognizer()
        with sr.Microphone() as mic:
            print("bot đang nghe")
            audio = r.record(mic, duration=5)
        try:
            text = r.recognize_google(audio, language='vi-VN')
            print(text)
        except:
            print(".....")
        text = input()
        if "không" in text:
            toan_player()
        elif "có" or "tấn công" or "đánh" in text:
            playsound.playsound('audio/hoi1.mp3')
            r = sr.Recognizer()
            with sr.Microphone() as mic:
                print("bot đang nghe")
                audio = r.record(mic, duration=5)
            try:
                text = r.recognize_google(audio, language='vi-VN')
                print(text)
            except:
                print(".....")
            text = input()
            if "toàn" in text:
                if kien.ki_nang == "thăng cấp":
                    setattr(kien,"mau",kien.mau + 1)
                    return kien.mau
                elif kien.ki_nang == "giảm cấp":
                    setattr(toan,"mau",toan.mau - 1)
                    return toan.mau
                elif kien.ki_nang == "hoán đổi":
                    setattr(kien,"mau",toan.mau)
                    setattr(toan,"mau",kien.mau)
                    return kien.mau,toan.mau
                elif kien.ki_nang == "ăn trộm":
                    setattr(toan,"mau",toan.mau - 1)
                    setattr(kien,"mau",kien.mau + 1)
                    return toan.mau, kien.mau
                elif kien.ki_nang == "hút máu":
                    if kien.mau == 5:
                        setattr(toan,"mau",toan.mau - 1)
                        setattr(dong,"mau",dong.mau - 1)
                        setattr(thanh,"mau",thanh.mau - 1)
                        setattr(dat,"mau",dat.mau - 1)
                        return kien.mau,toan.mau,dong.mau,thanh.mau,dat.mau
                    elif kien.mau < 5:
                        setattr(kien,"mau",5)
                        setattr(toan,"mau",toan.mau - 1)
                        setattr(dong,"mau",dong.mau - 1)
                        setattr(thanh,"mau",thanh.mau - 1)
                        setattr(dat,"mau",dat.mau - 1)
                        return kien.mau,toan.mau,dong.mau,thanh.mau,dat.mau
                toan_player()
            elif "thành" in text:
                if kien.ki_nang == "thăng cấp":
                    setattr(kien,"mau",kien.mau + 1)
                    return kien.mau
                elif kien.ki_nang == "giảm cấp":
                    setattr(thanh,"mau",thanh.mau - 1)
                    return thanh.mau
                elif kien.ki_nang == "hoán đổi":
                    setattr(kien,"mau",thanh.mau)
                    setattr(thanh,"mau",kien.mau)
                    return kien.mau,thanh.mau
                elif kien.ki_nang == "ăn trộm":
                    setattr(thanh,"mau",thanh.mau - 1)
                    setattr(kien,"mau",kien.mau + 1)
                    return thanh.mau, kien.mau
                elif kien.ki_nang == "hút máu":
                    if kien.mau == 5:
                        setattr(toan,"mau",toan.mau - 1)
                        setattr(dong,"mau",dong.mau - 1)
                        setattr(thanh,"mau",thanh.mau - 1)
                        setattr(dat,"mau",dat.mau - 1)
                        return kien.mau,toan.mau,dong.mau,thanh.mau,dat.mau
                    elif kien.mau < 5:
                        setattr(kien,"mau",5)
                        setattr(toan,"mau",toan.mau - 1)
                        setattr(dong,"mau",dong.mau - 1)
                        setattr(thanh,"mau",thanh.mau - 1)
                        setattr(dat,"mau",dat.mau - 1)
                        return kien.mau,toan.mau,dong.mau,thanh.mau,dat.mau
                toan_player()
            elif "đồng" in text:
                if kien.ki_nang == "thăng cấp":
                    setattr(kien,"mau",kien.mau + 1)
                    return kien.mau
                elif kien.ki_nang == "giảm cấp":
                    setattr(dong,"mau",dong.mau - 1)
                    return dong.mau
                elif kien.ki_nang == "hoán đổi":
                    setattr(kien,"mau",thanh.mau)
                    setattr(dong,"mau",kien.mau)
                    return kien.mau,dong.mau
                elif kien.ki_nang == "ăn trộm":
                    setattr(dong,"mau",dong.mau - 1)
                    setattr(kien,"mau",kien.mau + 1)
                    return dong.mau, kien.mau
                elif kien.ki_nang == "hút máu":
                    if kien.mau == 5:
                        setattr(toan,"mau",toan.mau - 1)
                        setattr(dong,"mau",dong.mau - 1)
                        setattr(thanh,"mau",thanh.mau - 1)
                        setattr(dat,"mau",dat.mau - 1)
                        return kien.mau,toan.mau,thanh.mau.dong.mau,dat.mau
                    elif kien.mau < 5:
                        setattr(kien,"mau",5)
                        setattr(toan,"mau",toan.mau - 1)
                        setattr(dong,"mau",dong.mau - 1)
                        setattr(thanh,"mau",thanh.mau - 1)
                        setattr(dat,"mau",dat.mau - 1)
                        return kien.mau,toan.mau,dong.mau,thanh.mau,dat.mau
                toan_player()
            elif "đạt" in text:
                if kien.ki_nang == "thăng cấp":
                    setattr(kien,"mau",kien.mau + 1)
                    return kien.mau
                elif kien.ki_nang == "giảm cấp":
                    setattr(dat,"mau",dat.mau - 1)
                    return dat.mau
                elif kien.ki_nang == "hoán đổi":
                    setattr(kien,"mau",dat.mau)
                    setattr(dat,"mau",kien.mau)
                    return kien.mau,dat.mau
                elif kien.ki_nang == "ăn trộm":
                    setattr(dat,"mau",dat.mau - 1)
                    setattr(kien,"mau",kien.mau + 1)
                    return dat.mau, kien.mau
                elif kien.ki_nang == "hút máu":
                    if kien.mau == 5:
                        setattr(toan,"mau",toan.mau - 1)
                        setattr(dong,"mau",dong.mau - 1)
                        setattr(thanh,"mau",thanh.mau - 1)
                        setattr(dat,"mau",dat.mau - 1)
                        return kien.mau,toan.mau,thanh.mau,dong.mau,dat.mau
                    elif kien.mau < 5:
                        setattr(kien,"mau",5)
                        setattr(toan,"mau",toan.mau - 1)
                        setattr(dong,"mau",dong.mau - 1)
                        setattr(thanh,"mau",thanh.mau - 1)
                        setattr(dat,"mau",dat.mau - 1)
                        return kien.mau,toan.mau,dong.mau,thanh.mau,dat.mau
        else :
            toan_player()
def toan_player():
    if toan.mau < 0:
      
        playsound.playsound('audio/toan_die.mp3')
        thanh_player()
    else:
        playsound.playsound('audio/hoi3.mp3')
        r = sr.Recognizer()
        with sr.Microphone() as mic:
            print("bot đang nghe")
            audio = r.record(mic, duration=5)
        try:
            text = r.recognize_google(audio, language='vi-VN')
            print(text)
        except:
            print(".....")
        text = input()
        if "không" in text:
            thanh_player()
        elif "có" or "tấn công" or "đánh" in text:
            playsound.playsound('audio/hoi1.mp3')
            r = sr.Recognizer()
            with sr.Microphone() as mic:
                print("bot đang nghe")
                audio = r.record(mic, duration=5)
            try:
                text = r.recognize_google(audio, language='vi-VN')
                print(text)
            except:
                print(".....")
            text = input()
            if "kiên" in text:
                if toan.ki_nang == "thăng cấp":
                    setattr(toan,"mau",toan.mau + 1)
                    return toan.mau
                elif toan.ki_nang == "giảm cấp":
                    setattr(kien,"mau",kien.mau - 1)
                    return kien.mau
                elif toan.ki_nang == "hoán đổi":
                    setattr(kien,"mau",toan.mau)
                    setattr(toan,"mau",kien.mau)
                    return kien.mau,toan.mau
                elif kien.ki_nang == "ăn trộm":
                    setattr(kien,"mau",kien.mau - 1)
                    setattr(toan,"mau",toan.mau + 1)
                    return toan.mau, kien.mau
                elif toan.ki_nang == "hút máu":
                    if toan.mau == 5:
                        setattr(toan,"mau",5)
                        setattr(kien,"mau",kien.mau - 1)
                        setattr(dong,"mau",dong.mau - 1)
                        setattr(thanh,"mau",thanh.mau - 1)
                        setattr(dat,"mau",dat.mau - 1)
                        return kien.mau,toan.mau,dong.mau,thanh.mau,dat.mau
                    elif toan.mau < 5:
                        setattr(toan,"mau",5)
                        setattr(kien,"mau",kien.mau - 1)
                        setattr(dong,"mau",dong.mau - 1)
                        setattr(thanh,"mau",thanh.mau - 1)
                        setattr(dat,"mau",dat.mau - 1)
                        return kien.mau,toan.mau,dong.mau,thanh.mau,dat.mau
                thanh_player()
            elif "thành" in text:
                if toan.ki_nang == "thăng cấp":
                    setattr(toan,"mau",kien.mau + 1)
                    return toan.mau
                elif toan.ki_nang == "giảm cấp":
                    setattr(thanh,"mau",thanh.mau - 1)
                    return thanh.mau
                elif toan.ki_nang == "hoán đổi":
                    setattr(toan,"mau",toan.mau)
                    setattr(thanh,"mau",kien.mau)
                    return toan.mau,thanh.mau
                elif toan.ki_nang == "ăn trộm":
                    setattr(thanh,"mau",thanh.mau - 1)
                    setattr(toan,"mau",toan.mau + 1)
                    return thanh.mau, toan.mau
                elif toan.ki_nang == "hút máu":
                    if toan.mau == 5:
                        setattr(toan,"mau",5)
                        setattr(kien,"mau",kien.mau - 1)
                        setattr(dong,"mau",dong.mau - 1)
                        setattr(thanh,"mau",thanh.mau - 1)
                        setattr(dat,"mau",dat.mau - 1)
                        return kien.mau,toan.mau,dong.mau,thanh.mau,dat.mau
                    elif toan.mau < 5:
                        setattr(toan,"mau",5)
                        setattr(kien,"mau",kien.mau - 1)
                        setattr(dong,"mau",dong.mau - 1)
                        setattr(thanh,"mau",thanh.mau - 1)
                        setattr(dat,"mau",dat.mau - 1)
                        return kien.mau,toan.mau,dong.mau,thanh.mau,dat.mau
                thanh_player()
            elif "đồng" in text:
                if toan.ki_nang == "thăng cấp":
                    setattr(toan,"mau",toan.mau + 1)
                    return toan.mau
                elif toan.ki_nang == "giảm cấp":
                    setattr(dong,"mau",dong.mau - 1)
                    return dong.mau
                elif toan.ki_nang == "hoán đổi":
                    setattr(toan,"mau",dong.mau)
                    setattr(dong,"mau",toan.mau)
                    return toan.mau,dong.mau
                elif toan.ki_nang == "ăn trộm":
                    setattr(dong,"mau",dong.mau - 1)
                    setattr(toan,"mau",toan.mau + 1)
                    return dong.mau, toan.mau
                elif toan.ki_nang == "hút máu":
                    if toan.mau == 5:
                   
                        setattr(kien,"mau",kien.mau - 1)
                        setattr(dong,"mau",dong.mau - 1)
                        setattr(thanh,"mau",thanh.mau - 1)
                        setattr(dat,"mau",dat.mau - 1)
                        return kien.mau,toan.mau,dong.mau,thanh.mau,dat.mau 
                    elif toan.mau < 5:
                        setattr(toan,"mau",5)
                        setattr(kien,"mau",kien.mau - 1)
                        setattr(dong,"mau",dong.mau - 1)
                        setattr(thanh,"mau",thanh.mau - 1)
                        setattr(dat,"mau",dat.mau - 1)
                        return kien.mau,toan.mau,dong.mau,thanh.mau,dat.mau  
                thanh_player()
            elif "đạt" in text:
                if toan.ki_nang == "thăng cấp":
                    setattr(toan,"mau",toan.mau + 1)
                    return toan.mau
                elif toan.ki_nang == "giảm cấp":
                    setattr(dat,"mau",dat.mau - 1)
                    return dat.mau
                elif toan.ki_nang == "hoán đổi":
                    setattr(toan,"mau",dat.mau)
                    setattr(dat,"mau",toan.mau)
                    return toan.mau,dat.mau
                elif toan.ki_nang == "ăn trộm":
                    setattr(dat,"mau",dat.mau - 1)
                    setattr(toan,"mau",toan.mau + 1)
                    return dat.mau, toan.mau
                elif toan.ki_nang == "hút máu":
                    if toan.mau == 5:
                        setattr(kien,"mau",kien.mau - 1)
                        setattr(dong,"mau",dong.mau - 1)
                        setattr(thanh,"mau",thanh.mau - 1)
                        setattr(dat,"mau",dat.mau - 1)
                        return kien.mau,toan.mau,dong.mau,thanh.mau,dat.mau
                    elif toan.mau < 5:
                        setattr(toan,"mau",5)
                        setattr(kien,"mau",kien.mau - 1)
                        setattr(dong,"mau",dong.mau - 1)
                        setattr(thanh,"mau",thanh.mau - 1)
                        setattr(dat,"mau",dat.mau - 1)
                        return kien.mau,toan.mau,dong.mau,thanh.mau,dat.mau
                thanh_player()
        else:
            thanh_player()
def thanh_player():
   
    if thanh.mau < 0:
        playsound.playsound('audio/thanh_die.mp3')
        dong_player()
    else:
        playsound.playsound('audio/hoi4.mp3')
        r = sr.Recognizer()
        with sr.Microphone() as mic:
            print("bot đang nghe")
            audio = r.record(mic, duration=5)
        try:
            text = r.recognize_google(audio, language='vi-VN')
            print(text)
        except:
            print(".....")
        text = input()
        if "không" in text:
            dong_player()
        elif "có" or "tấn công" or "đánh" in text:
            playsound.playsound('audio/hoi1.mp3')
            r = sr.Recognizer()
            with sr.Microphone() as mic:
                print("bot đang nghe")
                audio = r.record(mic, duration=5)
            try:
                text = r.recognize_google(audio, language='vi-VN')
                print(text)
            except:
                print(".....")
            text = input()
            if "toàn" in text:
                if thanh.ki_nang == "thăng cấp":
                    setattr(thanh,"mau",thanh.mau + 1)
                    return thanh.mau
                elif thanh.ki_nang == "giảm cấp":
                    setattr(toan,"mau",toan.mau - 1)
                    return toan.mau
                elif thanh.ki_nang == "hoán đổi":
                    setattr(thanh,"mau",toan.mau)
                    setattr(toan,"mau",thanh.mau)
                    return thanh.mau,toan.mau
                elif thanh.ki_nang == "ăn trộm":
                    setattr(toan,"mau",toan.mau - 1)
                    setattr(thanh,"mau",thanh.mau + 1)
                    return toan.mau, thanh.mau
                elif thanh.ki_nang == "hút máu":
                    if thanh.mau == 5:
                        setattr(toan,"mau",toan.mau - 1)
                        setattr(dong,"mau",dong.mau - 1)
                        setattr(kien,"mau",kien.mau - 1)
                        setattr(dat,"mau",dat.mau - 1)
                        return kien.mau,toan.mau,dong.mau,thanh.mau,dat.mau
                    elif thanh.mau < 5:
                        setattr(thanh,"mau",5)
                        setattr(toan,"mau",toan.mau - 1)
                        setattr(dong,"mau",dong.mau - 1)
                        setattr(kien,"mau",kien.mau - 1)
                        setattr(dat,"mau",dat.mau - 1)
                        return kien.mau,toan.mau,dong.mau,thanh.mau,dat.mau
                dong_player()
            elif "kiên" in text:
                if thanh.ki_nang == "thăng cấp":
                    setattr(thanh,"mau",thanh.mau + 1)
                    return thanh.mau
                elif thanh.ki_nang == "giảm cấp":
                    setattr(kien,"mau",thanh.mau - 1)
                    return kien.mau
                elif thanh.ki_nang == "hoán đổi":
                    setattr(kien,"mau",thanh.mau)
                    setattr(thanh,"mau",kien.mau)
                    return kien.mau,thanh.mau
                elif kien.ki_nang == "ăn trộm":
                    setattr(thanh,"mau",thanh.mau - 1)
                    setattr(kien,"mau",kien.mau + 1)
                    return thanh.mau, kien.mau
                elif kien.ki_nang == "hút máu":
                    if thanh.mau == 5:
                        setattr(thanh,"mau",5)
                        setattr(toan,"mau",toan.mau - 1)
                        setattr(dong,"mau",dong.mau - 1)
                        setattr(thanh,"mau",kien.mau - 1)
                        setattr(dat,"mau",dat.mau - 1)
                        return kien.mau,toan.mau,dong.mau,thanh.mau,dat.mau
                    elif thanh.mau < 5:
                        setattr(thanh,"mau",5)
                        setattr(toan,"mau",toan.mau - 1)
                        setattr(dong,"mau",dong.mau - 1)
                        setattr(thanh,"mau",kien.mau - 1)
                        setattr(dat,"mau",dat.mau - 1)
                        return kien.mau,toan.mau,dong.mau,thanh.mau,dat.mau
                dong_player()
            elif "đồng" in text:
                if thanh.ki_nang == "thăng cấp":
                    setattr(thanh,"mau",thanh.mau + 1)
                    return thanh.mau
                elif thanh.ki_nang == "giảm cấp":
                    setattr(dong,"mau",dong.mau - 1)
                    return dong.mau
                elif thanh.ki_nang == "hoán đổi":
                    setattr(thanh,"mau",dong.mau)
                    setattr(dong,"mau",thanh.mau)
                    return thanh.mau,dong.mau
                elif thanh.ki_nang == "ăn trộm":
                    setattr(dong,"mau",dong.mau - 1)
                    setattr(thanh,"mau",thanh.mau + 1)
                    return dong.mau, thanh.mau
                elif thanh.ki_nang == "hút máu":
                    if thanh.mau == 5:
                        setattr(toan,"mau",toan.mau - 1)
                        setattr(dong,"mau",dong.mau - 1)
                        setattr(kien,"mau",kien.mau - 1)
                        setattr(dat,"mau",dat.mau - 1)
                        return kien.mau,toan.mau,dong.mau,thanh.mau,dat.mau  
                    elif thanh.mau < 5:
                        setattr(thanh,"mau",5)
                        setattr(toan,"mau",toan.mau - 1)
                        setattr(dong,"mau",dong.mau - 1)
                        setattr(kien,"mau",kien.mau - 1)
                        setattr(dat,"mau",dat.mau - 1)
                        return kien.mau,toan.mau,dong.mau,thanh.mau,dat.mau  
                dong_player()
            elif "đạt" in text:
                if thanh.ki_nang == "thăng cấp":
                    setattr(thanh,"mau",thanh.mau + 1)
                    return thanh.mau
                elif thanh.ki_nang == "giảm cấp":
                    setattr(dat,"mau",dat.mau - 1)
                    return dat.mau
                elif thanh.ki_nang == "hoán đổi":
                    setattr(thanh,"mau",dat.mau)
                    setattr(dat,"mau",thanh.mau)
                    return thanh.mau,dat.mau
                elif thanh.ki_nang == "ăn trộm":
                    setattr(dat,"mau",dat.mau - 1)
                    setattr(thanh,"mau",thanh.mau + 1)
                    return dat.mau, thanh.mau
                elif thanh.ki_nang == "hút máu":
                    if thanh.mau == 5:
                        setattr(toan,"mau",toan.mau - 1)
                        setattr(dong,"mau",dong.mau - 1)
                        setattr(kien,"mau",kien.mau - 1)
                        setattr(dat,"mau",dat.mau - 1)
                        return kien.mau,toan.mau,dong.mau,thanh.mau,dat.mau
                    elif thanh.mau < 5:
                        setattr(thanh,"mau",5)
                        setattr(toan,"mau",toan.mau - 1)
                        setattr(dong,"mau",dong.mau - 1)
                        setattr(kien,"mau",kien.mau - 1)
                        setattr(dat,"mau",dat.mau - 1)
                        return kien.mau,toan.mau,dong.mau,thanh.mau,dat.mau
                dong_player()
        else:
            dong_player()
def dong_player():
  
    if dong.mau < 0:
        playsound.playsound('audio/dong_die.mp3')
        dat_player()
    else:
        playsound.playsound('audio/hoi5.mp3')
        r = sr.Recognizer()
        with sr.Microphone() as mic:
            print("bot đang nghe")
            audio = r.record(mic, duration=5)
        try:
            text = r.recognize_google(audio, language='vi-VN')
            print(text)
        except:
            print(".....")
        text = input()
        if "không" in  text:
            dat_player()
        elif "có" or "tấn công" or "đánh" in text:
            playsound.playsound('audio/hoi1.mp3')
            r = sr.Recognizer()
            with sr.Microphone() as mic:
                print("bot đang nghe")
                audio = r.record(mic, duration=5)
            try:
                text = r.recognize_google(audio, language='vi-VN')
                print(text)
            except:
                print(".....")
            text = input()
            if "toàn" in text:
                if dong.ki_nang == "thăng cấp":
                    setattr(dong,"mau",dong.mau + 1)
                    return dong.mau
                elif dong.ki_nang == "giảm cấp":
                    setattr(toan,"mau",toan.mau - 1)
                    return toan.mau
                elif dong.ki_nang == "hoán đổi":
                    setattr(dong,"mau",toan.mau)
                    setattr(toan,"mau",dong.mau)
                    return dong.mau,toan.mau
                elif dong.ki_nang == "ăn trộm":
                    setattr(toan,"mau",toan.mau - 1)
                    setattr(dong,"mau",dong.mau + 1)
                    return toan.mau, dong.mau
                elif dong.ki_nang == "hút máu":
                    if dong.mau == 5:
                        setattr(toan,"mau",toan.mau - 1)
                        setattr(kien,"mau",kien.mau - 1)
                        setattr(thanh,"mau",thanh.mau - 1)
                        setattr(dat,"mau",dat.mau - 1)
                        return dong.mau,toan.mau,dong.mau,thanh.mau,dat.mau
                    elif dong.mau < 5:
                        setattr(dong,"mau",5)
                        setattr(toan,"mau",toan.mau - 1)
                        setattr(kien,"mau",kien.mau - 1)
                        setattr(thanh,"mau",thanh.mau - 1)
                        setattr(dat,"mau",dat.mau - 1)
                        return dong.mau,toan.mau,dong.mau,thanh.mau,dat.mau
               
                dat_player()
            elif "thành" in text:
                if dong.ki_nang == "thăng cấp":
                    setattr(dong,"mau",dong.mau + 1)
                    return dong.mau
                elif dong.ki_nang == "giảm cấp":
                    setattr(thanh,"mau",thanh.mau - 1)
                    return thanh.mau
                elif dong.ki_nang == "hoán đổi":
                    setattr(dong,"mau",thanh.mau)
                    setattr(thanh,"mau",dong.mau)
                    return dong.mau,thanh.mau
                elif dong.ki_nang == "ăn trộm":
                    setattr(thanh,"mau",thanh.mau - 1)
                    setattr(dong,"mau",dong.mau + 1)
                    return thanh.mau, dong.mau
                elif dong.ki_nang == "hút máu":
                    if dong.mau == 5:
                        setattr(toan,"mau",toan.mau - 1)
                        setattr(kien,"mau",kien.mau - 1)
                        setattr(thanh,"mau",thanh.mau - 1)
                        setattr(dat,"mau",dat.mau - 1)
                        return dong.mau,toan.mau,dong.mau,thanh.mau,dat.mau
                    elif dong.mau < 5:
                        setattr(dong,"mau",5)
                        setattr(toan,"mau",toan.mau - 1)
                        setattr(kien,"mau",kien.mau - 1)
                        setattr(thanh,"mau",thanh.mau - 1)
                        setattr(dat,"mau",dat.mau - 1)
                        return dong.mau,toan.mau,dong.mau,thanh.mau,dat.mau
                dat_player()
            elif "kiên" in text:
                if dong.ki_nang == "thăng cấp":
                    setattr(dong,"mau",dong.mau + 1)
                    return dong.mau
                elif dong.ki_nang == "giảm cấp":
                    setattr(kien,"mau",kien.mau - 1)
                    return kien.mau
                elif dong.ki_nang == "hoán đổi":
                    setattr(dong,"mau",kien.mau)
                    setattr(kien,"mau",dong.mau)
                    return dong.mau,kien.mau
                elif dong.ki_nang == "ăn trộm":
                    setattr(kien,"mau",kien.mau - 1)
                    setattr(dong,"mau",dong.mau + 1)
                    return dong.mau, kien.mau
                elif dong.ki_nang == "hút máu":
                    if dong.mau == 5:
                        setattr(toan,"mau",toan.mau - 1)
                        setattr(kien,"mau",kien.mau - 1)
                        setattr(thanh,"mau",thanh.mau - 1)
                        setattr(dat,"mau",dat.mau - 1)
                        return dong.mau,toan.mau,dong.mau,thanh.mau,dat.mau  
                    elif dong.mau < 5:
                        setattr(dong,"mau",5)
                        setattr(toan,"mau",toan.mau - 1)
                        setattr(kien,"mau",kien.mau - 1)
                        setattr(thanh,"mau",thanh.mau - 1)
                        setattr(dat,"mau",dat.mau - 1)
                        return dong.mau,toan.mau,dong.mau,thanh.mau,dat.mau  
                dat_player()
            elif "đạt" in text:
                if dong.ki_nang == "thăng cấp":
                    setattr(dong,"mau",dong.mau + 1)
                    return dong.mau
                elif dong.ki_nang == "giảm cấp":
                    setattr(dat,"mau",dat.mau - 1)
                    return dat.mau
                elif dong.ki_nang == "hoán đổi":
                    setattr(dong,"mau",dat.mau)
                    setattr(dat,"mau",dong.mau)
                    return dong.mau,dat.mau
                elif dong.ki_nang == "ăn trộm":
                    setattr(dat,"mau",dat.mau - 1)
                    setattr(dong,"mau",dong.mau + 1)
                    return dat.mau, dong.mau
                elif dong.ki_nang == "hút máu":
                    if dong.mau == 5:
                        setattr(toan,"mau",toan.mau - 1)
                        setattr(kien,"mau",kien.mau - 1)
                        setattr(thanh,"mau",thanh.mau - 1)
                        setattr(dat,"mau",dat.mau - 1)
                        return dong.mau,toan.mau,dong.mau,thanh.mau,dat.mau
                    elif dong.mau < 5:
                        setattr(dong,"mau",5)
                        setattr(toan,"mau",toan.mau - 1)
                        setattr(kien,"mau",kien.mau - 1)
                        setattr(thanh,"mau",thanh.mau - 1)
                        setattr(dat,"mau",dat.mau - 1)
                        return dong.mau,toan.mau,dong.mau,thanh.mau,dat.mau
                dat_player()
        else:
            dat_player()         
def dat_player(): 
    
    if dat.mau < 0:
        playsound.playsound('audio/dat_die.mp3')
    else:
        playsound.playsound('audio/hoi6.mp3')
        r = sr.Recognizer()
        with sr.Microphone() as mic:
            print("bot đang nghe")
            audio = r.record(mic, duration=5)
        try:
            text = r.recognize_google(audio, language='vi-VN')
            print(text)
        except:
            print(".....")
        text = input()
        if "không" in text:
            kien_player()
        elif "có" or "tấn công" or "đánh" in text:
            playsound.playsound('audio/hoi1.mp3')
            r = sr.Recognizer()
            with sr.Microphone() as mic:
                print("bot đang nghe")
                audio = r.record(mic, duration=5)
            try:
                text = r.recognize_google(audio, language='vi-VN')
                print(text)
            except:
                print(".....")
            text = input()
            if "toàn" in text:
                if dat.ki_nang == "thăng cấp":
                    setattr(dat,"mau",dat.mau + 1)
                    return dat.mau
                elif dat.ki_nang == "giảm cấp":
                    setattr(toan,"mau",toan.mau - 1)
                    return toan.mau
                elif dat.ki_nang == "hoán đổi":
                    setattr(dat,"mau",toan.mau)
                    setattr(toan,"mau",dat.mau)
                    return dat.mau,toan.mau
                elif dat.ki_nang == "ăn trộm":
                    setattr(toan,"mau",toan.mau - 1)
                    setattr(dat,"mau",dat.mau + 1)
                    return toan.mau, dat.mau
                elif dat.ki_nang == "hút máu":
                    if dat.mau == 5:
                        setattr(toan,"mau",toan.mau - 1)
                        setattr(kien,"mau",kien.mau - 1)
                        setattr(thanh,"mau",thanh.mau - 1)
                        setattr(dat,"mau",dat.mau - 1)
                        return dat.mau,toan.mau,dat.mau,thanh.mau,dat.mau     
                    elif dat.mau < 5:
                        setattr(dat,"mau",5)
                        setattr(toan,"mau",toan.mau - 1)
                        setattr(kien,"mau",kien.mau - 1)
                        setattr(thanh,"mau",thanh.mau - 1)
                        setattr(dat,"mau",dat.mau - 1)
                        return dat.mau,toan.mau,dat.mau,thanh.mau,dat.mau     
                kien_player()
            elif "thành" in text:
                if dat.ki_nang == "thăng cấp":
                    setattr(dat,"mau",dat.mau + 1)
                    return dat.mau
                elif dat.ki_nang == "giảm cấp":
                    setattr(thanh,"mau",thanh.mau - 1)
                    return thanh.mau
                elif dat.ki_nang == "hoán đổi":
                    setattr(dat,"mau",thanh.mau)
                    setattr(thanh,"mau",dat.mau)
                    return dat.mau,thanh.mau
                elif dat.ki_nang == "ăn trộm":
                    setattr(thanh,"mau",thanh.mau - 1)
                    setattr(dat,"mau",dat.mau + 1)
                    return thanh.mau, dat.mau
                elif dat.ki_nang == "hút máu":
                    if dat.mau == 5:
                        setattr(toan,"mau",toan.mau - 1)
                        setattr(kien,"mau",kien.mau - 1)
                        setattr(thanh,"mau",thanh.mau - 1)
                        setattr(dat,"mau",dat.mau - 1)
                        return dat.mau,toan.mau,dat.mau,thanh.mau,dat.mau
                    elif dat.mau < 5:
                        setattr(dat,"mau",5)
                        setattr(toan,"mau",toan.mau - 1)
                        setattr(kien,"mau",kien.mau - 1)
                        setattr(thanh,"mau",thanh.mau - 1)
                        setattr(dat,"mau",dat.mau - 1)
                        return dat.mau,toan.mau,dat.mau,thanh.mau,dat.mau
                
                kien_player()
            elif "đồng" in text:
                if dat.ki_nang == "thăng cấp":
                    setattr(dat,"mau",dat.mau + 1)
                    return dat.mau
                elif dat.ki_nang == "giảm cấp":
                    setattr(dat,"mau",dat.mau - 1)
                    return dat.mau
                elif dat.ki_nang == "hoán đổi":
                    setattr(dat,"mau",thanh.mau)
                    setattr(dat,"mau",dat.mau)
                    return dat.mau,dat.mau
                elif dat.ki_nang == "ăn trộm":
                    setattr(dat,"mau",dat.mau - 1)
                    setattr(dat,"mau",dat.mau + 1)
                    return dat.mau, dat.mau
                elif dat.ki_nang == "hút máu":
                    if dat.mau == 5:
                        setattr(toan,"mau",toan.mau - 1)
                        setattr(kien,"mau",kien.mau - 1)
                        setattr(thanh,"mau",thanh.mau - 1)
                        setattr(dat,"mau",dat.mau - 1)
                        return dat.mau,toan.mau,dat.mau,thanh.mau,dat.mau    
                    elif dat.mau < 5:
                        setattr(dat,"mau",5)
                        setattr(toan,"mau",toan.mau - 1)
                        setattr(kien,"mau",kien.mau - 1)
                        setattr(thanh,"mau",thanh.mau - 1)
                        setattr(dat,"mau",dat.mau - 1)
                        return dat.mau,toan.mau,dat.mau,thanh.mau,dat.mau    
                kien_player()
            elif "kiên" in text:
                if dat.ki_nang == "thăng cấp":
                    setattr(dat,"mau",dat.mau + 1)
                    return dat.mau
                elif dat.ki_nang == "giảm cấp":
                    setattr(kien,"mau",kien.mau - 1)
                    return kien.mau
                elif dat.ki_nang == "hoán đổi":
                    setattr(dat,"mau",kien.mau)
                    setattr(kien,"mau",dat.mau)
                    return dat.mau,kien.mau
                elif dat.ki_nang == "ăn trộm":
                    setattr(kien,"mau",kien.mau - 1)
                    setattr(dat,"mau",dat.mau + 1)
                    return dat.mau, kien.mau
                elif dat.ki_nang == "hút máu":
                    if dat.mau == 5:
                        setattr(toan,"mau",toan.mau - 1)
                        setattr(kien,"mau",kien.mau - 1)
                        setattr(thanh,"mau",thanh.mau - 1)
                        setattr(dong,"mau",dong.mau - 1)
                        return dat.mau,toan.mau,dat.mau,thanh.mau,dat.mau
                    elif dat.mau < 5:
                        setattr(dat,"mau",5)
                        setattr(toan,"mau",toan.mau - 1)
                        setattr(kien,"mau",kien.mau - 1)
                        setattr(thanh,"mau",thanh.mau - 1)
                        setattr(dong,"mau",dong.mau - 1)
                        return dat.mau,toan.mau,dat.mau,thanh.mau,dat.mau
                        
                kien_player()
        else:
            kien_player()         

def main():
    handle()
    while True:
            kien_player()
            print(" Máu Kiên : %d\n Máu Toàn : %d\n Máu Thành : %d\n Máu Đồng : %d\n Máu Đạt : %d"%(kien.mau,toan.mau,thanh.mau,dong.mau,dat.mau))  
            toan_player()
            print(" Máu Kiên : %d\n Máu Toàn : %d\n Máu Thành : %d\n Máu Đồng : %d\n Máu Đạt : %d"%(kien.mau,toan.mau,thanh.mau,dong.mau,dat.mau))  
            thanh_player()
            print(" Máu Kiên : %d\n Máu Toàn : %d\n Máu Thành : %d\n Máu Đồng : %d\n Máu Đạt : %d"%(kien.mau,toan.mau,thanh.mau,dong.mau,dat.mau))  
            dong_player()
            print(" Máu Kiên : %d\n Máu Toàn : %d\n Máu Thành : %d\n Máu Đồng : %d\n Máu Đạt : %d"%(kien.mau,toan.mau,thanh.mau,dong.mau,dat.mau))  
            dat_player()
            print(" Máu Kiên : %d\n Máu Toàn : %d\n Máu Thành : %d\n Máu Đồng : %d\n Máu Đạt : %d"%(kien.mau,toan.mau,thanh.mau,dong.mau,dat.mau))
            thong_ke = " Máu Kiên : %d\n Máu Toàn : %d\n Máu Thành : %d\n Máu Đồng : %d\n Máu Đạt : %d"%(kien.mau,toan.mau,thanh.mau,dong.mau,dat.mau)
            thong_ke = str(thong_ke)
            sumary = open("data\\sumary.txt",mode='w',encoding='UTF-8')
            sumary.write(thong_ke) 
            sumary.close() 
            playsound.playsound("audio/pause.mp3")
            display.sumary_end()
            time.sleep(8)
            
