# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Text on phone
define op = Character("+4913..", kind=nvl, color="#052453")
define mp = Character ("Me", kind=nvl, color="#B3A400")

# Text when making choices
define m = Character("Me")

# Images

init:
    image character = Image ("character.png")
    image phone = Image ("phone.png")
    image scene1 = Image ("scene01/Scene1_BG.png")
    image aisle = Image("scene01/Scene1_Aisle_OFF.png")
    image aisle on = Image ("scene01/Scene1_Aisle_ON.png")
    image scene2 = Image ("scene02/Scene2_BG.png")
    image banana = Image ("scene02/Scene2_Banana_OFF.png")
    image banana on = Image ("scene02/Scene2_Banana_ON.png")
    image apple = Image ("scene02/Scene2_Apple_OFF.png")
    image apple on = Image ("scene02/Scene2_Apple_ON.png")
    image avocado = Image ("scene02/Scene2_Avocado_OFF.png")
    image avocado on = Image ("scene02/Scene2_Avocado_ON.png")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene scene1

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show character

    m "Let's see..."

    hide character

    show phone

    # These display lines of dialogue.

    op "Thank you for everything. Since I can´t go outside it´s kinda hard for me to get groceries."

    mp "No biggie. I just wanted to help. So, how are ya?"

    op "I'm feeling sick for days..."

    op "My family can't help me now and so being stuck in this apartment is hard."

    mp "Sorry to hear... so... what do you need?"

    hide phone

    window hide

    # Szene 'Go to the fruit aisle'

label entrance:
    call screen entrance

label scene02:
    scene scene2
    show banana
    show apple
    show avocado
    pause

    "Right before you are a lot of different fruits and vegetables. The variety is plenty. When you look out for some fruits you see three different kind that may fit the needs."

    "In front of you you see: Apples, Bananas, Avocados."

    show phone

    op "Please get me some X."

    hide phone

label scene02_2:

    screen aisle():
        imagemap:
            ground "scene02/Scene2_BG.png"
            hotspot() action Jump("")


label buybanana:

    m "Shall I buy bananas?"
    $ right = 0
    $ wrong = 0

    menu:
        "Yes, I'll take the bananas.":
            $ choice1 = "1"
            "You put the banana in your basket."
            jump scene03
        "No, let's take another look.":
            jump scene02_2

label buyapple:

    m "Shall I buy apples?"
    $ right = 0
    $ wrong = 0

    menu:
        "Yes, I'll take the apples.":
            $ choice1 = "2"
            "You put the apples in your basket."
            jump scene03
        "No, let's take another look.":
            jump scene02_2

label buyavocado:

    m "Shall I buy avocados?"
    $ right = 0
    $ wrong = 0

    menu:
        "Yes, I'll take the avocados.":
            $ choice1 = "3"
            "You put the avocados in your basket."
            jump scene03
        "No, let's take another look.":
            jump scene02_2

label scene03:
    if choice1 == "1":
        "Now that I bought some bananas, off to the next"
    $ right += 1

    if choice1 == "2":
        "Now that I got some apples, let's get some X"
    $ right += 1

    if choice1 == "3":
        "I took some of the avocados. Time to get X"
    $ right += 1



    pause
    # This ends the game.

    return
