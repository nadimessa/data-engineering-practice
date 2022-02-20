# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.

from turtle import down
import requests, os

failed_uris = []
successful_uris = []

download_uris = [
    'http://www.lancsngfl.ac.uk/cmsmanual/getfile.php?src=18/pscales.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip'
]

def create_downloads_folder():
    print(os.getcwd())
    
    try:
        os.mkdir("downloads222")
    except:
        if os.error(FileExistsError):
            print("The folder already exists. Manually delete the folder ")
        else:
            print("An error has occurred")
    else:
        print("Downloads folder created, continuing with downloads...")
        download_files()
    
def download_files():
    for uri in range(len(download_uris)):
        try:
            req = requests.get(download_uris[uri], stream=True)

            status = req.status_code
            
            if status == 200:
                print(f"Successfully downloaded {download_uris[uri]}")
                
            elif status != 200:
                print(f"Problems downloading {download_uris[uri]} (error code {status})")
                
        except:
            print(f"An error {req.status_code} occured when downloading {req}")


def main():
    
    create_downloads_folder()

    
if __name__ == '__main__':
    
    main()
