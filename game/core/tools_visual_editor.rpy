# ==========================================
# 可视化拖拽调位工具 (Visual Editor)
# ==========================================

default dev_mode = False

# 搜查物品坐标字典
default inv_pos_dict = {
    "cyrene": (800, 100),
    "sword": (200, 400),
    "books": (400, 500),
    "mailbox": (1100, 300)
}

init python:
    import pygame

    # 初始化 pygame.scrap 用于剪贴板
    try:
        pygame.scrap.init()
    except Exception:
        pass

    def dev_item_dragged(drags, drop):
        if not drags:
            return

        dragged_item = drags[0]
        item_id = dragged_item.drag_name

        # 更新字典坐标
        inv_pos_dict[item_id] = (int(dragged_item.x), int(dragged_item.y))

        # 强制刷新UI以应用新坐标（虽然 drag 元件自己会移动，但保证 state 一致）
        renpy.restart_interaction()
        return

    def copy_dev_coords():
        # 生成可直接粘贴的代码字符串
        lines = ["default inv_pos_dict = {"]
        for k, v in inv_pos_dict.items():
            lines.append(f'    "{k}": ({v[0]}, {v[1]}),')
        lines.append("}")

        copy_str = "\n".join(lines)

        # 写入剪贴板
        try:
            pygame.scrap.put(pygame.scrap.SCRAP_TEXT, copy_str.encode('utf-8'))
            renpy.notify("坐标已复制到剪贴板！")
        except Exception as e:
            renpy.notify("复制失败，请查看控制台！")
            print("Clipboard error:", e)

# ==========================================
# 智能互动组件
# ==========================================
screen smart_interactable(item_id, img_path, action_logic):
    $ item_pos = inv_pos_dict.get(item_id, (0, 0))

    if dev_mode:
        draggroup:
            drag:
                drag_name item_id
                child img_path
                pos item_pos
                dragged dev_item_dragged
                clicked action_logic
    else:
        imagebutton:
            idle img_path
            pos item_pos
            action action_logic

# ==========================================
# 全局热键与开发者UI层
# ==========================================
screen dev_mode_overlay():
    zorder 1000

    # 快捷键 F8 切换 dev_mode
    key "K_F8" action ToggleVariable("dev_mode", True, False)

    if dev_mode:
        vbox:
            align (0.0, 0.0)
            text "【Dev Mode: ON】 (F8切换)" color "#ff0000" size 30 outlines [(2, "#000", 0, 0)]
            textbutton "复制所有最新坐标":
                action Function(copy_dev_coords)
                text_color "#fff"
                background "#0008"

init python:
    # 将开发者 UI 层注入全局始终显示的 screen 列表中
    config.always_shown_screens.append("dev_mode_overlay")