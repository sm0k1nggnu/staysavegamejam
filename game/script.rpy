# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Text on phone
define op = Character("+4913..", kind=nvl, color="#052453")
define mp = Character ("[y]", kind=nvl, color="#B3A400")

# Text when making choices
define m = Character("You")

#Sounds
define audio.incoming = "audio/incoming_message_onphone.mp3"
define audio.outgoing = "audio/outgoing_message_onphone.mp3"
define audio.supermarkt = "audio/supermarktsong_Hintergrundmusik_im_Loop.mp3"
define audio.logo = "audio/Testspace_Logosound.mp3"
define audio.phonevibr = "audio/vibrieren_wenn_Telefon_auftaucht.mp3"
define audio.obst = "audio/Obst_wenn_mit_obst_interagiert_wird.mp3"
define audio.nudeln = "audio/Nudeln_wenn_mit_nudeln_interagiert_wird.mp3"
define audio.kasse = "audio/kasse_wennEtwas_Final_Gekauft_wird.mp3"

# Images

init:
    image character = Image ("character.png")
    image phone = Image ("phone.png")
    image scene1 = Image ("scene01/Scene1_BG.png")
    image aisle = Image("scene01/Scene1_Aisle_OFF.png")
    image aisle on = Image ("scene01/Scene1_Aisle_ON.png")
    image scene2 = Image ("scene02/Scene2_BG_OFF.png")
    image scene3 = Image ("scene03/Scene3_BG_Placehold.png")

# NVL Mode

init python:
    config.empty_window = nvl_show_core
    config.window_hide_transition = dissolve
    config.window_show_transition = dissolve

define adv_menu = menu

# The game starts here.

label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene scene1
    play music supermarkt
    $ y = renpy.input("What's your name?")
    if y == "":
        "Please enter a name"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show character

    window hide

    pause

    play sound phonevibr
    y "Let's see..."

    hide character
    show phone

    # These display lines of dialogue.
    play sound incoming
    op "Thank you for everything. Since I can´t go outside it´s kinda hard for me to get groceries."

    play sound outgoing
    mp "No biggie. I just wanted to help. So, how are ya?"

    play sound incoming
    op "I'm feeling sick for days..."

    play sound incoming
    op "My family can't help me now and so being stuck in this apartment is hard."

    play sound outgoing
    mp "Sorry to hear..."

    menu:
        "Hey! I'm heading out to the supermarket to buy groceries. Do you need something?":
            jump heygoing
        "Going out to buy some stuff. Need something?":
            jump needsmth
        "I'm at the mall and if you want I can bring you some stuff.":
            jump bringstuff

label heygoing:

    mp "Hey! I'm heading out to the supermarket to buy groceries. Do you need something?"

    play sound incoming
    op "Ahoy! How are you doing? Yes, in fact I need a few things."

    play sound incoming
    op "Uhm... Can you get me some fruits? I need a bunch for my breakfast."

    jump buyfruit

label needsmth:

    mp "Going out to buy some stuff. Need something?"

    play sound incoming
    op "Yeah. Wait a minute and let me check... I'll text you."

    play sound incoming
    op "Uhm... Can you get me some fruits? I need a bunch for my breakfast."

    jump buyfruit

label bringstuff:

    mp "I'm at the mall and if you want I can bring you some stuff."

    play sound incoming
    op "Cool! Let me just check!"

    play sound incoming
    op "Uhm... Can you get me some fruits? I need a bunch for my breakfast."

    jump buyfruit

label buyfruit:

    menu:
        "Sure! What kind do you want? I love me some apples, they are my favorite.":
            jump favorites
        "Ok. What do you want?":
            jump what
        "Yeah. I get you some.":
            jump getsome

label favorites:

    mp "Sure! What kind do you want? I love me some apples, they are my favorite."

    play sound incoming
    op "Thank you! Something fresh would be good."

    hide phone

    window hide

    jump entrance

label what:

    mp "Ok. What do you want?"

    play sound incoming
    op "I don't know, can you get me something easy and quick to eat?"

    hide phone

    window hide

    jump entrance

label getsome:

    mp "Yeah. I get you some."

    play sound incoming
    op "Thanks..."

    hide phone

    window hide

    jump entrance

    # Szene 'Scene 02, the fruit aisle'

label entrance:
    call screen entrance

label scene02:
    call screen scene02
    "Right before you are a lot of different fruits and vegetables. The variety is plenty. You see three different kind that may fit the needs."
    jump aisle

label aisle:
    call screen aisle

# Buy your produce choices

label buybanana:
    show scene2
    "Looking at the bananas you see a lot of green and some ripe ones. They are a bit more pricey but seem much fresher than the apples. And as the old saying goes: A banana a day, keeps the doctor away."
    $ right = 0
    $ wrong = 0

    menu:
        "Yes, I'll take the bananas.":
            $ choice1 = "banana"
            play sound obst
            "You put the banana in your basket."
            jump scene02end
        "No, let's take another look.":
            jump aisle

label buyapple:
    show scene2
    "The apples in front of you look ok but not fresh and shiny. But when you look at the price tag you see that they are really cheap. Should you pick'em? It would save some money..."
    $ right = 0
    $ wrong = 0

    menu:
        "Yes, I'll take the apples.":
            $ choice1 = "apple"
            play sound obst
            "You put the apples in your basket."
            jump scene02end
        "No, let's take another look.":
            jump aisle

label buyavocado:
    show scene2
    "The avocados are the most expensive fruit in the store. They look ripe, but they ain't sweet and can't be eaten right away. While looking at the avocados you hear someone whispering: ' ... that's why you'll never be able to afford a house.'"
    $ right = 0
    $ wrong = 0

    menu:
        "Yes, I'll take the avocados.":
            $ choice1 = "avocado"
            "You put the avocados in your basket."
            jump scene02end
        "No, let's take another look.":
            jump aisle

label scene02end:
    if choice1 == "banana":
        "Now that I bought some bananas, off to the next aisle!"
    $ right += 1

    if choice1 == "apple":
        "Now that I got some apples, let's get some X."
    $ right += 1

    if choice1 == "avocado":
        "I took some of the avocados. Time to get X."
    $ right += 1

    show phone
    mp "I got your fruits. I hope you like them. What do you need next?"

    play sound incoming
    op "I need some pasta, they're easy to store. Since I get dizzy all the time... I need something easy to cook that doesn't go bad so easily."

    menu:
        "Getting pasta is probably a good idea when you can't get out that much.":
            jump goodidea
        "That sucks... hope you get better soon. Making pasta seems like a good idea.":
            jump getbetter
        "kk":
            jump kk

label goodidea:
    mp "Getting pasta is probably a good idea when you can't get out that much."

    play sound incoming
    op "Yeah, they're a life saver."

    hide phone
    window hide
    jump prescene03

label getbetter:
    mp "That sucks... hope you get better soon. Making pasta seems like a good idea."

    play sound incoming
    op "Yeah... it's fine. Pasta is cheap and easy to cook."

    hide phone
    window hide
    jump prescene03

label kk:
    mp "kk"

    play sound incoming
    op "thx"

    hide phone
    window hide
    jump prescene03

# The pasta shelf, scene 03

label prescene03:
    call screen prescene03
    "Wandering around you find yourself in front of the pasta department. There are a lot of different types in the shelves. You don't know which one to get and start to look around."
    jump scene03

label scene03:
    call screen scene03

label buywholegrain:
    show scene3
    "Wholegrain is somewhat more pricey but it's healthy. Some may don't like the 'corny'-taste. The package says: 'We are using the whole grain. Not just 3/4 or 8/3 but the whole grain.'"
    $ right = 0
    $ wrong = 0

    menu:
        "Wholegrain is nice and healthy!":
            $ choice2 = "wholegrain"
            play sound obst
            "You put the wholegrain pasta in your basket."
            jump scene03end
        "Let's keep looking!":
            jump scene03

label buynormal:
    show scene3
    "Ah! The good ol' standard type. Yummy, cheap and easy to cook. But they are boring and some folks are allergic to it."
    $ right = 0
    $ wrong = 0

    menu:
        "Let's go for the normal ones.":
            $ choice2 = "normal"
            play sound obst
            "You put the regular pasta in your basket."
            jump scene03end
        "Let's keep looking!":
            jump scene03

label buyglutenfree:
    show scene3
    "Gluten-Tag! Gluten-free pasta is the priciest pasta. It comes in a brown paper package and smells funny. But it is a healthy choice."
    $ right = 0
    $ wrong = 0

    menu:
        "Can't go wrong with glutenfree, so let's take it!":
            $ choice2 = "glutenfree"
            "You put the glutenfree pasta in your basket."
            jump scene03end
        "Let's keep looking!":
            jump scene03

label scene03end:
    if choice2 == "wholegrain":
        "That's done!"
    $ right += 1

    if choice2 == "normal":
        "That's done!"
    $ right += 1

    if choice2 == "glutenfree":
        "That's done!"
    $ right += 1

    menu:
        "Hey! I got you some pasta. Hope you'll like them, didn't exactly know which ones to get.":
            jump pasta1
        "Bought some pasta for you. Wasn't easy to choose.":
            jump pasta2
        "Got your pasta. What's next?":
            jump pasta3

label pasta1:
    mp "Hey! I got you some pasta. Hope you'll like them, didn't exactly know which ones to get."

    op "Thank you very much. I know...  but that's the cool part about pasta. Endless possibilities. By the way, can you get me some milk?"
    jump prescene04

label pasta2:
    mp "Bought some pasta for you. Wasn't easy to choose."

    op "Thanks! Do you mind to buy me a box of milk?"
    jump prescene04

label pasta3:
    mp "Got your pasta. What's next?"

    op "I am in need of some milk."
    jump prescene04

# The milk shelf, scene 04

label prescene04:
    call screen prescene04
    "There are sooo many completely different looking boxes of milk. And you recognize that you can make milk out of literally everything. Soy, almonds, oats, rice... "
    jump scene04

label scene04:
    call screen scene04

label buycowmilk:
    show scene4
    "Made out of 100\% freshly pressed cows. The golden standard. Cheap and somewhat healthy."
    $ right = 0
    $ wrong = 0

    menu:
        "Let's take this!":
            $ choice4 = "cowmilk"
            play sound obst
            "You put the cow milk in your basket."
            jump scene04end
        "Hmm, what else is there?":
            jump scene04

label buyalmondmilk:
    show scene4
    "Almonds are a snack with a lot of benefits. This goes as well for almond milk. Its taste is described as 'slightly sweet'. Quite pricey though..."
    $ right = 0
    $ wrong = 0

    menu:
        "Let's go for almond milk!":
            $ choice4 = "almondmilk"
            play sound obst
            "You put the almond milk in your basket."
            jump scene04end
        "Hmm, what else is there?":
            jump scene04

label buyoatmilk:
    show scene4
    "You can eat oats but also produce milk out of it. Oat milk tastes a bit like hazelnut and is cheap. Not as cheap as your regular cow milk."
    $ right = 0
    $ wrong = 0

    menu:
        "Oat milk is delicious! That's the one!":
            $ choice4 = "oatmilk"
            "You put the oat milk in your basket."
            jump scene04end
        "Hmm, what else is there?":
            jump scene04

label scene04end:
    if choice4 == "cowmilk":
        "Let's wrap this up."
    $ right += 1

    if choice4 == "almondmilk":
        "Let's wrap this up."
    $ right += 1

    if choice4 == "oatmilk":
        "Let's wrap this up."
    $ right += 1

    menu:
        "Got milk? Yes, you got milk! :)":
            jump milk1
        "Hey! I got the milk you asked for.":
            jump milk2
        "Got milk! :D":
            jump milk3

label milk1:
    mp "Got milk? Yes, you got milk! :)"

    op "Yass! Thank you for your help. I love to eat rice pudding when I'm feeling down and you need milk for that. If you want, I can make you some sometime. "
    jump prescene05

label milk2:
    mp "Hey! I got the milk you asked for."

    op "Ahoy! I know it´s a hard choice but I´m sure you took a good one."
    jump prescene05

label milk3:
    mp "Got milk! 😀"

    op "Thanks! 😀"
    jump prescene05

label prescene05:
    


    pause
    # This ends the game.

    return
