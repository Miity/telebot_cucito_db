from loader import dp
from aiogram import types


media_folder = 'media/'
boat_photo_folder = media_folder + 'boats/'

async def save_photos(media, folder_name = 'not_sorted'):
    data = []
    path = boat_photo_folder + folder_name + '/'
    for photo in media:
        File = await dp.bot.get_file(photo['file_id'])
        file_name = File.file_path.split('/')[-1]
        await dp.bot.download_file(File.file_path, path + file_name)
        data.append({'path':path, 'name':file_name})
    return data