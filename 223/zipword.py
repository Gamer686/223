import zipfile             
import time

folderpath=input('Path to the file: ')   #Get the target file path and name from the user
zipf=zipfile.ZipFile(folderpath)   #Initialize a PdfFileReader object

global result
result=0

global tried
tried=0

c=0

if not zipf:         #Checks if the password is password encrypted
    print('The zipped file/folder is not password protected!You can successfully open it!')   #Notifies if the zipped file/folder is not password encrypted
else:
    starttime=time.time()
    wordListFile=open('wordlist.txt','r',errors='ignore')
    body=wordListFile.read().lower()
    words=body.split('\n')

    for i in range(len(words)):
        word=words[i]
        password=word.encode('utf8').strip()
        c=c+1
        print('Trying to decode password by:{}'.format(word))

        try:
            with zipfile.ZipFile(folderpath,'r') as zf:
                zf.extractall(pwd=password)
                print("Success! The password is: "+ word)
                endtime=time.time()          #Save the end time
                result=1              #Set the result variable to 1 on success
            break
        except:
            pass

    duration=endtime-starttime

    if(result==0):
        print("Sorry,password not found. A total of "+str(c)+"+ possible combinations tried in "+str(duration)+"seconds. Password is not of 4 characters.")
    else:
        duration=endtime-starttime
        print('Congratulations!!! Password found after trying '+str(c)+' combinations in '+str(duration)+' seconds')
        