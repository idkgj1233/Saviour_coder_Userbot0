"""COMMAND : .eye"""


import asyncio

from fridaybot import CMD_HELP
from fridaybot.utils import friday_on_cmd


@friday.on(friday_on_cmd(pattern="eye"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 103)

    # input_str = event.pattern_match.group(1)

    # if input_str == "eye":

    await event.edit("👁👁")

    animation_chars = [
        "👁👁\n  👄  =====> Abey Ja Na Gandu",
        "👁👁\n  👅  =====> Abey Ja Na Madarchod",
        "👁👁\n  💋  =====> Abey Ja Na Randi",
        "👁👁\n  👄  =====> Abey Ja Na Betichod",
        "👁👁\n  👅  =====> Abey Ja Na Behenchod",
        "👁👁\n  💋  =====> Abey Ja Na Na Mard",
        "👁👁\n  👄  =====> Abey Ja Na Randi",
        "👁👁\n  👅  =====> Abey Ja Na Bhosdk",
        "👁👁\n  💋  =====> Abey Ja Na Chutiye",
        "👁👁\n  👄  =====> Hi All, How Are You Guys...",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 103])


CMD_HELP.update(
    {
        "eye": "**Eye**\
\n\n**Syntax : **`.eye`\
\n**Usage :** Use this plugin to abuse someone."
    }
)