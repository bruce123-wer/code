# 角色信息
player = {
    "attributes": {"life": 100, "magic": 100},
    "skills": {
        "normal_attack": {"life": -5},
        "ultimate_skill": {"life": -20, "magic": -20},
    },
    "equipments": {
        "护盾": {"num": 0, "defense": 20, "cost": 20},
        "剑": {"num": 0, "attack": -10, "cost": 20},
    },
    "props": {
        "恢复药水": {"num": 0, "life": 20, "cost": 20},
        "魔法药水": {"num": 0, "magic": 20, "cost": 20},
    },
    "coins": 0,
}
little_monster = {
    "attributes": {
        "life": 50,
    },
    "skills": {"normal_attack": {"life": -5}},
    "drops": 20,
}
boss = {
    "attributes": {"life": 200},
    "skills": {"normal_attack": {"life": -10}, "ultimate_skill": {"life": -30}},
    "drops": 40,
}


# 挑战模式
def fight():
    # 初始化统计变量
    life_medicine_uesd = 0
    magic_medicine_used = 0
    shield_damaged = 0

    # 玩家选择
    while True:
        player_choose = input(
            "请输入你想要挑战的对象：\n按下1挑战小怪\n按下2挑战boss\n玩家输入："
        ).strip()
        print("")
        if player_choose == "1":
            monster_type = little_monster
            print("你选择了挑战小怪!")
            print("")
            break
        elif player_choose == "2":
            monster_type = boss
            print("你选择了挑战boss!")
            print("")
            break
        else:
            print("请在给出的范围里选择哦！")

    # 加载属性
    monster_attributes = monster_type["attributes"]
    monster_life = monster_attributes["life"]
    monster_skills = monster_type["skills"]
    monster_drops = monster_type["drops"]
    total_damage = 0
    player_attributes = player["attributes"]
    player_life = player_attributes["life"]
    player_magic = player_attributes["magic"]
    player_skills = player["skills"]
    player_equipments = player["equipments"]
    player_total_defense = (
        player_equipments["护盾"]["defense"] * player_equipments["护盾"]["num"]
    )
    player_attack_plus = (
        player_equipments["剑"]["attack"] * player_equipments["剑"]["num"]
    )
    player_props = player["props"]

    # 开始战斗!
    if monster_type == little_monster:
        while monster_life * player_life > 0:
            # 你的回合
            while True:
                player_input1 = input(
                    "现在是你的回合，请选择使用技能或道具：\n按下1选择技能\n按下2选择道具\n玩家输入："
                )
                print("")
                if player_input1 in ["1", "2"]:
                    break
                else:
                    print("请在给出的范围内选择哦！")
                    print("")
            if player_input1 == "1":
                while True:
                    player_input2 = input("按下1选择普攻，\n按下2选择大招\n玩家输入：")
                    print("")
                    if player_input2 == "1":
                        attack_sum = (
                            player_skills["normal_attack"]["life"] + player_attack_plus
                        )
                        monster_life += attack_sum
                        print(
                            f"你对小怪造成了{abs(attack_sum)}点伤害！小怪剩余血量为{monster_life}"
                        )
                        print("")
                        break
                    if player_input2 == "2":
                        player_magic += player_skills["ultimate_skill"]["magic"]
                        if player_magic >= 0:
                            attack_sum = (
                                player_skills["ultimate_skill"]["life"]
                                + player_attack_plus
                            )
                            monster_life += attack_sum
                            print(
                                f"你给小怪造成了{abs(attack_sum)}点伤害！小怪剩余血量为{monster_life}"
                            )
                            print(f"你的魔力还剩{player_magic}")
                            print("")
                            break
                        else:
                            print("魔力不足！")
                            print("")
                            player_magic -= player_skills["ultimate_skill"]["magic"]
                            break
                    else:
                        print("请在给定的范围内选择哦！")
                        print("")
            else:
                life_medicine_uesd = 0
                magic_medicine_used = 0
                while True:
                    player_input2 = input(
                        "按下1使用恢复药水，\n按下2使用魔法药水\n玩家输入："
                    )
                    print("")
                    if player_input2 == "1":
                        if player_props["恢复药水"]["num"] > 0:
                            player_life += player_props["恢复药水"]["life"]
                            player_props["恢复药水"]["num"] -= 1
                            life_medicine_uesd += 1
                            print(
                                f"你使用了恢复药水！生命值恢复{player_props['恢复药水']['life']}点"
                            )
                            print(f"剩余药水数量：{player_props['恢复药水']['num']}")
                            print("")
                            break
                        else:
                            print("恢复药水不足！")
                            print("")
                            break
                    elif player_input2 == "2":
                        if player_props["魔法药水"]["num"] > 0:
                            player_magic += player_props["魔法药水"]["magic"]
                            player_props["魔法药水"]["num"] -= 1
                            magic_medicine_used += 1
                            print(
                                f"你使用了魔法药水！魔力值恢复{player_props['魔法药水']['magic']}点"
                            )
                            print(f"剩余药水数量：{player_props['魔法药水']['num']}")
                            print("")
                            break
                        else:
                            print("魔法药水不足！")
                            print("")
                            break
                    else:
                        print("请在给定的范围内选择哦！")
                        print("")
            # 小怪的回合
            if monster_life > 0:
                print("现在是小怪的回合，小怪对你使用了普攻！")
                damage = abs(monster_skills["normal_attack"]["life"])
                total_damage += damage
                if player_total_defense > 0:
                    player_total_defense -= damage
                    if player_total_defense < 0:
                        player_life += player_total_defense
                        player_total_defense = 0
                    print(
                        f"护盾吸收了{player_equipments['护盾']['defense'] * player_equipments['护盾']['num']-player_total_defense}点伤害！剩余护盾值为{player_total_defense}"
                    )
                else:
                    player_life += monster_skills["normal_attack"]["life"]
                    print(f"你受到了{damage}点伤害！剩余血量为{player_life}")
                print("")
            else:
                print(f"恭喜你获得了胜利！小怪掉落了{monster_drops}个金币！")
                print("")

        else:
            if player_life <= 0:
                print("你输了！\n变强后再来吧！")
                print("")
            else:
                player["coins"] += monster_drops

        # 统计战损
        shield_damaged = min(
            total_damage // player_equipments["护盾"]["defense"],
            player["equipments"]["护盾"]["num"],
        )
        player["equipments"]["护盾"]["num"] -= shield_damaged
        print(
            f"这场战斗中你损失了{shield_damaged}个护盾，使用了{life_medicine_uesd}瓶恢复药水，{magic_medicine_used}瓶魔法药水"
        )
        print("")

    else:
        count = 0
        while monster_life * player_life > 0:
            count += 1
            # 你的回合
            while True:
                player_input1 = input(
                    "现在是你的回合，请选择使用技能或道具：\n按下1选择技能\n按下2选择道具\n玩家输入："
                )
                print("")
                if player_input1 in ["1", "2"]:
                    break
                else:
                    print("请在给出的范围内选择哦！")
                    print("")
            if player_input1 == "1":
                while True:
                    player_input2 = input("按下1选择普攻，\n按下2选择大招\n玩家输入：")
                    print("")
                    if player_input2 == "1":
                        attack_sum = (
                            player_skills["normal_attack"]["life"] + player_attack_plus
                        )
                        monster_life += attack_sum
                        print(
                            f"你对boss造成了{abs(attack_sum)}点伤害！boss剩余血量为{monster_life}"
                        )
                        break

                    elif player_input2 == "2":
                        player_magic += player_skills["ultimate_skill"]["magic"]
                        if player_magic >= 0:
                            attack_sum = (
                                player_skills["ultimate_skill"]["life"]
                                + player_attack_plus
                            )
                            monster_life += attack_sum
                            print(
                                f"你给boss造成了{abs(attack_sum)}点伤害！boss剩余血量为{monster_life}"
                            )
                            print(f"你的魔力还剩{player_magic}")
                            print("")
                            break
                        else:
                            print("魔力不足！")
                            print("")
                            player_magic -= player_skills["ultimate_skill"]["magic"]
                            break
                    else:
                        print("请在给定的范围内选择哦！")
                        print("")
            else:
                life_medicine_uesd = 0
                magic_medicine_used = 0
                while True:
                    player_input2 = input(
                        "按下1使用恢复药水，\n按下2使用魔法药水\n玩家输入："
                    )
                    print("")
                    if player_input2 == "1":
                        if player_props["恢复药水"]["num"] > 0:
                            player_life += player_props["恢复药水"]["life"]
                            player_props["恢复药水"]["num"] -= 1
                            life_medicine_uesd += 1
                            print(
                                f"你使用了恢复药水！生命值恢复{player_props['恢复药水']['life']}点"
                            )
                            print(f"剩余药水数量：{player_props['恢复药水']['num']}")
                            print("")
                            break
                        else:
                            print("恢复药水不足！")
                            print("")
                            break
                    elif player_input2 == "2":
                        if player_props["魔法药水"]["num"] > 0:
                            player_magic += player_props["魔法药水"]["magic"]
                            player_props["魔法药水"]["num"] -= 1
                            magic_medicine_used += 1
                            print(
                                f"你使用了魔法药水！魔力值恢复{player_props['魔法药水']['magic']}点"
                            )
                            print(f"剩余药水数量：{player_props['魔法药水']['num']}")
                            print("")
                            break
                        else:
                            print("魔法药水不足！")
                            print("")
                            break
                    else:
                        print("请在给定的范围内选择哦！")
                        print("")
            # boss的回合
            if monster_life > 0:
                if count % 3 != 0:
                    print("现在是boss的回合，boss对你使用了普攻！")
                    damage = abs(monster_skills["normal_attack"]["life"])
                    total_damage += damage
                    if player_total_defense > 0:
                        player_total_defense -= damage
                        if player_total_defense < 0:
                            player_life += player_total_defense
                            player_total_defense = 0
                        print(
                            f"护盾吸收了{player_equipments['护盾']['defense'] * player_equipments['护盾']['num']-player_total_defense}点伤害！剩余护盾值为{player_total_defense}"
                        )
                    else:
                        player_life += monster_skills["normal_attack"]["life"]
                        print(f"你受到了{damage}点伤害！剩余血量为{player_life}")
                    print("")
                else:
                    print("现在是boss的回合，boss对你使用了大招！")
                    damage = abs(monster_skills["ultimate_skill"]["life"])
                    total_damage += damage
                    if player_total_defense > 0:
                        player_total_defense -= damage
                        if player_total_defense < 0:
                            player_life += player_total_defense
                            player_total_defense = 0
                        print(
                            f"护盾吸收了{player_equipments['护盾']['defense'] * player_equipments['护盾']['num']-player_total_defense}点伤害！剩余护盾值为{player_total_defense}"
                        )
                    else:
                        player_life += monster_skills["ultimate_skill"]["life"]
                        print(f"你受到了{damage}点伤害！剩余血量为{player_life}")
                    print("")
            else:
                print(f"恭喜你获得了胜利！boss掉落了{monster_drops}个金币！")
                print("")

        else:
            if player_life <= 0:
                print("你输了！\n变强后再来吧！")
                print("")
            else:
                player["coins"] += monster_drops

        # 统计战损
        shield_damaged = min(
            total_damage // player_equipments["护盾"]["defense"],
            player["equipments"]["护盾"]["num"],
        )
        player["equipments"]["护盾"]["num"] -= shield_damaged
        print(
            f"这场战斗中你损失了{shield_damaged}个护盾，使用了{life_medicine_uesd}瓶恢复药水，{magic_medicine_used}瓶魔法药水"
        )
        print("")


def store():
    while True:
        print(f"玩家你好！你目前的金币总数为{player['coins']}")
        print("商店的商品有：\n1.护盾\n2.剑\n3.恢复药水\n4.魔法药水")
        print("")
        player_input = input(
            "请问你要了解什么商品？\n按下1了解护盾\n按下2了解剑\n按下3了解恢复药水\n按下4了解魔法药水\n按下5退出商店\n玩家输入："
        )
        print("")
        if player_input == "1":
            while True:
                player_input1 = input(
                    f"护盾可以提供{player['equipments']['护盾']['defense']}点护盾值，怪物必须破坏护盾才可以伤害到玩家，价值{player['equipments']['护盾']['cost']}金币,\n按下1购买，\n按下2返回商店初始界面,\n玩家输入："
                )
                if player_input1 == "1":
                    player["coins"] -= player["equipments"]["护盾"]["cost"]
                    if player["coins"] < 0:
                        print("金币不足！")
                        print("")
                        player["coins"] += player["equipments"]["护盾"]["cost"]
                    else:
                        print("购买成功!")
                        print("")
                        player["equipments"]["护盾"]["num"] += 1
                        break
                elif player_input1 == "2":
                    print("")
                    break
                else:
                    print("请在给出的范围里选择哦！")

        elif player_input == "2":
            while True:
                player_input1 = input(
                    f"剑可以增加{abs(player['equipments']['剑']['attack'])}点攻击伤害，价值{player['equipments']['剑']['cost']}金币\n按下1购买，\n按下2返回商店初始界面\n玩家输入："
                )
                if player_input1 == "1":
                    player["coins"] -= player["equipments"]["剑"]["cost"]
                    if player["coins"] < 0:
                        print("金币不足！")
                        print("")
                        player["coins"] += player["equipments"]["剑"]["cost"]
                    else:
                        print("购买成功!")
                        print("")
                        player["equipments"]["剑"]["num"] += 1
                        break
                elif player_input1 == "2":
                    print("")
                    break
                else:
                    print("请在给出的范围里选择哦！")

        elif player_input == "3":
            while True:
                player_input1 = input(
                    f"恢复药水可以恢复{player['props']['恢复药水']['life']}点生命值，价值{player['props']['恢复药水']['cost']}金币\n按下1购买，\n按下2返回商店初始界面\n玩家输入："
                )
                if player_input1 == "1":
                    player["coins"] -= player["props"]["恢复药水"]["cost"]
                    if player["coins"] < 0:
                        print("金币不足！")
                        print("")
                        player["coins"] += player["props"]["恢复药水"]["cost"]
                    else:
                        print("购买成功!")
                        print("")
                        player["props"]["恢复药水"]["num"] += 1
                        break
                elif player_input1 == "2":
                    print("")
                    break
                else:
                    print("请在给出的范围里选择哦！")

        elif player_input == "4":
            while True:
                player_input1 = input(
                    f"魔法药水可以恢复{player['props']['魔法药水']['magic']}点魔力值，价值{player['props']['魔法药水']['cost']}金币\n按下1购买，\n按下2返回商店初始界面\n玩家输入："
                )
                if player_input1 == "1":
                    player["coins"] -= player["props"]["魔法药水"]["cost"]
                    if player["coins"] < 0:
                        print("金币不足！")
                        print("")
                        player["coins"] += player["props"]["魔法药水"]["cost"]
                    else:
                        print("购买成功!")
                        print("")
                        player["props"]["魔法药水"]["num"] += 1
                        break
                elif player_input1 == "2":
                    print("")
                    break
                else:
                    print("请在给出的范围里选择哦！")
        elif player_input == "5":
            break
        else:
            print("请在给定的范围内选择哦！")


# 游戏开始
while True:
    print("欢迎来到大厅！请做出你的选择：\n按下1开始挑战\n按下2前往商店\n按下3结束游戏")
    player_input = input("玩家输入：")
    print("")
    match player_input:
        case "1":
            fight()
        case "2":
            store()
        case "3":
            print("游戏结束")
            break
        case _:
            print("请在给定的范围内选择哦！")
