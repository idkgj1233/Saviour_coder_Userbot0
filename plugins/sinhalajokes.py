"""
For SL"""

import os
import asyncio
import random
from asyncio import sleep

from  fridaybot import CMD_HELP, bot

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
IS_ENABLED = os.environ.get("SINHALA_JOKES",None)
if IS_ENABLED == "True":
    RUNSTRINGS = (
        "💔 මල්ලියෝ!! ම්ං අර දෙන්නෙක්ට ආදරේ කරේ නෑනේ සුදු මල්ලියෝ!! 💔",
        "❤ ආදලෙයි 150GB ක්!! ❤",
        "ඕයි...! පෙට්ටිය කැඩුවනම් දැන් ලමය බාරගනින්!!",
        "තමුසෙ පිස්සෙක්නෙ ඕයි!",
        "මොනාද හුත්තෝ බලන්නේ...??",
        "කවුරුන් කෙසේ කීවද ඵරුස වචන භාවිතය ඔබේ අරක පණ නැති කරවයි!!",
        "හායි!! කෝමද පැටියෝ ❣❣",
        "මැරිලත් පැය හතරක් ආදරෙයි.. අම්මපා",
        "ටෞකන්ඩ මූ යකෝ!!",
        "ඔයා අදත් මට අර යෝගට් පානය දෙනවද...?",
        "චූ කරල නිදාගනින් අයියේ...",
        "ඔයා හරි සෝයි අනේ.. සෝ කියුට්... 😋",
        "අපි දෙන්න පැනල යමු.. හාද?? . ",
        "පල යන්න වේසාවෝ!!",
        "💔 මල්ලියෝ!! ම්ං අර දෙන්නෙක්ට ආදරේ කරේ නෑනේ සුදු මල්ලියෝ!! 💔",
        "අඩ්ඩේහ්..! මේ මොකද කරන්නේ??",
        "පොඩිකාලෙ බිව්වෙ පොල්කිරිද මල්ලී 🤑",
        "සීනි කන්න ආපු කූඹියො නෙමෙයි සීනි බෝතලේ ඇරපු ඔයයි වැරදි..",
        "කවුරු කොහොම් කිව්වත් \nකොත්තු කෑවොත් බඩ යන එක යනවමයි!",
        "ආදරෙයි.. මැණික ❤❤",
        "❤ ආදලෙයි 250GB ක්!! ❤",
        "හදුන්වාදෙන වැඩි දිගකින් යුත් fens.. \nභාවිත කර බලා වෙනස හඳුනාගන්න!",
        "ඔයාට suprise එකක් තියෙයි.. /kickme කියල ගහල බලන්නකෝ 😂",
        "ට්‍රැක්ටරය පැදවීමට මාගේ ඡායාරූප භාවිත කිරීමෙන් වලකින්න ",
        "ඔයාට suprise එකක් තියෙයි.. /kickme කියල ගහල බලන්නකෝ 😂",
        "මූ හුත්තෝ..",
        "මොන හුයන්නක්ද මේ",
        "පෝන් එක හිරවෙනවාද?? ගලක්මත තබා හොඳින් තලන්න නිසැක ප්‍රතිඵල",
        "ටොයිලට් එකේ ඉද්දි හෙඩ්සෙට් එක ගහන් සින්දු අහන්න එපා ඕයි...",
        "බලු කූඩුව ඇරියෙ මොකාද යකෝ!!",
        "බය තරහ ඇති කරවයි. තරහ වයිරය උපදවයි. වරිරය පසුතැවීම ඇති කරයි. ඔබ බයෙන් ජීවත්වන තුරු ලංකාවේ බඩු මිල පහත නොයයි",
        "රට්ටු හිනස්සන්න එපා මල්ලී.",
        "හදිසි අවස්තාවකදී ගිලන්රථයක් ගෙන්වා ගැනීමට 1990 අමතන්න",
        "අපේ ගෲප් එකත් එක්ක අදම සෙට් වෙන්න t.me/InfinityJE ❤",
        "ඔයාට කොච්චර සල්ලි තිබුනත් කොච්චර බලය තිබුනත් කොත්තු කෑවොත් බඩ යන එක නවත්තන්න ඔයාට බෑ 🌮🌮.",
        "💔 මල්ලියෝ!! ම්ං අර දෙන්නෙක්ට ආදරේ කරේ නෑනේ සුදු මල්ලියෝ!! 💔",
        "ටෞකන්ඩ මූ යකෝ!!!",
        "කවුරුන් කෙසේ කීවද ඵරුස වචන භාවිතය ඔබේ අරක පණ නැති කරවයි!",
        "පොඩිකාලෙ බිව්වෙ පොල්කිරිද මල්ලී 🤑",
        "කවුරු කොහොම් කිව්වත් \nකොත්තු කෑවොත් බඩ යන එක යනවමයි!",
        "රට්ටු හිනස්සන්න එපා මල්ලී.",
        "ආදරෙයි.. මැණික ❤❤",
        "💔 මල්ලියෝ!! ම්ං අර දෙන්නෙක්ට ආදරේ කරේ නෑනේ සුදු මල්ලියෝ!! 💔",
    )


    @bot.on(admin_cmd(pattern=r"\.(.*)", outgoing=True))
    async def _(event):

        if event.fwd_from:

            return

        animation_interval = 0.1

        animation_ttl = range(0, 101)

        input_str = event.pattern_match.group(1)

        if input_str == "fuuk":

            await event.edit(input_str)

            animation_chars = ["👉       ✊️", "👉     ✊️", "👉  ✊️", "👉✊️💦"]

            for i in animation_ttl:

                await asyncio.sleep(animation_interval)

                await event.edit(animation_chars[i % 4])


    @bot.on(admin_cmd(pattern=r"(.*)", outgoing=True))
    async def _(event):

        if event.fwd_from:

            return

        animation_interval = 0.2

        animation_ttl = range(0, 101)

        input_str = event.pattern_match.group(1)

        if input_str == "sux":

            await event.edit(input_str)

            animation_chars = ["🤵       👰", "🤵     👰", "🤵  👰", "🤵👼👰"]

            for i in animation_ttl:

                await asyncio.sleep(animation_interval)

                await event.edit(animation_chars[i % 4])


    ""


    @bot.on(admin_cmd(pattern=r"(.*)", outgoing=True))
    async def _(event):

        if event.fwd_from:

            return

        animation_interval = 0.2

        animation_ttl = range(0, 101)

        input_str = event.pattern_match.group(1)

        if input_str == "kiss":

            await event.edit(input_str)

            animation_chars = ["🤵       👰", "🤵     👰", "🤵  👰", "🤵💋👰"]

            for i in animation_ttl:

                await asyncio.sleep(animation_interval)

                await event.edit(animation_chars[i % 4])


    @bot.on(admin_cmd(pattern="kp$"))
    @bot.on(sudo_cmd(pattern="kp$", allow_sudo=True))
    async def gn(event):
        if event.fwd_from:
            return
        await edit_or_reply(
            event,
            "** කැරි පකයා **",
        )





    @bot.on(admin_cmd(pattern="slo$"))
    @bot.on(sudo_cmd(pattern="slo$", allow_sudo=True))
    async def gn(event):
        if event.fwd_from:
            return
        await edit_or_reply(
            event,
            "** පෝන් එක හිරවෙනවාද?? ගලක්මත තබා හොඳින් තලන්න නිසැක ප්‍රතිඵල😎 **",
        )


    @bot.on(admin_cmd(pattern="hp$"))
    @bot.on(sudo_cmd(pattern="hp$", allow_sudo=True))
    async def gn(event):
        if event.fwd_from:
            return
        await edit_or_reply(
            event,
            "** හුත්තිගෙ පුතා **",
        )


    @bot.on(admin_cmd(pattern="hu$"))
    @bot.on(sudo_cmd(pattern="hu$", allow_sudo=True))
    async def gn(event):
        if event.fwd_from:
            return
        await edit_or_reply(
            event,
            "** කවුරුන් කෙසේ කීවද ඵරුස වචන භාවිතය ඔබේ අරක පණ නැති කරවයි!😂😂**",
        )


    @bot.on(admin_cmd(pattern="sm$"))
    @bot.on(sudo_cmd(pattern="sm$", allow_sudo=True))
    async def gn(event):
        if event.fwd_from:
            return
        await edit_or_reply(
            event,
            "** එහෙම එවා නෑ පුතා..😍 ඒ සෙලවෙන මනස **",
        )


    @bot.on(admin_cmd(pattern="fk$"))
    @bot.on(sudo_cmd(pattern="fk$", allow_sudo=True))
    async def gn(event):
        if event.fwd_from:
            return
        await edit_or_reply(
            event,
            "**පල හුත්තෝ යන්න 😂\n තෝ සමාජයට විහිළුවක් ඕයි 😒**",
        )


    @bot.on(admin_cmd(pattern="tah$"))
    @bot.on(sudo_cmd(pattern="tah$", allow_sudo=True))
    async def gn(event):
        if event.fwd_from:
            return
        await edit_or_reply(
            event,
            "** ටහුකන්න අලංකාර 😐🤚**",
        )


    @bot.on(admin_cmd(pattern="bs$"))
    @bot.on(sudo_cmd(pattern="bs$", allow_sudo=True))
    async def gn(event):
        if event.fwd_from:
            return
        await edit_or_reply(
            event,
            "** Good Night 🌙 Bs ☸️ Jp ✝️Tc 😘Byee...👋👋👋👋 **",
        )


    @bot.on(admin_cmd(pattern="aks$"))
    @bot.on(sudo_cmd(pattern="aks$", allow_sudo=True))
    async def gn(event):
        if event.fwd_from:
            return
        await edit_or_reply(
            event,
            "** අනියම් කාම සේවනය තරයේ හෙලා දකිමි 🙈 **",
        )


    @bot.on(admin_cmd(pattern="ja$"))
    @bot.on(sudo_cmd(pattern="ja$", allow_sudo=True))
    async def gn(event):
        if event.fwd_from:
            return
        await edit_or_reply(
            event,
            "** ජීවිතය අනියතය..☹️ මරණය නියතය 🙏 මහනවීම සැපය 🙏**",
        )


    @bot.on(admin_cmd(pattern=f"srun$", outgoing=True))
    @bot.on(sudo_cmd(pattern="snun$", allow_sudo=True))
    async def runstrings(event):
        if event.fwd_from:
            return
        txt = random.choice(RUNSTRINGS)
        await edit_or_reply(event, txt)





    @bot.on(admin_cmd("newyear"))
    async def _(event):
        if event.fwd_from:
            return
        animation_interval = 1
        animation_ttl = range(0, 80)
        await event.edit("😊 HAPPY NEW YEAR 😁")
        animation_chars = [
            "💖HAPPY NEW YEAR💖",
            "💙HAPPY NEW YEAR💙",
            "❤️HAPPY NEW YEAR❤️",
            "💚HAPPY NEW YEAR💚",
            "💜HAPPY NEW YEAR💜",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 5])


    @bot.on(admin_cmd("happynewyear"))
    async def _(event):
        if event.fwd_from:
            return
        animation_interval = 1
        animation_ttl = range(0, 22)
        await event.edit("😊 HAPPY NEW YEAR TO ALL 😁")
        animation_chars = [
            """💜💜                        💜💜
    💜💜                        💜💜
    💜💜                        💜💜
    💜💜                        💜💜
    💜💜💜💜💜💜💜💜💜
    💜💜💜💜💜💜💜💜💜
    💜💜                        💜💜
    💜💜                        💜💜
    💜💜                        💜💜
    💜💜                        💜💜""",
            """ㅤㅤㅤㅤㅤ ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ
                        💙💙
                     💙💙💙
                 💙💙💙💙
                💙💙 💙💙
              💙💙    💙💙
            💙💙       💙💙
         💙💙💙💙💙💙
          💙💙💙💙💙💙
       💙💙                 💙💙
      💙💙                    💙💙
    💙💙                       💙💙""",
            """💚💚💚💚💚💚💚
    💚💚💚💚💚💚💚💚
    💚💚                     💚💚
    💚💚                     💚💚
    💚💚💚💚💚💚💚💚
    💚💚💚💚💚💚💚
    💚💚
    💚💚
    💚💚
    💚💚""",
            """💛💛💛💛💛💛
    💛💛💛💛💛💛💛
    💛💛                💛💛
    💛💛                💛💛
    💛💛💛💛💛💛💛
    💛💛💛💛💛💛
    💛💛
    💛💛
    💛💛
    💛💛""",
            """💜💜                    💜💜
       💜💜              💜💜
          💜💜        💜💜
             💜💜  💜💜
                💜💜💜
                  💜💜
                  💜💜
                  💜💜
                  💜💜
                  💜💜""",
            """😺😺                           😺😺
    😺😺😺                       😺😺
    😺😺😺😺                 😺😺
    😺😺  😺😺               😺😺
    😺😺     😺😺            😺😺
    😺😺         😺😺        😺😺
    😺😺             😺😺    😺😺
    😺😺                 😺😺😺😺
    😺😺                     😺😺😺
    😺😺                          😺😺
    ⁭""",
            """😁😁😁😁😁😁😁😁
    😁😁😁😁😁😁😁😁
    😁😁
    😁😁
    😁😁😁😁😁😁
    😁😁😁😁😁😁
    😁😁
    😁😁
    😁😁😁😁😁😁😁😁
    😁😁😁😁😁😁😁😁""",
            """🥳🥳                               🥳🥳
    🥳🥳                               🥳🥳
    🥳🥳                               🥳🥳
    🥳🥳                               🥳🥳
    🥳🥳              🥳            🥳🥳
     🥳🥳           🥳🥳          🥳🥳
     🥳🥳        🥳🥳🥳       🥳🥳
      🥳🥳   🥳🥳  🥳🥳   🥳🥳
       🥳🥳🥳🥳      🥳🥳🥳🥳
        🥳🥳🥳             🥳🥳🥳""",
            """🌈🌈                    🌈🌈
       🌈🌈              🌈🌈
          🌈🌈        🌈🌈
             🌈🌈  🌈🌈
                🌈🌈🌈
                  🌈🌈
                  🌈🌈
                  🌈🌈
                  🌈🌈
                  🌈🌈""",
            """🎊🎊🎊🎊🎊🎊🎊🎊
    🎊🎊🎊🎊🎊🎊🎊🎊
    🎊🎊
    🎊🎊
    🎊🎊🎊🎊🎊🎊
    🎊🎊🎊🎊🎊🎊
    🎊🎊
    🎊🎊
    🎊🎊🎊🎊🎊🎊🎊🎊
    🎊🎊🎊🎊🎊🎊🎊🎊""",
            """⁭
                        ㅤ
                      🎉🎉
                   🎉🎉🎉
                🎉🎉 🎉🎉
              🎉🎉    🎉🎉
            🎉🎉       🎉🎉
          🎉🎉🎉🎉🎉🎉
         🎉🎉🎉🎉🎉🎉🎉
       🎉🎉                 🎉🎉
      🎉🎉                    🎉🎉
    🎉🎉                       🎉🎉""",
            """⁭
    🕉🕉🕉🕉🕉🕉🕉
    🕉🕉🕉🕉🕉🕉🕉🕉
    🕉🕉                     🕉🕉
    🕉🕉                     🕉🕉
    🕉🕉🕉🕉🕉🕉🕉🕉
    🕉🕉🕉🕉🕉🕉🕉
    🕉🕉    🕉🕉
    🕉🕉         🕉🕉
    🕉🕉              🕉🕉
    🕉🕉                  🕉🕉""",
        ]
        for i in animation_ttl:

            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 12])


    @bot.on(admin_cmd(pattern=f"cyfile$", outgoing=True))
    @bot.on(sudo_cmd(pattern=f"cyfile$", allow_sudo=True))
    async def _(event):
        if event.fwd_from:
            return
        event = await edit_or_reply(event, "cyfiles")
        await event.edit("❄️ **Disconnected**")
        await asyncio.sleep(2)
        await event.edit("🌩 **Connecting.**")
        await asyncio.sleep(0.5)
        await event.edit("🌧 **Connecting..**")
        await asyncio.sleep(0.5)
        await event.edit("🌩 **Connecting...**")
        await asyncio.sleep(0.5)
        await event.edit("🌧 **Connecting.**")
        await asyncio.sleep(0.5)
        await event.edit("🌩 **Connecting..**")
        await asyncio.sleep(0.5)
        await event.edit("🌧 **Connecting...**")
        await asyncio.sleep(0.5)
        await event.edit("💥 **Connection Established**")
        await asyncio.sleep(1)
        await event.edit("☁️ ** VPN Connected**")
        await asyncio.sleep(2)


    @bot.on(admin_cmd(pattern=f"fileunlock$", outgoing=True))
    @bot.on(sudo_cmd(pattern=f"fileunlock$", allow_sudo=True))
    async def _(event):
        if event.fwd_from:
            return
        event = await edit_or_reply(event, "fileunlock")
        await event.edit("📁 **File name : Dialog 0 Balance**")
        await asyncio.sleep(1)
        await event.edit("🔓 **Begin unlocking file...**")
        await asyncio.sleep(1)
        await event.edit("🔓 **Unlocked 50%**")
        await asyncio.sleep(0.5)
        await event.edit("🔓 **Unlocked 100%**")
        await asyncio.sleep(0.5)
        await event.edit("**Please do no share this host for longer use !!**")
        await asyncio.sleep(1)
        await event.edit(
            "**Your Host securaly stored. Get it from below link 👇\nhttps://telegra.ph/Dialog-Host-01-12**"
        )
        await asyncio.sleep(2)


    @bot.on(admin_cmd(pattern=f"freenet$", outgoing=True))
    @bot.on(sudo_cmd(pattern=f"freenet$", allow_sudo=True))
    async def _(event):
        if event.fwd_from:
            return
        event = await edit_or_reply(event, "freenet")
        await event.edit("**Connecting to Singapore Server 🇸🇬**")
        await asyncio.sleep(1)
        await event.edit("**Successfully Connected 💯**")
        await asyncio.sleep(1)
        await event.edit("**හරි පුතේ එල අය ඔයාගේ data කැපෙන්නේ නෑ 👌**")
        await asyncio.sleep(1)


    CMD_HELP.update(
        {
            "sinhala_Jokes": "\n**Config Fun**\n\n.freenet `- fun`\n.cyfiles `- cyh connecting`\n\n**RUN STRINGS**\n.srun - Sinhala Run Strings to Friday 😂..\n\n**Funny Animations.**\n.fuuk\n.sux\n.kiss\n\n**Frequently using quotes\n.hu - `කවුරුන් කෙසේ කීවද ඵරුස වචන භාවිතය ඔබේ අරක පණ නැති කරවයි!`\n.slo -  `පෝන් එක හිරවෙනවාද?? ගලක්මත තබා හොඳින් තලන්න නිසැක ප්‍රතිඵල`\n.hp - `හුත්තිගෙ පුතා`\n.kp - `කැරි පකයා`\n.sm - `එහෙම එවා නෑ පුතා.ඒ සෙලවෙන මනස`\n.fk - `පල හුත්තෝ යන්න. තෝ සමාජයට විහිලුවක් ඕයි`\n.aks - `අනියම් කාම සේවනය තරයේ හෙලා දකිමි`\n.ja - `ජීවිතය අනියතය.. මරණය නියතය  මහනවීම සැපය `\n.tah - `ටහුකන්න අලංකාර`"
        }
    )

