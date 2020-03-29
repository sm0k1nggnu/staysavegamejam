 screen scene01():
    text "Hello world"
    imagemap:
        ground "scene01/Scene1_BG.png"
        hotspot(985, 378, 554, 589) action Jump("prescene02")
    imagebutton:
        idle "scene01/Scene1_Aisle_OFF.png"
        xpos 846
        ypos 263  
        hover "scene01/Scene1_Aisle_ON.png"
        action Jump("prescene02")


 screen scene02():
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

 screen scene03():
    imagemap:
        ground "scene03/Scene3_BG_OFF.png"
    imagebutton:
        idle "scene03/Scene3_Wholegrain_OFF.png"
        xpos 190
        ypos 360
        hover "scene03/Scene3_Wholegrain_ON.png" action Jump("buywholegrain")
    imagebutton:
        idle "scene03/Scene3_Normal_OFF.png"
        xpos 760
        ypos 365
        hover "scene03/Scene3_Normal_ON.png" action Jump("buynormal")
    imagebutton:
        idle "scene03/Scene3_Glutenfree_OFF.png"
        xpos 1260
        ypos 323
        hover "scene03/Scene3_Glutenfree_ON.png" action Jump("buyglutenfree")

 screen scene04():
    imagemap:
        ground "scene04/Scene4_BG_OFF.png"
    imagebutton:
        idle "scene04/Scene4_Cow_OFF.png"
        xpos 395
        ypos 255
        hover "scene04/Scene4_Cow_ON.png" action Jump("buycowmilk")
    imagebutton:
        idle "scene04/Scene4_Oat_OFF.png"
        xpos 862
        ypos 307
        hover "scene04/Scene4_Oat_ON.png" action Jump("buyoatmilk")
    imagebutton:
        idle "scene04/Scene4_Almond_OFF.png"
        xpos 1255
        ypos 293
        hover "scene04/Scene4_Almond_ON.png" action Jump("buyalmondmilk")
