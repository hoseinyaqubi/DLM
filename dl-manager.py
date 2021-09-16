import requests  as rq
from requests.exceptions import ConnectionError
from tqdm import tqdm 
from math import floor , pow , log
import os

def download_file(url , address = ''):
   '''this func download any file in internet '''
   file = rq.get(url , stream= True)
   total_bit = int(file.headers.get('Content-Length' , 1024))
   # میام 1024 رو به 1000 تبدیل میکینم تا حجم فایل رو به درستی نمایش بده
   scale_paw = floor(log(total_bit , 1024))
   total_size = (total_bit/pow(1024 , scale_paw) * pow(1000, scale_paw))

   # درست کردن نام فایل 
   file_name = url.split(r'/')[-1]
   if address == '' :
      windowsname = os.getlogin()
      file_address = 'C:\\Users\\'+windowsname+'\\Downloads\\'+file_name
   else:
      file_address = address + '\\' + file_name
   block_dl =  2048
   t = tqdm(total=total_size , unit_scale=True , unit = 'B')
   

   with open(file_address , 'wb') as f: 
      for chunk in file.iter_content(block_dl):
            t.update((len(chunk)/pow(1024 , scale_paw) * pow(1000, scale_paw)))
            f.write(chunk)
   t.close()
   print(f'File storage location >>> {file_address}')


print(  'Welcome to download manager' )
url = input(' Link download  : ')
address = input(' Storage location : ') 
try :      
   download_file(url , address)
   print('Download voplit')

except ConnectionError:
   print('Check your internet connection')
