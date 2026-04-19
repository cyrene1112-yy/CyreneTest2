label chapter_1_start:
    # 初始化第一幕搜查的标志位
    $ inv_cyrene = False
    $ inv_sword = False
    $ inv_books = False
    $ inv_mailbox = False
    
    jump ch1_act1_main

label ch1_act1_main:
    scene bg study_room with fade
    show cyrene idle
    
    cyrene "。。。就这样，小浣熊和小妖精的故事就告一段落了。"
    cyrene "小浣熊和小妖精结下了爱的约定。随后，小妖精牺牲自己，为小浣熊开辟了前往明天的道路。"
    cyrene "它们会再见吗？它们未来的故事会是怎样的呢？"
    cyrene "唉，真可惜，故事到这里暂时结束了呢。"
    cyrene "还想听别的故事吗？还是要在房间里看看呢？"
    
    tb_inner "。。。"
    tb_inner "昔涟，我终于，又见到你了。"
    
    # 黑底白字转场
    scene bg black with fade
    centered "不久前，黑塔空间站。"
    
    scene bg herta_station with fade
    show herta idle
    
    herta "这是用你的力量开发的针对忆灵的记忆容器。以及可以传送到翁法罗斯任意地区的传送锚。"
    
    show screen custom_notify("获得物品：【记忆容器】\n获得物品：【传送锚】")
    pause 2.0
    
    herta "但在出发前，我再问一遍，你，真的做好准备了吗。"
    herta "计划一，小粉毛作为因你而在的忆灵，通过收集和她的回忆，然后用足够的记忆将她复原出来，确实有一定有可行性。"
    herta "考虑到你连将如我所书的数据生命升格到新生翁法罗斯这种事都能做到，我就勉为其难地相信你。"
    tb "哈哈哈。。。"
    herta "但是！"
    herta "计划二：去代替身为记忆星神的她，降下因果？你真是疯了。"
    herta "铁幕复生？甚至更可怕的事情？这种逆转因果的事，一旦发生差错，会发生什么，我不敢想。"
    tb "她说过，愿意相信我和身为人的自己。这一次，"
    tb "该我为她书写明天了。"
    tb "求求你了，美貌无双的黑塔女士，以后我一定天天帮你测试模拟宇宙。"
    herta "唉行了行了，你都求了我多少次了。"
    
    # 插入CG
    show cg herta_smile with dissolve
    herta "就当是为了感谢你和她阻止了我变成丑八怪的那个结局吧。"
    
    # 回到书房
    scene bg study_room with fade
    show cyrene idle
    
    show screen custom_notify("角色档案 【昔涟】 已更新\n角色档案 【大黑塔】 已更新")
    pause 2.5
    
    tb_inner "先试着和场景中的物品以及昔涟互动，多收集一些回忆，填充记忆容器吧。"

# ==========================================
# 搜查阶段循环
# ==========================================
label ch1_act1_investigation_loop:
    # 检查是否所有物品都已互动
    if inv_cyrene and inv_sword and inv_books and inv_mailbox:
        jump ch1_act1_end
        
    call screen ch1_act1_study_investigation
    
    if _return == "cyrene":
        jump ch1_act1_interact_cyrene
    elif _return == "sword":
        jump ch1_act1_interact_sword
    elif _return == "books":
        jump ch1_act1_interact_books
    elif _return == "mailbox":
        jump ch1_act1_interact_mailbox

# ==========================================
# 物品互动分支
# ==========================================
label ch1_act1_interact_cyrene:
    tb_inner "黑塔叮嘱过，一定要避免过多的影响因果。"
    tb_inner "所以，这个时间段的我只能以这个“心中的英雄”的姿态出现。并且只能说话，不要物理上干涉现实。"
    tb_inner "更严禁明确透露未来的事。"
    
    tb "昔涟，你回忆起来你的身世了吗？"
    cyrene "（摇头）在树下突然出现，永远没有变化的身体，天生拥有岁月的能力。。。"
    cyrene "虽然哀丽秘榭的大家对我都很好，村里的小朋友也愿意带我一起玩。"
    cyrene "但偶尔也会对自己的身世感到迷茫呢。"
    tb "那你对你的身世是怎么想的呢？"
    cyrene "我曾分析过，我现在是不是由前世的我因为某种原因转世而来的呢？"
    tb_inner "真聪明。"
    cyrene "虽然前世的我留下的记忆不多，"
    cyrene "（笑）但幸运的是，我还记得最重要的——你。"
    cyrene "（笑）我的未来的大英雄，只要你在我身边，我就什么都能做到。"
    cyrene "我会一直等待，等待你真正来到我身边的那一天。"
    
    if not inv_cyrene:
        $ memory_sys.add(1)
        $ inv_cyrene = True
    jump ch1_act1_investigation_loop

label ch1_act1_interact_sword:
    narrator "寄托了记忆命途的能力，一柄传承了绝望与希望的剑。未来会经历很多精彩的故事吧。"
    $ inv_sword = True
    jump ch1_act1_investigation_loop

label ch1_act1_interact_books:
    narrator "书房里堆满了书，看的出来主人非常喜欢各种故事。"
    tb "我看看，《逐火之旅》、《阳雷骑士传记》、《凯撒大帝的一生》"
    tb "《黄金迷境大饭店》、《最强奇美拉训练家》、《豹豹碰碰大作战》"
    tb "《再创天地的救世主》、《小浣熊与小妖精》、《苍天航路绒绒号》"
    tb "。。。怎么还有《苍天航路绒绒号》？是虚照派来的忆者流落的吗"
    tb "回头该找她收点版权费了。"
    cyrene "想听什么故事呢？"
    
    menu:
        "《逐火之旅》":
            cyrene "这是讲述翁法罗斯历史的故事。"
            cyrene "xxx年，最初的半神缇里西庇俄斯获得了逐火的神谕。收集火种，开启新世界。"
            cyrene "之前，凯撒大帝曾带领黄金裔发起一次逐火之旅，不过以凯撒的驾崩而终止了。"
            cyrene "我被选为岁月的继承者，以后应该也会踏上逐火的道路吧。"
            
        "《黄金迷境大饭店》":
            cyrene "这本书讲的是在末日时一对夫妻突然穿越到仙境经营饭店的故事。"
            cyrene "里面有很多奇特的幻想呢，比人高的南瓜，一天就能种出来的蔬菜。"
            cyrene "朋友们都死而复生，来饭店帮忙呢。"
            cyrene "可惜呀，最后发现只是一场梦。"
            cyrene "即使是梦，也很美好，愿意让人沉浸其中呢。"
            cyrene "真好呀，我也想和我最爱的人一起经营饭店呢。"
            
        "《再创天地的救世主》":
            cyrene "传说中，当世界陷入危机时，会有一道流星划破天空。"
            cyrene "天外的救世主，带着无名的善意来到这个世界。"
            cyrene "救世主虽然并非本地人，但他依然为这个世界一次次踏入险境，献出鲜血和生命。"
            cyrene "他和当地的英雄们成为了挚友，历经无数冒险，击败了幕后反派。"
            cyrene "（笑）很不错的故事，对吧。"
            cyrene "和这位救世主一起的冒险，一定很精彩吧。"
            
    if not inv_books:
        $ memory_sys.add(1)
        $ inv_books = True
    jump ch1_act1_investigation_loop

label ch1_act1_interact_mailbox:
    tb_inner "看起来是一个普通的信箱。"
    $ inv_mailbox = True
    jump ch1_act1_investigation_loop

label ch1_act1_end:
    tb_inner "之后去其他地方看看吧。"
    # 之后这里会改成 jump ch1_act2_start
    centered "【第一幕 结束】"
    return