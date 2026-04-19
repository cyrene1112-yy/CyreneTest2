# 第一章第一幕：书房搜查界面
screen ch1_act1_study_investigation():
    # 背景
    add "bg study_room"
    
    # 昔涟 (立绘交互)
    imagebutton:
        idle "cyrene idle"
        xpos 800 ypos 100
        action Return("cyrene")
        
    # 仪式剑
    imagebutton:
        idle "icon_sword"
        xpos 200 ypos 400
        action Return("sword")
        
    # 故事书
    imagebutton:
        idle "icon_books"
        xpos 400 ypos 500
        action Return("books")
        
    # 信箱
    imagebutton:
        idle "icon_mailbox"
        xpos 1100 ypos 300
        action Return("mailbox")