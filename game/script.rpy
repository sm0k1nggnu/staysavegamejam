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
    image aisle off = Image("scene01/Scene1_Aisle_OFF.png")
    image aisle on = Image ("scene01/Scene1_Aisle_ON.png")
    image scene2 = Image ("scene02/Scene2_BG.png")

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

    # Szene 'Go to the fruit aisle'

label entrance:
    screen entrance():
        imagemap:
            ground "scene01/Scene1_BG.png"
            hotspot(985, 378, 554, 589) action Jump("Scene1_Aisle_ON.png")

label aisle:
    show scene2
    
    m "Let's see agane"

    show phone




    # This ends the game.

    return
