# -*- encoding=utf8 -*-
__author__ = "dgino"

from airtest.core.api import *

from airtest.report.report import *

from datetime import datetime as DT

from airtest.core.api import using

import os

ST.SAVE_IMAGE = False
ST.LOG_DIR = ST.PROJECT_ROOT + '//log//'
gfolder = ST.PROJECT_ROOT + '//src//'

auto_setup(__file__)

print("test 2253")

# in normal: 1
firstacc = 1

def touchifexs(pic):
    coords = False
    if pic:
        coords = exists(pic)
        if (coords):
            touch((coords[0],coords[1]))
    return coords

def find_all_v2(v, conf = 0.9):
    items = find_all(v)
    filt_items = []
    try:
        for i in items:
            if (i['confidence']>=conf):
                filt_items.append(i)
    except:
        pass
    return filt_items

def find_v3(v):
    coords = False
    items = find_all(v)
    try:
        items.sort(key = lambda x: x['confidence'], reverse=True)
        coords = items[0]['result']
    except:
        pass
    return coords

def touchifexsFast(v):
    coords = False
    if v:
        coords = find_v3(v)
        if (coords):
            touch((coords[0],coords[1]))
    return coords

def stopgame():
    stop_app('com.diandian.gog')
    sleep(3)
    return

def restartgame():
    stop_app('com.diandian.gog')
    start_app('com.diandian.gog')
    sleep(50)
    skipstart3()
    return

def skipstart3():
    count = 0
    while (not (find_v3(Template(r"tpl1640808479835.png", record_pos=(-0.048, 0.029), resolution=(2280, 1080))) or find_v3(Template(r"tpl1640810146847.png", record_pos=(-0.065, 0.033), resolution=(2280, 1080))))):
        count += 1
        if count > 10:
            raise
        touchifexsFast(Template(r"tpl1611637985647.png", record_pos=(0.371, -0.179), resolution=(2280, 1080)))
        touchifexsFast(Template(r"tpl1611266590692.png", record_pos=(0.357, -0.177), resolution=(2280, 1080)))
        touchifexsFast(Template(r"tpl1640810005090.png", record_pos=(0.479, -0.217), resolution=(2280, 1080)))
        touchifexs(Template(r"tpl1615920304884.png", record_pos=(0.371, -0.178), resolution=(2280, 1080)))
        if (count % 2 == 0):
            keyevent("BACK")
        sleep(3)
    return

def selectAcc(num, maxnum = 21):
    touch((175,90))
    sleep(10)
    touch(Template(r"tpl1640809777914.png", record_pos=(0.448, 0.132), resolution=(2280, 1080)))
    touch(Template(r"tpl1611265104176.png", record_pos=(-0.057, -0.052), resolution=(2280, 1080)))
    sleep(4)
    touch(Template(r"tpl1611265119973.png", record_pos=(0.021, 0.071), resolution=(2280, 1080)))
    sleep(2)
    touch(Template(r"tpl1611265160150.png", record_pos=(0.023, -0.014), resolution=(2280, 1080)))
    sleep(3)
    wait(Template(r"tpl1611265200494.png", record_pos=(0.009, -0.138), resolution=(2280, 1080)))
    for i in range(0,num):
        swipe ((1128,677),(1120,477),duration=1)
    if (num >= maxnum-1):
        touch((907, 625))
    else:
        touch((907, 425))
    sleep(8)
    wait(Template(r"tpl1611267318849.png", record_pos=(0.256, -0.167), resolution=(2280, 1080)), timeout = 10)
    coords = exists(Template(r"tpl1611267318849.png", record_pos=(0.256, -0.167), resolution=(2280, 1080)))
    if (coords):
        touch((coords[0],coords[1]))
    sleep(2)
    coords = exists(Template(r"tpl1611269115634.png", record_pos=(0.449, -0.216), resolution=(2280, 1080)))
    if (coords):
        touch((coords[0],coords[1]))
    else:
        sleep(30)
    return

def snapshotWithName(prefix = ""):
    if prefix:
        prefix + '_'
    fullname = gfolder + prefix + timestamp() + '.png'
    snapshot(filename=fullname, msg='test', quality=95)
    return

def timestamp():
    dt_fmt = '%Y-%m-%d-%H-%M-%S-%f'
    return DT.now().strftime(dt_fmt)

def snapshotProfile():
    touch((175,90))
    sleep(4)
    snapshotWithName()
    keyevent("BACK")
    return

def snapshotRes():
    touch(Template(r"tpl1640816040662.png", record_pos=(0.307, 0.211), resolution=(2280, 1080)))
    sleep(10)
    touch(Template(r"tpl1640815942648.png", record_pos=(-0.364, -0.088), resolution=(2280, 1080)))
    touchifexs(Template(r"tpl1640816190560.png", record_pos=(0.267, -0.14), resolution=(2280, 1080)))
    swipe ((1027,807),(1010,850),duration=0.3)
    snapshotWithName()
    swipe ((1027,807),(1010,259),duration=0.3)
    sleep(2)
    snapshotWithName()
    keyevent("BACK")
    return

def shops():
    goToshops()
    try:
        shopTower()
        shopCatacombs()
    except Exception as e:
        print('!!!')
        print (e)
        log(e,desc='error')
        snapshotWithName(prefix = '..//errors//err')
        restartgame()
    outshops()
    return

def goToshops():
    for i in range(0,4):
        swipe((1870,229), (640, 713), duration=0.8)
        sleep(1)
    sleep(4)
    if not(touchifexs(Template(r"tpl1611162996513.png", record_pos=(0.079, -0.039), resolution=(2280, 1080)))):
        touchifexs(Template(r"tpl1640810339825.png", record_pos=(-0.117, -0.027), resolution=(2280, 1080)))
    
    sleep(2)
    touch(Template(r"tpl1612450579154.png", record_pos=(0.385, -0.212), resolution=(2280, 1080)))
    return

def outshops():
    sleep(3)
    touchifexs(Template(r"tpl1611264450097.png", record_pos=(0.457, -0.222), resolution=(2280, 1080)))
    sleep(8)
    return

def shopTower():
    icons = [Template(r"tpl1612451447833.png", record_pos=(-0.271, -0.081), resolution=(2280, 1080)),Template(r"tpl1612451463016.png", record_pos=(-0.271, 0.029), resolution=(2280, 1080))]
    touchifexs(Template(r"tpl1612450773468.png", record_pos=(0.056, -0.164), resolution=(2280, 1080)))
    sleep(2)
    for icon in icons:
        count = 0
        icon_coords = find_all_v2(icon, conf = 0.85)
        while (not icon_coords):
            swipe((1068,640), (1088,368), duration=1)
            count+=1
            sleep(1)
            icon_coords = find_all_v2(icon, conf = 0.85)
            if (count > 9):
                raise
        if count > 0:
            swipe((1072,884), (1064,764), duration=1)
            sleep(1)
            icon_coords = find_all_v2(icon, conf = 0.85)
        for ic in icon_coords:
            touch((ic['result'][0] + 246, ic['result'][1] + 90))
            sleep(2)
            if find_all_v2(Template(r"tpl1612519639784.png", record_pos=(0.237, -0.159), resolution=(2280, 1080))):
                touchifexs(Template(r"tpl1615715403122.png", record_pos=(-0.008, 0.118), resolution=(2280, 1080)))
                touchifexs(Template(r"tpl1612519639784.png", record_pos=(0.237, -0.159), resolution=(2280, 1080)))
    return

def shopCatacombs():
    touch(Template(r"tpl1612521841953.png", record_pos=(-0.26, -0.162), resolution=(2280, 1080)))
    sleep(5)
    icons = [Template(r"tpl1612522299729.png", record_pos=(-0.274, -0.084), resolution=(2280, 1080)), Template(r"tpl1612522313025.png", record_pos=(0.031, -0.088), resolution=(2280, 1080)),Template(r"tpl1612522322583.png", record_pos=(-0.271, 0.025), resolution=(2280, 1080)),Template(r"tpl1612522332413.png", record_pos=(0.03, 0.027), resolution=(2280, 1080))]
    for icon in icons:
        try:
            count = 0
            icon_coords = find_all_v2(icon, conf = 0.85)
            touch((icon_coords[0]['result'][0] + 246, icon_coords[0]['result'][1] + 90))
            sleep(1)
            if (find_all_v2(Template(r"tpl1612523043583.png", record_pos=(0.233, -0.159), resolution=(2280, 1080)))):
                touchifexs(Template(r"tpl1615715481175.png", record_pos=(0.011, 0.119), resolution=(2280, 1080)))
                touchifexs(Template(r"tpl1612523043583.png", record_pos=(0.233, -0.159), resolution=(2280, 1080)))
                sleep(4)
        except:
            pass
    return

def findTower():
    for i in range(0,4):
        swipe((1870,229), (640, 713), duration=0.8)
        sleep(1)
    return

def tower(doubleFlag = False):
    resetFlag = False
    if not(touchifexs(Template(r"tpl1611162996513.png", record_pos=(0.079, -0.039), resolution=(2280, 1080)))):
        touchifexs(Template(r"tpl1640810339825.png", record_pos=(-0.117, -0.027), resolution=(2280, 1080)))
    sleep(3)
    touchifexs(Template(r"tpl1611163232548.png", record_pos=(0.026, 0.197), resolution=(2280, 1080)))
    sleep(1)
    touch(Template(r"tpl1611163302845.png", record_pos=(-0.003, -0.046), resolution=(2280, 1080)))
    sleep(2)
    if exists(Template(r"tpl1611163344415.png", record_pos=(0.063, -0.011), resolution=(2280, 1080))):
        touch(Template(r"tpl1611163344415.png", record_pos=(0.063, -0.011), resolution=(2280, 1080)))
        sleep(3)
        if (exists(Template(r"tpl1640811198317.png", record_pos=(0.111, 0.196), resolution=(2280, 1080)))):
            if (exists(Template(r"tpl1613159044263.png", record_pos=(0.204, -0.123), resolution=(2280, 1080)))):
                snapshotWithName(prefix = '..//errors//err')
                raise
            touch(Template(r"tpl1640811198317.png", record_pos=(0.111, 0.196), resolution=(2280, 1080)))
            touch(Template(r"tpl1640811310154.png", record_pos=(0.105, 0.196), resolution=(2280, 1080)))
            touch(find_v3(Template(r"tpl1611163548726.png", record_pos=(0.283, 0.105), resolution=(2280, 1080))))
            touchifexs(Template(r"tpl1611163636164.png", record_pos=(-0.224, 0.206), resolution=(2280, 1080)))
            touch(Template(r"tpl1640811397065.png", record_pos=(0.247, 0.196), resolution=(2280, 1080)))
            touchifexs(Template(r"tpl1640810005090.png", record_pos=(0.479, -0.217), resolution=(2280, 1080)))
            touchifexs(Template(r"tpl1640810005090.png", record_pos=(0.479, -0.217), resolution=(2280, 1080)))
        else:
            resetFlag = True
    else:
        resetFlag = True
    if not doubleFlag and resetFlag:
        rebootTower()
    if not doubleFlag:
        touch(Template(r"tpl1611212808409.png", record_pos=(0.456, 0.196), resolution=(2280, 1080)))
        sleep(2)
        touch(Template(r"tpl1611212857909.png", record_pos=(0.024, 0.006), resolution=(2280, 1080)))
    return

def rebootTower():
    touch(Template(r"tpl1611212808409.png", record_pos=(0.456, 0.196), resolution=(2280, 1080)))
    touch(Template(r"tpl1613156540673.png", record_pos=(0.024, 0.069), resolution=(2280, 1080)))
    touch(Template(r"tpl1613156629976.png", record_pos=(0.126, 0.051), resolution=(2280, 1080)))
    sleep(14)
    touch(Template(r"tpl1613156666165.png", record_pos=(0.023, 0.194), resolution=(2280, 1080)))
    touch(Template(r"tpl1613156686490.png", record_pos=(0.131, 0.1), resolution=(2280, 1080)))
    sleep(4)
    touch(Template(r"tpl1613156729080.png", record_pos=(0.125, 0.12), resolution=(2280, 1080)))
    touch(Template(r"tpl1613156758117.png", record_pos=(0.125, 0.046), resolution=(2280, 1080)))
    sleep(3)
    tower(doubleFlag = True)
    return

def heal():
    sleep(7)
    findTower()
    count = 0
    hospital_coords = find_v3(Template(r"tpl1612542776083.png", record_pos=(0.202, -0.05), resolution=(2280, 1080)))
    while (not hospital_coords):
        count += 1
        swipe((1834,635),(1730,288), duration = 1)
        sleep(1.5)
        hospital_coords = find_v3(Template(r"tpl1612542776083.png", record_pos=(0.202, -0.05), resolution=(2280, 1080)))
        if count > 9:
            raise
    swipe((2031,709),(2059,310), duration = 1)
    resCollectSimple()
    sleep(4)
    hospital_coords = find_v3(Template(r"tpl1612542776083.png", record_pos=(0.202, -0.05), resolution=(2280, 1080)))
    if (hospital_coords):
        touch(hospital_coords)
        sleep(2)
        touch(Template(r"tpl1612540615967.png", record_pos=(0.003, 0.064), resolution=(2280, 1080)))
        touch(Template(r"tpl1612541129475.png", record_pos=(0.293, 0.161), resolution=(2280, 1080)))
        sleep(3)
        touchifexsFast(Template(r"tpl1612541149616.png", record_pos=(0.454, -0.216), resolution=(2280, 1080)))
    sleep(3)
    touchifexsFast(Template(r"tpl1612541149616.png", record_pos=(0.454, -0.216), resolution=(2280, 1080)))
    return

def towerNheal():
    healflag = False
    findTower()
    try:
        tower()
    except:
        touchifexs(Template(r"tpl1640810005090.png", record_pos=(0.479, -0.217), resolution=(2280, 1080)))
        touch(Template(r"tpl1611212808409.png", record_pos=(0.456, 0.196), resolution=(2280, 1080)))
        sleep(2)
        touch(Template(r"tpl1611212857909.png", record_pos=(0.024, 0.006), resolution=(2280, 1080)))
        healflag = True
    if healflag:
        heal()
    sleep(10)
    return

def resCollectSimple():
    items = [Template(r"tpl1613154900986.png", record_pos=(-0.101, 0.021), resolution=(2280, 1080)),Template(r"tpl1613154931038.png", record_pos=(-0.18, -0.02), resolution=(2280, 1080)),Template(r"tpl1613155046486.png", record_pos=(0.216, -0.03), resolution=(2280, 1080)),Template(r"tpl1613154868730.png", record_pos=(0.136, -0.023), resolution=(2280, 1080))]
    coords = []
    for item in items:
        coords += find_all_v2(item, conf = 0.8)
    for coord in coords:
        touch(coord['result'], duration = 0.3)
        sleep(0.4)
    return

def findCatacombs():
    for i in range(0,4):
        swipe((640, 713), (1870,229), duration=0.8)
        sleep(1)
    swipe((1361,589), (1154,836), duration=0.8)
    sleep(1)
    return

def catacombs():
    if (not touchifexs(Template(r"tpl1611212996129.png", record_pos=(-0.086, -0.021), resolution=(2280, 1080)))):
        touchifexs(Template(r"tpl1640814986519.png", record_pos=(-0.014, 0.027), resolution=(2280, 1080)))
    sleep(2)
    touch(Template(r"tpl1640812569191.png", record_pos=(0.039, 0.037), resolution=(2280, 1080)))
    sleep(4)
    touch(Template(r"tpl1611213249374.png", record_pos=(-0.408, -0.001), resolution=(2280, 1080)))
    catacombs = (Template(r"tpl1611213282817.png", record_pos=(0.246, -0.009), resolution=(2280, 1080)),Template(r"tpl1611213777488.png", record_pos=(0.094, -0.1), resolution=(2280, 1080)),Template(r"tpl1611264724209.png", record_pos=(-0.023, 0.115), resolution=(2280, 1080)),Template(r"tpl1611264739032.png", record_pos=(-0.203, 0.106), resolution=(2280, 1080)))

    for cat in catacombs:
        touch(cat)
        touch(Template(r"tpl1611213331053.png", record_pos=(0.134, 0.154), resolution=(2280, 1080)))
        sleep(1)
        if (exists(Template(r"tpl1611213463585.png", record_pos=(0.025, 0.173), resolution=(2280, 1080)))):
            touch(Template(r"tpl1611213463585.png", record_pos=(0.025, 0.173), resolution=(2280, 1080)))
        sleep(4)
        touchifexs(Template(r"tpl1616006004951.png", record_pos=(0.308, -0.17), resolution=(2280, 1080)))
    sleep(3)
    coords = exists(Template(r"tpl1612525323388.png", record_pos=(0.459, -0.218), resolution=(2280, 1080)))
    if (coords):
        touch((coords[0],coords[1]))
    return

def go():
    restartgame()
    for i in range(firstacc,21):
        try:
            selectAcc(i)
            skipstart3()
            snapshotProfile()
            snapshotRes()
        except Exception as e:
            print('!!!')
            print (e)
            snapshotWithName(prefix = '..//errors//err')
            restartgame()
        try:
            towerNheal()
        except Exception as e:
            print('!!!')
            print (e)
            snapshotWithName(prefix = '..//errors//err')
            restartgame()
        try:
            findCatacombs()
            catacombs()
        except Exception as e:
            print('!!!')
            print (e)
            log(e,desc='error')
            snapshotWithName(prefix = '..//errors//err')
            restartgame()
        try:
            shops()
            snapshotRes()
        except Exception as e:
            print('!!!')
            print (e)
            log(e,desc='error')
            snapshotWithName(prefix = '..//errors//err')
            restartgame()
    stopgame()
    return

def common_go():
    go()
    #os.system('shutdown -s')
    return

ST.LOG_FILE = "log_" + timestamp() + ".txt"
set_logdir(ST.LOG_DIR)

# skipstart3()

common_go()
# selectAcc(3)

# towerNheal()

# heal()
# resCollectSimple()
# tower()

# findCatacombs()
# catacombs()

# shops()
# snapshotRes()

# save current account number
