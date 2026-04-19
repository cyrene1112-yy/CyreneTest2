# 覆盖默认的对话框
screen say(who, what):
    style_prefix "say"
    window:
        id "window"
        background Image("assets/ui/textbox_custom.png") 
        padding (100, 50, 100, 30)

        if who is not None:
            window:
                id "namebox"
                style "namebox"
                xalign 0.5
                ypos -40 
                background None 
                
                text who:
                    id "who"
                    size 36
                    color "#e8c37d" 
                    outlines [ (2, "#000000", 0, 0) ]

        text what:
            id "what"
            size 30
            color "#ffffff"
            text_align 0.0 

# 覆盖默认的选项框
screen choice(items):
    style_prefix "choice"
    vbox:
        xalign 0.85 
        yalign 0.6
        spacing 20 

        for i in items:
            textbutton i.caption:
                action i.action
                idle_background "assets/ui/choice_idle.png"
                hover_background "assets/ui/choice_hover.png"
                xysize (450, 60)
                text_xpos 60
                text_yalign 0.5
                text_size 28
                text_idle_color "#dddddd"
                text_hover_color "#ffffff"
                text_outlines [ (1, "#00000088", 1, 1) ]