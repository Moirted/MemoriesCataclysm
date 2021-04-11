# Charas

define gg = Character('[name]', color='#f00')
define mom = Character("[mothername]", color="#0100fb", image = 'mom')
define dad = Character("[fathername]", color="ffc368", image = 'dad')
define careg = Character("Caregiver", color='c8d35f', image = 'careg')
define murder = Character("Murder", color='da6827')

init:
    image mom normal = 'mom/mom normal.png'
    image mom ang = 'mom/mom ang.png'
    image mom smile = 'mom/mom smile.png'
    image dad normal = 'dad/dad normal.png'

    image blackview = "bg/black.png"
    image room day = "bg/Комната_днем.png"
    image room after day = "bg/Комната_на_закате.png"
    image room night = "bg/Комната_ночью_без_света.png"
    image room night light = "bg/Комната_ночью_со_светом.png"
    image room red = "bg/Комната_красная.png"
    image room red half = "bg/Комната_красная_нет_глаза.png"
    image room blue = "bg/Комната_синяя.png"
    image room contur = "bg/Комната_воспоминания.png"
    image home building = "bg/Вход_в_подъезд.png"
    image elevator = "bg/Лифт.png"
    image floor = "bg/Вход_на_крышу.png"
    image floor w1th gg = "bg/Вход_на_крышу_с_гг.png"
    image lougnereoom = "bg/Гостинная.png"
    image detipriyut = "bg/Приют.png"
    image house = "bg/Дача.png"

    image forest gg = "cg/гг_смотрит_лес.png"
    image forest empty = 'cg/Пустой_лес.png'
    image forest parents = 'cg/родители_лес.png'
    image incar = "cg/В_машине.png"


transform slightleft:
    xalign 0.25
    yalign 1.0

transform slightright:
    xalign 0.75
    yalign 1.0

transform Mright:
    xalign 0.9
    yalign 1.0

transform Mleft:
    xalign 0.1
    yalign 1.0

# The game starts here.
label start:
    $ name = ''
    $ parents_root = 0
    $ bad_guy_root = 0
    $ mothername = 'Woman'
    $ fathername = 'Man'

    show text "{size=+20}Disclaimer{/size}.\n All names and events are fictitious, any coincidences are coincidental." at truecenter
    with dissolve
    pause 5
    hide text
    with dissolve

    show text '{size=+20}616-1 Team presents{/size}.\n\n{size=+30}{color=#f00}Memories Cataclysm{/color}{/size}' at truecenter
    with dissolve
    pause 5
    hide text
    with dissolve

    scene forest empty with Dissolve(.5)
    pause 3
    scene forest gg with Dissolve(.5)
    pause 3
    scene forest parents with Dissolve(.5)
    pause 3

    scene blackview with Dissolve(.5)
    play music "audio/music/avaria_first_vkl.mp3"
    'This nightmare won\'t come back, I don\'t want to...
    {w}After everything that\'s happened to me… I\'m not going back there!
    {w}I was obviously exhausted from that place.'
    'I hope that at least for someone in this world, I will be a living {color=#f00}person{/color}!'

    scene incar with Dissolve(1)
    mom smile 'This is my favorite!!! \"If you want to stay\"!{w}I love \"Diskoteka Avaria\"!'
    dad '{i}Oh, women, listen to such nonsense.{/i}'
    play sound "audio/sound/переключение_би2.mp3"
    dad ang'I\'ll switch it over, or I\'ll get some noise in my ears.'
    mom ang 'Well, that\'s fine.'
    stop sound
    play music "audio/music/песня_на_радио_би2.mp3"
    dad smile 'Oh, a beautiful song...'
    mom ang "{i}The \"Avaria\" was still better!{\i}"
    'She has realized that no one has ordered her, she is independent!'
    mom 'Come on, let\'s get your radio set up!'
    play music 'audio/music/car ride.mp3'

    'Tatiana suddenly turns off the radio and the characters and the player sit in a calm'
    $ mothername = 'Tatiana'
    dad ang 'What a pest!'
    mom normal 'You know that...{w} The weather is great today.'
    dad normal 'Yes, indeed...{w} It\'s like the sun came out of the clouds after we met such a beautiful little boy, adopted him, more than that.'
    mom 'Yes, a miracle happens. And by the way...'
    mom 'At the orphanage, we were informed that you were never called by your first name and nothing is known about him at all.'

    'The foster mother turned to the child'
    mom 'Do you mind if we give you a new name?'
    'Boy' 'I guess you can…'
    dad smile 'Vasyan!'
    mom ang 'Lyosha, well, it\'s not funny, let\'s be serious.{w} Maybe Sasha?'
    $ fathername = 'Alexey'
    play sound "audio/sound/смех_мужыка.mp3"
    dad smile 'And this woman is telling me about being serious? Don\'t make my horseshoes laugh, it\'s a terrible platitude!'
    dad normal 'He looks shy and constantly self-conscious, he needs a big name to\"sound\"!{w} Also, I think this name should be easy to translate into a short form, at the same time it should be important and serious...'
    mom 'From you as usual, a lot of words are not enough to do, it would be better to offer something yourself!'
    mom normal 'Is Valentine good?...'
    dad smile 'Cool! Tanya, this name will suit him well!{w} We\'ll call you \"Valek\" or \"Valya\" briefly, will that do? I wish that was my son\'s name!'
    dad normal 'Uh, son, do you agree?'
    'Boy' '{i}No one has ever given me the right to speak out before. My opinion didn\'t matter to anyone. Maybe I\'ve finally met the people who need me?

    And anyway, I don\'t understand why he started calling me son so suddenly.{/i}
    '
    'Boy' 'Why are you asking me? Is it really important for you to know my opinion?'
    dad 'Of course, you have no idea how much it means to us.'
    mom 'Son, don\'t even doubt it!'
    'Boy' 'Opinion… I have a choice. Is it so ... strange?{w} I\'ll try.'
    menu:
        'I agree.':
            jump choice1_yes

        'No, I\'ll choose it myself.':
            jump choice1_no

label choice1_yes:
    $ parents_root += 1
    $ name = 'Valentine'
    'The boy thought it was a good idea and saw the genuine smiles on their faces.{w} Of course, he smiled back.'
    'Both' 'That\'s great!'
    gg '{i}They repeated it in unison, it was cool…{/i}'
    jump choice1_done

label choice1_no:
    $ bad_guy_root += 1
    'Boy' 'I\'ll choose my own name?'
    'Parents are thinking...'
    dad normal 'Okay.'
    'Boy' 'Hmm-m.....{w} {i}So, this choice is entirely mine. Interesting…{/i}'
    mom smile 'We don\'t bite, come on.'
    'Boy' 'Okay… Good.'
    $ name = renpy.input ("My name is", "", length=20,)
    if name == "":
        $ name = "Andru"
    mom normal '[name]? That sounds interesting. I hope this name doesn\'t have any negative connotations.'
    dad 'Your will, son'
    '{i}The parents are not very happy with the name that the boy chose for himself, they were waiting for his consent, but there is nothing they can do...{/i}'
    jump choice1_done

label choice1_done:
    dad normal 'By the way, we\'re approaching the house now. Prepare to unload.'
    play sound 'audio/sound/заглушение.mp3'
    'The car gradually slows down and approaches a multi-storey building'
    play sound 'audio/sound/шум толпы.mp3'
    stop music

    dad 'So, let\'s unload!'
    scene home building with Dissolve(.5)
    play sound 'audio/sound/шум толпы.mp3'
    show mom smile at slightleft
    show dad smile at slightright
    mom 'Home, sweet home!'
    play music 'audio/music/спокойно.mp3'
    dad 'Now you will feel a new, lovely life. Although we don\'t live very richly, but it will be much better than your shelter.'
    'Then [name] thought: \"I\'d like to believe that.\" But he still looked at them warily, the echoes of the past haunted him.'
    stop sound

    scene elevator with Dissolve(.5)
    show mom normal at slightleft
    show dad normal at slightright
    dad 'I don\'t think you know how elevators work, let me explain.'
    'Holding down the elevator hold button, father went into theory.'
    dad 'The elevator is a container that goes up to the height of the house, from which you can get to any floor of the house, we live on the sixth.'
    dad 'I can tell you briefly about the buttons: Pressing a button means that the elevator will go to this floor.'
    '[name] has never seen such devices in his life'
    gg '{i}I have the right to choose. Can I go to any floor?{/i}'
    'Although he is serious for a child, still his childhood can easily get the better of him,\" the author thought.'
    gg 'Let\'s go to the fifteenth! I want to look down on the city!'
    dad 'Let\'s do it another time, we\'re a little tired right now and don\'t really want to run around the floors.'
    '[name] thought about the fact that he was given a name to choose, but he can\'t go to some random floor, what a stupid thing to do!'
    gg '{i}Are they hiding something from me? Interesting. What should I do?{/i}'
    gg 'If you don\'t want to, I\'ll go to the fifteenth floor myself.'
    play music 'audio/music/беспокойно.mp3'
    dad ang 'Are you crazy? Where are we going to let you go alone?!'
    mom ang 'Dad\'s right, of course you\'re free of the orphanage now, but we\'re very worried about you.'
    menu:
        gg '{i}I still don\'t know if I can trust them, but they look convincing.{w} Still, the choice needs to be carefully considered…{/i}'

        "I don\'t care, I\'ll go!.":
            $ bad_guy_root += 1
            '[name] ran out of the elevator and ran into the elevator of the next section'
            play sound 'audio/sound/выключение_лифта.mp3'
            'Mom and Dad' 'Wait!'
            play sound 'audio/sound/лифт_едет.mp3'
            'Then no one noticed that the elevator hold button was not pressed, the father and mother went to the previously pressed sixth floor'
            dad ang 'Damn! How did this happen?! What do we do now?'
            mom ang 'We\'re going to the fifteenth, you never know what will happen.'
            play sound 'audio/sound/включение_лифта.mp3'
            'Father pressed the 15th floor and they drove off.{w} When they arrived, they immediately looked around.'
            scene floor with Dissolve(.5)
            play sound 'audio/sound/выключение_лифта.mp3'

            mom 'There\'s a sunroof open.'
            dad 'Really...have to climb...'
            'Father climbed up on the roof and looked around{w} On the edge of the roof he saw [name]'
            scene floor w1th gg
            dad 'I see him!'
            'Come on, I was just wondering about the view. I\'ll be right down. [name] said a couple of meters from the edge of the roof.'
            gg '{i}I wonder if they came because they are responsible for me?{/i}'
            gg '{i}Or do they really care about me?{w} Interesting… As long as I believe them.{/i}'
            dad 'Let\'s go home, tomboy.'
            'The boy got off the roof and they went to the nearest elevator.'
            play music "audio/music/спокойно.mp3" fadeout 1.0 fadein 1.0
            'It seems to me that an adult and a child live in his body at the same time. Like he\'s trying to test us. {i}Tatiana whispered to Alexey.{/i}'
            dad normal 'I don\'t know, I don\'t think so. But even so...'
            dad 'Let him test us as much as he wants, and it looks like we don\'t tell him to...'
            dad 'Mischievous \"parenting \" in orphanages is doing its job, a nightmare...'

        'Okay, but we\'ll definitely go later.':
            $ parents_root += 1
            gg 'Okay, but we\'ll definitely go later.'
            mom smile 'Of course! We\'re really, really tired, you know.'
            dad smile 'We love you.'
            play sound 'audio/sound/включение_лифта.mp3'
            gg '{i}Let\'s see how honest you are with me. As long as I believe you.{/i}'
    mom normal '{i}You should always be on the lookout for his antics. Still, we can\'t miss our chance.{/i}'

    scene lougnereoom with Dissolve(.5)
    show text '{size=+15}Once upon a time.{/size}' at truecenter
    with dissolve
    pause 2
    hide text
    with dissolve
    show mom normal at slightleft
    play music 'audio/music/беспокойно.mp3' fadeout 1.0 fadein 1.0
    '{i}Holding a pregnancy test with a single strip{/i}'
    mom 'No...{w} What went wrong again?!{w} Apparently someone from above is just laughing at us!'
    show dad normal at slightright
    dad 'Do you think our attempts aren\'t useless yet?'
    mom 'I don\'t know...{w} I don\'t understand. Why does he just leave us out?'
    dad 'It\'s nobody\'s fault but our own, you know, you don\'t have kids at 50.'
    dad 'But, you know, there\'s an alternative.'
    mom @ ang 'Do you really want to take the child from the orphanage? Yes, we will definitely be refused with such a long marriage!'
    dad 'Why not just try it? This may be our only chance to give someone care and love.'
    mom 'I... I don\'t know...{w} We probably don\'t have any other choice, really.'
    dad 'That\'s settled.'
    stop music


    scene detipriyut with Dissolve(.5)
    show mom normal at Mleft
    show dad normal at Mright
    show careg normal at center
    play music 'audio/music/спокойно.mp3' fadeout 1.0 fadein 1.0
    careg 'We can help you with custody, but with one \"but\".'
    careg 'The boy we can give you to raise has problems. He\'s deranged at times.'
    dad 'What do you mean by \"insane\"?'
    careg 'His behavior is unstable. We do not know what this is due to, most likely it is a normal teenage \"protest\", which will eventually pass.'
    careg 'He\'s new to our shelter, so we don\'t know how long it\'s been going on.'
    show mom ang at Mleft
    'It\'s quite risky to take this step, but for the sake of having a child, I\'m willing to do anything. Tanya whispered to her husband.'
    'I totally agree with you. Moreover, we may not have another chance. Alexey whispered back.'
    'Both' 'We agree!'


    scene room after day with Dissolve(.5)
    show mom normal at slightleft
    show dad normal at slightright
    play music 'audio/music/добрая.mp3' fadeout 1.0 fadein 1.0
    dad 'This is your new home, son.'
    mom smile 'Now we will have a full-fledged family in our home!'
    gg '{i}Everyone considers me a member of the family, and they haven\'t even asked me if I consider them parents.{/i}'
    play sound 'audio/sound/дверь_открытие.mp3'
    dad @ smile 'Look, this is your room, isn\'t it cool?'
    gg 'Wow, a whole room of my own... I never dreamed of this before.'
    'But [name] still had doubts. He didn\'t believe that everything could be so easy to enjoy.'
    gg 'I\'m very happy, thank you.'
    show mom smile at slightleft
    show dad smile at slightright
    'This answer was filled with sincerity, but now the parents did not understand when he was trying to test them, and when he was serious.'
    dad 'Well, in general, everything is at your disposal. It\'s getting late, so we\'ll eat and go to bed.'
    mom 'Yes, I\'ll just get on with dinner.'
    if bad_guy_root == 2:
        scene lougnereoom with Dissolve(.5)
        show mom normal at slightright
        show dad normal at slightleft
        dad 'Honey, you don\'t look so good, why don\'t I just make us a couple of sandwiches?'
        mom 'Yeah, I\'ve been running around…{w} Let\'s do it this way.'
        scene room after day with Dissolve(.5)
        gg '{i}Did I do the right thing? If Dad hadn\'t intervened, it wouldn\'t have ended well...{/i}'
    else:
        gg 'Okay, I don\'t have the energy to think anymore, I\'ll eat and go to bed. To my room.{w} My...room...'


    scene room night light with Dissolve(.5)
    show mom normal at slightright with Dissolve(.5)
    show dad normal at slightleft with Dissolve(.5)
    dad 'Well, everyone is full, and time is no longer a child\'s time. It\'s time to go to bed!'
    mom 'Good night, Lesha.'
    dad 'Good night, Tanya.'
    'The parents looked at [name].'
    show mom smile at slightright
    show dad smile at slightleft
    'Both' 'Sweet dreams!'
    menu:
        'Both' 'Sweet dreams!'

        "Say good night.":
            $ parents_root += 1
            gg 'Good Night!'

        "Keep silent":
            $ bad_guy_root += 1
            show mom normal at slightright
            'Tatiana looked at [name] sadly.'
    gg 'I\'ll go to bed now, but I can\'t let my guard down.'
    stop music

    scene blackview with Dissolve(3)
    show text '{size=+20}Next Day{/size}' at truecenter
    scene room day with Dissolve(3)
    with dissolve
    pause 3
    hide text
    with dissolve

    gg 'Such a beautiful morning. Unless...'
    scene detipriyut with Fade(0.1, 0.0, 0.5)
    play music 'audio/music/злая.mp3' fadeout 1.0 fadein 1.0
    'In the shelter, he was beaten for nothing{w} And if you let your guard down, you could get hit on the head.'
    gg 'When will it end...?'
    gg 'I\'m tired of putting up with this, a little more and I\'ll have to go for the kill.'
    'Until then, he couldn\'t remember why he felt so bad there.'
    'After another blow from the teacher, he gets dizzy and loses consciousness'
    stop music

    scene room day with Dissolve(3)
    play music 'audio/music/беспокойно.mp3' fadeout 1.0 fadein 1.0
    gg 'What?'
    '[name] thought for a couple of seconds that these memories were coming to him for a reason, but later he decided that it was just a dream.'
    gg 'Stop.'
    gg '{i}Did I faint?{w} Idiot. Sure. I couldn\'t have fallen asleep on the floor!{/i}'
    gg '{i}So it wasn\'t a dream. And I fainted for real, not just {b}there{/b}.{/i}'
    'My parents\' voice comes from the bedroom.'
    dad 'And what should we do?'
    dad 'Do you think we can re-educate his {b}insanity{/b}?'
    mom 'We started this, we are responsible for him and for his inclinations.'
    gg '{i}What inclinations are they talking about? {b}Insanity{/b}?{/i}'
    gg '{i}What do they know about me that I don\'t?{/i}'
    mom 'Of course, it was a risky move, but who if not us can help him?'
    mom 'Not only that, I have suspicions that he didn\'t know anything about his life before the orphanage.'
    gg '{i}Yeah ... what a dialogue.{/i}'
    gg '{i}What do they want to protect me from? What was it like before the orphanage?{/i}'
    'Of course, [name] didn\'t remember anything, except for the recent manifestations in his memory.'
    gg '{i}Did they beat me up for nothing? Did I disturb them in any way?{/i}'
    gg '{i}I suspect it\'s not that simple.{w} I need to know more about this.{/i}'
    gg '[name] quietly goes into the living room and pulls out all the shelves from the chest of drawers'
    scene lougnereoom with Dissolve(.8)
    mom 'Let me go check on him instead.'
    gg '{i}Damn, we need to find something faster!{/i}'
    gg '{i}Eh? Did they even read what it says?{/i}'
    '\"...an unnamed child (not documented) living earlier with his parents on 15 Berezhnogo Street...\"'
    '\"...information about the parents is lost. The child suddenly became an orphan due to unknown circumstances.\"'
    gg '{i}Here\'s the clue! I\'m learning about my past!{/i}'
    dad 'She\'s taking a while, so I\'ll go check it out.'

    scene room day with Dissolve(.5)
    show dad normal at slightleft
    show mom normal at slightright
    'After walking a couple of meters and entering [name]\'s room, Alexey sees his wife sitting on her lap.'
    dad ang 'What happened? Where is he?'
    '[name] hears Alexey\'s scream and quickly puts all the papers back in the dresser.'
    mom 'I... don\'t know...{w} Just last night he was here, when did he run away?'
    gg '{i}I think I should leave.{w} Goodbye {u}family{/u}, thank you for keeping me overnight.{/i}'
    play sound 'audio/sound/бег.mp3'
    '[name] gets up and quickly runs away.'
    dad 'So that rustle wasn\'t my {b}glitch{/b}.'
    play sound 'audio/sound/бег.mp3'
    'Alexey quickly runs out of the room and heads towards the exit.'

    scene lougnereoom with Dissolve(.8)
    show dad ang at center
    dad 'Hey! Stop!!'
    'Alexey, running through the living room, sees [name], who opened the door.'
    play sound 'audio/sound/дверь_открытие.mp3'
    dad '{size=+5}I\'ll catch up with him!{/size}'
    stop music

    scene blackview with Dissolve(.8)
    'Running down the stairs, Alexey did not see anyone who looked like his {b}son{/b}.'

    scene house with Dissolve(.3)
    play music 'audio/music/беспокойно.mp3' fadeout 1.0 fadein 1.0
    gg 'Found it! This is the same house!'
    'After finding a loophole in the fence, he deftly slipped into the yard.'
    gg 'The window is broken? What was going on here...'
    'Looking through the broken window, [name] saw {s}his{/s} room identical to that apartment'
    gg 'What ... nonsense...{w} WHAT??'
    'There was a rustle from behind the main character'
    gg 'What kind of {b}farce{/b} is this? Now I\'ll turn around and it won\'t seem too much!'
    play sound 'audio/sound/удар_поголове.mp3'
    gg 'Ah...ah...'
    stop music

    scene blackview with fade
    '[name] woke up in a familiar room. It was the apartment he had visited last night.'

    scene room after day with Dissolve(.5)
    play music 'audio/music/brise.mp3' fadeout 1.0 fadein 1.0
    gg '...eh? AAAAAAH!'
    'His condition could be called shock.'
    gg 'What was that? Is this a dream?'
    dad 'So what do we do?{w} Do you think we can re-educate his insanity?'
    mom 'We started this, we\'re responsible for him.'
    mom 'Of course, it was a risky move, but who if not us can help him?'
    mom 'Not only that, I have suspicions that he didn\'t know anything about his life before the {b}orphanage{/b}.'
    gg '{i}WHAT THE HELL!?{w} Am I crazy? How can it be explained otherwise?{/i}'

    scene lougnereoom with Dissolve(.9)
    play sound 'audio/sound/бег.mp3'
    gg '{i}I came to the bedroom... right?{/i}'
    gg 'No, I\'ve been here before, this is the living room… I remember exactly... I wanted to go to the bed-'

    scene blackview with fade

    scene room red with fade
    show mom ang at slightleft with Dissolve(.9)
    show dad ang at slightright with Dissolve(.9)
    play music 'audio/music/morning.mp3' fadeout 1.0 fadein 1.0
    mom 'Oh, the mischievous one has come. Get ready, now we will tell you off for yesterday.'
    gg '{i}They...{/i}{w} What THE HELL IS GOING ON?'
    dad 'Oh yes… You\'ll be responsible for everything.'
    play sound 'audio/sound/поножовщина.mp3'
    'Alexey grabs a black helium pen from the table and attacks [name].'
    scene room red half
    show dad ang at slightright
    gg '{color=#f00}MY EYE! YOU FREAK! I KNEW I COULDN\'T TRUST YOU!{/color}'

    scene blackview with fade
    scene room red with fade
    dad 'This is your new home, son.'

    scene blackview with fade
    #'[name] faints.'

    scene detipriyut with Dissolve(.6)
    show mom smile with Dissolve(.6)
    mom 'Now we will have a full-fledged family in our house!'
    gg 'Everyone considers me a member of the family, and they haven\'t even asked me if I consider them parents.'
    gg '{i}Stop. What?{w} That\'s not what I meant.{w} Or rather, I didn\'t say it out loud.'
    gg 'It\'s all happening in my mind. Exactly. There must be consequences of the past. I must know -'
    scene detipriyut with Dissolve(.6)
    show careg ang at center with Dissolve(.6)
    careg 'No, {size=+5}it won\'t{/size}.'
    play sound 'audio/sound/поножовщина.mp3'
    'The Caregiver sticks black gel pen in the orphan\'s arm.'
    play music 'audio/music/signal.mp3' fadeout 1.0 fadein 1.0
    gg '{color=#f00}AAAAAAHHHH{/color}'
    menu:
        'Try to resist.':
            jump choice2_yes

        'Surrend.':
            jump choice2_no

label choice2_yes:
    $ parents_root += 1
    gg 'Why is this pain so distinct? It\'s like I\'m in a waking nightmare!'
    careg ang 'Think, freak, {size=+5}THINK{/size}'
    'The Caregiver takes a cup of hot tea and throws it at the hero'
    play sound 'audio/sound/пролитие.mp3'
    gg '{size=+5}AH{/size}{size=+10}AAAAAAHH{/size} ... {color=#f00}HOT{/color}!'
    gg 'No, there must be a way out!'
    menu:
        gg 'No, there must be a way out!'

        "Run away.":
            $ parents_root += 1
            '[name], scalded with boiling water, runs out of the orphanage and faints.'

        "Hit the caregiver.":
            $ bad_guy_root += 1
            careg ang 'Oh, well done, you seem to be doing fine!'
            gg '{i}Suddenly, my whole body feels fine and the pain is gone like a feather in the wind.{/i}'
            gg '{i}There\'s something wrong with me, no, there\'s something wrong with my mind.{/i}'
            gg '{i}What\'s going on in the real world right now?{/i}'
            careg 'Have you decided to question the reality of what is happening?'
            careg smile 'COME ON{w} THINK{w} BETTER.{w} {color=#f00}AHAHAHAH{/color}.'
            '[name]\'s pain and wounds returned.'
            'He, scalded with boiling water, runs out of the orphanage and faints.'
    jump choice2_done

label choice2_no:
    $ bad_guy_root += 1
    gg 'Yes, of course, why would I resist?'
    gg 'It\'s either a dream or reality. One of two things.'
    gg '{i}Two{/i} select buttons?{w} No, there are clearly more of them.{w} Clearly, the world is not divided into black and white…'
    gg 'But what can I do?'
    jump choice2_done

label choice2_done:
    scene blackview with fade
    pause 3

    scene room night with Dissolve(.5)
    gg 'Again, it\'s happening again!'
    gg '{i}I unconsciously said it out loud, I can\'t control myself?{/i}'
    gg '{i}Everything that happens to me is not my will!{/i}'
    gg '{size=+10}I HAVE A CHOICE, SO WHY ISN\'T EVERYTHING GOING ACCORDING TO THE PLAN?!{/size}'
    gg '{i}Again... again… I do not understand.{/i}'
    show mom normal with Dissolve(.8)
    play music 'audio/music/brise.mp3' fadeout 1.0 fadein 1.0
    'Mother entered the room with a wary look on her face'
    mom 'Son, what\'s wrong?'
    gg 'Mom?'
    mom 'Yes, son? Are you all right?'
    gg '{i}Well, how do I say ... will I have to improvise?{/i}'
    gg 'Yes. All right. I had a nightmare.'
    mom 'What plan were you talking about? Is it related to sleep?'
    gg 'Yeah, uh, I was just trying to master the lucid dream technique, and it came out in a lump, like the first pancake usually does. Not so important.'
    gg 'What nonsense am I talking about? There\'s clearly something wrong with me, it\'s not even improvisation, it\'s just {b}NONSENSE{/b}! The ravings of a madman'
    mom smile 'Okay, take care, there\'s dinner ready.'
    gg '{i}Dinner? Oh, it\'s evening outside. And how do I know what\'s happening in the {b}real world{/b} now?{/i}'
    gg '{i}And why in my head is she like... really my mother?{/i}'
    gg '{i}I have a lot of questions for this strange world, close to the world of a person with mental disorders...{/i}'
    gg '{i}Apparently, they will remain rhetorical. I\'ll have to find the answers myself.{/i}'
    gg 'Of course, I\'ll be right there!'
    mom normal 'By the way, we have guests who were not invited.'
    mom smile 'Can you imagine, my friend came!'
    mom 'By the way, she works as a caregiver in an orphanage, can you imagine what a good thing!!!'
    gg '{i}Wow. This is a clinic.{/i}'
    show careg normal at Mright
    careg 'Hello! Oh, I don\'t think it\'s the right time, I\'m sorry.'
    play music 'audio/music/life.mp3' fadeout 1.0 fadein 1.0
    mom 'Nothing, go th-'
    play sound 'audio/sound/падение.mp3'
    hide mom
    gg 'OK, nothing {b}unusual{/b} so far, as usual someone fainted. Except for a little bloodstain on your {color=#f00}DAMN{/color} WHITE {color=#f00}SHIRT. A FUCKING SERVANT OF GOD!{/color}'
    careg ang 'Y-you. Was it you?! Yes, without a doubt!'
    careg 'You, no, your father!... he... made me wipe the ass of the fucking babies in this filthy orphanage!'
    gg 'Well, well. Haha, this just can\'t be happening. My parents are dead! I, Who killed these creatures with my own hands, can\'t be wrong!!!'
    '{i}That again wasn\'t what [name] wanted to say.{/i}'
    gg '{i}Wh-what? I couldn\'t say it, it\'s not in my {b}scenario{/b}.{/i}'
    gg 'And... what kind of scenario are we talking about?'
    gg 'Yes, about the ordinary, you {color=#f00}stupid idiot{/color}! This is {i}my{/i} story!'
    show careg normal at Mright with moveoutright
    'The Caregiver runs out of the room in fright.'
    gg 'The one who calls himself names is the one who calls himself-'
    gg '{i}That is{w} it is… ANSWER ME!{/i}'
    gg '{i}WHAT\'S HAPPENING TO ME, WHAT?{w} AM I {b}CRAZY{/b}?{w} AM I ON {b}DRUGS{/b}?{w} DID I GO CRAZY BECAUSE OF THE {s}FUCKING{/s} SHELTER?{w} AT LEAST YOU CAN ANSWER IT{/i}'
    gg 'It\'s not necessary.'
    gg '{i}WHAT NECESSARY?{/i}'
    gg '{b}Calm down{/b}.{w} Take a deep breath. I realized that you have emotions, I\'m jealous, but you got carried away.'
    gg '{i}WHAT DID YOU LET YOURSELF DO?{/i}'
    play sound 'audio/sound/падение.mp3'

    scene blackview with fade
    pause 2

    scene room blue with Dissolve(.5)
    gg 'It seems to be real. No, what happened to the light in this room?'
    '???' 'Okay, cut!'
    gg '{i}I remember something. Exactly. I watched this movie!{/i}'
    gg 'There was a guy in it who…{w} Was he still crazy?'
    gg '{i}Aren\'t you the main character?{/i}'
    gg 'Yes, that\'s right. And... who am I talking to?'
    gg '{i}Fool.{w} Your {s}fucking{/s} friend.{/i}'
    gg 'Yes, that\'s right, Valya!'
    gg '{i}Is this some kind of joke?{/i}'
    gg 'Of course I\'m kidding you.{w} In particular, your involvement in the murder of your innocent and elderly parents is not a bad prank!'
    gg '{i}Stop reading my mind!{/i}'
    gg 'You still don\'t understand?{w} I{w} AM{w} YOU!'
    gg 'You can hear your own thoughts inside.{w} Funny guy.'
    gg 'You\'re interesting to deal with.'
    gg '{i}Ii-I-y-you-I\'m ... devastated.{w} THE END!'
    gg '{size=+10}Stupid{/size} man. You mess with him, and he doesn\'t learn from his mistakes...'
    gg '{i}What\'s {b}he{/b} saying...{/i}'
    gg 'I can\'t talk to myself, can I? Yes, these are my thoughts{w}, only{w} {b}MINE{/b}!'
    gg 'Why did you stop talking, did you feel ashamed?'
    gg 'I can resist him! I got it!'
    menu:
        'Resist.':
            jump choice3_yes

        'Surrend.':
            jump choice3_no

label choice3_yes:
    $ parents_root += 3
    gg '{i}What can you tell me?{/i}'
    gg 'Haha. You know, it\'s fun to talk to you.'
    play music 'audio/music/untitled.mp3' fadeout 1.0 fadein 1.0
    gg 'Try to force me. Can you? You\'ll get your answers.'
    menu:
        gg 'Try to force me. Can you? You\'ll get your answers.'

        "Your body – what is it?":                                 # 1
            gg '{i}Your body – what is it?{w} Who am I?{/i}'
            gg 'What kind of straightforwardness? Naive like a {size=-10}little{/size} boy.'
            gg 'You won\'t even {b}wriggle{/b} in your questions like you did when you were {b}alive{/b}?'
            menu:
                gg 'You won\'t even {b}wriggle{/b} in your questions like you did when you were {b}alive{/b}?'

                'In life?':
                    gg '{i}In life? What do you mean?{/i}'
                    gg 'I\'ll cut you some slack.{w} {color=#f00}From now on.{w} Less.{w} Straightness.{/color}'
                    gg 'Yes, you were alive once, haha. It was boring.'
                    gg 'You were beaten, you whined. And so {b}every {size=+10}every{/size} {size=+15}every{/size}{/b} day.'
                    gg 'Although I certainly wasn\'t in the mood for jokes then, not like I am now.'
                    menu:
                        gg 'Although I certainly wasn\'t in the mood for jokes then, not like I am now.'

                        'What happened before that?':               # 1.1.1
                            gg 'YOU\'RE NOT LISTENING WELL, AHAHAHAHA!'
                            $ bad_guy_root += 5

                        'And you\'re a prankster!':                 # 1.1.2
                            gg '{i}You\'re a prankster, haha. A natural clown.{/i}'
                            gg 'To some extent, I guess.'
                            gg 'Not {b}very normal{/b}, I suppose.'
                            gg '{i}What do you remember about yourself?{/i}'
                            gg 'Are you interested? Pfft, Ha Ha.{w} Ha.{w} Ha.'
                            gg '{i}Come on, it\'s interesting to hear{/i}'
                            gg 'So I took ki-'
                            gg 'What\'s wrong with me... what? I can\'t-u. The words a.'
                            gg '{i}What is it, lost? Where are your murders, madman?{/i}'
                            gg '{i}You can\'t put me down, but I can put you down, no problem.{/i}'
                            gg 'Ahhahahaha.{w} What?{w} You?{w} Who the hell are you-?'
                            gg '{i}Your nightmare. An innocent child that you decided to just use. More precisely, your soul. You read like a book.{/i}'
                            gg '{color=#f00}AHAHAHAHAHAHA. AHAHAHAHAHA. HA!{/color}'
                            gg '{i}What\'s wrong with him? Did it really work?{/i}'
                            $ parents_root += 10



                "That's right, I'm not a little boy.":                      # 1.2
                    gg '{i}Yes, I\'m not a little boy.{/i}'
                    gg '{i}My choices belong to me as a formed person.{/i}'
                    gg '{i}{b}You.{w} Me.{w} Not.{w} Edict.{/b}{/i}'
                    gg 'And you\'re good, but, man, I can take {b}offense{/b}, you know.'
                    gg 'And this can end badly for you, do you want {b}your parents to die{/b}?'
                    menu:
                        gg 'And this can end badly for you, do you want {b}your parents to die{/b}?'

                        'I don\'t have any parents.':                       # 1.2.1
                            gg 'Of course, you killed them with your own hands!'
                            gg '{i}No… I couldn\'t...{/i}'
                            gg 'I didn\'t understand anything. You\'re hopeless.{w} Bye-bye!!!'
                            $ bad_guy_root += 5

                        'Offended, funny.':                                  # 1.2.2
                            gg '{i}And how do you explain that a {b}ruthless freak} who kills people without a shadow of a doubt{/b} can be offended by a little boy\'s sobs?{/i}'
                            gg 'How did you...?'
                            gg '{i}Get lost.{/i}'
                            $ parents_root += 10

        'I shouldn\'t ask stupid questions, you told me so yourself.': # 2
            gg 'And you understand human speech well.'
            menu:
                gg 'And you understand human speech well.'

                'I wouldn\'t be so sure about that.':  # 2.1
                    gg '{i}I wouldn\'t be so sure about that. I still doubt that I\'m a normal person...{/i}'
                    gg '{i}Why do I feel like I\'m losing?{/i}'
                    gg 'Because you\'ve already lost to me.'
                    gg 'You couldn\'t think for a second, I immediately understood your train of thought.'
                    gg '{i}No, I can...{/i}'
                    gg 'No, you can\'t. I\'ll get the body.'
                    $ bad_guy_root += 5

                'When it\'s not a plea for mercy, it\'s easy.':  # 2.2
                    gg '{i}It\'s very easy when it\'s not a plea for mercy.{/i}'
                    gg 'What are you talking about?..'
                    gg '{i}Oh, it doesn\'t matter, next question?{/i}'
                    gg 'You\'re {b}PISSING me OFF. I ask the questions here.{/b}'
                    gg '{i}Life has shaken you. Aggressive what became.{w} I suppose you want to kill?{/i}'
                    gg 'Y-you!{w} {size=+10}YOU{/size} KILL.{w} NOT ME.'
                    gg '{i}What an obvious lie.{w} You know, even though you\'re an adult uncle-killer here, you\'re not far away from a child with your intellect.{/i}'
                    gg '{color=#f00}WHAT DO YOU EVEN KNOW?!{/color}'
                    gg 'I... I... didn\'t mean to...'
                    gg 'They... wanted to take me out, for the sake of saving their lives. {size=+10}TO THE DAMNED PENAL SERVITUDE! DO YOU UNDERSTAND?{/size}'
                    gg '{i}How interesting...{/i}'
                    gg 'I loved them, they ... they ...{color=#f00}DESTROYED MY IDENTITY.{/color}'
                    gg 'My father... he was a {b}servant of the lord... gave the children hope...{/b}'
                    gg 'But he called me by the name of \"Pavel\" and did not know what meaning it might carry. Ha-ha.'
                    gg 'I {color=#f00}DON\'T CARE!{w} I DON\'T CARE ABOUT THE KIDS!{/color}'
                    gg 'I\'ve already slaughtered them when I was a child your age, and there\'s not a trace of life left. I didn\'t realize then how wrong I was.'
                    gg 'He sacrificed me for his {color=#f00}{s}SHITTY{/s}{/color} job'
                    gg 'CAUSE {color=#f00}NOW{/color} I have to put up with {color=#f00}YOU{/color}, you little shit who\'s still talking nonsense.'
                    gg '{i}What a bastard...{/i}'
                    gg 'They also...loved...'
                    gg '{color=#f00}NO, I DID THE RIGHT THING.{w} IT\'S {b}MY{/b} CHOICE!{/color}'
                    gg '{i}Heh.{/i}'
                    gg '{i}It\'s interesting, as if I almost stepped on your {b}rake{/b}.{/i}'
                    gg '{i}Such scoundrels have no place on earth. It\'s good that I understand it now.{/i}'
                    gg '{i}You\'re just a resentful child who never grew up even after {b}death{/b}.{/i}'
                    gg '{b}Death?...{/b}'
                    gg '{i}You\'re a dead man{w}, accept it and give me back MY body.{w} I\'m surprised you didn\'t realize that yourself.{/i}'
                    gg 'NO, it can\'t be...'
                    $ parents_root += 10
    jump choice3_done

label choice3_no:
    gg '{i}It feels like I\'m getting weaker...{/i}'
    gg '{i}Why do I feel like I\'m losing?{/i}'
    gg 'Because you\'ve already lost to me.'
    gg 'You couldn\'t think for a second, I immediately understood your train of thought.'
    gg '{i}No, I can...{/i}'
    gg 'No, you can\'t. I\'ll get the body.'
    $ bad_guy_root += 5



label choice3_done:
    stop music
    scene blackview with fade
    pause 3

    # Is this a cataclysm?

    if bad_guy_root < parents_root:
        scene room day with Dissolve(.2)
        play music 'audio/music/morning.mp3' fadeout 1.0 fadein 1.0
        gg 'I remember everything. Every part of your life.'
        gg 'I understand who… Who has condemned me to all this suffering!'
        gg 'The crazy killer has somehow entered my mind for a while...'
        gg 'I was able to suppress it, it wasn\'t difficult... It was enough to be calm.'
        gg 'But... why? Why me? What is the reason for his arrival in my head?'
        gg 'Oh, I remember… Exactly...'

        scene room contur with Dissolve(1)
        play music 'audio/music/evening.mp3' fadeout 1.0 fadein 1.0
        '???' 'Son, breakfast is ready!'
        gg '{i}I heard the voice of a very familiar... father?...{/i}'
        'Dad' 'Hurry up, or you\' be late for school!'
        gg '{i}I remember... school!{/i}'
        gg '{i}There\'s always my friends teasing each other!{/i}'
        gg '{i}They were putting something like buttons on each other\'s chairs.{/i}'
        gg '{i}There were always exactly two of them, so they could identify each other!{/i}'
        'Dad' 'Oh, he\'s lazy again. Okay, I\'ll go see him.'
        gg '{i}Will I see my father... again?{/i}'
        'Dad' 'So-oooon, get up! I brought you some eggs!'
        gg '{i}Did ... I lose it... but how?{/i}'
        show dad contur with moveinright
        '???' 'What a happy family. Reminds me of the past...'
        play music 'audio/music/shelter.mp3' fadeout 1.0 fadein 1.0
        gg 'Suddenly I saw a face that was impossible not to recognize.'
        gg 'This was the true appearance of that madman.'

        scene room contur
        play sound 'audio/sound/поножовщина.mp3'
        'With a sharp movement of the blade, the killer cuts his father\'s throat.'
        play sound 'audio/sound/поднос.mp3'
        gg 'NOOO! Y-you! YOU {color=#f00}FREAK{/color}!!!'
        murder 'Unpleasant, isn\'t it? SO IT WAS VERY, {color=#f00}VERY UNPLEASANT{/color} FOR ME!'
        gg 'H-hell... no...'
        gg '{size=+15}{color=#f00}I\'LL KILL YOU!{/color}{/size}'
        play sound 'audio/sound/поножовщина.mp3'
        'The boy furiously jumps on the killer with the capillary pen and sticks it in his eye.'
        play sound 'audio/sound/поножовщина.mp3'
        'Then, the killer repeatedly wounds him in the body.'
        gg '{size=+15}{color=#f00}HOW DARE YOU?{/color}{/size}'
        murder 'AHHH IT HURTS! STOP! STOP IT!{w} PLEASE-...'
        scene blackview with fade
        pause 2

        scene room contur with Dissolve(.8)
        show careg contur at center with Dissolve(.2)
        careg 'It\'s not an easy situation, you know. You committed a murder.'
        careg 'Although you defended yourself, but there will be questions for you, perhaps you will be sent to a separate complex for orphans for re-education.'
        careg 'However, we can {b}hush it up{/b}. Your memory will be erased, and you will live in an {b}ordinary{/b} shelter without knowing grief.'
        gg '{i}Then I believed it and to get rid of the responsibility agreed immediately. Stupid choice. A choice {b}without a choice{/b} for me then.{/i}'
        careg 'All right, then we\'ll take you away.'
        stop music

        scene blackview with fade
        pause 2
        scene room day with Dissolve(.2)
        play music 'audio/music/evening.mp3' fadeout 1.0 fadein 1.0
        gg 'Then I repeatedly suffered from amnesia not only because of the drugs that I was given.'
        gg 'These beatings… I didn\'t want to remember that it happened to me at the orphanage.'
        gg 'In those moments, my memory seemed to be {b}erased every day{/b}.'
        gg 'Finally. I remembered.'
        '[name] staggers out of his room and slowly walks into the living room.'
        scene lougnereoom day with Dissolve(.2)
        show dad smile at slightleft
        show mom smile at slightright
        mom 'Wow, who\'s awake! And we made you breakfast here!'
        gg '{i}I won\'t reject you now. I\'m tired. I want a happy life.{/i}'
        gg 'I {color=e65440}love{/color} you so much...'
        show dad normal at slightleft
        show mom normal at slightright
        'Parents looked at Valentine in surprise.'
        '[name], bursting into tears, hugged them.'
        scene blackview with Dissolve(2)
        'January 4, 2005. [name]\'s birthday.'
        'The boy accepted his foster parents and henceforth did not hide anything from them.'
        stop music
        scene blackview with Dissolve(5)
        show text "{size=+20}{color=9cd4eb}You deserve this final.{/color}{/size}\n Good Ending" at truecenter
        with dissolve
        pause 5
        hide text
        with dissolve
    else:
        scene room day with Dissolve(.2)
        play music 'audio/music/signal.mp3' fadeout 1.0 fadein 1.0
        gg '...'
        'In his {b}real{/b} thoughts, [name] couldn\'t say a word.'
        'He was depressed.'
        gg 'The body ... belongs to me!{w} YES! {color=#f00}I WON!{/color}'
        gg 'It was so damn easy!'
        gg '{i}I don\'t need to get burned now, I\'m turning on the acting game.{/i}'
        gg '{i}And now… I can do my favorite things again.{/i}'
        gg '{i}I will go to seek revenge again after I have dealt with his half-ancestors.{/i}'
        show mom normal with moveinright
        mom smile 'Wow, who\'s awake! And we made you breakfast here!'
        gg 'A..a.. really? Yes, now, wait a minute.'
        mom 'OK, I\'ll go for now.'
        mom '{i}He doesn\'t look like himself.{/i}'
        show mom normal with easeinright
        'At this time, Valentine pulled out a pair of compasses from a pencil case that was lying nearby'
        play sound 'audio/sound/вытаскивание.mp3'
        gg 'S-STOP!{w} Don\'t move if life is precious.'
        play sound 'audio/sound/бег.mp3'
        dad 'What\'s going on there?'
        show dad normal at slightright with moveinright
        gg 'HEY YOU! WHAT DID I TELL YOU?! DON\'T PUSH IT!'
        hide mom normal
        play sound 'audio/sound/удар_поголове.mp3'
        'Tatiana fell to her knees.'
        dad ang '{b}What the fuck is going on here?!{/b}'
        gg 'Hey you, back off in a good way!'
        dad '{i}Is this exactly [name]?? I have to check it out!{/i}'
        dad 'What\'s my name?'
        gg 'What?'
        dad 'Answer me.'
        gg '{i}Did he understand something? I\'ll try to get out with a general answer, probably...{/i}'
        gg 'It\'s not that important. I d-don\'t know you, and I d-don\'t want to know you. M-my path is different!'
        dad 'An impostor! What are your goals?'
        gg 'I am your son, the real one. What are the goals?'
        dad '{color=#f00}Get out of here!{/color}'
        show mom ang
        mom ang 'What? No! HE\'s OUR SON!{w} {b}HE\'S NOT GOING ANYWHERE!{/b}'
        dad '{size=+8}{color=#f00}YOU FOOL, STAND STILL!{/color}{/size}'
        dad '{i}This rat has taken up residence in the boy\'s body and has apparently conquered his consciousness.{/i}'
        dad '{i}Now I finally understand that insanity is not his childish quarrel, it\'s something much more serious.{/i}'
        dad '{i}Now we must somehow pass this on to Tanya, otherwise the consequences are inevitable...{/i}'
        dad 'Believe me, believe me, please.'
        mom 'I... can\'t... let him go...'
        mom 'Our dreams have just begun to come true'
        hide mom normal
        play sound 'audio/sound/поножовщина.mp3'
        'With a precise stroke of the compass, the [name] wounds the mother.'

        scene lougnereoom with fade
        show dad ang at center with fade
        play sound 'audio/sound/бег.mp3'
        dad 'There is no way out. You\'ll have to pay the price, you beast.'
        play sound 'audio/sound/вытаскивание.mp3'
        gg 'LET ME JUST {color=#f00}KILL{/color} YOU! STOP RESISTING!'
        gg '{i}There is no way out. Either I die or they die. They will die.{/i}'

        scene blackview with fade
        play sound 'audio/sound/машина_дверь.mp3'
        'The killer runs out of the high-rise building and runs towards the house he once knew.'
        gg '{i}This is my home! I\'ve been living next door to them all this time?{/i}'
        scene house with Dissolve(.5)
        gg 'Wait. What?'
        gg 'I followed the kid and he... came here too?'
        gg 'No, it was his {b}glitch{/b}.'
        gg 'It was in his head, so I could {b}read{/b} it.'
        gg 'I don\'t feel well...'
        play music 'audio/music/untitled.mp3' fadeout 1.0 fadein 1.0
        'These were echoes of the real [name]\'s consciousness.'
        'He despaired after failing to suppress his second identity.'
        'But I decided that if he didn\'t live in his body, then no one would live in it.'
        play sound 'audio/sound/падение.mp3'
        gg 'Oh, my heart feels like...something\'s stopping...'
        stop music

        scene blackview with Dissolve(1)
        'Half an hour later, the boy was found in the courtyard of the same house.'
        'His pulse stopped, he wasn\'t breathing.'
        'January 4, 2005. [name]\'s birthday.'
        'The boy died. He couldn\'t overcome his fears.{w} At the last moment, he took with him the psychopath he was previously afraid of.'
        scene blackview with Dissolve(5)
        show text "{size=+20}{color=e70202}You deserve this final.{/color}{/size}\n Bad Ending" at truecenter
        with dissolve
        pause 5
        hide text
        with dissolve

    return
