# -*- coding: utf-8 -*-
def t400504_1():
    """State 0,1"""
    assert GetCurrentStateElapsedTime() > 1
    while True:
        """State 2"""
        call = t400504_x0()
        assert IsClientPlayer()
        """State 3"""
        call = t400504_x1()
        assert not IsClientPlayer()

def t400504_x0():
    """State 0,1"""
    t400504_x3()
    Quit()

def t400504_x1():
    """State 0,1"""
    assert t400504_x2()
    """State 2"""
    return 0

def t400504_x2():
    """State 0,1"""
    if not CheckSpecificPersonTalkHasEnded(0):
        """State 7"""
        ClearTalkProgressData()
        StopEventAnimWithoutForcingConversationEnd(0)
        """State 6"""
        ReportConversationEndToHavokBehavior()
    else:
        pass
    """State 2"""
    if CheckSpecificPersonGenericDialogIsOpen(0):
        """State 3"""
        ForceCloseGenericDialog()
    else:
        pass
    """State 4"""
    if CheckSpecificPersonMenuIsOpen(-1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0):
        """State 5"""
        ForceCloseMenu()
    else:
        pass
    """State 8"""
    return 0

def t400504_x3():
    """State 0,1"""
    call = t400504_x4()
    assert CheckSelfDeath()
    """State 2"""
    return 0

def t400504_x4():
    """State 0"""
    while True:
        """State 5"""
        call = t400504_x5()
        if call.Done():
            """State 3"""
            call = t400504_x8()
            if call.Done():
                pass
            elif IsAttackedBySomeone():
                """State 1"""
                Label('L0')
                call = t400504_x6()
                def ExitPause():
                    RemoveMyAggro()
                if call.Done():
                    pass
                elif IsPlayerDead():
                    break
            elif IsPlayerDead():
                break
            elif GetDistanceToPlayer() > 2 or GetPlayerYDistance() > 0.25:
                """State 4"""
                call = t400504_x7()
                if call.Done() and (GetDistanceToPlayer() < 1.5 and GetPlayerYDistance() < 0.249):
                    pass
                elif IsAttackedBySomeone():
                    Goto('L0')
        elif IsAttackedBySomeone():
            Goto('L0')
        elif IsPlayerDead():
            break
    """State 2"""
    t400504_x2()
    Quit()

def t400504_x5():
    """State 0"""
    while True:
        """State 1"""
        assert (not GetOneLineHelpStatus() and not IsTalkingToSomeoneElse() and not IsClientPlayer() and not IsPlayerDead()
                and not IsCharacterDisabled())
        """State 2"""
        if (not (not GetOneLineHelpStatus() and not IsTalkingToSomeoneElse() and not IsClientPlayer() and not IsPlayerDead()
            and not IsCharacterDisabled())):
            pass
        elif CheckActionButtonArea(6120):
            break
    """State 4"""
    return 0

def t400504_x6():
    """State 0,6"""
    assert t400504_x2()
    """State 3"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if GetDistanceToPlayer() > 3:
        """State 7"""
        assert t400504_x2()
    else:
        """State 5"""
        pass
    """State 9"""
    return 0

def t400504_x7():
    """State 0,1"""
    if CheckSpecificPersonMenuIsOpen(-1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0):
        """State 2,5"""
        assert GetDistanceToPlayer() > 3
    else:
        """State 3"""
        pass
    """State 4"""
    assert t400504_x2()
    """State 6"""
    return 0

def t400504_x8():
    """State 0,1"""
    assert t400504_x9()
    """State 24"""
    return 0

def t400504_x9():
    while True:
        """State 0"""
        MainBonfireMenuFlag()
        ClearTalkListData()
        # action:15010007:""
        AddTalkListDataIf(not GetEventFlag(25009850), 1, 15010007, -1)
        # action:15010008:""
        AddTalkListDataIf(not GetEventFlag(25009850) and GetEventFlag(25009812), 4, 15010008, -1)
        AddTalkListDataIf(not GetEventFlag(25009814), 3, 99002532, -1)
        # goods:2002:
        AddTalkListDataIf(not GetEventFlag(25009520) and ComparePlayerInventoryNumber(ItemType.Goods, 2002, CompareType.Greater, 0, False),
                          5, 99003500, -1)
        AddTalkListDataIf(not GetEventFlag(25008190) and ComparePlayerInventoryNumber(ItemType.Goods, 2000, CompareType.Greater, 0, False),
                          10, 15015040, -1)
        AddTalkListDataIf(GetEventFlag(25008190), 11, 15015041, -1)
        AddTalkListDataIf(GetEventFlag(25008190), 12, 15015042, -1)
        AddTalkListData(2, 99010001, -1)
        # action:15000005:"Leave"
        AddTalkListData(99, 15000005, -1)
        assert (not CheckSpecificPersonGenericDialogIsOpen(2) and not (CheckSpecificPersonMenuIsOpen(-1, 2) and
                not CheckSpecificPersonGenericDialogIsOpen(2)))
        """State 1"""
        ShowShopMessage(TalkOptionsType.Regular)
        if GetTalkListEntryResult() == 1:
            """State 2"""
            OpenRegularShop(260000, 260499)
        elif GetTalkListEntryResult() == 4:
            """State 3"""
            OpenTranspositionShop(260500, 260999)
        elif GetTalkListEntryResult() == 2:
            """State 4"""
            assert t400504_x10(text1=10018000, flag1=0, mode1=0)
        elif GetTalkListEntryResult() == 10:
            """State 5"""
            SetEventFlag(25008190, FlagState.On)
            PlayerEquipmentQuantityChange(ItemType.Goods, 2000, -1)
            assert t400504_x10(text1=10117030, flag1=0, mode1=0)
        elif GetTalkListEntryResult() == 11:
            """State 6"""
            if GetEventFlag(25008900):
                """State 7"""
                assert t400504_x10(text1=10117000, flag1=0, mode1=0)
                """State 8"""
                AwardItemLot(90180)
            elif GetEventFlag(25008901):
                """State 9"""
                assert t400504_x10(text1=10117010, flag1=0, mode1=0)
            elif GetEventFlag(25008902):
                """State 10"""
                assert t400504_x10(text1=10117020, flag1=0, mode1=0)
        elif GetTalkListEntryResult() == 12:
            """State 11"""
            assert t400504_x10(text1=10117020, flag1=0, mode1=0)
            """State 12"""
            SetEventFlag(25008190, FlagState.Off)
            return 0
        elif GetTalkListEntryResult() == 5:
            """State 13"""
            SetEventFlag(25009520, FlagState.On)
            # goods:2002:
            PlayerEquipmentQuantityChange(ItemType.Goods, 2002, -1)
            assert t400504_x10(text1=10117000, flag1=0, mode1=0)
        elif GetTalkListEntryResult() == 3:
            """State 14"""
            assert t400504_x20()
            """State 15"""
            return 0
        elif not (CheckSpecificPersonMenuIsOpen(-1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0)):
            """State 16"""
            return 0

def t400504_x10(text1=_, flag1=0, mode1=0):
    """State 0,4"""
    assert t400504_x11() and CheckSpecificPersonTalkHasEnded(0)
    """State 1"""
    TalkToPlayer(text1, -1, -1, flag1)
    assert CheckSpecificPersonTalkHasEnded(0)
    """State 3"""
    if mode1 == 0:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t400504_x11():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t400504_x20():
    while True:
        """State 0"""
        MainBonfireMenuFlag()
        ClearTalkListData()
        AddTalkListData(2, 99015001, -1)
        AddTalkListData(1, 99015000, -1)
        # action:15000005:"Leave"
        AddTalkListData(99, 15000005, -1)
        assert (not CheckSpecificPersonGenericDialogIsOpen(2) and not (CheckSpecificPersonMenuIsOpen(-1, 2) and
                not CheckSpecificPersonGenericDialogIsOpen(2)))
        """State 1"""
        ShowShopMessage(TalkOptionsType.Regular)
        if GetTalkListEntryResult() == 1:
            """State 2"""
            assert t400504_x40()
        elif GetTalkListEntryResult() == 2:
            """State 3"""
            OpenGenericDialog(DialogBoxType.CenterMiddleDimScreen1, 99015020, DialogResult.Cancel, DialogBoxStyle.OrnateNoOptions,
                              0)
        elif GetTalkListEntryResult() == 99:
            """State 4"""
            ReportConversationEndToHavokBehavior()
            return 0
        elif not (CheckSpecificPersonMenuIsOpen(-1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0)):
            """State 5"""
            return 0

def t400504_x40():
    """State 0"""
    MainBonfireMenuFlag()
    ClearTalkListData()
    AddTalkListData(1, 99015005, -1)
    AddTalkListData(2, 99015006, -1)
    AddTalkListData(3, 99015007, -1)
    AddTalkListData(4, 99015008, -1)
    AddTalkListData(5, 99015009, -1)
    # action:15000180:"Quit"
    AddTalkListData(99, 15000180, -1)
    assert (not CheckSpecificPersonGenericDialogIsOpen(2) and not (CheckSpecificPersonMenuIsOpen(-1, 2) and not
            CheckSpecificPersonGenericDialogIsOpen(2)))
    """State 1"""
    ShowShopMessage(TalkOptionsType.Regular)
    if GetTalkListEntryResult() == 1:
        """State 2"""
        assert t400504_x41()
        """State 3"""
        return 0
    elif GetTalkListEntryResult() == 2:
        """State 4"""
        assert t400504_x42()
        """State 5"""
        return 0
    elif GetTalkListEntryResult() == 3:
        """State 6"""
        assert t400504_x43()
        """State 7"""
        return 0
    elif GetTalkListEntryResult() == 4:
        """State 8"""
        assert t400504_x44()
        """State 9"""
        return 0
    elif GetTalkListEntryResult() == 5:
        """State 10"""
        assert t400504_x45()
        """State 11"""
        return 0
    elif not (CheckSpecificPersonMenuIsOpen(-1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0)):
        """State 12"""
        return 0

def t400504_x41():
    """State 0"""
    MainBonfireMenuFlag()
    ClearTalkListData()
    # accessory:20000:Life Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20000, CompareType.GreaterOrEqual, 1, False),
                      1, 99015100, -1)
    # accessory:20830:Dragonscale Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20830, CompareType.GreaterOrEqual, 1, False),
                      52, 99015151, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30050, CompareType.GreaterOrEqual, 1, False),
                      56, 99015155, -1)
    # accessory:20010:Chloranthy Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20010, CompareType.GreaterOrEqual, 1, False),
                      2, 99015101, -1)
    # accessory:20020:Havel's Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20020, CompareType.GreaterOrEqual, 1, False),
                      3, 99015102, -1)
    # accessory:20030:Ring of Favor
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20030, CompareType.GreaterOrEqual, 1, False),
                      4, 99015103, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30210, CompareType.GreaterOrEqual, 1, False),
                      62, 99015161, -1)
    # accessory:20430:Skull Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20430, CompareType.GreaterOrEqual, 1, False),
                      32, 99015131, -1)
    # accessory:20490:Magic Clutch Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20490, CompareType.GreaterOrEqual, 1, False),
                      36, 99015135, -1)
    # accessory:20500:Lightning Clutch Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20500, CompareType.GreaterOrEqual, 1, False),
                      37, 99015136, -1)
    # accessory:20510:Fire Clutch Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20510, CompareType.GreaterOrEqual, 1, False),
                      38, 99015137, -1)
    # accessory:20520:Dark Clutch Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20520, CompareType.GreaterOrEqual, 1, False),
                      39, 99015138, -1)
    # accessory:20340:Ring of the Sun's Firstborn
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20340, CompareType.GreaterOrEqual, 1, False),
                      25, 99015124, -1)
    # accessory:20350:Darkmoon Blade Covenant Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20350, CompareType.GreaterOrEqual, 1, False),
                      26, 99015125, -1)
    # accessory:20360:Leo Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20360, CompareType.GreaterOrEqual, 1, False),
                      27, 99015126, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30020, CompareType.GreaterOrEqual, 1, False),
                      55, 99015154, -1)
    # accessory:20040:Ring of Steel Protection
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20040, CompareType.GreaterOrEqual, 1, False),
                      5, 99015104, -1)
    # accessory:20050:Flame Stoneplate Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20050, CompareType.GreaterOrEqual, 1, False),
                      6, 99015105, -1)
    # accessory:20060:Thunder Stoneplate Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20060, CompareType.GreaterOrEqual, 1, False),
                      7, 99015106, -1)
    # accessory:20070:Magic Stoneplate Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20070, CompareType.GreaterOrEqual, 1, False),
                      8, 99015107, -1)
    # accessory:20080:Dark Stoneplate Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20080, CompareType.GreaterOrEqual, 1, False),
                      9, 99015108, -1)
    # accessory:20090:Speckled Stoneplate Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20090, CompareType.GreaterOrEqual, 1, False),
                      10, 99015109, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30660, CompareType.GreaterOrEqual, 1, False),
                      76, 99015175, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30670, CompareType.GreaterOrEqual, 1, False),
                      77, 99015176, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30680, CompareType.GreaterOrEqual, 1, False),
                      78, 99015177, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30690, CompareType.GreaterOrEqual, 1, False),
                      79, 99015178, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30700, CompareType.GreaterOrEqual, 1, False),
                      80, 99015179, -1)
    # accessory:20100:Bloodbite Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20100, CompareType.GreaterOrEqual, 1, False),
                      11, 99015110, -1)
    # accessory:20110:Poisonbite Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20110, CompareType.GreaterOrEqual, 1, False),
                      12, 99015111, -1)
    # accessory:20120:Cursebite Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20120, CompareType.GreaterOrEqual, 1, False),
                      13, 99015112, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 21000, CompareType.GreaterOrEqual, 1, False),
                      53, 99015152, -1)
    # accessory:20130:Fleshbite Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20130, CompareType.GreaterOrEqual, 1, False),
                      14, 99015113, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30930, CompareType.GreaterOrEqual, 1, False),
                      85, 99015184, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30890, CompareType.GreaterOrEqual, 1, False),
                      82, 99015181, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30940, CompareType.GreaterOrEqual, 1, False),
                      86, 99015185, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30950, CompareType.GreaterOrEqual, 1, False),
                      87, 99015186, -1)
    # accessory:20460:Knight's Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20460, CompareType.GreaterOrEqual, 1, False),
                      33, 99015132, -1)
    # accessory:20470:Hunter's Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20470, CompareType.GreaterOrEqual, 1, False),
                      34, 99015133, -1)
    # accessory:20150:Scholar Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20150, CompareType.GreaterOrEqual, 1, False),
                      16, 99015115, -1)
    # accessory:20160:Priestess Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20160, CompareType.GreaterOrEqual, 1, False),
                      17, 99015116, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30390, CompareType.GreaterOrEqual, 1, False),
                      68, 99015167, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30400, CompareType.GreaterOrEqual, 1, False),
                      69, 99015168, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30410, CompareType.GreaterOrEqual, 1, False),
                      70, 99015169, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30420, CompareType.GreaterOrEqual, 1, False),
                      71, 99015170, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30430, CompareType.GreaterOrEqual, 1, False),
                      72, 99015171, -1)
    # accessory:20140:Wood Grain Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20140, CompareType.GreaterOrEqual, 1, False),
                      15, 99015114, -1)
    # accessory:20170:Red Tearstone Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20170, CompareType.GreaterOrEqual, 1, False),
                      18, 99015117, -1)
    # accessory:20180:Blue Tearstone Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20180, CompareType.GreaterOrEqual, 1, False),
                      19, 99015118, -1)
    # accessory:20190:Wolf Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20190, CompareType.GreaterOrEqual, 1, False),
                      20, 99015119, -1)
    # accessory:20270:Lingering Dragoncrest Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20270, CompareType.GreaterOrEqual, 1, False),
                      21, 99015120, -1)
    # accessory:20280:Sage Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20280, CompareType.GreaterOrEqual, 1, False),
                      22, 99015121, -1)
    # accessory:20300:Dusk Crown Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20300, CompareType.GreaterOrEqual, 1, False),
                      23, 99015122, -1)
    # accessory:20330:Darkmoon Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20330, CompareType.GreaterOrEqual, 1, False),
                      24, 99015123, -1)
    # accessory:20370:Hawk Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20370, CompareType.GreaterOrEqual, 1, False),
                      28, 99015127, -1)
    # accessory:20390:Covetous Gold Serpent Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20390, CompareType.GreaterOrEqual, 1, False),
                      29, 99015128, -1)
    # accessory:20400:Covetous Silver Serpent Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20400, CompareType.GreaterOrEqual, 1, False),
                      30, 99015129, -1)
    # accessory:20410:Sun Princess Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20410, CompareType.GreaterOrEqual, 1, False),
                      31, 99015130, -1)
    # accessory:20480:Knight Slayer's Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20480, CompareType.GreaterOrEqual, 1, False),
                      35, 99015134, -1)
    # accessory:20540:Flynn's Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20540, CompareType.GreaterOrEqual, 1, False),
                      40, 99015139, -1)
    # accessory:20550:Prisoner's Chain
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20550, CompareType.GreaterOrEqual, 1, False),
                      41, 99015140, -1)
    # accessory:20590:Ring of the Evil Eye
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20590, CompareType.GreaterOrEqual, 1, False),
                      42, 99015141, -1)
    # accessory:20600:Calamity Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20600, CompareType.GreaterOrEqual, 1, False),
                      43, 99015142, -1)
    # accessory:20610:Farron Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20610, CompareType.GreaterOrEqual, 1, False),
                      44, 99015143, -1)
    # accessory:20660:Lloyd's Sword Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20660, CompareType.GreaterOrEqual, 1, False),
                      45, 99015144, -1)
    # accessory:20670:Lloyd's Shield Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20670, CompareType.GreaterOrEqual, 1, False),
                      46, 99015145, -1)
    # accessory:20700:Estus Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20700, CompareType.GreaterOrEqual, 1, False),
                      47, 99015146, -1)
    # accessory:20710:Ashen Estus Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20710, CompareType.GreaterOrEqual, 1, False),
                      48, 99015147, -1)
    # accessory:20720:Horsehoof Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20720, CompareType.GreaterOrEqual, 1, False),
                      49, 99015148, -1)
    # accessory:20750:Pontiff's Right Eye
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20750, CompareType.GreaterOrEqual, 1, False),
                      50, 99015149, -1)
    # accessory:20790:Pontiff's Left Eye
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20790, CompareType.GreaterOrEqual, 1, False),
                      51, 99015150, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30010, CompareType.GreaterOrEqual, 1, False),
                      54, 99015153, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30080, CompareType.GreaterOrEqual, 1, False),
                      57, 99015156, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30450, CompareType.GreaterOrEqual, 1, False),
                      73, 99015172, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30500, CompareType.GreaterOrEqual, 1, False),
                      74, 99015173, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30650, CompareType.GreaterOrEqual, 1, False),
                      75, 99015174, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30170, CompareType.GreaterOrEqual, 1, False),
                      58, 99015157, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30180, CompareType.GreaterOrEqual, 1, False),
                      59, 99015158, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30190, CompareType.GreaterOrEqual, 1, False),
                      60, 99015159, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30200, CompareType.GreaterOrEqual, 1, False),
                      61, 99015160, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30330, CompareType.GreaterOrEqual, 1, False),
                      63, 99015162, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30340, CompareType.GreaterOrEqual, 1, False),
                      64, 99015163, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30350, CompareType.GreaterOrEqual, 1, False),
                      65, 99015164, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30360, CompareType.GreaterOrEqual, 1, False),
                      66, 99015165, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30370, CompareType.GreaterOrEqual, 1, False),
                      67, 99015166, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30870, CompareType.GreaterOrEqual, 1, False),
                      90, 99015189, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30880, CompareType.GreaterOrEqual, 1, False),
                      91, 99015190, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30900, CompareType.GreaterOrEqual, 1, False),
                      92, 99015191, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31400, CompareType.GreaterOrEqual, 1, False),
                      93, 99015192, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31300, CompareType.GreaterOrEqual, 1, False),
                      94, 99015193, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31080, CompareType.GreaterOrEqual, 1, False),
                      95, 99015194, -1)
    # accessory:20380:Hornet Ring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20380, CompareType.GreaterOrEqual, 1, False),
                      96, 99015195, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31200, CompareType.GreaterOrEqual, 1, False),
                      97, 99015196, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30800, CompareType.GreaterOrEqual, 1, False),
                      98, 99015197, -1)
    # accessory:20450:Carthus Milkring
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20450, CompareType.GreaterOrEqual, 1, False),
                      99, 99015198, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30090, CompareType.GreaterOrEqual, 1, False),
                      100, 99015199, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30840, CompareType.GreaterOrEqual, 1, False),
                      101, 99015200, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30990, CompareType.GreaterOrEqual, 1, False),
                      102, 99015201, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30040, CompareType.GreaterOrEqual, 1, False),
                      103, 99015202, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31500, CompareType.GreaterOrEqual, 1, False),
                      104, 99015203, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31600, CompareType.GreaterOrEqual, 1, False),
                      105, 99015204, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31700, CompareType.GreaterOrEqual, 1, False),
                      106, 99015205, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31800, CompareType.GreaterOrEqual, 1, False),
                      107, 99015206, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31900, CompareType.GreaterOrEqual, 1, False),
                      108, 99015207, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 32000, CompareType.GreaterOrEqual, 1, False),
                      109, 99015208, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 32100, CompareType.GreaterOrEqual, 1, False),
                      110, 99015209, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 32200, CompareType.GreaterOrEqual, 1, False),
                      111, 99015210, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 32300, CompareType.GreaterOrEqual, 1, False),
                      112, 99015211, -1)
    # action:15000180:"Quit"
    AddTalkListData(999, 15000180, -1)
    assert (not CheckSpecificPersonGenericDialogIsOpen(2) and not (CheckSpecificPersonMenuIsOpen(-1, 2) and not
            CheckSpecificPersonGenericDialogIsOpen(2)))
    """State 1"""
    ShowShopMessage(TalkOptionsType.Regular)
    if GetTalkListEntryResult() == 1:
        """State 2"""
        # accessory:20000:Life Ring
        # accessory:20001:Life Ring+1
        assert t400504_x50(acc1=20000, acc2=20001, z1=1, z2=-2)
        """State 3"""
        return 0
    elif GetTalkListEntryResult() == 2:
        """State 4"""
        # accessory:20010:Chloranthy Ring
        # accessory:20011:Chloranthy Ring+1
        assert t400504_x50(acc1=20010, acc2=20011, z1=1, z2=-2)
        """State 5"""
        return 0
    elif GetTalkListEntryResult() == 3:
        """State 6"""
        # accessory:20020:Havel's Ring
        # accessory:20021:Havel's Ring+1
        assert t400504_x50(acc1=20020, acc2=20021, z1=1, z2=-2)
        """State 7"""
        return 0
    elif GetTalkListEntryResult() == 4:
        """State 8"""
        # accessory:20030:Ring of Favor
        # accessory:20031:Ring of Favor+1
        assert t400504_x50(acc1=20030, acc2=20031, z1=1, z2=-2)
        """State 9"""
        return 0
    elif GetTalkListEntryResult() == 5:
        """State 10"""
        # accessory:20040:Ring of Steel Protection
        # accessory:20041:Ring of Steel Protection+1
        assert t400504_x50(acc1=20040, acc2=20041, z1=1, z2=-2)
        """State 11"""
        return 0
    elif GetTalkListEntryResult() == 6:
        """State 12"""
        # accessory:20050:Flame Stoneplate Ring
        # accessory:20051:Flame Stoneplate Ring+1
        assert t400504_x50(acc1=20050, acc2=20051, z1=1, z2=-2)
        """State 13"""
        return 0
    elif GetTalkListEntryResult() == 7:
        """State 14"""
        # accessory:20060:Thunder Stoneplate Ring
        # accessory:20061:Thunder Stoneplate Ring+1
        assert t400504_x50(acc1=20060, acc2=20061, z1=1, z2=-2)
        """State 15"""
        return 0
    elif GetTalkListEntryResult() == 8:
        """State 16"""
        # accessory:20070:Magic Stoneplate Ring
        # accessory:20071:Magic Stoneplate Ring+1
        assert t400504_x50(acc1=20070, acc2=20071, z1=1, z2=-2)
        """State 17"""
        return 0
    elif GetTalkListEntryResult() == 9:
        """State 18"""
        # accessory:20080:Dark Stoneplate Ring
        # accessory:20081:Dark Stoneplate Ring+1
        assert t400504_x50(acc1=20080, acc2=20081, z1=1, z2=-2)
        """State 19"""
        return 0
    elif GetTalkListEntryResult() == 10:
        """State 20"""
        # accessory:20090:Speckled Stoneplate Ring
        # accessory:20091:Speckled Stoneplate Ring+1
        assert t400504_x50(acc1=20090, acc2=20091, z1=1, z2=-2)
        """State 21"""
        return 0
    elif GetTalkListEntryResult() == 11:
        """State 22"""
        # accessory:20100:Bloodbite Ring
        # accessory:20101:Bloodbite Ring+1
        assert t400504_x50(acc1=20100, acc2=20101, z1=1, z2=-2)
        """State 23"""
        return 0
    elif GetTalkListEntryResult() == 12:
        """State 24"""
        # accessory:20110:Poisonbite Ring
        # accessory:20111:Poisonbite Ring+1
        assert t400504_x50(acc1=20110, acc2=20111, z1=1, z2=-2)
        """State 25"""
        return 0
    elif GetTalkListEntryResult() == 13:
        """State 26"""
        # accessory:20120:Cursebite Ring
        # accessory:20121:
        assert t400504_x50(acc1=20120, acc2=20121, z1=1, z2=-2)
        """State 27"""
        return 0
    elif GetTalkListEntryResult() == 14:
        """State 28"""
        # accessory:20130:Fleshbite Ring
        # accessory:20131:Fleshbite Ring+1
        assert t400504_x50(acc1=20130, acc2=20131, z1=1, z2=-2)
        """State 29"""
        return 0
    elif GetTalkListEntryResult() == 15:
        """State 30"""
        # accessory:20140:Wood Grain Ring
        # accessory:20141:Wood Grain Ring+1
        assert t400504_x50(acc1=20140, acc2=20141, z1=1, z2=-2)
        """State 31"""
        return 0
    elif GetTalkListEntryResult() == 16:
        """State 32"""
        # accessory:20150:Scholar Ring
        # accessory:20151:
        assert t400504_x50(acc1=20150, acc2=20151, z1=1, z2=-2)
        """State 33"""
        return 0
    elif GetTalkListEntryResult() == 17:
        """State 34"""
        # accessory:20160:Priestess Ring
        # accessory:20161:
        assert t400504_x50(acc1=20160, acc2=20161, z1=1, z2=-2)
        """State 35"""
        return 0
    elif GetTalkListEntryResult() == 18:
        """State 36"""
        # accessory:20170:Red Tearstone Ring
        # accessory:20171:
        assert t400504_x50(acc1=20170, acc2=20171, z1=1, z2=-2)
        """State 37"""
        return 0
    elif GetTalkListEntryResult() == 19:
        """State 38"""
        # accessory:20180:Blue Tearstone Ring
        # accessory:20181:
        assert t400504_x50(acc1=20180, acc2=20181, z1=1, z2=-2)
        """State 39"""
        return 0
    elif GetTalkListEntryResult() == 20:
        """State 40"""
        # accessory:20190:Wolf Ring
        # accessory:20191:Wolf Ring+1
        assert t400504_x50(acc1=20190, acc2=20191, z1=1, z2=-2)
        """State 41"""
        return 0
    elif GetTalkListEntryResult() == 21:
        """State 42"""
        # accessory:20270:Lingering Dragoncrest Ring
        # accessory:20271:Lingering Dragoncrest Ring+1
        assert t400504_x50(acc1=20270, acc2=20271, z1=1, z2=-2)
        """State 43"""
        return 0
    elif GetTalkListEntryResult() == 22:
        """State 44"""
        # accessory:20280:Sage Ring
        # accessory:20281:Sage Ring+1
        assert t400504_x50(acc1=20280, acc2=20281, z1=1, z2=-2)
        """State 45"""
        return 0
    elif GetTalkListEntryResult() == 23:
        """State 46"""
        # accessory:20300:Dusk Crown Ring
        # accessory:20301:
        assert t400504_x50(acc1=20300, acc2=20301, z1=1, z2=-2)
        """State 47"""
        return 0
    elif GetTalkListEntryResult() == 24:
        """State 48"""
        # accessory:20330:Darkmoon Ring
        # accessory:20331:
        assert t400504_x50(acc1=20330, acc2=20331, z1=1, z2=-2)
        """State 49"""
        return 0
    elif GetTalkListEntryResult() == 25:
        """State 50"""
        # accessory:20340:Ring of the Sun's Firstborn
        # accessory:20341:
        assert t400504_x50(acc1=20340, acc2=20341, z1=1, z2=-2)
        """State 51"""
        return 0
    elif GetTalkListEntryResult() == 26:
        """State 52"""
        # accessory:20350:Darkmoon Blade Covenant Ring
        # accessory:20351:
        assert t400504_x50(acc1=20350, acc2=20351, z1=1, z2=-2)
        """State 53"""
        return 0
    elif GetTalkListEntryResult() == 27:
        """State 54"""
        # accessory:20360:Leo Ring
        # accessory:20361:
        assert t400504_x50(acc1=20360, acc2=20361, z1=1, z2=-2)
        """State 55"""
        return 0
    elif GetTalkListEntryResult() == 28:
        """State 56"""
        # accessory:20370:Hawk Ring
        # accessory:20371:
        assert t400504_x50(acc1=20370, acc2=20371, z1=1, z2=-2)
        """State 57"""
        return 0
    elif GetTalkListEntryResult() == 29:
        """State 58"""
        # accessory:20390:Covetous Gold Serpent Ring
        # accessory:20391:Covetous Gold Serpent Ring+1
        assert t400504_x50(acc1=20390, acc2=20391, z1=1, z2=-2)
        """State 59"""
        return 0
    elif GetTalkListEntryResult() == 30:
        """State 60"""
        # accessory:20400:Covetous Silver Serpent Ring
        # accessory:20401:Covetous Silver Serpent Ring+1
        assert t400504_x50(acc1=20400, acc2=20401, z1=1, z2=-2)
        """State 61"""
        return 0
    elif GetTalkListEntryResult() == 31:
        """State 62"""
        # accessory:20410:Sun Princess Ring
        # accessory:20411:
        assert t400504_x50(acc1=20410, acc2=20411, z1=1, z2=-2)
        """State 63"""
        return 0
    elif GetTalkListEntryResult() == 32:
        """State 64"""
        # accessory:20430:Skull Ring
        # accessory:20431:
        assert t400504_x50(acc1=20430, acc2=20431, z1=1, z2=-2)
        """State 65"""
        return 0
    elif GetTalkListEntryResult() == 33:
        """State 66"""
        # accessory:20460:Knight's Ring
        # accessory:20461:
        assert t400504_x50(acc1=20460, acc2=20461, z1=1, z2=-2)
        """State 67"""
        return 0
    elif GetTalkListEntryResult() == 34:
        """State 68"""
        # accessory:20470:Hunter's Ring
        # accessory:20471:
        assert t400504_x50(acc1=20470, acc2=20471, z1=1, z2=-2)
        """State 69"""
        return 0
    elif GetTalkListEntryResult() == 35:
        """State 70"""
        # accessory:20480:Knight Slayer's Ring
        # accessory:20481:
        assert t400504_x50(acc1=20480, acc2=20481, z1=1, z2=-2)
        """State 71"""
        return 0
    elif GetTalkListEntryResult() == 36:
        """State 72"""
        # accessory:20490:Magic Clutch Ring
        # accessory:20491:
        assert t400504_x50(acc1=20490, acc2=20491, z1=1, z2=-2)
        """State 73"""
        return 0
    elif GetTalkListEntryResult() == 37:
        """State 74"""
        # accessory:20500:Lightning Clutch Ring
        # accessory:20501:
        assert t400504_x50(acc1=20500, acc2=20501, z1=1, z2=-2)
        """State 75"""
        return 0
    elif GetTalkListEntryResult() == 38:
        """State 76"""
        # accessory:20510:Fire Clutch Ring
        # accessory:20511:
        assert t400504_x50(acc1=20510, acc2=20511, z1=1, z2=-2)
        """State 77"""
        return 0
    elif GetTalkListEntryResult() == 39:
        """State 78"""
        # accessory:20520:Dark Clutch Ring
        # accessory:20521:
        assert t400504_x50(acc1=20520, acc2=20521, z1=1, z2=-2)
        """State 79"""
        return 0
    elif GetTalkListEntryResult() == 40:
        """State 80"""
        # accessory:20540:Flynn's Ring
        # accessory:20541:
        assert t400504_x50(acc1=20540, acc2=20541, z1=1, z2=-2)
        """State 81"""
        return 0
    elif GetTalkListEntryResult() == 41:
        """State 82"""
        # accessory:20550:Prisoner's Chain
        # accessory:20551:
        assert t400504_x50(acc1=20550, acc2=20551, z1=1, z2=-2)
        """State 83"""
        return 0
    elif GetTalkListEntryResult() == 42:
        """State 84"""
        # accessory:20590:Ring of the Evil Eye
        # accessory:20591:Ring of the Evil Eye+1
        assert t400504_x50(acc1=20590, acc2=20591, z1=1, z2=-2)
        """State 85"""
        return 0
    elif GetTalkListEntryResult() == 43:
        """State 86"""
        # accessory:20600:Calamity Ring
        # accessory:20601:
        assert t400504_x50(acc1=20600, acc2=20601, z1=1, z2=-2)
        """State 87"""
        return 0
    elif GetTalkListEntryResult() == 44:
        """State 88"""
        # accessory:20610:Farron Ring
        # accessory:20611:
        assert t400504_x50(acc1=20610, acc2=20611, z1=1, z2=-2)
        """State 89"""
        return 0
    elif GetTalkListEntryResult() == 45:
        """State 90"""
        # accessory:20660:Lloyd's Sword Ring
        # accessory:20661:
        assert t400504_x50(acc1=20660, acc2=20661, z1=1, z2=-2)
        """State 91"""
        return 0
    elif GetTalkListEntryResult() == 46:
        """State 92"""
        # accessory:20670:Lloyd's Shield Ring
        # accessory:20671:
        assert t400504_x50(acc1=20670, acc2=20671, z1=1, z2=-2)
        """State 93"""
        return 0
    elif GetTalkListEntryResult() == 47:
        """State 94"""
        # accessory:20700:Estus Ring
        # accessory:20701:
        assert t400504_x50(acc1=20700, acc2=20701, z1=1, z2=-2)
        """State 95"""
        return 0
    elif GetTalkListEntryResult() == 48:
        """State 96"""
        # accessory:20710:Ashen Estus Ring
        # accessory:20711:
        assert t400504_x50(acc1=20710, acc2=20711, z1=1, z2=-2)
        """State 97"""
        return 0
    elif GetTalkListEntryResult() == 49:
        """State 98"""
        # accessory:20720:Horsehoof Ring
        # accessory:20721:
        assert t400504_x50(acc1=20720, acc2=20721, z1=1, z2=-2)
        """State 99"""
        return 0
    elif GetTalkListEntryResult() == 50:
        """State 100"""
        # accessory:20750:Pontiff's Right Eye
        # accessory:20751:
        assert t400504_x50(acc1=20750, acc2=20751, z1=1, z2=-2)
        """State 101"""
        return 0
    elif GetTalkListEntryResult() == 51:
        """State 102"""
        # accessory:20790:Pontiff's Left Eye
        # accessory:20791:
        assert t400504_x50(acc1=20790, acc2=20791, z1=1, z2=-2)
        """State 103"""
        return 0
    elif GetTalkListEntryResult() == 52:
        """State 104"""
        # accessory:20830:Dragonscale Ring
        assert t400504_x50(acc1=20830, acc2=20831, z1=1, z2=-2)
        """State 105"""
        return 0
    elif GetTalkListEntryResult() == 53:
        """State 106"""
        assert t400504_x50(acc1=21000, acc2=21001, z1=1, z2=-2)
        """State 107"""
        return 0
    elif GetTalkListEntryResult() == 54:
        """State 108"""
        assert t400504_x50(acc1=30010, acc2=30011, z1=1, z2=-2)
        """State 109"""
        return 0
    elif GetTalkListEntryResult() == 55:
        """State 110"""
        assert t400504_x50(acc1=30020, acc2=30021, z1=1, z2=-2)
        """State 111"""
        return 0
    elif GetTalkListEntryResult() == 56:
        """State 112"""
        assert t400504_x50(acc1=30050, acc2=30051, z1=1, z2=-2)
        """State 113"""
        return 0
    elif GetTalkListEntryResult() == 57:
        """State 114"""
        assert t400504_x50(acc1=30080, acc2=30081, z1=1, z2=-2)
        """State 115"""
        return 0
    elif GetTalkListEntryResult() == 58:
        """State 116"""
        assert t400504_x50(acc1=30170, acc2=30171, z1=1, z2=-2)
        """State 117"""
        return 0
    elif GetTalkListEntryResult() == 59:
        """State 118"""
        assert t400504_x50(acc1=30180, acc2=30181, z1=1, z2=-2)
        """State 119"""
        return 0
    elif GetTalkListEntryResult() == 60:
        """State 120"""
        assert t400504_x50(acc1=30190, acc2=30191, z1=1, z2=-2)
        """State 121"""
        return 0
    elif GetTalkListEntryResult() == 61:
        """State 122"""
        assert t400504_x50(acc1=30200, acc2=30201, z1=1, z2=-2)
        """State 123"""
        return 0
    elif GetTalkListEntryResult() == 62:
        """State 124"""
        assert t400504_x50(acc1=30210, acc2=30211, z1=1, z2=-2)
        """State 125"""
        return 0
    elif GetTalkListEntryResult() == 63:
        """State 126"""
        assert t400504_x50(acc1=30330, acc2=30331, z1=1, z2=-2)
        """State 127"""
        return 0
    elif GetTalkListEntryResult() == 64:
        """State 128"""
        assert t400504_x50(acc1=30340, acc2=30341, z1=1, z2=-2)
        """State 129"""
        return 0
    elif GetTalkListEntryResult() == 65:
        """State 130"""
        assert t400504_x50(acc1=30350, acc2=30351, z1=1, z2=-2)
        """State 131"""
        return 0
    elif GetTalkListEntryResult() == 66:
        """State 132"""
        assert t400504_x50(acc1=30360, acc2=30361, z1=1, z2=-2)
        """State 133"""
        return 0
    elif GetTalkListEntryResult() == 67:
        """State 134"""
        assert t400504_x50(acc1=30370, acc2=30371, z1=1, z2=-2)
        """State 135"""
        return 0
    elif GetTalkListEntryResult() == 68:
        """State 136"""
        assert t400504_x50(acc1=30390, acc2=30391, z1=1, z2=-2)
        """State 137"""
        return 0
    elif GetTalkListEntryResult() == 69:
        """State 138"""
        assert t400504_x50(acc1=30400, acc2=30401, z1=1, z2=-2)
        """State 139"""
        return 0
    elif GetTalkListEntryResult() == 70:
        """State 140"""
        assert t400504_x50(acc1=30410, acc2=30411, z1=1, z2=-2)
        """State 141"""
        return 0
    elif GetTalkListEntryResult() == 71:
        """State 142"""
        assert t400504_x50(acc1=30420, acc2=30421, z1=1, z2=-2)
        """State 143"""
        return 0
    elif GetTalkListEntryResult() == 72:
        """State 144"""
        assert t400504_x50(acc1=30430, acc2=30431, z1=1, z2=-2)
        """State 145"""
        return 0
    elif GetTalkListEntryResult() == 73:
        """State 146"""
        assert t400504_x50(acc1=30450, acc2=30451, z1=1, z2=-2)
        """State 147"""
        return 0
    elif GetTalkListEntryResult() == 74:
        """State 148"""
        assert t400504_x50(acc1=30500, acc2=30501, z1=1, z2=-2)
        """State 149"""
        return 0
    elif GetTalkListEntryResult() == 75:
        """State 150"""
        assert t400504_x50(acc1=30650, acc2=30651, z1=1, z2=-2)
        """State 151"""
        return 0
    elif GetTalkListEntryResult() == 76:
        """State 152"""
        assert t400504_x50(acc1=30660, acc2=30661, z1=1, z2=-2)
        """State 153"""
        return 0
    elif GetTalkListEntryResult() == 77:
        """State 154"""
        assert t400504_x50(acc1=30670, acc2=30671, z1=1, z2=-2)
        """State 155"""
        return 0
    elif GetTalkListEntryResult() == 78:
        """State 156"""
        assert t400504_x50(acc1=30680, acc2=30681, z1=1, z2=-2)
        """State 157"""
        return 0
    elif GetTalkListEntryResult() == 79:
        """State 158"""
        assert t400504_x50(acc1=30690, acc2=30691, z1=1, z2=-2)
        """State 159"""
        return 0
    elif GetTalkListEntryResult() == 80:
        """State 160"""
        assert t400504_x50(acc1=30700, acc2=30701, z1=1, z2=-2)
        """State 161"""
        return 0
    elif GetTalkListEntryResult() == 81:
        """State 162"""
        assert t400504_x50(acc1=30800, acc2=30801, z1=1, z2=-2)
        """State 163"""
        return 0
    elif GetTalkListEntryResult() == 82:
        """State 164"""
        assert t400504_x50(acc1=30890, acc2=30891, z1=1, z2=-2)
        """State 165"""
        return 0
    elif GetTalkListEntryResult() == 85:
        """State 166"""
        assert t400504_x50(acc1=30930, acc2=30931, z1=1, z2=-2)
        """State 167"""
        return 0
    elif GetTalkListEntryResult() == 86:
        """State 168"""
        assert t400504_x50(acc1=30940, acc2=30941, z1=1, z2=-2)
        """State 169"""
        return 0
    elif GetTalkListEntryResult() == 87:
        """State 170"""
        assert t400504_x50(acc1=30950, acc2=30951, z1=1, z2=-2)
        """State 171"""
        return 0
    elif GetTalkListEntryResult() == 90:
        """State 172"""
        assert t400504_x50(acc1=30870, acc2=30871, z1=1, z2=-2)
        """State 173"""
        return 0
    elif GetTalkListEntryResult() == 91:
        """State 174"""
        assert t400504_x50(acc1=30880, acc2=30881, z1=1, z2=-2)
        """State 175"""
        return 0
    elif GetTalkListEntryResult() == 92:
        """State 176"""
        assert t400504_x50(acc1=30900, acc2=30901, z1=1, z2=-2)
        """State 177"""
        return 0
    elif GetTalkListEntryResult() == 93:
        """State 178"""
        assert t400504_x50(acc1=31400, acc2=31401, z1=1, z2=-2)
        """State 179"""
        return 0
    elif GetTalkListEntryResult() == 94:
        """State 180"""
        assert t400504_x50(acc1=31300, acc2=31301, z1=1, z2=-2)
        """State 181"""
        return 0
    elif GetTalkListEntryResult() == 95:
        """State 182"""
        assert t400504_x50(acc1=31080, acc2=31081, z1=1, z2=-2)
        """State 183"""
        return 0
    elif GetTalkListEntryResult() == 96:
        """State 184"""
        # accessory:20380:Hornet Ring
        # accessory:20381:
        assert t400504_x50(acc1=20380, acc2=20381, z1=1, z2=-2)
        """State 185"""
        return 0
    elif GetTalkListEntryResult() == 97:
        """State 186"""
        assert t400504_x50(acc1=31200, acc2=31201, z1=1, z2=-2)
        """State 187"""
        return 0
    elif GetTalkListEntryResult() == 98:
        """State 188"""
        assert t400504_x50(acc1=30800, acc2=30801, z1=1, z2=-2)
        """State 189"""
        return 0
    elif GetTalkListEntryResult() == 99:
        """State 190"""
        # accessory:20450:Carthus Milkring
        # accessory:20451:
        assert t400504_x50(acc1=20450, acc2=20451, z1=1, z2=-2)
        """State 191"""
        return 0
    elif GetTalkListEntryResult() == 100:
        """State 192"""
        assert t400504_x50(acc1=30090, acc2=30091, z1=1, z2=-2)
        """State 193"""
        return 0
    elif GetTalkListEntryResult() == 101:
        """State 194"""
        assert t400504_x50(acc1=30840, acc2=30841, z1=1, z2=-2)
        """State 195"""
        return 0
    elif GetTalkListEntryResult() == 102:
        """State 196"""
        assert t400504_x50(acc1=30990, acc2=30991, z1=1, z2=-2)
        """State 197"""
        return 0
    elif GetTalkListEntryResult() == 103:
        """State 198"""
        assert t400504_x50(acc1=30040, acc2=30041, z1=1, z2=-2)
        """State 199"""
        return 0
    elif GetTalkListEntryResult() == 104:
        """State 200"""
        assert t400504_x50(acc1=31500, acc2=31501, z1=1, z2=-2)
        """State 201"""
        return 0
    elif GetTalkListEntryResult() == 105:
        """State 202"""
        assert t400504_x50(acc1=31600, acc2=31601, z1=1, z2=-2)
        """State 203"""
        return 0
    elif GetTalkListEntryResult() == 106:
        """State 204"""
        assert t400504_x50(acc1=31700, acc2=31701, z1=1, z2=-2)
        """State 205"""
        return 0
    elif GetTalkListEntryResult() == 107:
        """State 206"""
        assert t400504_x50(acc1=31800, acc2=31801, z1=1, z2=-2)
        """State 207"""
        return 0
    elif GetTalkListEntryResult() == 108:
        """State 208"""
        assert t400504_x50(acc1=31900, acc2=31901, z1=1, z2=-2)
        """State 209"""
        return 0
    elif GetTalkListEntryResult() == 109:
        """State 210"""
        assert t400504_x50(acc1=32000, acc2=32001, z1=1, z2=-2)
        """State 211"""
        return 0
    elif GetTalkListEntryResult() == 110:
        """State 212"""
        assert t400504_x50(acc1=32100, acc2=32101, z1=1, z2=-2)
        """State 213"""
        return 0
    elif GetTalkListEntryResult() == 111:
        """State 214"""
        assert t400504_x50(acc1=32200, acc2=32201, z1=1, z2=-2)
        """State 215"""
        return 0
    elif GetTalkListEntryResult() == 112:
        """State 216"""
        assert t400504_x50(acc1=32300, acc2=32301, z1=1, z2=-2)
        """State 217"""
        return 0
    elif not (CheckSpecificPersonMenuIsOpen(-1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0)):
        """State 218"""
        return 0

def t400504_x42():
    """State 0"""
    MainBonfireMenuFlag()
    ClearTalkListData()
    # accessory:20001:Life Ring+1
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20001, CompareType.GreaterOrEqual, 1, False),
                      1, 99015100, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20831, CompareType.GreaterOrEqual, 1, False),
                      52, 99015151, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30051, CompareType.GreaterOrEqual, 1, False),
                      56, 99015155, -1)
    # accessory:20011:Chloranthy Ring+1
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20011, CompareType.GreaterOrEqual, 1, False),
                      2, 99015101, -1)
    # accessory:20021:Havel's Ring+1
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20021, CompareType.GreaterOrEqual, 1, False),
                      3, 99015102, -1)
    # accessory:20031:Ring of Favor+1
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20031, CompareType.GreaterOrEqual, 1, False),
                      4, 99015103, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30211, CompareType.GreaterOrEqual, 1, False),
                      62, 99015161, -1)
    # accessory:20431:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20431, CompareType.GreaterOrEqual, 1, False),
                      32, 99015131, -1)
    # accessory:20491:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20491, CompareType.GreaterOrEqual, 1, False),
                      36, 99015135, -1)
    # accessory:20501:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20501, CompareType.GreaterOrEqual, 1, False),
                      37, 99015136, -1)
    # accessory:20511:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20511, CompareType.GreaterOrEqual, 1, False),
                      38, 99015137, -1)
    # accessory:20521:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20521, CompareType.GreaterOrEqual, 1, False),
                      39, 99015138, -1)
    # accessory:20341:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20341, CompareType.GreaterOrEqual, 1, False),
                      25, 99015124, -1)
    # accessory:20351:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20351, CompareType.GreaterOrEqual, 1, False),
                      26, 99015125, -1)
    # accessory:20361:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20361, CompareType.GreaterOrEqual, 1, False),
                      27, 99015126, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30021, CompareType.GreaterOrEqual, 1, False),
                      55, 99015154, -1)
    # accessory:20041:Ring of Steel Protection+1
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20041, CompareType.GreaterOrEqual, 1, False),
                      5, 99015104, -1)
    # accessory:20051:Flame Stoneplate Ring+1
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20051, CompareType.GreaterOrEqual, 1, False),
                      6, 99015105, -1)
    # accessory:20061:Thunder Stoneplate Ring+1
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20061, CompareType.GreaterOrEqual, 1, False),
                      7, 99015106, -1)
    # accessory:20071:Magic Stoneplate Ring+1
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20071, CompareType.GreaterOrEqual, 1, False),
                      8, 99015107, -1)
    # accessory:20081:Dark Stoneplate Ring+1
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20081, CompareType.GreaterOrEqual, 1, False),
                      9, 99015108, -1)
    # accessory:20091:Speckled Stoneplate Ring+1
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20091, CompareType.GreaterOrEqual, 1, False),
                      10, 99015109, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30661, CompareType.GreaterOrEqual, 1, False),
                      76, 99015175, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30671, CompareType.GreaterOrEqual, 1, False),
                      77, 99015176, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30681, CompareType.GreaterOrEqual, 1, False),
                      78, 99015177, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30691, CompareType.GreaterOrEqual, 1, False),
                      79, 99015178, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30701, CompareType.GreaterOrEqual, 1, False),
                      80, 99015179, -1)
    # accessory:20101:Bloodbite Ring+1
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20101, CompareType.GreaterOrEqual, 1, False),
                      11, 99015110, -1)
    # accessory:20111:Poisonbite Ring+1
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20111, CompareType.GreaterOrEqual, 1, False),
                      12, 99015111, -1)
    # accessory:20121:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20121, CompareType.GreaterOrEqual, 1, False),
                      13, 99015112, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 21001, CompareType.GreaterOrEqual, 1, False),
                      53, 99015152, -1)
    # accessory:20131:Fleshbite Ring+1
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20131, CompareType.GreaterOrEqual, 1, False),
                      14, 99015113, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30931, CompareType.GreaterOrEqual, 1, False),
                      85, 99015184, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30891, CompareType.GreaterOrEqual, 1, False),
                      82, 99015181, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30941, CompareType.GreaterOrEqual, 1, False),
                      86, 99015185, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30951, CompareType.GreaterOrEqual, 1, False),
                      87, 99015186, -1)
    # accessory:20461:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20461, CompareType.GreaterOrEqual, 1, False),
                      33, 99015132, -1)
    # accessory:20471:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20471, CompareType.GreaterOrEqual, 1, False),
                      34, 99015133, -1)
    # accessory:20151:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20151, CompareType.GreaterOrEqual, 1, False),
                      16, 99015115, -1)
    # accessory:20161:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20161, CompareType.GreaterOrEqual, 1, False),
                      17, 99015116, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30391, CompareType.GreaterOrEqual, 1, False),
                      68, 99015167, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30401, CompareType.GreaterOrEqual, 1, False),
                      69, 99015168, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30411, CompareType.GreaterOrEqual, 1, False),
                      70, 99015169, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30421, CompareType.GreaterOrEqual, 1, False),
                      71, 99015170, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30431, CompareType.GreaterOrEqual, 1, False),
                      72, 99015171, -1)
    # accessory:20141:Wood Grain Ring+1
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20141, CompareType.GreaterOrEqual, 1, False),
                      15, 99015114, -1)
    # accessory:20171:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20171, CompareType.GreaterOrEqual, 1, False),
                      18, 99015117, -1)
    # accessory:20181:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20181, CompareType.GreaterOrEqual, 1, False),
                      19, 99015118, -1)
    # accessory:20191:Wolf Ring+1
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20191, CompareType.GreaterOrEqual, 1, False),
                      20, 99015119, -1)
    # accessory:20271:Lingering Dragoncrest Ring+1
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20271, CompareType.GreaterOrEqual, 1, False),
                      21, 99015120, -1)
    # accessory:20281:Sage Ring+1
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20281, CompareType.GreaterOrEqual, 1, False),
                      22, 99015121, -1)
    # accessory:20301:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20301, CompareType.GreaterOrEqual, 1, False),
                      23, 99015122, -1)
    # accessory:20331:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20331, CompareType.GreaterOrEqual, 1, False),
                      24, 99015123, -1)
    # accessory:20371:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20371, CompareType.GreaterOrEqual, 1, False),
                      28, 99015127, -1)
    # accessory:20391:Covetous Gold Serpent Ring+1
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20391, CompareType.GreaterOrEqual, 1, False),
                      29, 99015128, -1)
    # accessory:20401:Covetous Silver Serpent Ring+1
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20401, CompareType.GreaterOrEqual, 1, False),
                      30, 99015129, -1)
    # accessory:20411:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20411, CompareType.GreaterOrEqual, 1, False),
                      31, 99015130, -1)
    # accessory:20481:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20481, CompareType.GreaterOrEqual, 1, False),
                      35, 99015134, -1)
    # accessory:20541:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20541, CompareType.GreaterOrEqual, 1, False),
                      40, 99015139, -1)
    # accessory:20551:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20551, CompareType.GreaterOrEqual, 1, False),
                      41, 99015140, -1)
    # accessory:20591:Ring of the Evil Eye+1
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20591, CompareType.GreaterOrEqual, 1, False),
                      42, 99015141, -1)
    # accessory:20601:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20601, CompareType.GreaterOrEqual, 1, False),
                      43, 99015142, -1)
    # accessory:20611:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20611, CompareType.GreaterOrEqual, 1, False),
                      44, 99015143, -1)
    # accessory:20661:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20661, CompareType.GreaterOrEqual, 1, False),
                      45, 99015144, -1)
    # accessory:20671:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20671, CompareType.GreaterOrEqual, 1, False),
                      46, 99015145, -1)
    # accessory:20701:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20701, CompareType.GreaterOrEqual, 1, False),
                      47, 99015146, -1)
    # accessory:20711:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20711, CompareType.GreaterOrEqual, 1, False),
                      48, 99015147, -1)
    # accessory:20721:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20721, CompareType.GreaterOrEqual, 1, False),
                      49, 99015148, -1)
    # accessory:20751:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20751, CompareType.GreaterOrEqual, 1, False),
                      50, 99015149, -1)
    # accessory:20791:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20791, CompareType.GreaterOrEqual, 1, False),
                      51, 99015150, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30011, CompareType.GreaterOrEqual, 1, False),
                      54, 99015153, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30081, CompareType.GreaterOrEqual, 1, False),
                      57, 99015156, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30451, CompareType.GreaterOrEqual, 1, False),
                      73, 99015172, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30501, CompareType.GreaterOrEqual, 1, False),
                      74, 99015173, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30651, CompareType.GreaterOrEqual, 1, False),
                      75, 99015174, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30171, CompareType.GreaterOrEqual, 1, False),
                      58, 99015157, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30181, CompareType.GreaterOrEqual, 1, False),
                      59, 99015158, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30191, CompareType.GreaterOrEqual, 1, False),
                      60, 99015159, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30201, CompareType.GreaterOrEqual, 1, False),
                      61, 99015160, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30331, CompareType.GreaterOrEqual, 1, False),
                      63, 99015162, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30341, CompareType.GreaterOrEqual, 1, False),
                      64, 99015163, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30351, CompareType.GreaterOrEqual, 1, False),
                      65, 99015164, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30361, CompareType.GreaterOrEqual, 1, False),
                      66, 99015165, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30371, CompareType.GreaterOrEqual, 1, False),
                      67, 99015166, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30871, CompareType.GreaterOrEqual, 1, False),
                      90, 99015189, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30881, CompareType.GreaterOrEqual, 1, False),
                      91, 99015190, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30901, CompareType.GreaterOrEqual, 1, False),
                      92, 99015191, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31401, CompareType.GreaterOrEqual, 1, False),
                      93, 99015192, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31301, CompareType.GreaterOrEqual, 1, False),
                      94, 99015193, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31081, CompareType.GreaterOrEqual, 1, False),
                      95, 99015194, -1)
    # accessory:20381:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20381, CompareType.GreaterOrEqual, 1, False),
                      96, 99015195, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31201, CompareType.GreaterOrEqual, 1, False),
                      97, 99015196, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30801, CompareType.GreaterOrEqual, 1, False),
                      98, 99015197, -1)
    # accessory:20451:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20451, CompareType.GreaterOrEqual, 1, False),
                      99, 99015198, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30091, CompareType.GreaterOrEqual, 1, False),
                      100, 99015199, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30841, CompareType.GreaterOrEqual, 1, False),
                      101, 99015200, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30991, CompareType.GreaterOrEqual, 1, False),
                      102, 99015201, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30041, CompareType.GreaterOrEqual, 1, False),
                      103, 99015202, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31501, CompareType.GreaterOrEqual, 1, False),
                      104, 99015203, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31601, CompareType.GreaterOrEqual, 1, False),
                      105, 99015204, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31701, CompareType.GreaterOrEqual, 1, False),
                      106, 99015205, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31801, CompareType.GreaterOrEqual, 1, False),
                      107, 99015206, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31901, CompareType.GreaterOrEqual, 1, False),
                      108, 99015207, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 32001, CompareType.GreaterOrEqual, 1, False),
                      109, 99015208, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 32101, CompareType.GreaterOrEqual, 1, False),
                      110, 99015209, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 32201, CompareType.GreaterOrEqual, 1, False),
                      111, 99015210, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 32301, CompareType.GreaterOrEqual, 1, False),
                      112, 99015211, -1)
    # action:15000180:"Quit"
    AddTalkListData(999, 15000180, -1)
    assert (not CheckSpecificPersonGenericDialogIsOpen(2) and not (CheckSpecificPersonMenuIsOpen(-1, 2) and not
            CheckSpecificPersonGenericDialogIsOpen(2)))
    """State 1"""
    ShowShopMessage(TalkOptionsType.Regular)
    if GetTalkListEntryResult() == 1:
        """State 2"""
        # accessory:20001:Life Ring+1
        # accessory:20002:Life Ring+2
        assert t400504_x50(acc1=20001, acc2=20002, z1=3, z2=-4)
        """State 3"""
        return 0
    elif GetTalkListEntryResult() == 2:
        """State 4"""
        # accessory:20011:Chloranthy Ring+1
        # accessory:20012:Chloranthy Ring+2
        assert t400504_x50(acc1=20011, acc2=20012, z1=3, z2=-4)
        """State 5"""
        return 0
    elif GetTalkListEntryResult() == 3:
        """State 6"""
        # accessory:20021:Havel's Ring+1
        # accessory:20022:Havel's Ring+2
        assert t400504_x50(acc1=20021, acc2=20022, z1=3, z2=-4)
        """State 7"""
        return 0
    elif GetTalkListEntryResult() == 4:
        """State 8"""
        # accessory:20031:Ring of Favor+1
        # accessory:20032:Ring of Favor+2
        assert t400504_x50(acc1=20031, acc2=20032, z1=3, z2=-4)
        """State 9"""
        return 0
    elif GetTalkListEntryResult() == 5:
        """State 10"""
        # accessory:20041:Ring of Steel Protection+1
        # accessory:20042:Ring of Steel Protection+2
        assert t400504_x50(acc1=20041, acc2=20042, z1=3, z2=-4)
        """State 11"""
        return 0
    elif GetTalkListEntryResult() == 6:
        """State 12"""
        # accessory:20051:Flame Stoneplate Ring+1
        # accessory:20052:Flame Stoneplate Ring+2
        assert t400504_x50(acc1=20051, acc2=20052, z1=3, z2=-4)
        """State 13"""
        return 0
    elif GetTalkListEntryResult() == 7:
        """State 14"""
        # accessory:20061:Thunder Stoneplate Ring+1
        # accessory:20062:Thunder Stoneplate Ring+2
        assert t400504_x50(acc1=20061, acc2=20062, z1=3, z2=-4)
        """State 15"""
        return 0
    elif GetTalkListEntryResult() == 8:
        """State 16"""
        # accessory:20071:Magic Stoneplate Ring+1
        # accessory:20072:Magic Stoneplate Ring+2
        assert t400504_x50(acc1=20071, acc2=20072, z1=3, z2=-4)
        """State 17"""
        return 0
    elif GetTalkListEntryResult() == 9:
        """State 18"""
        # accessory:20081:Dark Stoneplate Ring+1
        # accessory:20082:Dark Stoneplate Ring+2
        assert t400504_x50(acc1=20081, acc2=20082, z1=3, z2=-4)
        """State 19"""
        return 0
    elif GetTalkListEntryResult() == 10:
        """State 20"""
        # accessory:20091:Speckled Stoneplate Ring+1
        # accessory:20092:
        assert t400504_x50(acc1=20091, acc2=20092, z1=3, z2=-4)
        """State 21"""
        return 0
    elif GetTalkListEntryResult() == 11:
        """State 22"""
        # accessory:20101:Bloodbite Ring+1
        # accessory:20102:
        assert t400504_x50(acc1=20101, acc2=20102, z1=3, z2=-4)
        """State 23"""
        return 0
    elif GetTalkListEntryResult() == 12:
        """State 24"""
        # accessory:20111:Poisonbite Ring+1
        # accessory:20112:
        assert t400504_x50(acc1=20111, acc2=20112, z1=3, z2=-4)
        """State 25"""
        return 0
    elif GetTalkListEntryResult() == 13:
        """State 26"""
        # accessory:20121:
        # accessory:20122:
        assert t400504_x50(acc1=20121, acc2=20122, z1=3, z2=-4)
        """State 27"""
        return 0
    elif GetTalkListEntryResult() == 14:
        """State 28"""
        # accessory:20131:Fleshbite Ring+1
        # accessory:20132:
        assert t400504_x50(acc1=20131, acc2=20132, z1=3, z2=-4)
        """State 29"""
        return 0
    elif GetTalkListEntryResult() == 15:
        """State 30"""
        # accessory:20141:Wood Grain Ring+1
        # accessory:20142:Wood Grain Ring+2
        assert t400504_x50(acc1=20141, acc2=20142, z1=3, z2=-4)
        """State 31"""
        return 0
    elif GetTalkListEntryResult() == 16:
        """State 32"""
        # accessory:20151:
        # accessory:20152:
        assert t400504_x50(acc1=20151, acc2=20152, z1=3, z2=-4)
        """State 33"""
        return 0
    elif GetTalkListEntryResult() == 17:
        """State 34"""
        # accessory:20161:
        # accessory:20162:
        assert t400504_x50(acc1=20161, acc2=20162, z1=3, z2=-4)
        """State 35"""
        return 0
    elif GetTalkListEntryResult() == 18:
        """State 36"""
        # accessory:20171:
        # accessory:20172:
        assert t400504_x50(acc1=20171, acc2=20172, z1=3, z2=-4)
        """State 37"""
        return 0
    elif GetTalkListEntryResult() == 19:
        """State 38"""
        # accessory:20181:
        # accessory:20182:
        assert t400504_x50(acc1=20181, acc2=20182, z1=3, z2=-4)
        """State 39"""
        return 0
    elif GetTalkListEntryResult() == 20:
        """State 40"""
        # accessory:20191:Wolf Ring+1
        # accessory:20192:Wolf Ring+2
        assert t400504_x50(acc1=20191, acc2=20192, z1=3, z2=-4)
        """State 41"""
        return 0
    elif GetTalkListEntryResult() == 21:
        """State 42"""
        # accessory:20271:Lingering Dragoncrest Ring+1
        # accessory:20272:Lingering Dragoncrest Ring+2
        assert t400504_x50(acc1=20271, acc2=20272, z1=3, z2=-4)
        """State 43"""
        return 0
    elif GetTalkListEntryResult() == 22:
        """State 44"""
        # accessory:20281:Sage Ring+1
        # accessory:20282:Sage Ring+2
        assert t400504_x50(acc1=20281, acc2=20282, z1=3, z2=-4)
        """State 45"""
        return 0
    elif GetTalkListEntryResult() == 23:
        """State 46"""
        # accessory:20301:
        # accessory:20302:
        assert t400504_x50(acc1=20301, acc2=20302, z1=3, z2=-4)
        """State 47"""
        return 0
    elif GetTalkListEntryResult() == 24:
        """State 48"""
        # accessory:20331:
        # accessory:20332:
        assert t400504_x50(acc1=20331, acc2=20332, z1=3, z2=-4)
        """State 49"""
        return 0
    elif GetTalkListEntryResult() == 25:
        """State 50"""
        # accessory:20341:
        # accessory:20342:
        assert t400504_x50(acc1=20341, acc2=20342, z1=3, z2=-4)
        """State 51"""
        return 0
    elif GetTalkListEntryResult() == 26:
        """State 52"""
        # accessory:20351:
        # accessory:20352:
        assert t400504_x50(acc1=20351, acc2=20352, z1=3, z2=-4)
        """State 53"""
        return 0
    elif GetTalkListEntryResult() == 27:
        """State 54"""
        # accessory:20361:
        # accessory:20362:
        assert t400504_x50(acc1=20361, acc2=20362, z1=3, z2=-4)
        """State 55"""
        return 0
    elif GetTalkListEntryResult() == 28:
        """State 56"""
        # accessory:20371:
        # accessory:20372:
        assert t400504_x50(acc1=20371, acc2=20372, z1=3, z2=-4)
        """State 57"""
        return 0
    elif GetTalkListEntryResult() == 29:
        """State 58"""
        # accessory:20391:Covetous Gold Serpent Ring+1
        # accessory:20392:Covetous Gold Serpent Ring+2
        assert t400504_x50(acc1=20391, acc2=20392, z1=3, z2=-4)
        """State 59"""
        return 0
    elif GetTalkListEntryResult() == 30:
        """State 60"""
        # accessory:20401:Covetous Silver Serpent Ring+1
        # accessory:20402:Covetous Silver Serpent Ring+2
        assert t400504_x50(acc1=20401, acc2=20402, z1=3, z2=-4)
        """State 61"""
        return 0
    elif GetTalkListEntryResult() == 31:
        """State 62"""
        # accessory:20411:
        # accessory:20412:
        assert t400504_x50(acc1=20411, acc2=20412, z1=3, z2=-4)
        """State 63"""
        return 0
    elif GetTalkListEntryResult() == 32:
        """State 64"""
        # accessory:20431:
        # accessory:20432:
        assert t400504_x50(acc1=20431, acc2=20432, z1=3, z2=-4)
        """State 65"""
        return 0
    elif GetTalkListEntryResult() == 33:
        """State 66"""
        # accessory:20461:
        # accessory:20462:
        assert t400504_x50(acc1=20461, acc2=20462, z1=3, z2=-4)
        """State 67"""
        return 0
    elif GetTalkListEntryResult() == 34:
        """State 68"""
        # accessory:20471:
        # accessory:20472:
        assert t400504_x50(acc1=20471, acc2=20472, z1=3, z2=-4)
        """State 69"""
        return 0
    elif GetTalkListEntryResult() == 35:
        """State 70"""
        # accessory:20481:
        # accessory:20482:
        assert t400504_x50(acc1=20481, acc2=20482, z1=3, z2=-4)
        """State 71"""
        return 0
    elif GetTalkListEntryResult() == 36:
        """State 72"""
        # accessory:20491:
        # accessory:20492:
        assert t400504_x50(acc1=20491, acc2=20492, z1=3, z2=-4)
        """State 73"""
        return 0
    elif GetTalkListEntryResult() == 37:
        """State 74"""
        # accessory:20501:
        # accessory:20502:
        assert t400504_x50(acc1=20501, acc2=20502, z1=3, z2=-4)
        """State 75"""
        return 0
    elif GetTalkListEntryResult() == 38:
        """State 76"""
        # accessory:20511:
        # accessory:20512:
        assert t400504_x50(acc1=20511, acc2=20512, z1=3, z2=-4)
        """State 77"""
        return 0
    elif GetTalkListEntryResult() == 39:
        """State 78"""
        # accessory:20521:
        # accessory:20522:
        assert t400504_x50(acc1=20521, acc2=20522, z1=3, z2=-4)
        """State 79"""
        return 0
    elif GetTalkListEntryResult() == 40:
        """State 80"""
        # accessory:20541:
        # accessory:20542:
        assert t400504_x50(acc1=20541, acc2=20542, z1=3, z2=-4)
        """State 81"""
        return 0
    elif GetTalkListEntryResult() == 41:
        """State 82"""
        # accessory:20551:
        # accessory:20552:
        assert t400504_x50(acc1=20551, acc2=20552, z1=3, z2=-4)
        """State 83"""
        return 0
    elif GetTalkListEntryResult() == 42:
        """State 84"""
        # accessory:20591:Ring of the Evil Eye+1
        # accessory:20592:Ring of the Evil Eye+2
        assert t400504_x50(acc1=20591, acc2=20592, z1=3, z2=-4)
        """State 85"""
        return 0
    elif GetTalkListEntryResult() == 43:
        """State 86"""
        # accessory:20601:
        # accessory:20602:
        assert t400504_x50(acc1=20601, acc2=20602, z1=3, z2=-4)
        """State 87"""
        return 0
    elif GetTalkListEntryResult() == 44:
        """State 88"""
        # accessory:20611:
        # accessory:20612:
        assert t400504_x50(acc1=20611, acc2=20612, z1=3, z2=-4)
        """State 89"""
        return 0
    elif GetTalkListEntryResult() == 45:
        """State 90"""
        # accessory:20661:
        # accessory:20662:
        assert t400504_x50(acc1=20661, acc2=20662, z1=3, z2=-4)
        """State 91"""
        return 0
    elif GetTalkListEntryResult() == 46:
        """State 92"""
        # accessory:20671:
        # accessory:20672:
        assert t400504_x50(acc1=20671, acc2=20672, z1=3, z2=-4)
        """State 93"""
        return 0
    elif GetTalkListEntryResult() == 47:
        """State 94"""
        # accessory:20701:
        # accessory:20702:
        assert t400504_x50(acc1=20701, acc2=20702, z1=3, z2=-4)
        """State 95"""
        return 0
    elif GetTalkListEntryResult() == 48:
        """State 96"""
        # accessory:20711:
        # accessory:20712:
        assert t400504_x50(acc1=20711, acc2=20712, z1=3, z2=-4)
        """State 97"""
        return 0
    elif GetTalkListEntryResult() == 49:
        """State 98"""
        # accessory:20721:
        # accessory:20722:
        assert t400504_x50(acc1=20721, acc2=20722, z1=3, z2=-4)
        """State 99"""
        return 0
    elif GetTalkListEntryResult() == 50:
        """State 100"""
        # accessory:20751:
        # accessory:20752:
        assert t400504_x50(acc1=20751, acc2=20752, z1=3, z2=-4)
        """State 101"""
        return 0
    elif GetTalkListEntryResult() == 51:
        """State 102"""
        # accessory:20791:
        # accessory:20792:
        assert t400504_x50(acc1=20791, acc2=20792, z1=3, z2=-4)
        """State 103"""
        return 0
    elif GetTalkListEntryResult() == 52:
        """State 104"""
        assert t400504_x50(acc1=20831, acc2=20832, z1=3, z2=-4)
        """State 105"""
        return 0
    elif GetTalkListEntryResult() == 53:
        """State 106"""
        assert t400504_x50(acc1=21001, acc2=21002, z1=3, z2=-4)
        """State 107"""
        return 0
    elif GetTalkListEntryResult() == 54:
        """State 108"""
        assert t400504_x50(acc1=30011, acc2=30012, z1=3, z2=-4)
        """State 109"""
        return 0
    elif GetTalkListEntryResult() == 55:
        """State 110"""
        assert t400504_x50(acc1=30021, acc2=30022, z1=3, z2=-4)
        """State 111"""
        return 0
    elif GetTalkListEntryResult() == 56:
        """State 112"""
        assert t400504_x50(acc1=30051, acc2=30052, z1=3, z2=-4)
        """State 113"""
        return 0
    elif GetTalkListEntryResult() == 57:
        """State 114"""
        assert t400504_x50(acc1=30081, acc2=30082, z1=3, z2=-4)
        """State 115"""
        return 0
    elif GetTalkListEntryResult() == 58:
        """State 116"""
        assert t400504_x50(acc1=30171, acc2=30172, z1=3, z2=-4)
        """State 117"""
        return 0
    elif GetTalkListEntryResult() == 59:
        """State 118"""
        assert t400504_x50(acc1=30181, acc2=30182, z1=3, z2=-4)
        """State 119"""
        return 0
    elif GetTalkListEntryResult() == 60:
        """State 120"""
        assert t400504_x50(acc1=30191, acc2=30192, z1=3, z2=-4)
        """State 121"""
        return 0
    elif GetTalkListEntryResult() == 61:
        """State 122"""
        assert t400504_x50(acc1=30201, acc2=30202, z1=3, z2=-4)
        """State 123"""
        return 0
    elif GetTalkListEntryResult() == 62:
        """State 124"""
        assert t400504_x50(acc1=30211, acc2=30212, z1=3, z2=-4)
        """State 125"""
        return 0
    elif GetTalkListEntryResult() == 63:
        """State 126"""
        assert t400504_x50(acc1=30331, acc2=30332, z1=3, z2=-4)
        """State 127"""
        return 0
    elif GetTalkListEntryResult() == 64:
        """State 128"""
        assert t400504_x50(acc1=30341, acc2=30342, z1=3, z2=-4)
        """State 129"""
        return 0
    elif GetTalkListEntryResult() == 65:
        """State 130"""
        assert t400504_x50(acc1=30351, acc2=30352, z1=3, z2=-4)
        """State 131"""
        return 0
    elif GetTalkListEntryResult() == 66:
        """State 132"""
        assert t400504_x50(acc1=30361, acc2=30362, z1=3, z2=-4)
        """State 133"""
        return 0
    elif GetTalkListEntryResult() == 67:
        """State 134"""
        assert t400504_x50(acc1=30371, acc2=30372, z1=3, z2=-4)
        """State 135"""
        return 0
    elif GetTalkListEntryResult() == 68:
        """State 136"""
        assert t400504_x50(acc1=30391, acc2=30392, z1=3, z2=-4)
        """State 137"""
        return 0
    elif GetTalkListEntryResult() == 69:
        """State 138"""
        assert t400504_x50(acc1=30401, acc2=30402, z1=3, z2=-4)
        """State 139"""
        return 0
    elif GetTalkListEntryResult() == 70:
        """State 140"""
        assert t400504_x50(acc1=30411, acc2=30412, z1=3, z2=-4)
        """State 141"""
        return 0
    elif GetTalkListEntryResult() == 71:
        """State 142"""
        assert t400504_x50(acc1=30421, acc2=30422, z1=3, z2=-4)
        """State 143"""
        return 0
    elif GetTalkListEntryResult() == 72:
        """State 144"""
        assert t400504_x50(acc1=30431, acc2=30432, z1=3, z2=-4)
        """State 145"""
        return 0
    elif GetTalkListEntryResult() == 73:
        """State 146"""
        assert t400504_x50(acc1=30451, acc2=30452, z1=3, z2=-4)
        """State 147"""
        return 0
    elif GetTalkListEntryResult() == 74:
        """State 148"""
        assert t400504_x50(acc1=30501, acc2=30502, z1=3, z2=-4)
        """State 149"""
        return 0
    elif GetTalkListEntryResult() == 75:
        """State 150"""
        assert t400504_x50(acc1=30651, acc2=30652, z1=3, z2=-4)
        """State 151"""
        return 0
    elif GetTalkListEntryResult() == 76:
        """State 152"""
        assert t400504_x50(acc1=30661, acc2=30662, z1=3, z2=-4)
        """State 153"""
        return 0
    elif GetTalkListEntryResult() == 77:
        """State 154"""
        assert t400504_x50(acc1=30671, acc2=30672, z1=3, z2=-4)
        """State 155"""
        return 0
    elif GetTalkListEntryResult() == 78:
        """State 156"""
        assert t400504_x50(acc1=30681, acc2=30682, z1=3, z2=-4)
        """State 157"""
        return 0
    elif GetTalkListEntryResult() == 79:
        """State 158"""
        assert t400504_x50(acc1=30691, acc2=30692, z1=3, z2=-4)
        """State 159"""
        return 0
    elif GetTalkListEntryResult() == 80:
        """State 160"""
        assert t400504_x50(acc1=30701, acc2=30702, z1=3, z2=-4)
        """State 161"""
        return 0
    elif GetTalkListEntryResult() == 81:
        """State 162"""
        assert t400504_x50(acc1=30801, acc2=30802, z1=3, z2=-4)
        """State 163"""
        return 0
    elif GetTalkListEntryResult() == 82:
        """State 164"""
        assert t400504_x50(acc1=30891, acc2=30892, z1=3, z2=-4)
        """State 165"""
        return 0
    elif GetTalkListEntryResult() == 85:
        """State 166"""
        assert t400504_x50(acc1=30931, acc2=30932, z1=3, z2=-4)
        """State 167"""
        return 0
    elif GetTalkListEntryResult() == 86:
        """State 168"""
        assert t400504_x50(acc1=30941, acc2=30942, z1=3, z2=-4)
        """State 169"""
        return 0
    elif GetTalkListEntryResult() == 87:
        """State 170"""
        assert t400504_x50(acc1=30951, acc2=30952, z1=3, z2=-4)
        """State 171"""
        return 0
    elif GetTalkListEntryResult() == 90:
        """State 172"""
        assert t400504_x50(acc1=30871, acc2=30872, z1=3, z2=-4)
        """State 173"""
        return 0
    elif GetTalkListEntryResult() == 91:
        """State 174"""
        assert t400504_x50(acc1=30881, acc2=30882, z1=3, z2=-4)
        """State 175"""
        return 0
    elif GetTalkListEntryResult() == 92:
        """State 176"""
        assert t400504_x50(acc1=30901, acc2=30902, z1=3, z2=-4)
        """State 177"""
        return 0
    elif GetTalkListEntryResult() == 93:
        """State 178"""
        assert t400504_x50(acc1=31401, acc2=31402, z1=3, z2=-4)
        """State 179"""
        return 0
    elif GetTalkListEntryResult() == 94:
        """State 180"""
        assert t400504_x50(acc1=31301, acc2=31302, z1=3, z2=-4)
        """State 181"""
        return 0
    elif GetTalkListEntryResult() == 95:
        """State 182"""
        assert t400504_x50(acc1=31081, acc2=31082, z1=3, z2=-4)
        """State 183"""
        return 0
    elif GetTalkListEntryResult() == 96:
        """State 184"""
        # accessory:20381:
        # accessory:20382:
        assert t400504_x50(acc1=20381, acc2=20382, z1=3, z2=-4)
        """State 185"""
        return 0
    elif GetTalkListEntryResult() == 97:
        """State 186"""
        assert t400504_x50(acc1=31201, acc2=31202, z1=3, z2=-4)
        """State 187"""
        return 0
    elif GetTalkListEntryResult() == 98:
        """State 188"""
        assert t400504_x50(acc1=30801, acc2=30802, z1=3, z2=-4)
        """State 189"""
        return 0
    elif GetTalkListEntryResult() == 99:
        """State 190"""
        # accessory:20451:
        # accessory:20452:
        assert t400504_x50(acc1=20451, acc2=20452, z1=3, z2=-4)
        """State 191"""
        return 0
    elif GetTalkListEntryResult() == 100:
        """State 192"""
        assert t400504_x50(acc1=30091, acc2=30092, z1=3, z2=-4)
        """State 193"""
        return 0
    elif GetTalkListEntryResult() == 101:
        """State 194"""
        assert t400504_x50(acc1=30841, acc2=30842, z1=3, z2=-4)
        """State 195"""
        return 0
    elif GetTalkListEntryResult() == 102:
        """State 196"""
        assert t400504_x50(acc1=30991, acc2=30992, z1=3, z2=-4)
        """State 197"""
        return 0
    elif GetTalkListEntryResult() == 103:
        """State 198"""
        assert t400504_x50(acc1=30041, acc2=30042, z1=3, z2=-4)
        """State 199"""
        return 0
    elif GetTalkListEntryResult() == 104:
        """State 200"""
        assert t400504_x50(acc1=31501, acc2=31502, z1=3, z2=-4)
        """State 201"""
        return 0
    elif GetTalkListEntryResult() == 105:
        """State 202"""
        assert t400504_x50(acc1=31601, acc2=31602, z1=3, z2=-4)
        """State 203"""
        return 0
    elif GetTalkListEntryResult() == 106:
        """State 204"""
        assert t400504_x50(acc1=31701, acc2=31702, z1=3, z2=-4)
        """State 205"""
        return 0
    elif GetTalkListEntryResult() == 107:
        """State 206"""
        assert t400504_x50(acc1=31801, acc2=31802, z1=3, z2=-4)
        """State 207"""
        return 0
    elif GetTalkListEntryResult() == 108:
        """State 208"""
        assert t400504_x50(acc1=31901, acc2=31902, z1=3, z2=-4)
        """State 209"""
        return 0
    elif GetTalkListEntryResult() == 109:
        """State 210"""
        assert t400504_x50(acc1=32001, acc2=32002, z1=3, z2=-4)
        """State 211"""
        return 0
    elif GetTalkListEntryResult() == 110:
        """State 212"""
        assert t400504_x50(acc1=32101, acc2=32102, z1=3, z2=-4)
        """State 213"""
        return 0
    elif GetTalkListEntryResult() == 111:
        """State 214"""
        assert t400504_x50(acc1=32201, acc2=32202, z1=3, z2=-4)
        """State 215"""
        return 0
    elif GetTalkListEntryResult() == 112:
        """State 216"""
        assert t400504_x50(acc1=32301, acc2=32302, z1=3, z2=-4)
        """State 217"""
        return 0
    elif not (CheckSpecificPersonMenuIsOpen(-1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0)):
        """State 218"""
        return 0

def t400504_x43():
    """State 0"""
    MainBonfireMenuFlag()
    ClearTalkListData()
    # accessory:20002:Life Ring+2
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20002, CompareType.GreaterOrEqual, 1, False),
                      1, 99015100, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20832, CompareType.GreaterOrEqual, 1, False),
                      52, 99015151, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30052, CompareType.GreaterOrEqual, 1, False),
                      56, 99015155, -1)
    # accessory:20012:Chloranthy Ring+2
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20012, CompareType.GreaterOrEqual, 1, False),
                      2, 99015101, -1)
    # accessory:20022:Havel's Ring+2
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20022, CompareType.GreaterOrEqual, 1, False),
                      3, 99015102, -1)
    # accessory:20032:Ring of Favor+2
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20032, CompareType.GreaterOrEqual, 1, False),
                      4, 99015103, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30212, CompareType.GreaterOrEqual, 1, False),
                      62, 99015161, -1)
    # accessory:20432:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20432, CompareType.GreaterOrEqual, 1, False),
                      32, 99015131, -1)
    # accessory:20492:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20492, CompareType.GreaterOrEqual, 1, False),
                      36, 99015135, -1)
    # accessory:20502:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20502, CompareType.GreaterOrEqual, 1, False),
                      37, 99015136, -1)
    # accessory:20512:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20512, CompareType.GreaterOrEqual, 1, False),
                      38, 99015137, -1)
    # accessory:20522:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20522, CompareType.GreaterOrEqual, 1, False),
                      39, 99015138, -1)
    # accessory:20342:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20342, CompareType.GreaterOrEqual, 1, False),
                      25, 99015124, -1)
    # accessory:20352:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20352, CompareType.GreaterOrEqual, 1, False),
                      26, 99015125, -1)
    # accessory:20362:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20362, CompareType.GreaterOrEqual, 1, False),
                      27, 99015126, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30022, CompareType.GreaterOrEqual, 1, False),
                      55, 99015154, -1)
    # accessory:20042:Ring of Steel Protection+2
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20042, CompareType.GreaterOrEqual, 1, False),
                      5, 99015104, -1)
    # accessory:20052:Flame Stoneplate Ring+2
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20052, CompareType.GreaterOrEqual, 1, False),
                      6, 99015105, -1)
    # accessory:20062:Thunder Stoneplate Ring+2
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20062, CompareType.GreaterOrEqual, 1, False),
                      7, 99015106, -1)
    # accessory:20072:Magic Stoneplate Ring+2
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20072, CompareType.GreaterOrEqual, 1, False),
                      8, 99015107, -1)
    # accessory:20082:Dark Stoneplate Ring+2
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20082, CompareType.GreaterOrEqual, 1, False),
                      9, 99015108, -1)
    # accessory:20092:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20092, CompareType.GreaterOrEqual, 1, False),
                      10, 99015109, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30662, CompareType.GreaterOrEqual, 1, False),
                      76, 99015175, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30672, CompareType.GreaterOrEqual, 1, False),
                      77, 99015176, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30682, CompareType.GreaterOrEqual, 1, False),
                      78, 99015177, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30692, CompareType.GreaterOrEqual, 1, False),
                      79, 99015178, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30702, CompareType.GreaterOrEqual, 1, False),
                      80, 99015179, -1)
    # accessory:20102:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20102, CompareType.GreaterOrEqual, 1, False),
                      11, 99015110, -1)
    # accessory:20112:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20112, CompareType.GreaterOrEqual, 1, False),
                      12, 99015111, -1)
    # accessory:20122:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20122, CompareType.GreaterOrEqual, 1, False),
                      13, 99015112, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 21002, CompareType.GreaterOrEqual, 1, False),
                      53, 99015152, -1)
    # accessory:20132:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20132, CompareType.GreaterOrEqual, 1, False),
                      14, 99015113, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30932, CompareType.GreaterOrEqual, 1, False),
                      85, 99015184, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30892, CompareType.GreaterOrEqual, 1, False),
                      82, 99015181, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30942, CompareType.GreaterOrEqual, 1, False),
                      86, 99015185, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30952, CompareType.GreaterOrEqual, 1, False),
                      87, 99015186, -1)
    # accessory:20462:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20462, CompareType.GreaterOrEqual, 1, False),
                      33, 99015132, -1)
    # accessory:20472:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20472, CompareType.GreaterOrEqual, 1, False),
                      34, 99015133, -1)
    # accessory:20152:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20152, CompareType.GreaterOrEqual, 1, False),
                      16, 99015115, -1)
    # accessory:20162:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20162, CompareType.GreaterOrEqual, 1, False),
                      17, 99015116, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30392, CompareType.GreaterOrEqual, 1, False),
                      68, 99015167, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30402, CompareType.GreaterOrEqual, 1, False),
                      69, 99015168, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30412, CompareType.GreaterOrEqual, 1, False),
                      70, 99015169, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30422, CompareType.GreaterOrEqual, 1, False),
                      71, 99015170, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30432, CompareType.GreaterOrEqual, 1, False),
                      72, 99015171, -1)
    # accessory:20142:Wood Grain Ring+2
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20142, CompareType.GreaterOrEqual, 1, False),
                      15, 99015114, -1)
    # accessory:20172:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20172, CompareType.GreaterOrEqual, 1, False),
                      18, 99015117, -1)
    # accessory:20182:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20182, CompareType.GreaterOrEqual, 1, False),
                      19, 99015118, -1)
    # accessory:20192:Wolf Ring+2
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20192, CompareType.GreaterOrEqual, 1, False),
                      20, 99015119, -1)
    # accessory:20272:Lingering Dragoncrest Ring+2
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20272, CompareType.GreaterOrEqual, 1, False),
                      21, 99015120, -1)
    # accessory:20282:Sage Ring+2
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20282, CompareType.GreaterOrEqual, 1, False),
                      22, 99015121, -1)
    # accessory:20302:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20302, CompareType.GreaterOrEqual, 1, False),
                      23, 99015122, -1)
    # accessory:20332:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20332, CompareType.GreaterOrEqual, 1, False),
                      24, 99015123, -1)
    # accessory:20372:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20372, CompareType.GreaterOrEqual, 1, False),
                      28, 99015127, -1)
    # accessory:20392:Covetous Gold Serpent Ring+2
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20392, CompareType.GreaterOrEqual, 1, False),
                      29, 99015128, -1)
    # accessory:20402:Covetous Silver Serpent Ring+2
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20402, CompareType.GreaterOrEqual, 1, False),
                      30, 99015129, -1)
    # accessory:20412:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20412, CompareType.GreaterOrEqual, 1, False),
                      31, 99015130, -1)
    # accessory:20482:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20482, CompareType.GreaterOrEqual, 1, False),
                      35, 99015134, -1)
    # accessory:20542:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20542, CompareType.GreaterOrEqual, 1, False),
                      40, 99015139, -1)
    # accessory:20552:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20552, CompareType.GreaterOrEqual, 1, False),
                      41, 99015140, -1)
    # accessory:20592:Ring of the Evil Eye+2
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20592, CompareType.GreaterOrEqual, 1, False),
                      42, 99015141, -1)
    # accessory:20602:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20602, CompareType.GreaterOrEqual, 1, False),
                      43, 99015142, -1)
    # accessory:20612:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20612, CompareType.GreaterOrEqual, 1, False),
                      44, 99015143, -1)
    # accessory:20662:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20662, CompareType.GreaterOrEqual, 1, False),
                      45, 99015144, -1)
    # accessory:20672:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20672, CompareType.GreaterOrEqual, 1, False),
                      46, 99015145, -1)
    # accessory:20702:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20702, CompareType.GreaterOrEqual, 1, False),
                      47, 99015146, -1)
    # accessory:20712:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20712, CompareType.GreaterOrEqual, 1, False),
                      48, 99015147, -1)
    # accessory:20722:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20722, CompareType.GreaterOrEqual, 1, False),
                      49, 99015148, -1)
    # accessory:20752:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20752, CompareType.GreaterOrEqual, 1, False),
                      50, 99015149, -1)
    # accessory:20792:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20792, CompareType.GreaterOrEqual, 1, False),
                      51, 99015150, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30012, CompareType.GreaterOrEqual, 1, False),
                      54, 99015153, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30082, CompareType.GreaterOrEqual, 1, False),
                      57, 99015156, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30452, CompareType.GreaterOrEqual, 1, False),
                      73, 99015172, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30502, CompareType.GreaterOrEqual, 1, False),
                      74, 99015173, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30652, CompareType.GreaterOrEqual, 1, False),
                      75, 99015174, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30172, CompareType.GreaterOrEqual, 1, False),
                      58, 99015157, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30182, CompareType.GreaterOrEqual, 1, False),
                      59, 99015158, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30192, CompareType.GreaterOrEqual, 1, False),
                      60, 99015159, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30202, CompareType.GreaterOrEqual, 1, False),
                      61, 99015160, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30332, CompareType.GreaterOrEqual, 1, False),
                      63, 99015162, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30342, CompareType.GreaterOrEqual, 1, False),
                      64, 99015163, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30352, CompareType.GreaterOrEqual, 1, False),
                      65, 99015164, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30362, CompareType.GreaterOrEqual, 1, False),
                      66, 99015165, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30372, CompareType.GreaterOrEqual, 1, False),
                      67, 99015166, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30872, CompareType.GreaterOrEqual, 1, False),
                      90, 99015189, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30882, CompareType.GreaterOrEqual, 1, False),
                      91, 99015190, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30902, CompareType.GreaterOrEqual, 1, False),
                      92, 99015191, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31402, CompareType.GreaterOrEqual, 1, False),
                      93, 99015192, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31302, CompareType.GreaterOrEqual, 1, False),
                      94, 99015193, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31082, CompareType.GreaterOrEqual, 1, False),
                      95, 99015194, -1)
    # accessory:20382:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20382, CompareType.GreaterOrEqual, 1, False),
                      96, 99015195, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31202, CompareType.GreaterOrEqual, 1, False),
                      97, 99015196, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30802, CompareType.GreaterOrEqual, 1, False),
                      98, 99015197, -1)
    # accessory:20452:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20452, CompareType.GreaterOrEqual, 1, False),
                      99, 99015198, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30092, CompareType.GreaterOrEqual, 1, False),
                      100, 99015199, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30842, CompareType.GreaterOrEqual, 1, False),
                      101, 99015200, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30992, CompareType.GreaterOrEqual, 1, False),
                      102, 99015201, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30042, CompareType.GreaterOrEqual, 1, False),
                      103, 99015202, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31502, CompareType.GreaterOrEqual, 1, False),
                      104, 99015203, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31602, CompareType.GreaterOrEqual, 1, False),
                      105, 99015204, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31702, CompareType.GreaterOrEqual, 1, False),
                      106, 99015205, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31802, CompareType.GreaterOrEqual, 1, False),
                      107, 99015206, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31902, CompareType.GreaterOrEqual, 1, False),
                      108, 99015207, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 32002, CompareType.GreaterOrEqual, 1, False),
                      109, 99015208, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 32102, CompareType.GreaterOrEqual, 1, False),
                      110, 99015209, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 32202, CompareType.GreaterOrEqual, 1, False),
                      111, 99015210, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 32302, CompareType.GreaterOrEqual, 1, False),
                      112, 99015211, -1)
    # action:15000180:"Quit"
    AddTalkListData(999, 15000180, -1)
    assert (not CheckSpecificPersonGenericDialogIsOpen(2) and not (CheckSpecificPersonMenuIsOpen(-1, 2) and not
            CheckSpecificPersonGenericDialogIsOpen(2)))
    """State 1"""
    ShowShopMessage(TalkOptionsType.Regular)
    if GetTalkListEntryResult() == 1:
        """State 2"""
        # accessory:20002:Life Ring+2
        # accessory:20003:Life Ring+3
        assert t400504_x50(acc1=20002, acc2=20003, z1=5, z2=-6)
        """State 3"""
        return 0
    elif GetTalkListEntryResult() == 2:
        """State 4"""
        # accessory:20012:Chloranthy Ring+2
        # accessory:20013:
        assert t400504_x50(acc1=20012, acc2=20013, z1=5, z2=-6)
        """State 5"""
        return 0
    elif GetTalkListEntryResult() == 3:
        """State 6"""
        # accessory:20022:Havel's Ring+2
        # accessory:20023:
        assert t400504_x50(acc1=20022, acc2=20023, z1=5, z2=-6)
        """State 7"""
        return 0
    elif GetTalkListEntryResult() == 4:
        """State 8"""
        # accessory:20032:Ring of Favor+2
        # accessory:20033:
        assert t400504_x50(acc1=20032, acc2=20033, z1=5, z2=-6)
        """State 9"""
        return 0
    elif GetTalkListEntryResult() == 5:
        """State 10"""
        # accessory:20042:Ring of Steel Protection+2
        # accessory:20043:
        assert t400504_x50(acc1=20042, acc2=20043, z1=5, z2=-6)
        """State 11"""
        return 0
    elif GetTalkListEntryResult() == 6:
        """State 12"""
        # accessory:20052:Flame Stoneplate Ring+2
        # accessory:20053:
        assert t400504_x50(acc1=20052, acc2=20053, z1=5, z2=-6)
        """State 13"""
        return 0
    elif GetTalkListEntryResult() == 7:
        """State 14"""
        # accessory:20062:Thunder Stoneplate Ring+2
        # accessory:20063:
        assert t400504_x50(acc1=20062, acc2=20063, z1=5, z2=-6)
        """State 15"""
        return 0
    elif GetTalkListEntryResult() == 8:
        """State 16"""
        # accessory:20072:Magic Stoneplate Ring+2
        # accessory:20073:
        assert t400504_x50(acc1=20072, acc2=20073, z1=5, z2=-6)
        """State 17"""
        return 0
    elif GetTalkListEntryResult() == 9:
        """State 18"""
        # accessory:20082:Dark Stoneplate Ring+2
        # accessory:20083:
        assert t400504_x50(acc1=20082, acc2=20083, z1=5, z2=-6)
        """State 19"""
        return 0
    elif GetTalkListEntryResult() == 10:
        """State 20"""
        # accessory:20092:
        # accessory:20093:
        assert t400504_x50(acc1=20092, acc2=20093, z1=5, z2=-6)
        """State 21"""
        return 0
    elif GetTalkListEntryResult() == 11:
        """State 22"""
        # accessory:20102:
        # accessory:20103:
        assert t400504_x50(acc1=20102, acc2=20103, z1=5, z2=-6)
        """State 23"""
        return 0
    elif GetTalkListEntryResult() == 12:
        """State 24"""
        # accessory:20112:
        # accessory:20113:
        assert t400504_x50(acc1=20112, acc2=20113, z1=5, z2=-6)
        """State 25"""
        return 0
    elif GetTalkListEntryResult() == 13:
        """State 26"""
        # accessory:20122:
        # accessory:20123:
        assert t400504_x50(acc1=20122, acc2=20123, z1=5, z2=-6)
        """State 27"""
        return 0
    elif GetTalkListEntryResult() == 14:
        """State 28"""
        # accessory:20132:
        # accessory:20133:
        assert t400504_x50(acc1=20132, acc2=20133, z1=5, z2=-6)
        """State 29"""
        return 0
    elif GetTalkListEntryResult() == 15:
        """State 30"""
        # accessory:20142:Wood Grain Ring+2
        # accessory:20143:
        assert t400504_x50(acc1=20142, acc2=20143, z1=5, z2=-6)
        """State 31"""
        return 0
    elif GetTalkListEntryResult() == 16:
        """State 32"""
        # accessory:20152:
        # accessory:20153:
        assert t400504_x50(acc1=20152, acc2=20153, z1=5, z2=-6)
        """State 33"""
        return 0
    elif GetTalkListEntryResult() == 17:
        """State 34"""
        # accessory:20162:
        # accessory:20163:
        assert t400504_x50(acc1=20162, acc2=20163, z1=5, z2=-6)
        """State 35"""
        return 0
    elif GetTalkListEntryResult() == 18:
        """State 36"""
        # accessory:20172:
        # accessory:20173:
        assert t400504_x50(acc1=20172, acc2=20173, z1=5, z2=-6)
        """State 37"""
        return 0
    elif GetTalkListEntryResult() == 19:
        """State 38"""
        # accessory:20182:
        # accessory:20183:
        assert t400504_x50(acc1=20182, acc2=20183, z1=5, z2=-6)
        """State 39"""
        return 0
    elif GetTalkListEntryResult() == 20:
        """State 40"""
        # accessory:20192:Wolf Ring+2
        # accessory:20193:
        assert t400504_x50(acc1=20192, acc2=20193, z1=5, z2=-6)
        """State 41"""
        return 0
    elif GetTalkListEntryResult() == 21:
        """State 42"""
        # accessory:20272:Lingering Dragoncrest Ring+2
        # accessory:20273:
        assert t400504_x50(acc1=20272, acc2=20273, z1=5, z2=-6)
        """State 43"""
        return 0
    elif GetTalkListEntryResult() == 22:
        """State 44"""
        # accessory:20282:Sage Ring+2
        # accessory:20283:
        assert t400504_x50(acc1=20282, acc2=20283, z1=5, z2=-6)
        """State 45"""
        return 0
    elif GetTalkListEntryResult() == 23:
        """State 46"""
        # accessory:20302:
        # accessory:20303:
        assert t400504_x50(acc1=20302, acc2=20303, z1=5, z2=-6)
        """State 47"""
        return 0
    elif GetTalkListEntryResult() == 24:
        """State 48"""
        # accessory:20332:
        # accessory:20333:
        assert t400504_x50(acc1=20332, acc2=20333, z1=5, z2=-6)
        """State 49"""
        return 0
    elif GetTalkListEntryResult() == 25:
        """State 50"""
        # accessory:20342:
        # accessory:20343:
        assert t400504_x50(acc1=20342, acc2=20343, z1=5, z2=-6)
        """State 51"""
        return 0
    elif GetTalkListEntryResult() == 26:
        """State 52"""
        # accessory:20352:
        # accessory:20353:
        assert t400504_x50(acc1=20352, acc2=20353, z1=5, z2=-6)
        """State 53"""
        return 0
    elif GetTalkListEntryResult() == 27:
        """State 54"""
        # accessory:20362:
        # accessory:20363:
        assert t400504_x50(acc1=20362, acc2=20363, z1=5, z2=-6)
        """State 55"""
        return 0
    elif GetTalkListEntryResult() == 28:
        """State 56"""
        # accessory:20372:
        # accessory:20373:
        assert t400504_x50(acc1=20372, acc2=20373, z1=5, z2=-6)
        """State 57"""
        return 0
    elif GetTalkListEntryResult() == 29:
        """State 58"""
        # accessory:20392:Covetous Gold Serpent Ring+2
        # accessory:20393:
        assert t400504_x50(acc1=20392, acc2=20393, z1=5, z2=-6)
        """State 59"""
        return 0
    elif GetTalkListEntryResult() == 30:
        """State 60"""
        # accessory:20402:Covetous Silver Serpent Ring+2
        # accessory:20403:
        assert t400504_x50(acc1=20402, acc2=20403, z1=5, z2=-6)
        """State 61"""
        return 0
    elif GetTalkListEntryResult() == 31:
        """State 62"""
        # accessory:20412:
        # accessory:20413:
        assert t400504_x50(acc1=20412, acc2=20413, z1=5, z2=-6)
        """State 63"""
        return 0
    elif GetTalkListEntryResult() == 32:
        """State 64"""
        # accessory:20432:
        # accessory:20433:
        assert t400504_x50(acc1=20432, acc2=20433, z1=5, z2=-6)
        """State 65"""
        return 0
    elif GetTalkListEntryResult() == 33:
        """State 66"""
        # accessory:20462:
        # accessory:20463:
        assert t400504_x50(acc1=20462, acc2=20463, z1=5, z2=-6)
        """State 67"""
        return 0
    elif GetTalkListEntryResult() == 34:
        """State 68"""
        # accessory:20472:
        # accessory:20473:
        assert t400504_x50(acc1=20472, acc2=20473, z1=5, z2=-6)
        """State 69"""
        return 0
    elif GetTalkListEntryResult() == 35:
        """State 70"""
        # accessory:20482:
        # accessory:20483:
        assert t400504_x50(acc1=20482, acc2=20483, z1=5, z2=-6)
        """State 71"""
        return 0
    elif GetTalkListEntryResult() == 36:
        """State 72"""
        # accessory:20492:
        # accessory:20493:
        assert t400504_x50(acc1=20492, acc2=20493, z1=5, z2=-6)
        """State 73"""
        return 0
    elif GetTalkListEntryResult() == 37:
        """State 74"""
        # accessory:20502:
        # accessory:20503:
        assert t400504_x50(acc1=20502, acc2=20503, z1=5, z2=-6)
        """State 75"""
        return 0
    elif GetTalkListEntryResult() == 38:
        """State 76"""
        # accessory:20512:
        # accessory:20513:
        assert t400504_x50(acc1=20512, acc2=20513, z1=5, z2=-6)
        """State 77"""
        return 0
    elif GetTalkListEntryResult() == 39:
        """State 78"""
        # accessory:20522:
        # accessory:20523:
        assert t400504_x50(acc1=20522, acc2=20523, z1=5, z2=-6)
        """State 79"""
        return 0
    elif GetTalkListEntryResult() == 40:
        """State 80"""
        # accessory:20542:
        # accessory:20543:
        assert t400504_x50(acc1=20542, acc2=20543, z1=5, z2=-6)
        """State 81"""
        return 0
    elif GetTalkListEntryResult() == 41:
        """State 82"""
        # accessory:20552:
        # accessory:20553:
        assert t400504_x50(acc1=20552, acc2=20553, z1=5, z2=-6)
        """State 83"""
        return 0
    elif GetTalkListEntryResult() == 42:
        """State 84"""
        # accessory:20592:Ring of the Evil Eye+2
        # accessory:20593:
        assert t400504_x50(acc1=20592, acc2=20593, z1=5, z2=-6)
        """State 85"""
        return 0
    elif GetTalkListEntryResult() == 43:
        """State 86"""
        # accessory:20602:
        # accessory:20603:
        assert t400504_x50(acc1=20602, acc2=20603, z1=5, z2=-6)
        """State 87"""
        return 0
    elif GetTalkListEntryResult() == 44:
        """State 88"""
        # accessory:20612:
        # accessory:20613:
        assert t400504_x50(acc1=20612, acc2=20613, z1=5, z2=-6)
        """State 89"""
        return 0
    elif GetTalkListEntryResult() == 45:
        """State 90"""
        # accessory:20662:
        # accessory:20663:
        assert t400504_x50(acc1=20662, acc2=20663, z1=5, z2=-6)
        """State 91"""
        return 0
    elif GetTalkListEntryResult() == 46:
        """State 92"""
        # accessory:20672:
        # accessory:20673:
        assert t400504_x50(acc1=20672, acc2=20673, z1=5, z2=-6)
        """State 93"""
        return 0
    elif GetTalkListEntryResult() == 47:
        """State 94"""
        # accessory:20702:
        # accessory:20703:
        assert t400504_x50(acc1=20702, acc2=20703, z1=5, z2=-6)
        """State 95"""
        return 0
    elif GetTalkListEntryResult() == 48:
        """State 96"""
        # accessory:20712:
        # accessory:20713:
        assert t400504_x50(acc1=20712, acc2=20713, z1=5, z2=-6)
        """State 97"""
        return 0
    elif GetTalkListEntryResult() == 49:
        """State 98"""
        # accessory:20722:
        # accessory:20723:
        assert t400504_x50(acc1=20722, acc2=20723, z1=5, z2=-6)
        """State 99"""
        return 0
    elif GetTalkListEntryResult() == 50:
        """State 100"""
        # accessory:20752:
        # accessory:20753:
        assert t400504_x50(acc1=20752, acc2=20753, z1=5, z2=-6)
        """State 101"""
        return 0
    elif GetTalkListEntryResult() == 51:
        """State 102"""
        # accessory:20792:
        # accessory:20793:
        assert t400504_x50(acc1=20792, acc2=20793, z1=5, z2=-6)
        """State 103"""
        return 0
    elif GetTalkListEntryResult() == 52:
        """State 104"""
        assert t400504_x50(acc1=20832, acc2=20833, z1=5, z2=-6)
        """State 105"""
        return 0
    elif GetTalkListEntryResult() == 53:
        """State 106"""
        assert t400504_x50(acc1=21002, acc2=21003, z1=5, z2=-6)
        """State 107"""
        return 0
    elif GetTalkListEntryResult() == 54:
        """State 108"""
        assert t400504_x50(acc1=30012, acc2=30013, z1=5, z2=-6)
        """State 109"""
        return 0
    elif GetTalkListEntryResult() == 55:
        """State 110"""
        assert t400504_x50(acc1=30022, acc2=30023, z1=5, z2=-6)
        """State 111"""
        return 0
    elif GetTalkListEntryResult() == 56:
        """State 112"""
        assert t400504_x50(acc1=30052, acc2=30053, z1=5, z2=-6)
        """State 113"""
        return 0
    elif GetTalkListEntryResult() == 57:
        """State 114"""
        assert t400504_x50(acc1=30082, acc2=30083, z1=5, z2=-6)
        """State 115"""
        return 0
    elif GetTalkListEntryResult() == 58:
        """State 116"""
        assert t400504_x50(acc1=30172, acc2=30173, z1=5, z2=-6)
        """State 117"""
        return 0
    elif GetTalkListEntryResult() == 59:
        """State 118"""
        assert t400504_x50(acc1=30182, acc2=30183, z1=5, z2=-6)
        """State 119"""
        return 0
    elif GetTalkListEntryResult() == 60:
        """State 120"""
        assert t400504_x50(acc1=30192, acc2=30193, z1=5, z2=-6)
        """State 121"""
        return 0
    elif GetTalkListEntryResult() == 61:
        """State 122"""
        assert t400504_x50(acc1=30202, acc2=30203, z1=5, z2=-6)
        """State 123"""
        return 0
    elif GetTalkListEntryResult() == 62:
        """State 124"""
        assert t400504_x50(acc1=30212, acc2=30213, z1=5, z2=-6)
        """State 125"""
        return 0
    elif GetTalkListEntryResult() == 63:
        """State 126"""
        assert t400504_x50(acc1=30332, acc2=30333, z1=5, z2=-6)
        """State 127"""
        return 0
    elif GetTalkListEntryResult() == 64:
        """State 128"""
        assert t400504_x50(acc1=30342, acc2=30343, z1=5, z2=-6)
        """State 129"""
        return 0
    elif GetTalkListEntryResult() == 65:
        """State 130"""
        assert t400504_x50(acc1=30352, acc2=30353, z1=5, z2=-6)
        """State 131"""
        return 0
    elif GetTalkListEntryResult() == 66:
        """State 132"""
        assert t400504_x50(acc1=30362, acc2=30363, z1=5, z2=-6)
        """State 133"""
        return 0
    elif GetTalkListEntryResult() == 67:
        """State 134"""
        assert t400504_x50(acc1=30372, acc2=30373, z1=5, z2=-6)
        """State 135"""
        return 0
    elif GetTalkListEntryResult() == 68:
        """State 136"""
        assert t400504_x50(acc1=30392, acc2=30393, z1=5, z2=-6)
        """State 137"""
        return 0
    elif GetTalkListEntryResult() == 69:
        """State 138"""
        assert t400504_x50(acc1=30402, acc2=30403, z1=5, z2=-6)
        """State 139"""
        return 0
    elif GetTalkListEntryResult() == 70:
        """State 140"""
        assert t400504_x50(acc1=30412, acc2=30413, z1=5, z2=-6)
        """State 141"""
        return 0
    elif GetTalkListEntryResult() == 71:
        """State 142"""
        assert t400504_x50(acc1=30422, acc2=30423, z1=5, z2=-6)
        """State 143"""
        return 0
    elif GetTalkListEntryResult() == 72:
        """State 144"""
        assert t400504_x50(acc1=30432, acc2=30433, z1=5, z2=-6)
        """State 145"""
        return 0
    elif GetTalkListEntryResult() == 73:
        """State 146"""
        assert t400504_x50(acc1=30452, acc2=30453, z1=5, z2=-6)
        """State 147"""
        return 0
    elif GetTalkListEntryResult() == 74:
        """State 148"""
        assert t400504_x50(acc1=30502, acc2=30503, z1=5, z2=-6)
        """State 149"""
        return 0
    elif GetTalkListEntryResult() == 75:
        """State 150"""
        assert t400504_x50(acc1=30652, acc2=30653, z1=5, z2=-6)
        """State 151"""
        return 0
    elif GetTalkListEntryResult() == 76:
        """State 152"""
        assert t400504_x50(acc1=30662, acc2=30663, z1=5, z2=-6)
        """State 153"""
        return 0
    elif GetTalkListEntryResult() == 77:
        """State 154"""
        assert t400504_x50(acc1=30672, acc2=30673, z1=5, z2=-6)
        """State 155"""
        return 0
    elif GetTalkListEntryResult() == 78:
        """State 156"""
        assert t400504_x50(acc1=30682, acc2=30683, z1=5, z2=-6)
        """State 157"""
        return 0
    elif GetTalkListEntryResult() == 79:
        """State 158"""
        assert t400504_x50(acc1=30692, acc2=30693, z1=5, z2=-6)
        """State 159"""
        return 0
    elif GetTalkListEntryResult() == 80:
        """State 160"""
        assert t400504_x50(acc1=30702, acc2=30703, z1=5, z2=-6)
        """State 161"""
        return 0
    elif GetTalkListEntryResult() == 81:
        """State 162"""
        assert t400504_x50(acc1=30802, acc2=30803, z1=5, z2=-6)
        """State 163"""
        return 0
    elif GetTalkListEntryResult() == 82:
        """State 164"""
        assert t400504_x50(acc1=30892, acc2=30893, z1=5, z2=-6)
        """State 165"""
        return 0
    elif GetTalkListEntryResult() == 85:
        """State 166"""
        assert t400504_x50(acc1=30932, acc2=30933, z1=5, z2=-6)
        """State 167"""
        return 0
    elif GetTalkListEntryResult() == 86:
        """State 168"""
        assert t400504_x50(acc1=30942, acc2=30943, z1=5, z2=-6)
        """State 169"""
        return 0
    elif GetTalkListEntryResult() == 87:
        """State 170"""
        assert t400504_x50(acc1=30952, acc2=30953, z1=5, z2=-6)
        """State 171"""
        return 0
    elif GetTalkListEntryResult() == 90:
        """State 172"""
        assert t400504_x50(acc1=30872, acc2=30873, z1=5, z2=-6)
        """State 173"""
        return 0
    elif GetTalkListEntryResult() == 91:
        """State 174"""
        assert t400504_x50(acc1=30882, acc2=30883, z1=5, z2=-6)
        """State 175"""
        return 0
    elif GetTalkListEntryResult() == 92:
        """State 176"""
        assert t400504_x50(acc1=30902, acc2=30903, z1=5, z2=-6)
        """State 177"""
        return 0
    elif GetTalkListEntryResult() == 93:
        """State 178"""
        assert t400504_x50(acc1=31402, acc2=31403, z1=5, z2=-6)
        """State 179"""
        return 0
    elif GetTalkListEntryResult() == 94:
        """State 180"""
        assert t400504_x50(acc1=31302, acc2=31303, z1=5, z2=-6)
        """State 181"""
        return 0
    elif GetTalkListEntryResult() == 95:
        """State 182"""
        assert t400504_x50(acc1=31082, acc2=31083, z1=5, z2=-6)
        """State 183"""
        return 0
    elif GetTalkListEntryResult() == 96:
        """State 184"""
        # accessory:20382:
        # accessory:20383:
        assert t400504_x50(acc1=20382, acc2=20383, z1=5, z2=-6)
        """State 185"""
        return 0
    elif GetTalkListEntryResult() == 97:
        """State 186"""
        assert t400504_x50(acc1=31202, acc2=31203, z1=5, z2=-6)
        """State 187"""
        return 0
    elif GetTalkListEntryResult() == 98:
        """State 188"""
        assert t400504_x50(acc1=30802, acc2=30803, z1=5, z2=-6)
        """State 189"""
        return 0
    elif GetTalkListEntryResult() == 99:
        """State 190"""
        # accessory:20452:
        # accessory:20453:
        assert t400504_x50(acc1=20452, acc2=20453, z1=5, z2=-6)
        """State 191"""
        return 0
    elif GetTalkListEntryResult() == 100:
        """State 192"""
        assert t400504_x50(acc1=30092, acc2=30093, z1=5, z2=-6)
        """State 193"""
        return 0
    elif GetTalkListEntryResult() == 101:
        """State 194"""
        assert t400504_x50(acc1=30842, acc2=30843, z1=5, z2=-6)
        """State 195"""
        return 0
    elif GetTalkListEntryResult() == 102:
        """State 196"""
        assert t400504_x50(acc1=30992, acc2=30993, z1=5, z2=-6)
        """State 197"""
        return 0
    elif GetTalkListEntryResult() == 103:
        """State 198"""
        assert t400504_x50(acc1=30042, acc2=30043, z1=5, z2=-6)
        """State 199"""
        return 0
    elif GetTalkListEntryResult() == 104:
        """State 200"""
        assert t400504_x50(acc1=31502, acc2=31503, z1=5, z2=-6)
        """State 201"""
        return 0
    elif GetTalkListEntryResult() == 105:
        """State 202"""
        assert t400504_x50(acc1=31602, acc2=31603, z1=5, z2=-6)
        """State 203"""
        return 0
    elif GetTalkListEntryResult() == 106:
        """State 204"""
        assert t400504_x50(acc1=31702, acc2=31703, z1=5, z2=-6)
        """State 205"""
        return 0
    elif GetTalkListEntryResult() == 107:
        """State 206"""
        assert t400504_x50(acc1=31802, acc2=31803, z1=5, z2=-6)
        """State 207"""
        return 0
    elif GetTalkListEntryResult() == 108:
        """State 208"""
        assert t400504_x50(acc1=31902, acc2=31903, z1=5, z2=-6)
        """State 209"""
        return 0
    elif GetTalkListEntryResult() == 109:
        """State 210"""
        assert t400504_x50(acc1=32002, acc2=32003, z1=5, z2=-6)
        """State 211"""
        return 0
    elif GetTalkListEntryResult() == 110:
        """State 212"""
        assert t400504_x50(acc1=32102, acc2=32103, z1=5, z2=-6)
        """State 213"""
        return 0
    elif GetTalkListEntryResult() == 111:
        """State 214"""
        assert t400504_x50(acc1=32202, acc2=32203, z1=5, z2=-6)
        """State 215"""
        return 0
    elif GetTalkListEntryResult() == 112:
        """State 216"""
        assert t400504_x50(acc1=32302, acc2=32303, z1=5, z2=-6)
        """State 217"""
        return 0
    elif not (CheckSpecificPersonMenuIsOpen(-1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0)):
        """State 218"""
        return 0

def t400504_x44():
    """State 0"""
    MainBonfireMenuFlag()
    ClearTalkListData()
    # accessory:20003:Life Ring+3
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20003, CompareType.GreaterOrEqual, 1, False),
                      1, 99015100, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20833, CompareType.GreaterOrEqual, 1, False),
                      52, 99015151, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30053, CompareType.GreaterOrEqual, 1, False),
                      56, 99015155, -1)
    # accessory:20013:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20013, CompareType.GreaterOrEqual, 1, False),
                      2, 99015101, -1)
    # accessory:20023:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20023, CompareType.GreaterOrEqual, 1, False),
                      3, 99015102, -1)
    # accessory:20033:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20033, CompareType.GreaterOrEqual, 1, False),
                      4, 99015103, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30213, CompareType.GreaterOrEqual, 1, False),
                      62, 99015161, -1)
    # accessory:20433:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20433, CompareType.GreaterOrEqual, 1, False),
                      32, 99015131, -1)
    # accessory:20493:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20493, CompareType.GreaterOrEqual, 1, False),
                      36, 99015135, -1)
    # accessory:20503:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20503, CompareType.GreaterOrEqual, 1, False),
                      37, 99015136, -1)
    # accessory:20513:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20513, CompareType.GreaterOrEqual, 1, False),
                      38, 99015137, -1)
    # accessory:20523:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20523, CompareType.GreaterOrEqual, 1, False),
                      39, 99015138, -1)
    # accessory:20343:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20343, CompareType.GreaterOrEqual, 1, False),
                      25, 99015124, -1)
    # accessory:20353:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20353, CompareType.GreaterOrEqual, 1, False),
                      26, 99015125, -1)
    # accessory:20363:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20363, CompareType.GreaterOrEqual, 1, False),
                      27, 99015126, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30023, CompareType.GreaterOrEqual, 1, False),
                      55, 99015154, -1)
    # accessory:20043:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20043, CompareType.GreaterOrEqual, 1, False),
                      5, 99015104, -1)
    # accessory:20053:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20053, CompareType.GreaterOrEqual, 1, False),
                      6, 99015105, -1)
    # accessory:20063:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20063, CompareType.GreaterOrEqual, 1, False),
                      7, 99015106, -1)
    # accessory:20073:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20073, CompareType.GreaterOrEqual, 1, False),
                      8, 99015107, -1)
    # accessory:20083:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20083, CompareType.GreaterOrEqual, 1, False),
                      9, 99015108, -1)
    # accessory:20093:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20093, CompareType.GreaterOrEqual, 1, False),
                      10, 99015109, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30663, CompareType.GreaterOrEqual, 1, False),
                      76, 99015175, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30673, CompareType.GreaterOrEqual, 1, False),
                      77, 99015176, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30683, CompareType.GreaterOrEqual, 1, False),
                      78, 99015177, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30693, CompareType.GreaterOrEqual, 1, False),
                      79, 99015178, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30703, CompareType.GreaterOrEqual, 1, False),
                      80, 99015179, -1)
    # accessory:20103:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20103, CompareType.GreaterOrEqual, 1, False),
                      11, 99015110, -1)
    # accessory:20113:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20113, CompareType.GreaterOrEqual, 1, False),
                      12, 99015111, -1)
    # accessory:20123:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20123, CompareType.GreaterOrEqual, 1, False),
                      13, 99015112, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 21003, CompareType.GreaterOrEqual, 1, False),
                      53, 99015152, -1)
    # accessory:20133:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20133, CompareType.GreaterOrEqual, 1, False),
                      14, 99015113, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30933, CompareType.GreaterOrEqual, 1, False),
                      85, 99015184, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30893, CompareType.GreaterOrEqual, 1, False),
                      82, 99015181, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30943, CompareType.GreaterOrEqual, 1, False),
                      86, 99015185, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30953, CompareType.GreaterOrEqual, 1, False),
                      87, 99015186, -1)
    # accessory:20463:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20463, CompareType.GreaterOrEqual, 1, False),
                      33, 99015132, -1)
    # accessory:20473:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20473, CompareType.GreaterOrEqual, 1, False),
                      34, 99015133, -1)
    # accessory:20153:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20153, CompareType.GreaterOrEqual, 1, False),
                      16, 99015115, -1)
    # accessory:20163:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20163, CompareType.GreaterOrEqual, 1, False),
                      17, 99015116, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30393, CompareType.GreaterOrEqual, 1, False),
                      68, 99015167, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30403, CompareType.GreaterOrEqual, 1, False),
                      69, 99015168, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30413, CompareType.GreaterOrEqual, 1, False),
                      70, 99015169, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30423, CompareType.GreaterOrEqual, 1, False),
                      71, 99015170, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30433, CompareType.GreaterOrEqual, 1, False),
                      72, 99015171, -1)
    # accessory:20143:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20143, CompareType.GreaterOrEqual, 1, False),
                      15, 99015114, -1)
    # accessory:20173:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20173, CompareType.GreaterOrEqual, 1, False),
                      18, 99015117, -1)
    # accessory:20183:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20183, CompareType.GreaterOrEqual, 1, False),
                      19, 99015118, -1)
    # accessory:20193:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20193, CompareType.GreaterOrEqual, 1, False),
                      20, 99015119, -1)
    # accessory:20273:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20273, CompareType.GreaterOrEqual, 1, False),
                      21, 99015120, -1)
    # accessory:20283:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20283, CompareType.GreaterOrEqual, 1, False),
                      22, 99015121, -1)
    # accessory:20303:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20303, CompareType.GreaterOrEqual, 1, False),
                      23, 99015122, -1)
    # accessory:20333:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20333, CompareType.GreaterOrEqual, 1, False),
                      24, 99015123, -1)
    # accessory:20373:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20373, CompareType.GreaterOrEqual, 1, False),
                      28, 99015127, -1)
    # accessory:20393:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20393, CompareType.GreaterOrEqual, 1, False),
                      29, 99015128, -1)
    # accessory:20403:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20403, CompareType.GreaterOrEqual, 1, False),
                      30, 99015129, -1)
    # accessory:20413:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20413, CompareType.GreaterOrEqual, 1, False),
                      31, 99015130, -1)
    # accessory:20483:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20483, CompareType.GreaterOrEqual, 1, False),
                      35, 99015134, -1)
    # accessory:20543:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20543, CompareType.GreaterOrEqual, 1, False),
                      40, 99015139, -1)
    # accessory:20553:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20553, CompareType.GreaterOrEqual, 1, False),
                      41, 99015140, -1)
    # accessory:20593:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20593, CompareType.GreaterOrEqual, 1, False),
                      42, 99015141, -1)
    # accessory:20603:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20603, CompareType.GreaterOrEqual, 1, False),
                      43, 99015142, -1)
    # accessory:20613:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20613, CompareType.GreaterOrEqual, 1, False),
                      44, 99015143, -1)
    # accessory:20663:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20663, CompareType.GreaterOrEqual, 1, False),
                      45, 99015144, -1)
    # accessory:20673:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20673, CompareType.GreaterOrEqual, 1, False),
                      46, 99015145, -1)
    # accessory:20703:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20703, CompareType.GreaterOrEqual, 1, False),
                      47, 99015146, -1)
    # accessory:20713:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20713, CompareType.GreaterOrEqual, 1, False),
                      48, 99015147, -1)
    # accessory:20723:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20723, CompareType.GreaterOrEqual, 1, False),
                      49, 99015148, -1)
    # accessory:20753:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20753, CompareType.GreaterOrEqual, 1, False),
                      50, 99015149, -1)
    # accessory:20793:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20793, CompareType.GreaterOrEqual, 1, False),
                      51, 99015150, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30013, CompareType.GreaterOrEqual, 1, False),
                      54, 99015153, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30083, CompareType.GreaterOrEqual, 1, False),
                      57, 99015156, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30453, CompareType.GreaterOrEqual, 1, False),
                      73, 99015172, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30503, CompareType.GreaterOrEqual, 1, False),
                      74, 99015173, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30653, CompareType.GreaterOrEqual, 1, False),
                      75, 99015174, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30173, CompareType.GreaterOrEqual, 1, False),
                      58, 99015157, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30183, CompareType.GreaterOrEqual, 1, False),
                      59, 99015158, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30193, CompareType.GreaterOrEqual, 1, False),
                      60, 99015159, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30203, CompareType.GreaterOrEqual, 1, False),
                      61, 99015160, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30333, CompareType.GreaterOrEqual, 1, False),
                      63, 99015162, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30343, CompareType.GreaterOrEqual, 1, False),
                      64, 99015163, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30353, CompareType.GreaterOrEqual, 1, False),
                      65, 99015164, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30363, CompareType.GreaterOrEqual, 1, False),
                      66, 99015165, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30373, CompareType.GreaterOrEqual, 1, False),
                      67, 99015166, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30873, CompareType.GreaterOrEqual, 1, False),
                      90, 99015189, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30883, CompareType.GreaterOrEqual, 1, False),
                      91, 99015190, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30903, CompareType.GreaterOrEqual, 1, False),
                      92, 99015191, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31403, CompareType.GreaterOrEqual, 1, False),
                      93, 99015192, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31303, CompareType.GreaterOrEqual, 1, False),
                      94, 99015193, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31083, CompareType.GreaterOrEqual, 1, False),
                      95, 99015194, -1)
    # accessory:20383:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20383, CompareType.GreaterOrEqual, 1, False),
                      96, 99015195, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31203, CompareType.GreaterOrEqual, 1, False),
                      97, 99015196, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30803, CompareType.GreaterOrEqual, 1, False),
                      98, 99015197, -1)
    # accessory:20453:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20453, CompareType.GreaterOrEqual, 1, False),
                      99, 99015198, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30093, CompareType.GreaterOrEqual, 1, False),
                      100, 99015199, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30843, CompareType.GreaterOrEqual, 1, False),
                      101, 99015200, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30993, CompareType.GreaterOrEqual, 1, False),
                      102, 99015201, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30043, CompareType.GreaterOrEqual, 1, False),
                      103, 99015202, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31503, CompareType.GreaterOrEqual, 1, False),
                      104, 99015203, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31603, CompareType.GreaterOrEqual, 1, False),
                      105, 99015204, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31703, CompareType.GreaterOrEqual, 1, False),
                      106, 99015205, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31803, CompareType.GreaterOrEqual, 1, False),
                      107, 99015206, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31903, CompareType.GreaterOrEqual, 1, False),
                      108, 99015207, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 32003, CompareType.GreaterOrEqual, 1, False),
                      109, 99015208, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 32103, CompareType.GreaterOrEqual, 1, False),
                      110, 99015209, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 32203, CompareType.GreaterOrEqual, 1, False),
                      111, 99015210, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 32303, CompareType.GreaterOrEqual, 1, False),
                      112, 99015211, -1)
    # action:15000180:"Quit"
    AddTalkListData(999, 15000180, -1)
    assert (not CheckSpecificPersonGenericDialogIsOpen(2) and not (CheckSpecificPersonMenuIsOpen(-1, 2) and not
            CheckSpecificPersonGenericDialogIsOpen(2)))
    """State 1"""
    ShowShopMessage(TalkOptionsType.Regular)
    if GetTalkListEntryResult() == 1:
        """State 2"""
        # accessory:20003:Life Ring+3
        # accessory:20004:
        assert t400504_x50(acc1=20003, acc2=20004, z1=7, z2=-8)
        """State 3"""
        return 0
    elif GetTalkListEntryResult() == 2:
        """State 4"""
        # accessory:20013:
        # accessory:20014:
        assert t400504_x50(acc1=20013, acc2=20014, z1=7, z2=-8)
        """State 5"""
        return 0
    elif GetTalkListEntryResult() == 3:
        """State 6"""
        # accessory:20023:
        # accessory:20024:
        assert t400504_x50(acc1=20023, acc2=20024, z1=7, z2=-8)
        """State 7"""
        return 0
    elif GetTalkListEntryResult() == 4:
        """State 8"""
        # accessory:20033:
        # accessory:20034:
        assert t400504_x50(acc1=20033, acc2=20034, z1=7, z2=-8)
        """State 9"""
        return 0
    elif GetTalkListEntryResult() == 5:
        """State 10"""
        # accessory:20043:
        # accessory:20044:
        assert t400504_x50(acc1=20043, acc2=20044, z1=7, z2=-8)
        """State 11"""
        return 0
    elif GetTalkListEntryResult() == 6:
        """State 12"""
        # accessory:20053:
        # accessory:20054:
        assert t400504_x50(acc1=20053, acc2=20054, z1=7, z2=-8)
        """State 13"""
        return 0
    elif GetTalkListEntryResult() == 7:
        """State 14"""
        # accessory:20063:
        # accessory:20064:
        assert t400504_x50(acc1=20063, acc2=20064, z1=7, z2=-8)
        """State 15"""
        return 0
    elif GetTalkListEntryResult() == 8:
        """State 16"""
        # accessory:20073:
        # accessory:20074:
        assert t400504_x50(acc1=20073, acc2=20074, z1=7, z2=-8)
        """State 17"""
        return 0
    elif GetTalkListEntryResult() == 9:
        """State 18"""
        # accessory:20083:
        # accessory:20084:
        assert t400504_x50(acc1=20083, acc2=20084, z1=7, z2=-8)
        """State 19"""
        return 0
    elif GetTalkListEntryResult() == 10:
        """State 20"""
        # accessory:20093:
        # accessory:20094:
        assert t400504_x50(acc1=20093, acc2=20094, z1=7, z2=-8)
        """State 21"""
        return 0
    elif GetTalkListEntryResult() == 11:
        """State 22"""
        # accessory:20103:
        # accessory:20104:
        assert t400504_x50(acc1=20103, acc2=20104, z1=7, z2=-8)
        """State 23"""
        return 0
    elif GetTalkListEntryResult() == 12:
        """State 24"""
        # accessory:20113:
        # accessory:20114:
        assert t400504_x50(acc1=20113, acc2=20114, z1=7, z2=-8)
        """State 25"""
        return 0
    elif GetTalkListEntryResult() == 13:
        """State 26"""
        # accessory:20123:
        # accessory:20124:
        assert t400504_x50(acc1=20123, acc2=20124, z1=7, z2=-8)
        """State 27"""
        return 0
    elif GetTalkListEntryResult() == 14:
        """State 28"""
        # accessory:20133:
        # accessory:20134:
        assert t400504_x50(acc1=20133, acc2=20134, z1=7, z2=-8)
        """State 29"""
        return 0
    elif GetTalkListEntryResult() == 15:
        """State 30"""
        # accessory:20143:
        # accessory:20144:
        assert t400504_x50(acc1=20143, acc2=20144, z1=7, z2=-8)
        """State 31"""
        return 0
    elif GetTalkListEntryResult() == 16:
        """State 32"""
        # accessory:20153:
        # accessory:20154:
        assert t400504_x50(acc1=20153, acc2=20154, z1=7, z2=-8)
        """State 33"""
        return 0
    elif GetTalkListEntryResult() == 17:
        """State 34"""
        # accessory:20163:
        # accessory:20164:
        assert t400504_x50(acc1=20163, acc2=20164, z1=7, z2=-8)
        """State 35"""
        return 0
    elif GetTalkListEntryResult() == 18:
        """State 36"""
        # accessory:20173:
        # accessory:20174:
        assert t400504_x50(acc1=20173, acc2=20174, z1=7, z2=-8)
        """State 37"""
        return 0
    elif GetTalkListEntryResult() == 19:
        """State 38"""
        # accessory:20183:
        # accessory:20184:
        assert t400504_x50(acc1=20183, acc2=20184, z1=7, z2=-8)
        """State 39"""
        return 0
    elif GetTalkListEntryResult() == 20:
        """State 40"""
        # accessory:20193:
        # accessory:20194:
        assert t400504_x50(acc1=20193, acc2=20194, z1=7, z2=-8)
        """State 41"""
        return 0
    elif GetTalkListEntryResult() == 21:
        """State 42"""
        # accessory:20273:
        # accessory:20274:
        assert t400504_x50(acc1=20273, acc2=20274, z1=7, z2=-8)
        """State 43"""
        return 0
    elif GetTalkListEntryResult() == 22:
        """State 44"""
        # accessory:20283:
        # accessory:20284:
        assert t400504_x50(acc1=20283, acc2=20284, z1=7, z2=-8)
        """State 45"""
        return 0
    elif GetTalkListEntryResult() == 23:
        """State 46"""
        # accessory:20303:
        # accessory:20304:
        assert t400504_x50(acc1=20303, acc2=20304, z1=7, z2=-8)
        """State 47"""
        return 0
    elif GetTalkListEntryResult() == 24:
        """State 48"""
        # accessory:20333:
        # accessory:20334:
        assert t400504_x50(acc1=20333, acc2=20334, z1=7, z2=-8)
        """State 49"""
        return 0
    elif GetTalkListEntryResult() == 25:
        """State 50"""
        # accessory:20343:
        # accessory:20344:
        assert t400504_x50(acc1=20343, acc2=20344, z1=7, z2=-8)
        """State 51"""
        return 0
    elif GetTalkListEntryResult() == 26:
        """State 52"""
        # accessory:20353:
        # accessory:20354:
        assert t400504_x50(acc1=20353, acc2=20354, z1=7, z2=-8)
        """State 53"""
        return 0
    elif GetTalkListEntryResult() == 27:
        """State 54"""
        # accessory:20363:
        # accessory:20364:
        assert t400504_x50(acc1=20363, acc2=20364, z1=7, z2=-8)
        """State 55"""
        return 0
    elif GetTalkListEntryResult() == 28:
        """State 56"""
        # accessory:20373:
        # accessory:20374:
        assert t400504_x50(acc1=20373, acc2=20374, z1=7, z2=-8)
        """State 57"""
        return 0
    elif GetTalkListEntryResult() == 29:
        """State 58"""
        # accessory:20393:
        # accessory:20394:
        assert t400504_x50(acc1=20393, acc2=20394, z1=7, z2=-8)
        """State 59"""
        return 0
    elif GetTalkListEntryResult() == 30:
        """State 60"""
        # accessory:20403:
        # accessory:20404:
        assert t400504_x50(acc1=20403, acc2=20404, z1=7, z2=-8)
        """State 61"""
        return 0
    elif GetTalkListEntryResult() == 31:
        """State 62"""
        # accessory:20413:
        # accessory:20414:
        assert t400504_x50(acc1=20413, acc2=20414, z1=7, z2=-8)
        """State 63"""
        return 0
    elif GetTalkListEntryResult() == 32:
        """State 64"""
        # accessory:20433:
        # accessory:20434:
        assert t400504_x50(acc1=20433, acc2=20434, z1=7, z2=-8)
        """State 65"""
        return 0
    elif GetTalkListEntryResult() == 33:
        """State 66"""
        # accessory:20463:
        # accessory:20464:
        assert t400504_x50(acc1=20463, acc2=20464, z1=7, z2=-8)
        """State 67"""
        return 0
    elif GetTalkListEntryResult() == 34:
        """State 68"""
        # accessory:20473:
        # accessory:20474:
        assert t400504_x50(acc1=20473, acc2=20474, z1=7, z2=-8)
        """State 69"""
        return 0
    elif GetTalkListEntryResult() == 35:
        """State 70"""
        # accessory:20483:
        # accessory:20484:
        assert t400504_x50(acc1=20483, acc2=20484, z1=7, z2=-8)
        """State 71"""
        return 0
    elif GetTalkListEntryResult() == 36:
        """State 72"""
        # accessory:20493:
        # accessory:20494:
        assert t400504_x50(acc1=20493, acc2=20494, z1=7, z2=-8)
        """State 73"""
        return 0
    elif GetTalkListEntryResult() == 37:
        """State 74"""
        # accessory:20503:
        # accessory:20504:
        assert t400504_x50(acc1=20503, acc2=20504, z1=7, z2=-8)
        """State 75"""
        return 0
    elif GetTalkListEntryResult() == 38:
        """State 76"""
        # accessory:20513:
        # accessory:20514:
        assert t400504_x50(acc1=20513, acc2=20514, z1=7, z2=-8)
        """State 77"""
        return 0
    elif GetTalkListEntryResult() == 39:
        """State 78"""
        # accessory:20523:
        # accessory:20524:
        assert t400504_x50(acc1=20523, acc2=20524, z1=7, z2=-8)
        """State 79"""
        return 0
    elif GetTalkListEntryResult() == 40:
        """State 80"""
        # accessory:20543:
        # accessory:20544:
        assert t400504_x50(acc1=20543, acc2=20544, z1=7, z2=-8)
        """State 81"""
        return 0
    elif GetTalkListEntryResult() == 41:
        """State 82"""
        # accessory:20553:
        # accessory:20554:
        assert t400504_x50(acc1=20553, acc2=20554, z1=7, z2=-8)
        """State 83"""
        return 0
    elif GetTalkListEntryResult() == 42:
        """State 84"""
        # accessory:20593:
        # accessory:20594:
        assert t400504_x50(acc1=20593, acc2=20594, z1=7, z2=-8)
        """State 85"""
        return 0
    elif GetTalkListEntryResult() == 43:
        """State 86"""
        # accessory:20603:
        # accessory:20604:
        assert t400504_x50(acc1=20603, acc2=20604, z1=7, z2=-8)
        """State 87"""
        return 0
    elif GetTalkListEntryResult() == 44:
        """State 88"""
        # accessory:20613:
        # accessory:20614:
        assert t400504_x50(acc1=20613, acc2=20614, z1=7, z2=-8)
        """State 89"""
        return 0
    elif GetTalkListEntryResult() == 45:
        """State 90"""
        # accessory:20663:
        # accessory:20664:
        assert t400504_x50(acc1=20663, acc2=20664, z1=7, z2=-8)
        """State 91"""
        return 0
    elif GetTalkListEntryResult() == 46:
        """State 92"""
        # accessory:20673:
        # accessory:20674:
        assert t400504_x50(acc1=20673, acc2=20674, z1=7, z2=-8)
        """State 93"""
        return 0
    elif GetTalkListEntryResult() == 47:
        """State 94"""
        # accessory:20703:
        # accessory:20704:
        assert t400504_x50(acc1=20703, acc2=20704, z1=7, z2=-8)
        """State 95"""
        return 0
    elif GetTalkListEntryResult() == 48:
        """State 96"""
        # accessory:20713:
        # accessory:20714:
        assert t400504_x50(acc1=20713, acc2=20714, z1=7, z2=-8)
        """State 97"""
        return 0
    elif GetTalkListEntryResult() == 49:
        """State 98"""
        # accessory:20723:
        # accessory:20724:
        assert t400504_x50(acc1=20723, acc2=20724, z1=7, z2=-8)
        """State 99"""
        return 0
    elif GetTalkListEntryResult() == 50:
        """State 100"""
        # accessory:20753:
        # accessory:20754:
        assert t400504_x50(acc1=20753, acc2=20754, z1=7, z2=-8)
        """State 101"""
        return 0
    elif GetTalkListEntryResult() == 51:
        """State 102"""
        # accessory:20793:
        # accessory:20794:
        assert t400504_x50(acc1=20793, acc2=20794, z1=7, z2=-8)
        """State 103"""
        return 0
    elif GetTalkListEntryResult() == 52:
        """State 104"""
        assert t400504_x50(acc1=20833, acc2=20834, z1=7, z2=-8)
        """State 105"""
        return 0
    elif GetTalkListEntryResult() == 53:
        """State 106"""
        assert t400504_x50(acc1=21003, acc2=21004, z1=7, z2=-8)
        """State 107"""
        return 0
    elif GetTalkListEntryResult() == 54:
        """State 108"""
        assert t400504_x50(acc1=30013, acc2=30014, z1=7, z2=-8)
        """State 109"""
        return 0
    elif GetTalkListEntryResult() == 55:
        """State 110"""
        assert t400504_x50(acc1=30023, acc2=30024, z1=7, z2=-8)
        """State 111"""
        return 0
    elif GetTalkListEntryResult() == 56:
        """State 112"""
        assert t400504_x50(acc1=30053, acc2=30054, z1=7, z2=-8)
        """State 113"""
        return 0
    elif GetTalkListEntryResult() == 57:
        """State 114"""
        assert t400504_x50(acc1=30083, acc2=30084, z1=7, z2=-8)
        """State 115"""
        return 0
    elif GetTalkListEntryResult() == 58:
        """State 116"""
        assert t400504_x50(acc1=30173, acc2=30174, z1=7, z2=-8)
        """State 117"""
        return 0
    elif GetTalkListEntryResult() == 59:
        """State 118"""
        assert t400504_x50(acc1=30183, acc2=30184, z1=7, z2=-8)
        """State 119"""
        return 0
    elif GetTalkListEntryResult() == 60:
        """State 120"""
        assert t400504_x50(acc1=30193, acc2=30194, z1=7, z2=-8)
        """State 121"""
        return 0
    elif GetTalkListEntryResult() == 61:
        """State 122"""
        assert t400504_x50(acc1=30203, acc2=30204, z1=7, z2=-8)
        """State 123"""
        return 0
    elif GetTalkListEntryResult() == 62:
        """State 124"""
        assert t400504_x50(acc1=30213, acc2=30214, z1=7, z2=-8)
        """State 125"""
        return 0
    elif GetTalkListEntryResult() == 63:
        """State 126"""
        assert t400504_x50(acc1=30333, acc2=30334, z1=7, z2=-8)
        """State 127"""
        return 0
    elif GetTalkListEntryResult() == 64:
        """State 128"""
        assert t400504_x50(acc1=30343, acc2=30344, z1=7, z2=-8)
        """State 129"""
        return 0
    elif GetTalkListEntryResult() == 65:
        """State 130"""
        assert t400504_x50(acc1=30353, acc2=30354, z1=7, z2=-8)
        """State 131"""
        return 0
    elif GetTalkListEntryResult() == 66:
        """State 132"""
        assert t400504_x50(acc1=30363, acc2=30364, z1=7, z2=-8)
        """State 133"""
        return 0
    elif GetTalkListEntryResult() == 67:
        """State 134"""
        assert t400504_x50(acc1=30373, acc2=30374, z1=7, z2=-8)
        """State 135"""
        return 0
    elif GetTalkListEntryResult() == 68:
        """State 136"""
        assert t400504_x50(acc1=30393, acc2=30394, z1=7, z2=-8)
        """State 137"""
        return 0
    elif GetTalkListEntryResult() == 69:
        """State 138"""
        assert t400504_x50(acc1=30403, acc2=30404, z1=7, z2=-8)
        """State 139"""
        return 0
    elif GetTalkListEntryResult() == 70:
        """State 140"""
        assert t400504_x50(acc1=30413, acc2=30414, z1=7, z2=-8)
        """State 141"""
        return 0
    elif GetTalkListEntryResult() == 71:
        """State 142"""
        assert t400504_x50(acc1=30423, acc2=30424, z1=7, z2=-8)
        """State 143"""
        return 0
    elif GetTalkListEntryResult() == 72:
        """State 144"""
        assert t400504_x50(acc1=30433, acc2=30434, z1=7, z2=-8)
        """State 145"""
        return 0
    elif GetTalkListEntryResult() == 73:
        """State 146"""
        assert t400504_x50(acc1=30453, acc2=30454, z1=7, z2=-8)
        """State 147"""
        return 0
    elif GetTalkListEntryResult() == 74:
        """State 148"""
        assert t400504_x50(acc1=30503, acc2=30504, z1=7, z2=-8)
        """State 149"""
        return 0
    elif GetTalkListEntryResult() == 75:
        """State 150"""
        assert t400504_x50(acc1=30653, acc2=30654, z1=7, z2=-8)
        """State 151"""
        return 0
    elif GetTalkListEntryResult() == 76:
        """State 152"""
        assert t400504_x50(acc1=30663, acc2=30664, z1=7, z2=-8)
        """State 153"""
        return 0
    elif GetTalkListEntryResult() == 77:
        """State 154"""
        assert t400504_x50(acc1=30673, acc2=30674, z1=7, z2=-8)
        """State 155"""
        return 0
    elif GetTalkListEntryResult() == 78:
        """State 156"""
        assert t400504_x50(acc1=30683, acc2=30684, z1=7, z2=-8)
        """State 157"""
        return 0
    elif GetTalkListEntryResult() == 79:
        """State 158"""
        assert t400504_x50(acc1=30693, acc2=30694, z1=7, z2=-8)
        """State 159"""
        return 0
    elif GetTalkListEntryResult() == 80:
        """State 160"""
        assert t400504_x50(acc1=30703, acc2=30704, z1=7, z2=-8)
        """State 161"""
        return 0
    elif GetTalkListEntryResult() == 81:
        """State 162"""
        assert t400504_x50(acc1=30803, acc2=30804, z1=7, z2=-8)
        """State 163"""
        return 0
    elif GetTalkListEntryResult() == 82:
        """State 164"""
        assert t400504_x50(acc1=30893, acc2=30894, z1=7, z2=-8)
        """State 165"""
        return 0
    elif GetTalkListEntryResult() == 85:
        """State 166"""
        assert t400504_x50(acc1=30933, acc2=30934, z1=7, z2=-8)
        """State 167"""
        return 0
    elif GetTalkListEntryResult() == 86:
        """State 168"""
        assert t400504_x50(acc1=30943, acc2=30944, z1=7, z2=-8)
        """State 169"""
        return 0
    elif GetTalkListEntryResult() == 87:
        """State 170"""
        assert t400504_x50(acc1=30953, acc2=30954, z1=7, z2=-8)
        """State 171"""
        return 0
    elif GetTalkListEntryResult() == 90:
        """State 172"""
        assert t400504_x50(acc1=30873, acc2=30874, z1=7, z2=-8)
        """State 173"""
        return 0
    elif GetTalkListEntryResult() == 91:
        """State 174"""
        assert t400504_x50(acc1=30883, acc2=30884, z1=7, z2=-8)
        """State 175"""
        return 0
    elif GetTalkListEntryResult() == 92:
        """State 176"""
        assert t400504_x50(acc1=30903, acc2=30904, z1=7, z2=-8)
        """State 177"""
        return 0
    elif GetTalkListEntryResult() == 93:
        """State 178"""
        assert t400504_x50(acc1=31403, acc2=31404, z1=7, z2=-8)
        """State 179"""
        return 0
    elif GetTalkListEntryResult() == 94:
        """State 180"""
        assert t400504_x50(acc1=31303, acc2=31304, z1=7, z2=-8)
        """State 181"""
        return 0
    elif GetTalkListEntryResult() == 95:
        """State 182"""
        assert t400504_x50(acc1=31083, acc2=31084, z1=7, z2=-8)
        """State 183"""
        return 0
    elif GetTalkListEntryResult() == 96:
        """State 184"""
        # accessory:20383:
        # accessory:20384:
        assert t400504_x50(acc1=20383, acc2=20384, z1=7, z2=-8)
        """State 185"""
        return 0
    elif GetTalkListEntryResult() == 97:
        """State 186"""
        assert t400504_x50(acc1=31203, acc2=31204, z1=7, z2=-8)
        """State 187"""
        return 0
    elif GetTalkListEntryResult() == 98:
        """State 188"""
        assert t400504_x50(acc1=30803, acc2=30804, z1=7, z2=-8)
        """State 189"""
        return 0
    elif GetTalkListEntryResult() == 99:
        """State 190"""
        # accessory:20453:
        # accessory:20454:
        assert t400504_x50(acc1=20453, acc2=20454, z1=7, z2=-8)
        """State 191"""
        return 0
    elif GetTalkListEntryResult() == 100:
        """State 192"""
        assert t400504_x50(acc1=30093, acc2=30094, z1=7, z2=-8)
        """State 193"""
        return 0
    elif GetTalkListEntryResult() == 101:
        """State 194"""
        assert t400504_x50(acc1=30843, acc2=30844, z1=7, z2=-8)
        """State 195"""
        return 0
    elif GetTalkListEntryResult() == 102:
        """State 196"""
        assert t400504_x50(acc1=30993, acc2=30994, z1=7, z2=-8)
        """State 197"""
        return 0
    elif GetTalkListEntryResult() == 103:
        """State 198"""
        assert t400504_x50(acc1=30043, acc2=30044, z1=7, z2=-8)
        """State 199"""
        return 0
    elif GetTalkListEntryResult() == 104:
        """State 200"""
        assert t400504_x50(acc1=31503, acc2=31504, z1=7, z2=-8)
        """State 201"""
        return 0
    elif GetTalkListEntryResult() == 105:
        """State 202"""
        assert t400504_x50(acc1=31603, acc2=31604, z1=7, z2=-8)
        """State 203"""
        return 0
    elif GetTalkListEntryResult() == 106:
        """State 204"""
        assert t400504_x50(acc1=31703, acc2=31704, z1=7, z2=-8)
        """State 205"""
        return 0
    elif GetTalkListEntryResult() == 107:
        """State 206"""
        assert t400504_x50(acc1=31803, acc2=31804, z1=7, z2=-8)
        """State 207"""
        return 0
    elif GetTalkListEntryResult() == 108:
        """State 208"""
        assert t400504_x50(acc1=31903, acc2=31904, z1=7, z2=-8)
        """State 209"""
        return 0
    elif GetTalkListEntryResult() == 109:
        """State 210"""
        assert t400504_x50(acc1=32003, acc2=32004, z1=7, z2=-8)
        """State 211"""
        return 0
    elif GetTalkListEntryResult() == 110:
        """State 212"""
        assert t400504_x50(acc1=32103, acc2=32104, z1=7, z2=-8)
        """State 213"""
        return 0
    elif GetTalkListEntryResult() == 111:
        """State 214"""
        assert t400504_x50(acc1=32203, acc2=32204, z1=7, z2=-8)
        """State 215"""
        return 0
    elif GetTalkListEntryResult() == 112:
        """State 216"""
        assert t400504_x50(acc1=32303, acc2=32304, z1=7, z2=-8)
        """State 217"""
        return 0
    elif not (CheckSpecificPersonMenuIsOpen(-1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0)):
        """State 218"""
        return 0

def t400504_x45():
    """State 0"""
    MainBonfireMenuFlag()
    ClearTalkListData()
    # accessory:20004:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20004, CompareType.GreaterOrEqual, 1, False),
                      1, 99015100, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20834, CompareType.GreaterOrEqual, 1, False),
                      52, 99015151, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30054, CompareType.GreaterOrEqual, 1, False),
                      56, 99015155, -1)
    # accessory:20014:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20014, CompareType.GreaterOrEqual, 1, False),
                      2, 99015101, -1)
    # accessory:20024:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20024, CompareType.GreaterOrEqual, 1, False),
                      3, 99015102, -1)
    # accessory:20034:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20034, CompareType.GreaterOrEqual, 1, False),
                      4, 99015103, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30214, CompareType.GreaterOrEqual, 1, False),
                      62, 99015161, -1)
    # accessory:20434:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20434, CompareType.GreaterOrEqual, 1, False),
                      32, 99015131, -1)
    # accessory:20494:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20494, CompareType.GreaterOrEqual, 1, False),
                      36, 99015135, -1)
    # accessory:20504:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20504, CompareType.GreaterOrEqual, 1, False),
                      37, 99015136, -1)
    # accessory:20514:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20514, CompareType.GreaterOrEqual, 1, False),
                      38, 99015137, -1)
    # accessory:20524:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20524, CompareType.GreaterOrEqual, 1, False),
                      39, 99015138, -1)
    # accessory:20344:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20344, CompareType.GreaterOrEqual, 1, False),
                      25, 99015124, -1)
    # accessory:20354:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20354, CompareType.GreaterOrEqual, 1, False),
                      26, 99015125, -1)
    # accessory:20364:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20364, CompareType.GreaterOrEqual, 1, False),
                      27, 99015126, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30024, CompareType.GreaterOrEqual, 1, False),
                      55, 99015154, -1)
    # accessory:20044:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20044, CompareType.GreaterOrEqual, 1, False),
                      5, 99015104, -1)
    # accessory:20054:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20054, CompareType.GreaterOrEqual, 1, False),
                      6, 99015105, -1)
    # accessory:20064:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20064, CompareType.GreaterOrEqual, 1, False),
                      7, 99015106, -1)
    # accessory:20074:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20074, CompareType.GreaterOrEqual, 1, False),
                      8, 99015107, -1)
    # accessory:20084:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20084, CompareType.GreaterOrEqual, 1, False),
                      9, 99015108, -1)
    # accessory:20094:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20094, CompareType.GreaterOrEqual, 1, False),
                      10, 99015109, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30664, CompareType.GreaterOrEqual, 1, False),
                      76, 99015175, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30674, CompareType.GreaterOrEqual, 1, False),
                      77, 99015176, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30684, CompareType.GreaterOrEqual, 1, False),
                      78, 99015177, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30694, CompareType.GreaterOrEqual, 1, False),
                      79, 99015178, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30704, CompareType.GreaterOrEqual, 1, False),
                      80, 99015179, -1)
    # accessory:20104:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20104, CompareType.GreaterOrEqual, 1, False),
                      11, 99015110, -1)
    # accessory:20114:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20114, CompareType.GreaterOrEqual, 1, False),
                      12, 99015111, -1)
    # accessory:20124:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20124, CompareType.GreaterOrEqual, 1, False),
                      13, 99015112, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 21004, CompareType.GreaterOrEqual, 1, False),
                      53, 99015152, -1)
    # accessory:20134:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20134, CompareType.GreaterOrEqual, 1, False),
                      14, 99015113, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30934, CompareType.GreaterOrEqual, 1, False),
                      85, 99015184, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30894, CompareType.GreaterOrEqual, 1, False),
                      82, 99015181, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30944, CompareType.GreaterOrEqual, 1, False),
                      86, 99015185, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30954, CompareType.GreaterOrEqual, 1, False),
                      87, 99015186, -1)
    # accessory:20464:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20464, CompareType.GreaterOrEqual, 1, False),
                      33, 99015132, -1)
    # accessory:20474:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20474, CompareType.GreaterOrEqual, 1, False),
                      34, 99015133, -1)
    # accessory:20154:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20154, CompareType.GreaterOrEqual, 1, False),
                      16, 99015115, -1)
    # accessory:20164:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20164, CompareType.GreaterOrEqual, 1, False),
                      17, 99015116, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30394, CompareType.GreaterOrEqual, 1, False),
                      68, 99015167, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30404, CompareType.GreaterOrEqual, 1, False),
                      69, 99015168, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30414, CompareType.GreaterOrEqual, 1, False),
                      70, 99015169, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30424, CompareType.GreaterOrEqual, 1, False),
                      71, 99015170, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30434, CompareType.GreaterOrEqual, 1, False),
                      72, 99015171, -1)
    # accessory:20144:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20144, CompareType.GreaterOrEqual, 1, False),
                      15, 99015114, -1)
    # accessory:20174:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20174, CompareType.GreaterOrEqual, 1, False),
                      18, 99015117, -1)
    # accessory:20184:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20184, CompareType.GreaterOrEqual, 1, False),
                      19, 99015118, -1)
    # accessory:20194:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20194, CompareType.GreaterOrEqual, 1, False),
                      20, 99015119, -1)
    # accessory:20274:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20274, CompareType.GreaterOrEqual, 1, False),
                      21, 99015120, -1)
    # accessory:20284:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20284, CompareType.GreaterOrEqual, 1, False),
                      22, 99015121, -1)
    # accessory:20304:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20304, CompareType.GreaterOrEqual, 1, False),
                      23, 99015122, -1)
    # accessory:20334:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20334, CompareType.GreaterOrEqual, 1, False),
                      24, 99015123, -1)
    # accessory:20374:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20374, CompareType.GreaterOrEqual, 1, False),
                      28, 99015127, -1)
    # accessory:20394:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20394, CompareType.GreaterOrEqual, 1, False),
                      29, 99015128, -1)
    # accessory:20404:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20404, CompareType.GreaterOrEqual, 1, False),
                      30, 99015129, -1)
    # accessory:20414:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20414, CompareType.GreaterOrEqual, 1, False),
                      31, 99015130, -1)
    # accessory:20484:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20484, CompareType.GreaterOrEqual, 1, False),
                      35, 99015134, -1)
    # accessory:20544:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20544, CompareType.GreaterOrEqual, 1, False),
                      40, 99015139, -1)
    # accessory:20554:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20554, CompareType.GreaterOrEqual, 1, False),
                      41, 99015140, -1)
    # accessory:20594:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20594, CompareType.GreaterOrEqual, 1, False),
                      42, 99015141, -1)
    # accessory:20604:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20604, CompareType.GreaterOrEqual, 1, False),
                      43, 99015142, -1)
    # accessory:20614:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20614, CompareType.GreaterOrEqual, 1, False),
                      44, 99015143, -1)
    # accessory:20664:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20664, CompareType.GreaterOrEqual, 1, False),
                      45, 99015144, -1)
    # accessory:20674:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20674, CompareType.GreaterOrEqual, 1, False),
                      46, 99015145, -1)
    # accessory:20704:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20704, CompareType.GreaterOrEqual, 1, False),
                      47, 99015146, -1)
    # accessory:20714:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20714, CompareType.GreaterOrEqual, 1, False),
                      48, 99015147, -1)
    # accessory:20724:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20724, CompareType.GreaterOrEqual, 1, False),
                      49, 99015148, -1)
    # accessory:20754:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20754, CompareType.GreaterOrEqual, 1, False),
                      50, 99015149, -1)
    # accessory:20794:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20794, CompareType.GreaterOrEqual, 1, False),
                      51, 99015150, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30014, CompareType.GreaterOrEqual, 1, False),
                      54, 99015153, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30084, CompareType.GreaterOrEqual, 1, False),
                      57, 99015156, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30454, CompareType.GreaterOrEqual, 1, False),
                      73, 99015172, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30504, CompareType.GreaterOrEqual, 1, False),
                      74, 99015173, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30654, CompareType.GreaterOrEqual, 1, False),
                      75, 99015174, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30174, CompareType.GreaterOrEqual, 1, False),
                      58, 99015157, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30184, CompareType.GreaterOrEqual, 1, False),
                      59, 99015158, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30194, CompareType.GreaterOrEqual, 1, False),
                      60, 99015159, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30204, CompareType.GreaterOrEqual, 1, False),
                      61, 99015160, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30334, CompareType.GreaterOrEqual, 1, False),
                      63, 99015162, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30344, CompareType.GreaterOrEqual, 1, False),
                      64, 99015163, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30354, CompareType.GreaterOrEqual, 1, False),
                      65, 99015164, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30364, CompareType.GreaterOrEqual, 1, False),
                      66, 99015165, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30374, CompareType.GreaterOrEqual, 1, False),
                      67, 99015166, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30874, CompareType.GreaterOrEqual, 1, False),
                      90, 99015189, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30884, CompareType.GreaterOrEqual, 1, False),
                      91, 99015190, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30904, CompareType.GreaterOrEqual, 1, False),
                      92, 99015191, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31404, CompareType.GreaterOrEqual, 1, False),
                      93, 99015192, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31304, CompareType.GreaterOrEqual, 1, False),
                      94, 99015193, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31084, CompareType.GreaterOrEqual, 1, False),
                      95, 99015194, -1)
    # accessory:20384:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20384, CompareType.GreaterOrEqual, 1, False),
                      96, 99015195, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31204, CompareType.GreaterOrEqual, 1, False),
                      97, 99015196, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30804, CompareType.GreaterOrEqual, 1, False),
                      98, 99015197, -1)
    # accessory:20454:
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 20454, CompareType.GreaterOrEqual, 1, False),
                      99, 99015198, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30094, CompareType.GreaterOrEqual, 1, False),
                      100, 99015199, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30844, CompareType.GreaterOrEqual, 1, False),
                      101, 99015200, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30994, CompareType.GreaterOrEqual, 1, False),
                      102, 99015201, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 30044, CompareType.GreaterOrEqual, 1, False),
                      103, 99015202, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31504, CompareType.GreaterOrEqual, 1, False),
                      104, 99015203, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31604, CompareType.GreaterOrEqual, 1, False),
                      105, 99015204, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31704, CompareType.GreaterOrEqual, 1, False),
                      106, 99015205, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31804, CompareType.GreaterOrEqual, 1, False),
                      107, 99015206, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 31904, CompareType.GreaterOrEqual, 1, False),
                      108, 99015207, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 32004, CompareType.GreaterOrEqual, 1, False),
                      109, 99015208, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 32104, CompareType.GreaterOrEqual, 1, False),
                      110, 99015209, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 32204, CompareType.GreaterOrEqual, 1, False),
                      111, 99015210, -1)
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Accessory, 32304, CompareType.GreaterOrEqual, 1, False),
                      112, 99015211, -1)
    # action:15000180:"Quit"
    AddTalkListData(999, 15000180, -1)
    assert (not CheckSpecificPersonGenericDialogIsOpen(2) and not (CheckSpecificPersonMenuIsOpen(-1, 2) and not
            CheckSpecificPersonGenericDialogIsOpen(2)))
    """State 1"""
    ShowShopMessage(TalkOptionsType.Regular)
    if GetTalkListEntryResult() == 1:
        """State 2"""
        # accessory:20004:
        # accessory:20005:
        assert t400504_x50(acc1=20004, acc2=20005, z1=9, z2=-10)
        """State 3"""
        return 0
    elif GetTalkListEntryResult() == 2:
        """State 4"""
        # accessory:20014:
        # accessory:20015:
        assert t400504_x50(acc1=20014, acc2=20015, z1=9, z2=-10)
        """State 5"""
        return 0
    elif GetTalkListEntryResult() == 3:
        """State 6"""
        # accessory:20024:
        # accessory:20025:
        assert t400504_x50(acc1=20024, acc2=20025, z1=9, z2=-10)
        """State 7"""
        return 0
    elif GetTalkListEntryResult() == 4:
        """State 8"""
        # accessory:20034:
        # accessory:20035:
        assert t400504_x50(acc1=20034, acc2=20035, z1=9, z2=-10)
        """State 9"""
        return 0
    elif GetTalkListEntryResult() == 5:
        """State 10"""
        # accessory:20044:
        # accessory:20045:
        assert t400504_x50(acc1=20044, acc2=20045, z1=9, z2=-10)
        """State 11"""
        return 0
    elif GetTalkListEntryResult() == 6:
        """State 12"""
        # accessory:20054:
        # accessory:20055:
        assert t400504_x50(acc1=20054, acc2=20055, z1=9, z2=-10)
        """State 13"""
        return 0
    elif GetTalkListEntryResult() == 7:
        """State 14"""
        # accessory:20064:
        # accessory:20065:
        assert t400504_x50(acc1=20064, acc2=20065, z1=9, z2=-10)
        """State 15"""
        return 0
    elif GetTalkListEntryResult() == 8:
        """State 16"""
        # accessory:20074:
        # accessory:20075:
        assert t400504_x50(acc1=20074, acc2=20075, z1=9, z2=-10)
        """State 17"""
        return 0
    elif GetTalkListEntryResult() == 9:
        """State 18"""
        # accessory:20084:
        # accessory:20085:
        assert t400504_x50(acc1=20084, acc2=20085, z1=9, z2=-10)
        """State 19"""
        return 0
    elif GetTalkListEntryResult() == 10:
        """State 20"""
        # accessory:20094:
        # accessory:20095:
        assert t400504_x50(acc1=20094, acc2=20095, z1=9, z2=-10)
        """State 21"""
        return 0
    elif GetTalkListEntryResult() == 11:
        """State 22"""
        # accessory:20104:
        # accessory:20105:
        assert t400504_x50(acc1=20104, acc2=20105, z1=9, z2=-10)
        """State 23"""
        return 0
    elif GetTalkListEntryResult() == 12:
        """State 24"""
        # accessory:20114:
        # accessory:20115:
        assert t400504_x50(acc1=20114, acc2=20115, z1=9, z2=-10)
        """State 25"""
        return 0
    elif GetTalkListEntryResult() == 13:
        """State 26"""
        # accessory:20124:
        # accessory:20125:
        assert t400504_x50(acc1=20124, acc2=20125, z1=9, z2=-10)
        """State 27"""
        return 0
    elif GetTalkListEntryResult() == 14:
        """State 28"""
        # accessory:20134:
        # accessory:20135:
        assert t400504_x50(acc1=20134, acc2=20135, z1=9, z2=-10)
        """State 29"""
        return 0
    elif GetTalkListEntryResult() == 15:
        """State 30"""
        # accessory:20144:
        # accessory:20145:
        assert t400504_x50(acc1=20144, acc2=20145, z1=9, z2=-10)
        """State 31"""
        return 0
    elif GetTalkListEntryResult() == 16:
        """State 32"""
        # accessory:20154:
        # accessory:20155:
        assert t400504_x50(acc1=20154, acc2=20155, z1=9, z2=-10)
        """State 33"""
        return 0
    elif GetTalkListEntryResult() == 17:
        """State 34"""
        # accessory:20164:
        # accessory:20165:
        assert t400504_x50(acc1=20164, acc2=20165, z1=9, z2=-10)
        """State 35"""
        return 0
    elif GetTalkListEntryResult() == 18:
        """State 36"""
        # accessory:20174:
        # accessory:20175:
        assert t400504_x50(acc1=20174, acc2=20175, z1=9, z2=-10)
        """State 37"""
        return 0
    elif GetTalkListEntryResult() == 19:
        """State 38"""
        # accessory:20184:
        # accessory:20185:
        assert t400504_x50(acc1=20184, acc2=20185, z1=9, z2=-10)
        """State 39"""
        return 0
    elif GetTalkListEntryResult() == 20:
        """State 40"""
        # accessory:20194:
        # accessory:20195:
        assert t400504_x50(acc1=20194, acc2=20195, z1=9, z2=-10)
        """State 41"""
        return 0
    elif GetTalkListEntryResult() == 21:
        """State 42"""
        # accessory:20274:
        # accessory:20275:
        assert t400504_x50(acc1=20274, acc2=20275, z1=9, z2=-10)
        """State 43"""
        return 0
    elif GetTalkListEntryResult() == 22:
        """State 44"""
        # accessory:20284:
        # accessory:20285:
        assert t400504_x50(acc1=20284, acc2=20285, z1=9, z2=-10)
        """State 45"""
        return 0
    elif GetTalkListEntryResult() == 23:
        """State 46"""
        # accessory:20304:
        # accessory:20305:
        assert t400504_x50(acc1=20304, acc2=20305, z1=9, z2=-10)
        """State 47"""
        return 0
    elif GetTalkListEntryResult() == 24:
        """State 48"""
        # accessory:20334:
        # accessory:20335:
        assert t400504_x50(acc1=20334, acc2=20335, z1=9, z2=-10)
        """State 49"""
        return 0
    elif GetTalkListEntryResult() == 25:
        """State 50"""
        # accessory:20344:
        # accessory:20345:
        assert t400504_x50(acc1=20344, acc2=20345, z1=9, z2=-10)
        """State 51"""
        return 0
    elif GetTalkListEntryResult() == 26:
        """State 52"""
        # accessory:20354:
        # accessory:20355:
        assert t400504_x50(acc1=20354, acc2=20355, z1=9, z2=-10)
        """State 53"""
        return 0
    elif GetTalkListEntryResult() == 27:
        """State 54"""
        # accessory:20364:
        # accessory:20365:
        assert t400504_x50(acc1=20364, acc2=20365, z1=9, z2=-10)
        """State 55"""
        return 0
    elif GetTalkListEntryResult() == 28:
        """State 56"""
        # accessory:20374:
        # accessory:20375:
        assert t400504_x50(acc1=20374, acc2=20375, z1=9, z2=-10)
        """State 57"""
        return 0
    elif GetTalkListEntryResult() == 29:
        """State 58"""
        # accessory:20394:
        # accessory:20395:
        assert t400504_x50(acc1=20394, acc2=20395, z1=9, z2=-10)
        """State 59"""
        return 0
    elif GetTalkListEntryResult() == 30:
        """State 60"""
        # accessory:20404:
        # accessory:20405:
        assert t400504_x50(acc1=20404, acc2=20405, z1=9, z2=-10)
        """State 61"""
        return 0
    elif GetTalkListEntryResult() == 31:
        """State 62"""
        # accessory:20414:
        # accessory:20415:
        assert t400504_x50(acc1=20414, acc2=20415, z1=9, z2=-10)
        """State 63"""
        return 0
    elif GetTalkListEntryResult() == 32:
        """State 64"""
        # accessory:20434:
        # accessory:20435:
        assert t400504_x50(acc1=20434, acc2=20435, z1=9, z2=-10)
        """State 65"""
        return 0
    elif GetTalkListEntryResult() == 33:
        """State 66"""
        # accessory:20464:
        # accessory:20465:
        assert t400504_x50(acc1=20464, acc2=20465, z1=9, z2=-10)
        """State 67"""
        return 0
    elif GetTalkListEntryResult() == 34:
        """State 68"""
        # accessory:20474:
        # accessory:20475:
        assert t400504_x50(acc1=20474, acc2=20475, z1=9, z2=-10)
        """State 69"""
        return 0
    elif GetTalkListEntryResult() == 35:
        """State 70"""
        # accessory:20484:
        # accessory:20485:
        assert t400504_x50(acc1=20484, acc2=20485, z1=9, z2=-10)
        """State 71"""
        return 0
    elif GetTalkListEntryResult() == 36:
        """State 72"""
        # accessory:20494:
        # accessory:20495:
        assert t400504_x50(acc1=20494, acc2=20495, z1=9, z2=-10)
        """State 73"""
        return 0
    elif GetTalkListEntryResult() == 37:
        """State 74"""
        # accessory:20504:
        # accessory:20505:
        assert t400504_x50(acc1=20504, acc2=20505, z1=9, z2=-10)
        """State 75"""
        return 0
    elif GetTalkListEntryResult() == 38:
        """State 76"""
        # accessory:20514:
        # accessory:20515:
        assert t400504_x50(acc1=20514, acc2=20515, z1=9, z2=-10)
        """State 77"""
        return 0
    elif GetTalkListEntryResult() == 39:
        """State 78"""
        # accessory:20524:
        # accessory:20525:
        assert t400504_x50(acc1=20524, acc2=20525, z1=9, z2=-10)
        """State 79"""
        return 0
    elif GetTalkListEntryResult() == 40:
        """State 80"""
        # accessory:20544:
        # accessory:20545:
        assert t400504_x50(acc1=20544, acc2=20545, z1=9, z2=-10)
        """State 81"""
        return 0
    elif GetTalkListEntryResult() == 41:
        """State 82"""
        # accessory:20554:
        # accessory:20555:
        assert t400504_x50(acc1=20554, acc2=20555, z1=9, z2=-10)
        """State 83"""
        return 0
    elif GetTalkListEntryResult() == 42:
        """State 84"""
        # accessory:20594:
        # accessory:20595:
        assert t400504_x50(acc1=20594, acc2=20595, z1=9, z2=-10)
        """State 85"""
        return 0
    elif GetTalkListEntryResult() == 43:
        """State 86"""
        # accessory:20604:
        # accessory:20605:
        assert t400504_x50(acc1=20604, acc2=20605, z1=9, z2=-10)
        """State 87"""
        return 0
    elif GetTalkListEntryResult() == 44:
        """State 88"""
        # accessory:20614:
        # accessory:20615:
        assert t400504_x50(acc1=20614, acc2=20615, z1=9, z2=-10)
        """State 89"""
        return 0
    elif GetTalkListEntryResult() == 45:
        """State 90"""
        # accessory:20664:
        # accessory:20665:
        assert t400504_x50(acc1=20664, acc2=20665, z1=9, z2=-10)
        """State 91"""
        return 0
    elif GetTalkListEntryResult() == 46:
        """State 92"""
        # accessory:20674:
        # accessory:20675:
        assert t400504_x50(acc1=20674, acc2=20675, z1=9, z2=-10)
        """State 93"""
        return 0
    elif GetTalkListEntryResult() == 47:
        """State 94"""
        # accessory:20704:
        # accessory:20705:
        assert t400504_x50(acc1=20704, acc2=20705, z1=9, z2=-10)
        """State 95"""
        return 0
    elif GetTalkListEntryResult() == 48:
        """State 96"""
        # accessory:20714:
        # accessory:20715:
        assert t400504_x50(acc1=20714, acc2=20715, z1=9, z2=-10)
        """State 97"""
        return 0
    elif GetTalkListEntryResult() == 49:
        """State 98"""
        # accessory:20724:
        # accessory:20725:
        assert t400504_x50(acc1=20724, acc2=20725, z1=9, z2=-10)
        """State 99"""
        return 0
    elif GetTalkListEntryResult() == 50:
        """State 100"""
        # accessory:20754:
        # accessory:20755:
        assert t400504_x50(acc1=20754, acc2=20755, z1=9, z2=-10)
        """State 101"""
        return 0
    elif GetTalkListEntryResult() == 51:
        """State 102"""
        # accessory:20794:
        # accessory:20795:
        assert t400504_x50(acc1=20794, acc2=20795, z1=9, z2=-10)
        """State 103"""
        return 0
    elif GetTalkListEntryResult() == 52:
        """State 104"""
        assert t400504_x50(acc1=20834, acc2=20835, z1=9, z2=-10)
        """State 105"""
        return 0
    elif GetTalkListEntryResult() == 53:
        """State 106"""
        assert t400504_x50(acc1=21004, acc2=21005, z1=9, z2=-10)
        """State 107"""
        return 0
    elif GetTalkListEntryResult() == 54:
        """State 108"""
        assert t400504_x50(acc1=30014, acc2=30015, z1=9, z2=-10)
        """State 109"""
        return 0
    elif GetTalkListEntryResult() == 55:
        """State 110"""
        assert t400504_x50(acc1=30024, acc2=30025, z1=9, z2=-10)
        """State 111"""
        return 0
    elif GetTalkListEntryResult() == 56:
        """State 112"""
        assert t400504_x50(acc1=30054, acc2=30055, z1=9, z2=-10)
        """State 113"""
        return 0
    elif GetTalkListEntryResult() == 57:
        """State 114"""
        assert t400504_x50(acc1=30084, acc2=30085, z1=9, z2=-10)
        """State 115"""
        return 0
    elif GetTalkListEntryResult() == 58:
        """State 116"""
        assert t400504_x50(acc1=30174, acc2=30175, z1=9, z2=-10)
        """State 117"""
        return 0
    elif GetTalkListEntryResult() == 59:
        """State 118"""
        assert t400504_x50(acc1=30184, acc2=30185, z1=9, z2=-10)
        """State 119"""
        return 0
    elif GetTalkListEntryResult() == 60:
        """State 120"""
        assert t400504_x50(acc1=30194, acc2=30195, z1=9, z2=-10)
        """State 121"""
        return 0
    elif GetTalkListEntryResult() == 61:
        """State 122"""
        assert t400504_x50(acc1=30204, acc2=30205, z1=9, z2=-10)
        """State 123"""
        return 0
    elif GetTalkListEntryResult() == 62:
        """State 124"""
        assert t400504_x50(acc1=30214, acc2=30215, z1=9, z2=-10)
        """State 125"""
        return 0
    elif GetTalkListEntryResult() == 63:
        """State 126"""
        assert t400504_x50(acc1=30334, acc2=30335, z1=9, z2=-10)
        """State 127"""
        return 0
    elif GetTalkListEntryResult() == 64:
        """State 128"""
        assert t400504_x50(acc1=30344, acc2=30345, z1=9, z2=-10)
        """State 129"""
        return 0
    elif GetTalkListEntryResult() == 65:
        """State 130"""
        assert t400504_x50(acc1=30354, acc2=30355, z1=9, z2=-10)
        """State 131"""
        return 0
    elif GetTalkListEntryResult() == 66:
        """State 132"""
        assert t400504_x50(acc1=30364, acc2=30365, z1=9, z2=-10)
        """State 133"""
        return 0
    elif GetTalkListEntryResult() == 67:
        """State 134"""
        assert t400504_x50(acc1=30374, acc2=30375, z1=9, z2=-10)
        """State 135"""
        return 0
    elif GetTalkListEntryResult() == 68:
        """State 136"""
        assert t400504_x50(acc1=30394, acc2=30395, z1=9, z2=-10)
        """State 137"""
        return 0
    elif GetTalkListEntryResult() == 69:
        """State 138"""
        assert t400504_x50(acc1=30404, acc2=30405, z1=9, z2=-10)
        """State 139"""
        return 0
    elif GetTalkListEntryResult() == 70:
        """State 140"""
        assert t400504_x50(acc1=30414, acc2=30415, z1=9, z2=-10)
        """State 141"""
        return 0
    elif GetTalkListEntryResult() == 71:
        """State 142"""
        assert t400504_x50(acc1=30424, acc2=30425, z1=9, z2=-10)
        """State 143"""
        return 0
    elif GetTalkListEntryResult() == 72:
        """State 144"""
        assert t400504_x50(acc1=30434, acc2=30435, z1=9, z2=-10)
        """State 145"""
        return 0
    elif GetTalkListEntryResult() == 73:
        """State 146"""
        assert t400504_x50(acc1=30454, acc2=30455, z1=9, z2=-10)
        """State 147"""
        return 0
    elif GetTalkListEntryResult() == 74:
        """State 148"""
        assert t400504_x50(acc1=30504, acc2=30505, z1=9, z2=-10)
        """State 149"""
        return 0
    elif GetTalkListEntryResult() == 75:
        """State 150"""
        assert t400504_x50(acc1=30654, acc2=30655, z1=9, z2=-10)
        """State 151"""
        return 0
    elif GetTalkListEntryResult() == 76:
        """State 152"""
        assert t400504_x50(acc1=30664, acc2=30665, z1=9, z2=-10)
        """State 153"""
        return 0
    elif GetTalkListEntryResult() == 77:
        """State 154"""
        assert t400504_x50(acc1=30674, acc2=30675, z1=9, z2=-10)
        """State 155"""
        return 0
    elif GetTalkListEntryResult() == 78:
        """State 156"""
        assert t400504_x50(acc1=30684, acc2=30685, z1=9, z2=-10)
        """State 157"""
        return 0
    elif GetTalkListEntryResult() == 79:
        """State 158"""
        assert t400504_x50(acc1=30694, acc2=30695, z1=9, z2=-10)
        """State 159"""
        return 0
    elif GetTalkListEntryResult() == 80:
        """State 160"""
        assert t400504_x50(acc1=30704, acc2=30705, z1=9, z2=-10)
        """State 161"""
        return 0
    elif GetTalkListEntryResult() == 81:
        """State 162"""
        assert t400504_x50(acc1=30804, acc2=30805, z1=9, z2=-10)
        """State 163"""
        return 0
    elif GetTalkListEntryResult() == 82:
        """State 164"""
        assert t400504_x50(acc1=30894, acc2=30895, z1=9, z2=-10)
        """State 165"""
        return 0
    elif GetTalkListEntryResult() == 85:
        """State 166"""
        assert t400504_x50(acc1=30934, acc2=30935, z1=9, z2=-10)
        """State 167"""
        return 0
    elif GetTalkListEntryResult() == 86:
        """State 168"""
        assert t400504_x50(acc1=30944, acc2=30945, z1=9, z2=-10)
        """State 169"""
        return 0
    elif GetTalkListEntryResult() == 87:
        """State 170"""
        assert t400504_x50(acc1=30954, acc2=30955, z1=9, z2=-10)
        """State 171"""
        return 0
    elif GetTalkListEntryResult() == 90:
        """State 172"""
        assert t400504_x50(acc1=30874, acc2=30875, z1=9, z2=-10)
        """State 173"""
        return 0
    elif GetTalkListEntryResult() == 91:
        """State 174"""
        assert t400504_x50(acc1=30884, acc2=30885, z1=9, z2=-10)
        """State 175"""
        return 0
    elif GetTalkListEntryResult() == 92:
        """State 176"""
        assert t400504_x50(acc1=30904, acc2=30905, z1=9, z2=-10)
        """State 177"""
        return 0
    elif GetTalkListEntryResult() == 93:
        """State 178"""
        assert t400504_x50(acc1=31404, acc2=31405, z1=9, z2=-10)
        """State 179"""
        return 0
    elif GetTalkListEntryResult() == 94:
        """State 180"""
        assert t400504_x50(acc1=31304, acc2=31305, z1=9, z2=-10)
        """State 181"""
        return 0
    elif GetTalkListEntryResult() == 95:
        """State 182"""
        assert t400504_x50(acc1=31084, acc2=31085, z1=9, z2=-10)
        """State 183"""
        return 0
    elif GetTalkListEntryResult() == 96:
        """State 184"""
        # accessory:20384:
        # accessory:20385:
        assert t400504_x50(acc1=20384, acc2=20385, z1=9, z2=-10)
        """State 185"""
        return 0
    elif GetTalkListEntryResult() == 97:
        """State 186"""
        assert t400504_x50(acc1=31204, acc2=31205, z1=9, z2=-10)
        """State 187"""
        return 0
    elif GetTalkListEntryResult() == 98:
        """State 188"""
        assert t400504_x50(acc1=30804, acc2=30805, z1=9, z2=-10)
        """State 189"""
        return 0
    elif GetTalkListEntryResult() == 99:
        """State 190"""
        # accessory:20454:
        # accessory:20455:
        assert t400504_x50(acc1=20454, acc2=20455, z1=9, z2=-10)
        """State 191"""
        return 0
    elif GetTalkListEntryResult() == 100:
        """State 192"""
        assert t400504_x50(acc1=30094, acc2=30095, z1=9, z2=-10)
        """State 193"""
        return 0
    elif GetTalkListEntryResult() == 101:
        """State 194"""
        assert t400504_x50(acc1=30844, acc2=30845, z1=9, z2=-10)
        """State 195"""
        return 0
    elif GetTalkListEntryResult() == 102:
        """State 196"""
        assert t400504_x50(acc1=30994, acc2=30995, z1=9, z2=-10)
        """State 197"""
        return 0
    elif GetTalkListEntryResult() == 103:
        """State 198"""
        assert t400504_x50(acc1=30044, acc2=30045, z1=9, z2=-10)
        """State 199"""
        return 0
    elif GetTalkListEntryResult() == 104:
        """State 200"""
        assert t400504_x50(acc1=31504, acc2=31505, z1=9, z2=-10)
        """State 201"""
        return 0
    elif GetTalkListEntryResult() == 105:
        """State 202"""
        assert t400504_x50(acc1=31604, acc2=31605, z1=9, z2=-10)
        """State 203"""
        return 0
    elif GetTalkListEntryResult() == 106:
        """State 204"""
        assert t400504_x50(acc1=31704, acc2=31705, z1=9, z2=-10)
        """State 205"""
        return 0
    elif GetTalkListEntryResult() == 107:
        """State 206"""
        assert t400504_x50(acc1=31804, acc2=31805, z1=9, z2=-10)
        """State 207"""
        return 0
    elif GetTalkListEntryResult() == 108:
        """State 208"""
        assert t400504_x50(acc1=31904, acc2=31905, z1=9, z2=-10)
        """State 209"""
        return 0
    elif GetTalkListEntryResult() == 109:
        """State 210"""
        assert t400504_x50(acc1=32004, acc2=32005, z1=9, z2=-10)
        """State 211"""
        return 0
    elif GetTalkListEntryResult() == 110:
        """State 212"""
        assert t400504_x50(acc1=32104, acc2=32105, z1=9, z2=-10)
        """State 213"""
        return 0
    elif GetTalkListEntryResult() == 111:
        """State 214"""
        assert t400504_x50(acc1=32204, acc2=32205, z1=9, z2=-10)
        """State 215"""
        return 0
    elif GetTalkListEntryResult() == 112:
        """State 216"""
        assert t400504_x50(acc1=32304, acc2=32305, z1=9, z2=-10)
        """State 217"""
        return 0
    elif not (CheckSpecificPersonMenuIsOpen(-1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0)):
        """State 218"""
        return 0

def t400504_x50(acc1=_, acc2=_, z1=_, z2=_):
    """State 0"""
    call = t400504_x51(action2=99015010)
    if call.Get() == 0:
        """State 1"""
        if ComparePlayerInventoryNumber(ItemType.Goods, 901, CompareType.Less, z1, False):
            """State 2"""
            assert t400504_x52(action1=99015012)
        else:
            """State 3"""
            PlayerEquipmentQuantityChange(ItemType.Goods, 901, z2)
            PlayerEquipmentQuantityChange(ItemType.Accessory, acc1, -1)
            PlayerEquipmentQuantityChange(ItemType.Accessory, acc2, 1)
            assert t400504_x52(action1=99015013)
    elif call.Get() == 1:
        pass
    """State 4"""
    return 0

def t400504_x51(action2=99015010):
    """State 0,1"""
    OpenGenericDialog(DialogBoxType.CenterBottom2, action2, DialogResult.Leave, DialogBoxStyle.Unk, 2)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    if GetGenericDialogButtonResult() == DialogResult.Left:
        """State 3"""
        return 0
    else:
        """State 4"""
        return 1

def t400504_x52(action1=_):
    """State 0,1"""
    OpenGenericDialog(DialogBoxType.CenterBottom1, action1, DialogResult.Left, DialogBoxStyle.OrnateNoOptions, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0

