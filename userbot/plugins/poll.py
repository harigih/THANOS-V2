import random

from telethon.errors.rpcbaseerrors import ForbiddenError
from telethon.errors.rpcerrorlist import PollOptionInvalidError
from telethon.tl.types import InputMediaPoll, Poll

from userbot import THANOSPRO

from ..core.managers import edit_or_reply
from . import Build_Poll, reply_id

plugin_thanosegory = "extra"


@THANOSPRO.thanos_cmd(
    pattern="poll(?:\s|$)([\s\S]*)",
    command=("poll", plugin_thanosegory),
    info={
        "header": "To create a poll.",
        "description": "If you doesnt give any input it sends a default poll",
        "usage": ["{tr}poll", "{tr}poll question ; option 1; option2"],
        "examples": "{tr}poll Are you an early bird or a night owl ;Early bird ; Night owl",
    },
)
async def pollcreator(thanospoll):
    "To create a poll"
    reply_to_id = await reply_id(thanospoll)
    if string := "".join(thanospoll.text.split(maxsplit=1)[1:]):
        thanosinput = string.split(";")
        if len(thanosinput) > 2 and len(thanosinput) < 12:
            options = Build_Poll(thanosinput[1:])
            try:
                await thanospoll.client.send_message(
                    thanospoll.chat_id,
                    file=InputMediaPoll(
                        poll=Poll(
                            id=random.getrandbits(32),
                            question=thanosinput[0],
                            answers=options,
                        )
                    ),
                    reply_to=reply_to_id,
                )
                await thanospoll.delete()
            except PollOptionInvalidError:
                await edit_or_reply(
                    thanospoll,
                    "`A poll option used invalid data (the data may be too long).`",
                )
            except ForbiddenError:
                await edit_or_reply(thanospoll, "`This chat has forbidden the polls`")
            except Exception as e:
                await edit_or_reply(thanospoll, str(e))
        else:
            await edit_or_reply(
                thanospoll,
                "Make sure that you used Correct syntax `.poll question ; option1 ; option2`",
            )

    else:
        options = Build_Poll(["Yah sure 😊✌️", "Nah 😏😕", "Whatever die sur 🥱🙄"])
        try:
            await thanospoll.client.send_message(
                thanospoll.chat_id,
                file=InputMediaPoll(
                    poll=Poll(
                        id=random.getrandbits(32),
                        question="👆👆So do you guys agree with this?",
                        answers=options,
                    )
                ),
                reply_to=reply_to_id,
            )
            await thanospoll.delete()
        except PollOptionInvalidError:
            await edit_or_reply(
                thanospoll, "`A poll option used invalid data (the data may be too long).`"
            )
        except ForbiddenError:
            await edit_or_reply(thanospoll, "`This chat has forbidden the polls`")
        except Exception as e:
            await edit_or_reply(thanospoll, str(e))
