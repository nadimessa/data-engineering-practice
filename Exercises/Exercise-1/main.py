# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.

from turtle import down
import requests, os
import myutils


download_uris = [
    'http://www.lancsngfl.ac.uk/cmsmanual/getfile.php?src=18/pscales.zip',
    'https://file-examples-com.github.io/uploads/2017/02/zip_2MB.zip',
    'http://ipv4.download.thinkbroadband.com/5MB.zip',
    'https://drive.google.com/uc?export=download&id=1yAmFc15GtP52El_RTxl6uqmZZJi-h4BG',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip'
]

failed_uris = []
no_of_downloads = len(download_uris)

def create_downloads_folder(dest_folder="downloads"):
    
    try:
        if not os.path.exists(dest_folder):
            os.mkdir(dest_folder)  # create folder if it does not exist

    except:
        print("An error has occurred, check you have permission to create this folder")
    else:
        print("Downloads folder created, continuing with downloads...")
        download_files(dest_folder)
    
def download_files(dest_folder):
    for uri in range(no_of_downloads):
        try:
            req = requests.get(download_uris[uri], stream=True)
        except:
            print(f"An error {req.status_code} occured when downloading {req}")

        status = req.status_code
        url = download_uris[uri]

        if status == 200:
            print(f"Successfully downloaded {url}")
            
            filename = myutils.get_filename(url)
            
            path = os.path.join(dest_folder, filename)

            if req.headers.get('content-type') == 'application/zip':
             
                with open(path, "wb") as file:
                    file.write(req.content)
                

        elif status != 200:
            print(f"Problems downloading {url} (error code {status})")
            failed_uris.append(url)
            
    
    

if __name__ == '__main__':
    
    create_downloads_folder("downloads")
    