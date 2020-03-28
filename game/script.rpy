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
    image banana = Image ("scene02/Scene2_Banana_OFF.png")
    image banana on = Image ("scene02/Scene2_Banana_ON.png")
    image apple = Image ("scene02/Scene2_Apple_OFF.png")
    image apple on = Image ("scene02/Scene2_Apple_ON.png")
    image avocado = Image ("scene02/Scene2_Avocado_OFF.png")
    image avocado on = Image ("scene02/Scene2_Avocado_ON.png")

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

    y "Let's see..."

    hide character

    play sound phonevibr
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

    # Szene 'Go to the fruit aisle'

label entrance:
    call screen entrance

label scene02:
    call screen scene02
    "Right before you are a lot of different fruits and vegetables. The variety is plenty. You see three different kind that may fit the needs."

    show phone

    play sound incoming
    op "Please get me some X."

    hide phone
    jump aisle

label aisle:
    call screen aisle

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
            jump scene03
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
            jump scene03
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
            jump scene03
        "No, let's take another look.":
            jump aisle

label scene03:
    if choice1 == "banana":
        "Now that I bought some bananas, off to the next aisle!"
    $ right += 1

    if choice1 == "apple":
        "Now that I got some apples, let's get some X."
    $ right += 1

    if choice1 == "avocado":
        "I took some of the avocados. Time to get X."
    $ right += 1



    pause
    # This ends the game.

    return
