 screen entrance():
    text "Hello world"
    imagemap:
        ground "scene01/Scene1_BG.png"
        hotspot(985, 378, 554, 589) action Jump("scene02")
    add "scene01/Scene1_Aisle_OFF.png"
    imagebutton:
        idle "scene01/Scene1_Aisle_OFF.png"
        hover "scene01/Scene1_Aisle_ON.png"
        action Jump("scene02")