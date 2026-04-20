# 覆盖默认的对话框
screen say(who, what):
    style_prefix "say"
    window:
        id "window"
        # 使用 Transform 增加半透明效果 (alpha=0.85)，并使用拉伸确保图片沾满1920宽
        background Transform(Image("assets/ui/textbox_custom.png"), alpha=0.85)
        xysize (1920, 290)
        xalign 0.5
        yalign 1.0
        xmargin 0
        ymargin 0
        xpadding 100
        ypadding 40
        xfill True # 重点：告诉引擎这个窗口要在水平方向上沾满空间

        if who is not None:
            window:
                id "namebox"
                style "namebox"
                xalign 0.5
                ypos -20 # 前一个值为 -40，再向下移动 20px 变为 -20
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
            ypos 80 # 由于对话框也变高了 50px，要保持绝对位置不变，正文坐标要额外 +50 (从 30 变 80)

# 覆盖默认的选项框
screen choice(items):
    style_prefix "choice"
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 30

        for i in items:
            textbutton i.caption:
                action i.action
                # 调整背景，设定强制满长(比如800)并按适当比例显示
                idle_background Frame("assets/ui/choice_idle.png", 10, 10, 10, 10)
                hover_background Frame("assets/ui/choice_hover.png", 10, 10, 10, 10)
                xysize (800, 80)
                text_xalign 0.5
                text_yalign 0.5
                text_size 36
                text_idle_color "#dddddd"
                text_hover_color "#ffffff"
                text_outlines [ (2, "#000000", 0, 0) ]