 screen entrance():
    text "Hello world"
    imagemap:
        ground "scene01/Scene1_BG.png"
        hotspot(985, 378, 554, 589) action Jump("scene02")
    imagebutton:
        idle "scene01/Scene1_Aisle_OFF.png"
        xpos 921
        ypos 340    
        hover "scene01/Scene1_Aisle_ON.png"
        action Jump("scene02")

 screen scene02():
    imagemap:
        ground "scene02/Scene2_BG_ON.png"
        hotspot(0, 0, 1920, 1080) action Jump("aisle")


 screen aisle():
    imagemap:
        ground "scene02/Scene2_BG_OFF.png"
    imagebutton:
        idle "scene02/Scene2_Banana_OFF.png"
        xpos 156
        ypos 292
        hover "scene02/Scene2_Banana_ON.png" action Jump("buybanana")
    imagebutton:
        idle "scene02/Scene2_Apple_OFF.png"
        xpos 745
        ypos 342
        hover "scene02/Scene2_Apple_ON.png" action Jump("buyapple")
    imagebutton:
        idle "scene02/Scene2_Avocado_OFF.png"
        xpos 1366
        ypos 308
        hover "scene02/Scene2_Avocado_ON.png" action Jump("buyavocado")
