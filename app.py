from flask import Flask,render_template,request
from playsound import playsound
import subprocess
import random


app = Flask(__name__)

option={
      "song.mp3":["pal pal","khwaab","duniya","tu hai kaha"],
     
    "song2.mp3":["tu jane na","kya","teri zuki najar","maula mere"],
    "song3.mp3": ["itna na muzse","mere mehboob","saiyara","gulabi aankhe"],
    "song4.mp3":["gulabi aankhe","ye rate ye mausam","pal pal dil ke pas","kahi dur jab"], 
    "song5.mp3": ["mere rashke kamar","ek mulakat","dekhte dekhte","kya"],
    "song6.mp3": ["teri meri","ishq sufiyana","abhi kuchh dino se","i love you"],
    "song7.mp3": ["teri meri","pani da","teri zhuki najar","dekhte dekhte"],
    "song8.mp3": ["ishq sufiyana","khwaab","pal pal","tu mera"],
    "song9.mp3":["dekhte dekhte","mere rashke kamar","sathiya","teri meri"],
    "song10.mp3":["pani da","kaise hua","teri meri","kalank"],
    "song11.mp3":["khwaab","abhi kuchh dino se","tu jane na","sathiya"],
     "song12.mp3":["hosh walo ko","yeh tune kya kiya","fida","ek mulakat"],
     "song13.mp3":["kya","ban ja tu meri","duniya","khaab"],
      "song14.mp3":["duniya","khaab","teri aur","kya"],
      "song15.mp3":["duniya","ek mulakat","o sathi","dekhte dekhte"],
       "song16.mp3":["pani da rang","khabar nahi","afreen","tu hi tu"],
       "song17.mp3":["paniyo sa","mai tera","teri aur","duniya"],
        "song18.mp3":["dil diya gallan","khabar nahi","duniya","sehmi hai dhadakan"]


}
SONGS = {
    "song.mp3": "pal pal",
    "song2.mp3": "kya",
    "song3.mp3": "mere mehboob",
    "song4.mp3": "gulabi",
    "song5.mp3": "mere rashke kamar",
    "song6.mp3": "i love you",
    "song7.mp3": "teri meri",
    "song8.mp3": "ishq sufiyana",
    "song9.mp3": "dekhte dekhte",
    "song10.mp3": "kaise hua",
    "song11.mp3":"abhi kuchh dino se",
    "song12.mp3":"hosh walo ko",
    "song13.mp3":"ban ja tu meri",
    "song14.mp3":"duniya",
    "song15.mp3":"o sathi",
    "song16.mp3":"pani da rang",
    "song17.mp3":"paniyo sa",
    "song18.mp3":"sehmi hai dhadakan"

}
current_song=None
remaining_songs=(list(SONGS.keys()))
 
score=0
def play(filename):

    return subprocess.run(["ffplay", "-nodisp", "-autoexit", "-t", "5", filename])

 
 
@app.route("/",methods=["GET","POST"])
def index():
      global remaining_songs
      global  score
      global op
      global  file
      global again
      again=None
      file=None

      op=None
      
      message=None
      song_played=False
      global current_song
      if request.method=="POST":
          if "play" in request.form:
                 if len(remaining_songs)==0:
                         
                         again="playing again"
                         remaining_songs=(list(SONGS.keys()))
                  
                     
                   
                 current_song = random.choice(remaining_songs)

                 remaining_songs.remove(current_song)
                 play(f"static/{current_song}")
                 song_played=True
                
                 op=option[current_song]
          elif "guess" in request.form:
                if current_song is None:
                     message="play the song please"
                # user_guess=request.form["guess"].strip().lower()
                
                else:
                      
                     user_guess = request.form["guess"].strip().lower()
                     correct_answer = SONGS[current_song].lower()
                     
                     if user_guess==correct_answer:
                          score+=10
                          message="yeh you got it !"
                          file="geuss1i.jpg"

                     else:
                           message="you got a wrong tune!"
                           file="guess3.png"
    #   if request.method=="POST":
            
      return render_template("index.html",message=message,score=score,op=op,file=file)
       
 