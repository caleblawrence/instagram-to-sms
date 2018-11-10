import subprocess
import os
import glob
from twilio.rest import Client
import json
import os.path

# download new pictures
def downloadPictures(users_to_watch, path): 
    for user in users_to_watch:
        print("[INFO] Checking for new images from: " + user)
        api_location = path + "instagramScraperMaster/instagram_scraper/app.py"
        parameters = "--comments --latest-stamps " + path + "/latestImageInformation.txt" + " --retain-username --destination " + path + "images"
        bot_information = "-u calebjohnsontosms -p " +  os.environ['instagram_password']
        # bot_information = "-u calebjohnsontosms -p instagramToSms1021"
        command = "python " + api_location + " " + parameters + " " + user + " " + bot_information
        subprocess.call(command, shell=True)

def sendImages(users_to_watch):
    for username in users_to_watch:
        comments = getComments(username)
        commentsCounter = 0

        print("[INFO] Sending images for: " + username)
        directory = os.getenv("HOME") + "/projects/instagramToSms/images/" + username
        for filename in os.listdir(directory):
            if "jpg" in filename: 
                print("jpg found in: " + filename)
                try:
                    if len(comments) >= commentsCounter:
                        # print("[DEBUG] Comment counter: " + str(commentsCounter) + ". Comment array: " + str(comments))
                        sendImage(username, filename, comments[commentsCounter])
                        commentsCounter = commentsCounter + 1
                    else:
                        sendImage(username, filename, "no caption")
                except:
                    sendImage(username, filename, "no caption")
                
            
             

def sendImage(username, filename, comment):
    client = Client(os.environ['twillio_account_sid'], os.environ['twillio_auth_token'])
    # this is the URL to an image file we're going to send in the MMS
    url = getNgorkURL()
    url = ' '.join(url.split())

    media = "http://" + url + "/uploads/" + username + "/" + filename

    print("[INFO] Sending image at: " + media)
 
    # account to send MMS to any phone number that MMS is available
    client.api.account.messages.create(to=os.environ['caleb_phone_number'],
                                    from_=os.environ['twillio_phone_number'],
                                    body=username + ": " + comment,
                                    media_url=media)

    # account to send MMS to any phone number that MMS is available
    client.api.account.messages.create(to=os.environ['kai_phone_number'],
                                    from_=os.environ['twillio_phone_number'],
                                    body=username + ": " + comment,
                                    media_url=media)

def cleanup(users_to_watch):
    for username in users_to_watch:
        print("[INFO] cleaning up directory for: " + username)

        directory = os.getenv("HOME") + "/projects/instagramToSms/images/" + username
        command = "rm " + directory + "/*"
        subprocess.call(command, shell=True)

def getComments(username):  
    comments_array = [] 
    filename = os.getenv("HOME") + "/projects/instagramToSms/images/" + username + "/" + username + ".json"

    if os.path.exists(filename):
        # path exists
        with open(filename) as f:
            dict_data = json.load(f)
        for data in dict_data: 
            for attribute, value in data.iteritems():
                # print attribute, value
                if attribute == "edge_media_to_caption":
                    comments_array.append(value['edges'][0]['node']['text'])
        return comments_array
    else:
        comments = []
        comments = comments.reverse()
        return comments

def getNgorkURL():
    command = "curl --silent --show-error http://127.0.0.1:4040/api/tunnels | sed -nE 's/.*public_url\":\"https:..([^\"]*).*/\\1/p'"
    url = subprocess.check_output(command, shell=True)
    return url


# main
def main():
    # instagram uesr information
    # to skip initial download just view source on users page and look for 'taken_at_timestamp' and add time stamp to the "latestImageInformation.txt"
    users_to_watch = ['annameizhi', 'corrine.lawrence', 'testlawrence', 'kadebrummet', 'michaelpsalm139', 'a.layne_brummet', 'noah_zachary97', 'itz_abz_', 'txmom2four_']
    # users_to_watch = ['testlawrence']

    path=os.getenv("HOME") + "/projects/instagramToSms/"

    downloadPictures(users_to_watch, path)
    sendImages(users_to_watch)
    cleanup(users_to_watch)

if __name__== "__main__":
    main()




