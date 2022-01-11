import random 
import sys
import time

def printy(text, delay=0.045):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def printyl(text, delay=0.02):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

hangman =['''

    ==========
    |       ||
            ||
            ||
            ||
            ||
            ||
            ||
            ||
          ======''' , 
'''

    ==========
    |       ||
    O       ||
            ||
            ||
            ||
            ||
            ||
            ||
          ======''' , '''

    ==========
    |       ||
    O       ||
    |       ||
            ||
            ||
            ||
            ||
            ||
          ======''' , '''

    ==========
    |       ||
    O       ||
    |       ||
    |       ||
            ||
            ||
            ||
            ||
          ======''' , '''

    ==========
    |       ||
    O       ||
    |       ||
    |       ||
   /        ||
            ||
            ||
            ||
          ======''' , '''

    ==========
    |       ||
    O       ||
    |       ||
    |       ||
   /        ||
  |         ||
            ||
            ||
          ======''' , '''

    ==========
    |       ||
    O       ||
    |       ||
    |       ||
   / \      ||
  |         ||
            ||
            ||
          ======''', '''

    ==========
    |       ||
    O       ||
    |       ||
    |       ||
   / \      ||
  |   |     ||
            ||
            ||
          ======''', '''

    ==========
    |       ||
    O       ||
    |\      ||
    |       ||
   / \      ||
  |   |     ||
            ||
            ||
          ======''', '''

    ==========
    |       ||
    O       ||
    |\      ||
    | \     ||
   / \      ||
  |   |     ||
            ||
            ||
          ======''', '''

    ==========
    |       ||
    O       ||
   /|\      ||
    | \     ||
   / \      ||
  |   |     ||
            ||
            ||
          ======''', '''

    ==========
    |       ||
    O       ||
   /|\      ||
  / | \     ||
   / \      ||
  |   |     ||
            ||
            ||
          ======'''
]
#^Rosendo

# Word Lists
gamelist = ["roblox", "fortnite", "minecraft", "pubg battlegrounds", "free fire", "geometry dash", "assassin's creed", "league of legends", "grand theft auto", "overwatch", "super mario", "bomberman", "call of duty", "dark souls", "rocket league", "forza horizon", "apex legends", "valorant", "resident evil", "among us", "pokemon", "halo infinite", "battlefield", "cyberpunk", "destiny","Animal crossing","fifa","maden nfl","life is strange","pac-man","god of war","stardew valley","nba","world of warcraft","terraria","tetris","ark: survival evolved","the legend of zelda","watch dogs","sea of thieves","red dead redemption","genshin impact","super smash bros","mario kart","the last of us","bioshock","spider-man","half-life","the witcher","space invaders","wii sports","pong","dark souls","metal gear solid","doom","street fighter","final fantasy","portal","silent hill","dota"]

fruitlist = ["apple","avocado","acerola","apricots","banana","blueberries","blackberries","blackcurrant","breadfruit","coconut","cherries","cantaloupe","carambola","cherimoya","clementine","cranberries","date fruit","durian","elderberries","feijoa","figs","grape","gooseberries","grapefruit","guava","honeydew melon","jackfruit","java-plum","jujube fruit","mango","kiwi","kumquat","lemon","lime","longan","loquat","lychee","mandarin","mangosteen","mulberries","nectarine","olives","orange","papaya","passion fruit","persimmon","dragonfruit","pineapple","pitanga","plantain","plums","pomegranate","prickly Pear","prunes","pummelo","quince","raspberries","rhubarb","rose-apple","sapodilla","sapote","mamey","soursop","sugar-apple","tamarind""strawberry","peaches","pear","watermelon","asparagus","beans","beetroot","broccoli","brussels sprouts","cabbage","carrot","cauliflower","celery","corn","cucumber","eggplant","lettuce"]

countrylist = ["afghanistan", "albania", "algeria", "andorra", "angola", "argentina", "armenia", "autralia", "austria", "azerbaijan", "bahamas", "bahrain", "bangladesh", "barbados", "belarus", "belgium", "belize", "benin", "bhutan", "bolivia", "botswana", "brazil", "brunei", "bulgaria", "burkina faso", "burundi", "cote d'lvoire", "cabo verde", "cambodia", "cameroon", "canada", "central africa republic", "chad", "chile", "china", "colombia", "comoros", "congo", "costa rica", "croatia", "cuba", "cyprus", "czechia", "democratic republic of congo", "denmark", "djibouti", "dominica", "dominican republic", "ecuador", "egypt", "el salvador", "equatorial guinea", "eritrea", "estonia", "eswatini", "ethiopia", "fiji", "finland", "france", "france", "gabon", "gambia", "georgia", "germany", "ghana", "greece", "grenada", "guatemala", "guinea", "guyana", "haiti", "hosy see", "honduras", "hungary", "iceland", "india", "indonesia", "iran", "iraq", "ireland", "israel", "italy", "jamaica", "japan", "jordan" , "kazakhstan" , "kenya" , "kiribati", "kuwait" , "kyrgyzstan" , "laos" , "latvia", "levanon", "lesotho", "liberia", "libya", "liechtenstein", "lithuania", "luxembourg" , "madagascar", "malawi", "malaysia", "maldives", "mali", "malta", "marshall islands", "mauritania", "mexico", "micronesia", "moldova", "monaco", "mongolia", "montenegro", "morocco", "mozambique", "myanmar", "namibia", "nauru", "nepal", "netherlands", "new zealand", "nicaragua", "niger", "nigeria", "north korea", "north macedonia", "norway", "oman", "pakistan", "palau", "palestine state", "panama", "papua new guinea", "paraguay", "peru", "philippines", "poland", "portugal", "qatar", "romania", "russia", "rwanda", "saint kitts and nevis", "saint lucia", "saint vincent and the grenadines", "samoa", "san marino", "sao tome and principe", "saudi arabia", "senegal", "serbia", "seychelles", "sierra loene", "singapore", "slovakia", "slovenia", "solomond islands", "somalia", "south africa","south korea", "south sudan", "spain", "sri lanka", "sudan", "suriname", "sweeden", "switzerland", "syria", "tajikistan", "tanzania", "thailand", "timor-leste", "togo", "tonga", "trinidad and tobago", "tunisia", "turkey", "turkmenistan", "tuvalu", "uganda", "ukraine", "united arab emirates", "united kingdom", "united states of america", "uruguay", "uzbekistan", "vanuatu", "venezuela", "vietnam", "yemen", "zambia", "zimbabwe"]
# ^Both

again='y'
wordsg=0
lettersg=1
lettersgw=0

time.sleep(0.5)
printy("Welcome to Hangman")
time.sleep(0.5)
printy("You have to guess each letter of the word, all lowercase, signs and contais spaces.")
time.sleep(0.5)
printy("You only have 13 lives (stages), if one letter is not correct you lose a live")
time.sleep(0.5)
printy("Spaces, ', and : all count as letters")
printy("Would you like to play with games, fruits and veggies, or countries?")

while again=='y':
  time.sleep(.3)
  printy("\nType 'g' for a game, 'f' for a fruits and veggies, or 'c' for a country")
  listselected = input("-")
  while True :
    if listselected.lower() == "g" :
      time.sleep(0.5)
      printy("Nice, lets do games then: \n")
      secretword = random.choice(gamelist)
      break
    elif listselected.lower() == "f" :
      time.sleep(0.5)
      printy("Nice, lets do fruits: \n")
      secretword = random.choice(fruitlist)
      break
    elif listselected.lower() == "c" :
      time.sleep(0.5)
      printy("Nice, lets do countries: \n")
      secretword = random.choice(countrylist)
      break
    else :
      printy("That's not a list, plese insert a valid letter: \n")
      time.sleep(0.5)
      listselected = input("\nType 'G' for a game, 'F' for a fruit, or 'C' for a country:\n-")
      time.sleep(0.5)
  #^Rosendo
  n=0
  lives = 12
  ltg = []
    
  printy('_' * len(secretword))

  lettersg-=1
  while True:
    while True:
      time.sleep(0.3)
      printyl("Guess a letter or the word:")
      galow = input("-")
      if(len(galow) >= 1 and galow.isnumeric()) :
        time.sleep(0.3)
        printy("That's not a letter, try with a letter: \n")
      else :
        if galow in ltg :
          time.sleep(0.3)
          printy("You already tried with that one, try with a different one: \n")
        else :
          ltg.append(galow)
          if galow==secretword:
            break
          elif galow in secretword :
            time.sleep(0.1)
            printyl("Congratulation! You guessed a letter")
            lettersg+=1
            break

          else :
            lives = lives - 1
            printyl("You are wrong and lose a life")
            time.sleep(0.15)
            printyl("You one have " + str(lives) + " attempts left")
            time.sleep(0.15)
            print(hangman[n])
            time.sleep(0.15)
            lettersgw+=1
            n+=1
            break
            
    print
    if lives==0 :
      printy("You lose, the secret word was: " + secretword)
      time.sleep(0.3)
      printy("Words guess correctly= ",wordsg)
      time.sleep(0.3)
      break
    #^Both
    actualstatus = ""
    missingletter = 0 

    for word in secretword :
      
      if word in ltg :
        actualstatus = actualstatus + word
      else :
        actualstatus = actualstatus + "_"
        missingletter = missingletter + 1

    if galow==secretword:
      missingletter=0
    printy(actualstatus)

    if missingletter == 0 :
      printy("Congratulations! You win")
      time.sleep(0.3)
      printy("The secret word is: " + secretword)
      if listselected == "g" :
        gamelist.remove(secretword)
      elif listselected == "f" :
        fruitlist.remove(secretword)
      elif listselected == "c" :
        countrylist.remove(secretword)
      break
      #^Rosendo
  wordsg+=1
  lettersg-=1
  printy("\nDo you want to play again('y' or 'n')")
  again=input("-")
  time.sleep(0.3)
  
  if again=='n':
    printy("\nLetters guessed correctly=",lettersg)
    time.sleep(0.3)
    printy("Letters guessed incorrectly=",lettersgw)
    time.sleep(0.3)
    printy("Words guessed correctly=",wordsg)
    time.sleep(0.3)
    printy("Goodbye!")
    time.sleep(0.3)
    
  #^Logan



  #Logan worked on fixing up the code fixing errors and adding loops
  #Rosendo worked on most main code and lists