# 第一章第一幕：书房搜查界面
screen ch1_act1_study_investigation():
    # 背景
    add "bg study_room"

    # 昔涟 (立绘交互)
    use smart_interactable("cyrene", "cyrene idle", Return("cyrene"))

    # 仪式剑
    use smart_interactable("sword", "icon_sword", Return("sword"))

    # 故事书
    use smart_interactable("books", "icon_books", Return("books"))

    # 信箱
    use smart_interactable("mailbox", "icon_mailbox", Return("mailbox"))