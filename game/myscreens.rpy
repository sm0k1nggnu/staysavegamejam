screen entrance():
    text "Hello world"
    imagemap:
        ground "scene01/Scene1_BG.png"
        hotspot(985, 378, 554, 589) action Jump("aisle")
    add "scene01/Scene1_Aisle_ON.png"