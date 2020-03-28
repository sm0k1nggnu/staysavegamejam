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

 screen prescene03():
    imagemap:
        ground "scene03/Scene3_BG_Placehold.png"
        hotspot(0, 0, 1920, 1080) action Jump("scene03")

 screen scene03():
    imagemap:
        ground "scene03/Scene3_BG_Placehold.png"
    imagebutton:
        idle "scene03/Scene3_Wholegrain_OFF.png"
        xpos 252
        ypos 360
        hover "scene03/Scene3_Wholegrain_ON.png" action Jump("buywholegrain")
    imagebutton:
        idle "scene03/Scene3_Normal_Placehold.png"
        xpos 821
        ypos 365
        hover "scene02/Scene2_Apple_ON.png" action Jump("buynormal")
    imagebutton:
        idle "scene03/Scene3_Glutenfree_Placehold.png"
        xpos 1322
        ypos 323
        hover "scene02/Scene2_Avocado_ON.png" action Jump("buyglutenfree")

 screen prescene04():
    imagemap:
        ground "scene03/Scene3_BG_Placehold.png"
        hotspot(0, 0, 1920, 1080) action Jump("scene04")

 screen scene04():
    imagemap:
        ground "scene03/Scene3_BG_Placehold.png"
    imagebutton:
        idle "scene03/Scene3_Wholegrain_OFF.png"
        xpos 252
        ypos 360
        hover "scene03/Scene3_Wholegrain_ON.png" action Jump("buycowmilk")
    imagebutton:
        idle "scene03/Scene3_Normal_Placehold.png"
        xpos 821
        ypos 365
        hover "scene02/Scene2_Apple_ON.png" action Jump("buyalmondmilk")
    imagebutton:
        idle "scene03/Scene3_Glutenfree_Placehold.png"
        xpos 1322
        ypos 323
        hover "scene02/Scene2_Avocado_ON.png" action Jump("buyoatmilk")
