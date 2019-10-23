@bot.message_handler(content_types=['sticker'])
def predefined_stickers(message):
    global first_group
    global second_group
    global first_group_eng
    global second_group_eng

    cid = message.chat.id
    uid = message.from_user.id

    sticker_rnm = random.randint(1, 25)

    if sticker_rnm == 1:
        sid = "CAADAgADNwADTV8oGAcnDK_zzifQFgQ"
    elif sticker_rnm == 2:
        sid = "CAADAgADOAADTV8oGIkHWmw4--6sFgQ"
    elif sticker_rnm == 3:
        sid = "CAADAgADOQADTV8oGB0jpTwBtJ3qFgQ"
    elif sticker_rnm == 4:
        sid = "CAADAgADOgADTV8oGMRKEjeYMD-iFgQ"
    elif sticker_rnm == 5:
        sid = "CAADAgADOwADTV8oGPYpjAugj5MkFgQ"
    elif sticker_rnm == 6:
        sid = "CAADAgADPAADTV8oGNHRaGn8VRqSFgQ"
    elif sticker_rnm == 7:
        sid = "CAADAgADPQADTV8oGGv7CE-jUh8EFgQ"
    elif sticker_rnm == 8:
        sid = "CAADAgADPwADTV8oGGEa15DV51VsFgQ"
    elif sticker_rnm == 9:
        sid = "CAADAgADQQADTV8oGHxIB3e9wuKQFgQ"
    elif sticker_rnm == 10:
        sid = "CAADAgADQgADTV8oGOKRYZfYhYJFFgQ"
    elif sticker_rnm == 11:
        sid = "CAADAgADQwADTV8oGE78wiPH81acFgQ"
    elif sticker_rnm == 12:
        sid = "CAADAgADRAADTV8oGAtV7hSpVNtaFgQ"
    elif sticker_rnm == 13:
        sid = "CAADAgADRQADTV8oGFslQVK175XIFgQ"
    elif sticker_rnm == 14:
        sid = "CAADAgADRgADTV8oGNfQA4YP9hbGFgQ"
    elif sticker_rnm == 15:
        sid = "CAADAgADRwADTV8oGE_kCZ6bNeYWFgQ"
    elif sticker_rnm == 16:
        sid = "CAADAgADSAADTV8oGAW7JHvjQFXFFgQ"
    elif sticker_rnm == 17:
        sid = "CAADAgADSQADTV8oGJ2B3Lds1bOCFgQ"
    elif sticker_rnm == 18:
        sid = "CAADAgADSgADTV8oGM58vpLz3FuoFgQ"
    elif sticker_rnm == 19:
        sid = "CAADAgADSwADTV8oGOxJeXJbuuKHFgQ"
    elif sticker_rnm == 20:
        sid = "CAADAgADTQADTV8oGLiiZvA26ikuFgQ"
    elif sticker_rnm == 21:
        sid = "CAADAgADTAADTV8oGJhTCjwdw5EYFgQ"
    elif sticker_rnm == 22:
        sid = "CAADAgADTwADTV8oGJzFxvw-eMa5FgQ"
    elif sticker_rnm == 23:
        sid = "CAADAgADTgADTV8oGOMvW5CjVqGhFgQ"
    elif sticker_rnm == 24:
        sid = "CAADAgADUAADTV8oGMB0LsS6SDJtFgQ"
    elif sticker_rnm == 25:
        sid = "CAADAgADUQADTV8oGM5oZrUGiKN-FgQ"

    if uid in first_group.keys() or uid in second_group.keys():
        bot.send_sticker(cid, sid)