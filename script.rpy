# defining all the characters:

define m = Character("Marta")
define j = Character("Juli")
define J = Character("Jack")
define d = Character("Dad")
define M = Character("Mom")
define f = Character("Mrs.carter")

# these are the sprites of the charcters:

# marta (our main character)
image marta_annoyed = "images/marta_annoyed.png"
image marta_normal = "images/marta_normal.png"
image marta_sad = "images/marta_sad.png"
image marta_smile = "images/marta_smile.png"

# mom (marta's mom)
image mom = "images/mom.png"

# dad (jack's dad or :o)
image dad_angry= "images/dad_angry.png"
image dad_normal="images/dad_normal.png"
image dad_shocked = "images/dad_shocked.png"

# juli 
image juli_sad = "images/juli_sad.png"
image juli_normal = "images/juli_normal.png"
image juli_shocked = "images/juli_shocked.png"

# mrs.carter
image mrs_normal="images/mrscarter_normal.png"
image mrs_angry="images/mrscarter_angry.png"

# jack ( so called)
image jack_angry="images/jack_angry.png"
image jack_gym = "images/jack_gym.png"
image jack_normal = "images/jack_normal.png"
image jack_sad = "images/jack_sad.png"
image jack_shocked = "images/jack_shocked.png"

# now bg:

image class="images/class.png"
image bedroom="images/bedroom.png"
image gym ="images/gym.png"
image hallway="images/hallway.png"
image street = "images/street.png"
image forest = "images/forest.png"
image bridge = "images/bridge.png"


# scene 1 : 
label start:
    play music "audio/normal.mp3"
        
    scene hallway with fade
    j "He's so hot...... I'd die to get him"

    show juli_normal at left:
            zoom 0.7
    j "Aghh.. Why doesn't he look at me"     

    show marta_sad at right:
            zoom 0.7   
    m "Proably cuz 'the rumours are real' "
    m "And he has a girlfriend in college "
    hide juli_normal
    show juli_sad at left:
            zoom 0.7
    j "Stop marta, my heart says he will be mine"
    m "Then keep dreaming juli, its been 6 months"
    j "onedayy he'll.."
    m "Let's go... we are late to mrs.carter's class"

    hide marta_sad
    hide juli_sad


# scene 2 :

    scene class with fade 
    show mrs_angry at left:
            zoom 0.7
    f "Come in girls, you guys are always late."
    show marta_annoyed at right:
            zoom 0.7   
    m "Sorry, Mrs.carter we were at the nurse's room "
    hide marta_annoyed
    hide mrs_angry


    show mrs_normal at left:
            zoom 0.7
    f "Ok, class today we are studying about the ....."
    show jack_normal at right:
            zoom 0.7
    J "Good morning!!!!!, Mrs.carter"
    f "Class.. I totally forgot this is our new student for senior year :Jack"
    hide mrs_normal
    hide jack_normal

    show juli_shocked at right:
        zoom 0.7
    show marta_smile at left:
        zoom 0.7

    "Seeing jack, marta felt a chill in her heart"
    m "damn, look at him "
    j "I'm..... he's so good looking"
    hide marta_smile
    hide juli_shocked
    show juli_normal at right:
        zoom 0.7
    show marta_annoyed at left:
        zoom 0.7
    m "NO NO , he's mine.... don't look at him"
    m "Weren't you saying james is your true love and heart!!!!!"
    j "Yea Yea......🙄"
    hide marta_annoyed
    hide juli_normal

    show mrs_angry at center:
        zoom 0.7
    f "Anything special??? girls!!!!!" 
    f "That's it. First you are late then you disturb the class"
    f "DETENTION!!!!!!!!"  
    hide mrs_angry 

    scene hallway with fade 
    show marta_annoyed at left:
        zoom 0.7
    m "This Mrs.carter, always has a problem with us and this our 3rd detention this week"
    show juli_normal at right:
        zoom 0.7
    j "No wayyyy!!! we're not gonna stay at all"
    j " Maybe we should stay slient all day, I don't want another detention"

    hide marta_annoyed
    show marta_sad at left:
        zoom 0.7
    m "Yea, I have english now, I should go"
    j "Ohh yea, I have spanish too"    

    hide marta_sad
    hide juli_normal

    #scene 3:
    scene class with fade 
    show marta_smile at left:
        zoom 0.7
    m "Maybe the last bench or mid......."   
    show jack_sad at right :
        zoom 0.7
    J "Is this Mr.Brown's english class?"  
    m "Yes!!"  


    menu:
        "Talk with him":
            m "Is there are thing, you look kinda sad"
            J "No, nothing. I jus... miss my old"
            hide jack_sad
            show jack_normal at right:
                zoom 0.7
            J "Aren't you the girl that got detention today??"
            hide marta_smile
            show marta_annoyed at left:
                zoom 0.7
            m "Yea....🙄"       
            "Shit he embarrassed  you 💀"
            hide marta_annoyed
            hide jack_normal

        "Take a sit":
            hide jack_sad
            show marta_normal at left:
                zoom 0.7
            m "Shit, I should have talked with him"
            show jack_sad at right:
                zoom 0.7
            J "Can I sit next to you??"
            m "Ofcc, Jack"
            J "How do you know my name?"
            hide jack_sad
            show jack_normal at right:
                zoom 0.7
            J "Oh, you're the gurl that got dentention today"
            hide marta_normal
            hide jack_normal
            show marta_annoyed at left:
                zoom 0.7
            m "yea"       
            "Shit embarrassing 💀"
            hide marta_annoyed

#scene 4 :
    scene gym with fade 
    show mrs_angry at center:
        zoom 0.7
    f "Kids nowdays.... didn't expect sasha to be like this"
    f "And now these girls....aghhh....why did I even become a teacher????"
    hide mrs_angry
    show marta_smile at left:
        zoom 0.7
    m "Last class of today........"

    show juli_normal at right:
        zoom 0.7
    j "Yeaaaaaaa"
    m "Btw today, I talked with Jack, hehehhe"
    j "whatt????"
    m "yea, it was quite embarrassing but atleast I see some possiblities!!"   
    show mrs_angry at center:
        zoom 0.7
    f "Girls again!!!!!!! you guys will now get 2 weeks of dentention!!!!"
    hide marta_smile
    show marta_annoyed at left:
        zoom 0.7
    m "Yea yea, sorry ig"
    f "Okxs, everyone 10 laps of the ground and 20 laps for marta and juli"
    hide mrs_angry
    hide juli_normal

    show juli_shocked at center:
        zoom 0.7
    j "What????"        
    m "Let's run away after school, we won't stay in detention"

# scene 5:
    scene hallway with fade 
    show marta_normal at center:
        zoom 0.7
    m "They have locked the doors"
    show juli_sad at left:
        zoom 0.7
    j "Shit, now 2 hrs in detention"
    hide marta_normal
    show marta_annoyed at center:
        zoom 0.7
    m "Yea....shit"
    show jack_normal at right:
        zoom 0.7
    hide juli_sad
    show juli_shocked at left:
        zoom 0.7      
    J "ohh..hello"
    j "You are in detention???"
    J "yes...I didn't run 10 laps "
    m "Mrs.carter has gone crazy for sure"
    hide juli_shocked
    hide jack_normal

    scene class with fade 
    show mrs_angry at center:
        zoom 0.7
    f "Everyone stay here and don't go anywhere"
    f "I'll be right back!!"
    hide mrs_angry

    show jack_normal at center:
        zoom 0.7
    J "shit"    
    hide jack_normal
    show marta_normal at left:
        zoom 0.7

    "whisper"    
    m "Blood in his pants"  
    show juli_shocked at right:
        zoom 0.7
    j "yea, what is that"
    j "Maybe ask him"
    stop music
    menu:
        play music "audio/calm.mp3"
        "Ask him":
            hide juli_shocked
            m "hey... jack .... there's something like blood in your pants"
            show jack_shocked at right:
                zoom 0.7
            J "no nthg...........Its......It's probably from soccer pratice today"
            hide marta_normal
            show marta_annoyed at left:
                zoom 0.7
            m "It's football"
            hide jack_shocked
            show jack_normal at right:
                zoom 0.7
            J "Yea,totally...... haha"
            hide jack_normal
            hide marta_annoyed    
        
        "Let it go":
            hide juli_shocked
            m "It probably from pratice or smthg"
            hide marta_normal


# scene 6:
    scene street with fade 
    show marta_smile at center:
        zoom 0.7
    m "She thought she could stop us. Hahahhaha"
    show juli_normal at left:
        zoom 0.7
    j "Yes lmao!!!! hahha"

    hide marta_smile
    hide juli_normal

    show jack_sad at center:
        zoom 0.7

    J "back......"
    hide jack_sad

    show marta_smile at center:
        zoom 0.7
    m "Isn't that Jack!!"
    show juli_shocked at left:
        zoom 0.7
    j "Yea!!!!!!!!"
    j "What is he doing there at this time??"
    j "Let's follow him!!!!!!"

    menu:
        "Follow him":
            m "yess!!!"
            hide marta_smile
            hide juli_shocked

            show jack_sad at center:
                zoom 0.7
            J "Dad.....Dad......"

            show dad_angry at left:
                zoom 0.7
            d "Why are you so late!!!!!??? huhh....... come in... I'll show you the result of this"
            J "Sorry dad.......Dad.."
            hide dad_angry
            hide jack_sad

            show marta_annoyed at center:
                zoom 0.7
            m "Damn!!! his dad is so toxic"
            m "My poor pretty face"
            show juli_shocked at left:
                zoom 0.7
            j "Yea,poor boy"
            j "should we spy from the window?"

            menu:
                "Yes":
                    m "Yes, I want to see what his dad will do"
                    j "Yes!!!!"
                    hide marta_annoyed
                    hide juli_shocked

                    scene bedroom with fade 
                    show dad_angry at center:
                        zoom 0.7
                    d "You Bitch, 2 more months and I'll sell you"
                    d "You worthless shitty girl"  
                    hide dad_angry

                    scene street with fade 
                    show marta_annoyed at left:
                        zoom 0.7
                    show juli_shocked at right:
                        zoom 0.7
                    j "Omg...He's dad is abusive  "
                    m "Is he cursing his sister or mom.... juli let's hide inside"
                    hide marta_annoyed
                    hide juli_shocked

                    show bedroom with fade 
                    show jack_gym at center:
                        zoom 0.7
                    J "sorry dad"
                    show dad_shocked at right:
                        zoom 0.7
                    d "Who is your dad huh!!!! you orphan "
                    hide dad_shocked
                    hide jack_gym

                    show marta_annoyed at left:
                        zoom 0.7
                    m "His dad is abusing his sister!!!!!!"
                    show juli_shocked at right:
                        zoom 0.7
                    j "Should we run away????!!!!!"
                    m "yesss!!!"
                "NO":    
                    m "no no, let's go home"
                    j "no way, we have to look inside"
                    j "what if he's being abused"
                    hide marta_annoyed
                    hide juli_shocked

                    scene bedroom with fade 
                    show dad_angry at center:
                        zoom 0.7
                    d "You Bitch, 2 more months and I'll sell you"
                    d "You worthless shitty girl"  
                    hide dad_angry

                    scene street with fade 
                    show marta_annoyed at left:
                        zoom 0.7
                    show juli_shocked at right:
                        zoom 0.7
                    j "Omg...He's dad is abusive  "
                    m "Is he cursing his sister or mom.... juli let's hide inside"
                    hide marta_annoyed
                    hide juli_shocked

                    show bedroom with fade 
                    show jack_gym at center:
                        zoom 0.7
                    J "sorry dad"
                    show dad_shocked at right:
                        zoom 0.7
                    d "Who is your dad huh!!!! you orphan "
                    hide dad_shocked
                    hide jack_gym

                    show marta_annoyed at left:
                        zoom 0.7
                    m "His dad is abusing his sista!!!!"
                    show juli_shocked at right:
                        zoom 0.7
                    j "Should we run away????!!!!!"
                    m "yesss!!!"

        "GO home":
            m "no let's go home instead"
            j "but what if...."
            m "NO, let's go!!!!!!!!"     
            "Juli peeks through the window"
            hide marta_annoyed
            hide juli_shocked

            scene bedroom with fade 
            show dad_angry at center:
                zoom 0.7
            d "You Bitch, 2 more months and I'll sell to prostitution"
            d "You worthless shitty girl"  
            hide dad_angry

            scene street with fade 
            show marta_annoyed at left:
                zoom 0.7
            show juli_shocked at right:
                zoom 0.7
            j "Omg...He's dad is abusive  "
            m "Is he cursing his sister or mom.... juli let's hide inside"
            hide marta_annoyed
            hide juli_shocked

            show bedroom with fade 
            show jack_gym at center:
                zoom 0.7
            J "sorry dad"
            show dad_shocked at right:
                zoom 0.7
            d "Who is your dad huh!!!! you orphan "
            hide dad_shocked
            hide jack_gym

            show marta_annoyed at left:
                zoom 0.7
            m "His dad is abusing his sister!!!"
            show juli_shocked at right:
                zoom 0.7
            j "Should we run away????!!!!!"
            m "yesss!!!"
            hide marta_annoyed
            hide juli_shocked

stop music
# scene 6:
play music "audio/normal.mp3"
"The next day"
scene hallway with fade   
show marta_normal at center:
    zoom 0.7
m "Do think he is abused too??"
show juli_shocked at left:
    zoom 0.7
j "Why are you even thinking about him, ig he's not a great influence for you"
hide marta_normal
show marta_annoyed at right:
    zoom 0.7
m "shutup!!!! he's such a sweetheart"
j "And how do you know.. huh!!! "
j "Just cuz you have a fat crush on him??"
m "Jus gooooo"

hide marta_annoyed
hide juli_shocked

# scene 7:

scene class with fade 
show mrs_normal at center:
    zoom 0.7
f "James?"    
"Present teacher"

f "Jaliet?"
show juli_normal at left:
    zoom 0.7
j "Present teacher"
f "Jack?"   
hide juli_normal 
"Absent today"

f "oh okie, his dad had informed he had got in a accident"

hide mrs_normal
show marta_normal at center:
    zoom 0.7
m "Absent????? Accident??? and juli we should go to his house today"
show juli_shocked at left:
    zoom 0.7
j "why!!! why??? to spy on him.. huh... to spy?"
hide marta_normal
show marta_annoyed at center:
    zoom 0.7
m "yess!!!! and if you dont want I'll go alone"
m "I don't need you jaliet"          

j "come on... don't be mad"
j "fine we'll follow him"


# scene 8:
scene street with fade 
show marta_annoyed at center:
    zoom 0.7
m "Imma kill his dad if he's being abused"

show juli_sad at left:
    zoom 0.7
j "Calm down....Marta, I'm a bit scared"
m "Come on... don't be scared, I have dialed the cops"
m "Any thing goes wrong then, I'll call them" 
j "Okie, let's look at the windows first" 

hide marta_annoyed
hide juli_sad

# scene 9 :
scene bedroom with fade 
show jack_gym at center:
    zoom 0.7
d "Hey, kid get dressed, I'mma take you today to meet new people"
J "Ok sir"
show dad_normal at left:
    zoom 0.7
d "dad kid........it's dad"
hide dad_normal
hide jack_gym
stop music
# scene 10:

scene street with fade 
play music "audio/calm.mp3"
show marta_annoyed at center:
    zoom 0.7
m "I can't see anything..."

show juli_sad at left:
    zoom 0.7
j "they are going somewhere....so he's not probably injured"
hide juli_sad
show juli_shocked at left:
    zoom 0.7
j "What if he's evil like his father and going to sell his sister"
m "Or mom??"
hide marta_annoyed
show marta_normal at center:
    zoom 0.7
m "Or he's abused too!!!!!"
j "Maybe we should sneak in and check from a corner"

menu:
    "Yes, go in":
        hide juli_shocked
        show juli_sad at left:
            zoom 0.7
        j "I'm kinda scared"
        hide marta_normal
        hide juli_sad

        show jack_gym at center:
            zoom 0.7
        "...."

        show marta_normal at left:
            zoom 0.7
        m "what!!!!!!????"
        show juli_shocked at right:
            zoom 0.7
        j "Your're a girl????"
        J  "Let me explain"

        hide marta_normal  
        hide juli_shocked
        hide jack_gym

        show dad_shocked at center:
            zoom 0.7
        d "Who are you??? reveal your identity"


    "No, stay outside":
        m "No, that will be a bit risky"
        j "Let's peek a little then"
        hide juli_shocked
        hide marta_normal

        scene street with fade 
        show dad_angry at center:
            zoom 0.7
        d "Who is there???"
        d "who are you girls??"
        show marta_smile at left:
            zoom 0.7
        m "We are from the cookie scout"
        d "Go away, I don't want anything"      
        show juli_normal at right:
            zoom 0.7
        j "Sir, your daughter might like it"
        hide dad_angry
        show dad_shocked at center:
            zoom 0.7
        d "How do you know about my daughter??"
        d "Are you spying on my house!!"
        m "Sir, she meant your kids might like it yk....you look like a lovely man... you might have wife and kids"
        hide dad_shocked
        show dad_normal at center:
            zoom 0.7
        d "Yea..yea, go away..."
        hide dad_normal    

        m "Shittttt...What were you thinking"
        j "Sorry, I got scared"
        j "let's go in from the back door"
        m "okxs"
        hide juli_normal
        hide marta_smile
        scene bedroom with fade 
        show juli_sad at left:
            zoom 0.7
        j "I'm kinda scared"
        hide juli_sad

        show jack_gym at center:
            zoom 0.7
        "...."

        show marta_normal at left:
            zoom 0.7
        m "what!!!!!!????"
        show juli_shocked at right:
            zoom 0.7
        j "Your're a girl????"
        J  "Let me explain"

# scene 11:
scene forest with fade
"Wake up"
"Oh...wakeup"
show jack_sad at center:
    zoom 0.7
J "Girls.....heyyy..."
show marta_annoyed at right:
    zoom 0.7 
m "Where..... are we.... JAck JAck...you are here too"
hide marta_annoyed
show marta_smile at right:
    zoom 0.7
m "Oh you came too....save..........!!!!!!"
hide marta_smile
show marta_normal at right:
    zoom 0.7
m "You are a girl.....huh......answer me!!!!!!!!"
J "I'm sorry....."
m "Answer me....you knew i liked you....you knew......!!!!!"
J "I'm sorry!!!!"     
J "i'm.....!!!!"
J "yes...yess...I'm a biological girl!!!!"
m "Then, why are you living like this and are being..."
J "When I  was 12............. I was kidnapped..........this man and he fed me horomonal pills in puberty to make me look like a boy so he could adopt me as a single dad"
J "He manipulated me intooo this........" 
hide marta_normal
show marta_sad at right:
    zoom 0.7
m "Poor you.....you must have suffered alot"
"Jack......or really amanda sobs"
J "Now, he wants to......... sell me"  
show juli_shocked at left:
    zoom 0.7
j "He is... where are we????"  
m "Let's run away"
hide juli_shocked
hide jack_sad
hide marta_sad

# scene 11:
scene bridge with fade 
show marta_smile at center:
    zoom 0.7
m "Just a little and we're gonna escape..."    
show dad_normal at left:
    zoom 0.7
d "who said so?? hahahha"   
hide marta_smile
show marta_normal at center:
    zoom 0.7
m "YOU.....!!!!!!!!!you"
d "yes me....haha..you thought you'd run!!! from me"
d "In your dreams...now that's good....hahaa 3 girls...imma be a milloniare"

show jack_sad at right:
    zoom 0.7
J "Please sir...your problem is with me leave them"
hide dad_normal
show dad_angry at left:
    zoom 0.7
d "SHUTUP..!!!! did I ask you...huh????"
hide dad_angry
hide jack_sad
show mom at left:
    zoom 0.7
M "BUT I DID"
show juli_shocked at right:
    zoom 0.7
j "Momm!!!!!!!!!!!! save us!!"
M "Don't worry sweetie, the cops are on there way"
hide mom
hide marta_normal   
hide juli_shocked

stop music
# scene 12:
play music "audio/normal.mp3"
scene hallway with fade
show marta_smile at center:
    zoom 0.7
m "After school, the haven icecream parlour?"     
show jack_normal at left:
    zoom 0.7
J "Ofc,babe"
show juli_normal at right:
    zoom 0.7
j "Did I disturb our highschool's hotest couple??? huhhh!!"
J "We are there all because of you"
m "Nah, her loving mother who tracked her down"
j "Shutup..marta!! You'd probably been washing dish if she didnt come"

# scene end:
scene street with fade
"The end"
"Mason was arrested and marta indeed gets jack orrr amanda"
"Now, marta spends detention with both her bsf and gf"
stop music









        
  























 



    











