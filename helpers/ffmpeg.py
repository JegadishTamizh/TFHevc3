#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


from helpers.tools import execute, clean_up
from helpers.upload import upload_audio, upload_subtitle

async def extract_audio(client, message, data):
    await message.edit_text("Extracting Audio Fie...")

    dwld_loc = data['location']
    out_loc = data['location'] + ".mkv"

    if data['name'] == "mkv":
        out, err, rcode, pid = await execute(f"ffmpeg -i '{dwld_loc}' -vf crop=1280:536 -c:v libx265 -crf 22 -preset slow -c:a copy -c:s copy -metadata title='Tamil Fusion - t.me/TamilFusion1' -metadata:s:v title='Tamil Fusion - t.me/TamilFusion1' -metadata:s:a title='Tamil Fusion - t.me/TamilFusion1' -metadata:s:s title='Tamil Fusion - t.me/TamilFusion1' '{out_loc}' -y")
        if rcode != 0:
            await message.edit_text("**Error Occured. See Logs for more info.**")
            print(err)
            await clean_up(dwld_loc, out_loc)
            return
    else:
        out, err, rcode, pid = await execute(f"ffmpeg -i '{dwld_loc}' -vf crop=1280:536 -c:v libx265 -crf 22 -preset slow -c:a copy -c:s copy -metadata title='Tamil Fusion - t.me/TamilFusion1' -metadata:s:v title='Tamil Fusion - t.me/TamilFusion1' -metadata:s:a title='Tamil Fusion - t.me/TamilFusion1' -metadata:s:s title='Tamil Fusion - t.me/TamilFusion1' '{out_loc}' -y")
        if rcode != 0:
            await message.edit_text("**Error Occured. See Logs for more info.**")
            print(err)
            await clean_up(dwld_loc, out_loc)
            return

    await clean_up(dwld_loc)
    await upload_audio(client, message, out_loc)



async def extract_subtitle(client, message, data):
    await message.edit_text("Extracting Stream from file")

    dwld_loc = data['location']
    out_loc = data['location'] + ".mkv"   

    out, err, rcode, pid = await execute(f"ffmpeg -i '{dwld_loc}' -vf crop=1280:536 -c:v libx265 -crf 22 -preset slow -c:a libopus -b:a 70k -ac 2 -af 'pan=stereo|FL=0.5FC+0.707FL+0.707BL+0.5LFE|FR=0.5FC+0.707FR+0.707BR+0.5LFE' -metadata title='Tamil Fusion - t.me/TamilFusion1' -metadata:s:v title='Tamil Fusion - t.me/TamilFusion1' -metadata:s:a title='Tamil Fusion - t.me/TamilFusion1' -metadata:s:s title='Tamil Fusion - t.me/TamilFusion1' '{out_loc}' -y")
    if rcode != 0:
        await message.edit_text("**Error Occured. See Logs for more info.**")
        print(err)
        await clean_up(dwld_loc, out_loc)
        return

    await clean_up(dwld_loc)  
    await upload_subtitle(client, message, out_loc)
    
