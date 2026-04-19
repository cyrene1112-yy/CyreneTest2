# ==========================================
# 角色定义
# ==========================================
define tb = Character("主角", color="#d4a135")
define tb_inner = Character("主角内心", color="#888888", what_prefix="（", what_suffix="）")
define cyrene = Character("昔涟", color="#ffd700")
define herta = Character("大黑塔", color="#8a2be2")
define narrator = Character("旁白", color="#cccccc")

# ==========================================
# 图像与CG定义
# ==========================================
image bg black = "#000000"
image bg study_room = "assets/bg/study_room.jpg" 
image bg herta_station = "assets/bg/herta_station.jpg" 
image cg herta_smile = "assets/cg/herta_smile.jpg" 

# 立绘占位
image cyrene idle = "assets/sprites/cyrene_idle.png" 
image herta idle = "assets/sprites/herta_idle.png"

# 利用 Transform 自动将高清道具图等比例缩放至最大 200x200
image icon_sword = Transform("assets/items/sword_idle.png", maxsize=(200, 200))
image icon_books = Transform("assets/items/books_idle.png", maxsize=(200, 200))
image icon_mailbox = Transform("assets/items/mailbox_idle.png", maxsize=(200, 200))

# ==========================================
# UI 界面与系统逻辑
# ==========================================
# 自定义弹窗提示 UI
screen custom_notify(message, icon=""):
    zorder 100
    frame:
        align (0.5, 0.1)
        background Solid("#000000cc")
        padding (20, 10)
        hbox:
            spacing 10
            if icon:
                add icon size (40, 40)
            text message size 28 color "#ffffff"
    timer 3.0 action Hide("custom_notify")

init python:
    # 回忆碎片系统
    class MemorySystem:
        def __init__(self):
            self.shards = 0
            self.max_shards = 100
            
        def add(self, amount=1):
            self.shards += amount
            renpy.show_screen("custom_notify", f"【回忆碎片 +{amount}】")
            # 暂时注释音效，等你有 sfx_shard.ogg 素材后再取消注释
            # renpy.play("assets/audio/sfx_shard.ogg") 

    memory_sys = MemorySystem()