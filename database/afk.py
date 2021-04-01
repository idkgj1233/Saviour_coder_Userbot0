# Copyright (C) 2020-2021 by DevsExpo@Github, < https://github.com/DevsExpo >.
#
# This file is part of < https://github.com/DevsExpo/FridayUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevsExpo/blob/master/LICENSE >
#
# All rights reserved.

from database import db_x

afk = db_x["AFK"]

def go_afk(time, reason=""):
    
    midhun = afk.find_one({"_id": "AFK"})
    if midhun:
        afk.update_one({"_id": "AFK"}, {"$set": {"time": time, "reason": reason}})
    else:
        afk.insert_one({"_id": "AFK", "time": time, "reason": reason})

def no_afk():
    midhun = afk.find_one({"_id": "AFK"})
    if midhun:
        afk.delete_one({"_id": "AFK"})
    
def check_afk():
    midhun = afk.find_one({"_id": "AFK"})
    if midhun:
        return midhun
    else:
        return False
