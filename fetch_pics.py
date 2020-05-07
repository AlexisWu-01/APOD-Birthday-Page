'''Get all your birthday photos of galaxies from APOD.
Author: Alexis Wu
'''
import requests
import os
import shutil
import datetime as dt
import json


def inputBirthday(year, month, date):
    '''input birthday in the format of year, month, date 
    and gets a return of these and also their current age.'''
    birthdate = dt.datetime(year,month,date)
    now = dt.datetime.now()
    age = int(now.strftime('%Y')) - int(birthdate.strftime('%Y'))
    year = int(birthdate.strftime('%Y'))
    month = int(birthdate.strftime('%m'))
    date = int(birthdate.strftime('%d'))
    return year, month, date, age


def createFolder(dir, motherdir):
    '''creates or rewrites a directory under the giver mother directory.'''
    #check if the directory was already created
    path = motherdir+'/'+dir
    if os.path.isdir(path) == True:
        #deletes this directory
        shutil.rmtree(dir)
    #creates an empty directory
    directory = 'Apod_photos'
    parent_dir = '.'
    path = os.path.join(parent_dir,directory)
    os.mkdir(path)

def downloadPhotos(directory,year,month,date,age):
#downloads all birthday photos
    doc = open(directory+'/titles.txt','w+')

    for count in range(age):
        new_year = year + count
        #generates the new date and link of each year's photo 
        new_date = '{yr}-{mth}-{dt}'.format(yr = new_year, mth = month, dt = date)
        new_url = "https://api.nasa.gov/planetary/apod?api_key=fU8w812PMqudNcgk9DDT8J2TSXEnRtz5BzTalWAa&date=" + new_date
        #read the json file and translate to picture link    
        photo = requests.get(new_url)
        photo = photo.json()
        photo_link = photo['url']
        photo_title = photo['title']

        #download into the folder from picture link
        photo = requests.get(photo_link)
        file = open(directory+'/'+str(count)+'.jpg','wb')
        file.write(photo.content)
        file.close()
        doc.write(photo_title)
        doc.write('\n')
    doc.close()
        
# createFolder('Apod_photos','.')
# downloadPhotos('./Apod_photos',2000,5,8,20)