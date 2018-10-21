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
        command = "python " + api_location + " " + parameters + " " + user + " " + bot_information
        subprocess.call(command, shell=True)

def sendImages(users_to_watch):
    for username in users_to_watch:
        comments = getComments(username)
        commentsCounter = 0

        print("[INFO] Sending images for: " + username)
        directory = "/home/caleblawrence/Projects/instagramToSms/images/" + username
        for filename in os.listdir(directory):
            if "jpg" in filename: 
                print("jpg found in: " + filename)
                if len(comments) >= commentsCounter:
                    # print("[DEBUG] Comment counter: " + str(commentsCounter) + ". Comment array: " + str(comments))
                    sendImage(username, filename, comments[commentsCounter])
                    commentsCounter = commentsCounter + 1
                
                else:
                    sendImage(username, filename, "ERROR")
                
            
             

def sendImage(username, filename, comment):
    client = Client(os.environ['twillio_account_sid'], os.environ['twillio_auth_token'])
    # this is the URL to an image file we're going to send in the MMS
    media = "http://23312b8c.ngrok.io" + "/uploads/" + username + "/" + filename

    print("[INFO] Sending image at: " + media)
 
    # account to send MMS to any phone number that MMS is available
    client.api.account.messages.create(to=os.environ['caleb_phone_number'],
                                    from_=os.environ['twillio_phone_number'],
                                    body=username + ": " + comment,
                                    media_url=media)

    # # account to send MMS to any phone number that MMS is available
    # client.api.account.messages.create(to=os.environ['kai_phone_number'],
    #                                 from_=os.environ['twillio_phone_number'],
    #                                 body=username + ": " + comment,
    #                                 media_url=media)

def cleanup(users_to_watch):
    for username in users_to_watch:
        print("[INFO] cleaning up directory for: " + username)

        directory = "/home/caleblawrence/Projects/instagramToSms/images/" + username
        command = "rm " + directory + "/*"
        subprocess.call(command, shell=True)

def getComments(username):  
    comments_array = [] 
    filename = "/home/caleblawrence/Projects/instagramToSms/images/" + username + "/" + username + ".json"

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


# main
def main():
    # steps for setting up server: 
    # export FLASK_APP=flaskImageServer.py
    # python -m flask run
    # ngrok http 5000


    # instagram uesr information
    # to skip initial download just view source on users page and look for 'taken_at_timestamp' and add time stamp to the "latestImageInformation.txt"
    users_to_watch = ['annameizhi', 'corrine.lawrence', 'testlawrence', 'kadebrummet', 'michaelpsalm139', 'a.layne_brummet', 'noah_zachary97', 'itz_abz_', 'txmom2four_']
    # users_to_watch = ['testlawrence']

    path="/home/caleblawrence/Projects/instagramToSms/"

    # downloadPictures(users_to_watch, path)
    # sendImages(users_to_watch)
    # cleanup(users_to_watch)

if __name__== "__main__":
    main()




