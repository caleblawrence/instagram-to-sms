# instagram-to-sms
This is an application that sends select users Instagram posts to you as text messages (even if they are private). It's a way of receiving images/updates from family members without being on social media. 
#### Example screenshot
![alt text](https://raw.githubusercontent.com/caleblawrence/instagram-to-sms/master/example_screenshot.jpg)

## Motivation
The reasoning for this project because is that I wanted to receive images (Instagram posts) from my family members but at the same time I'm not on social media. I wanted to have a way of "following" them but not being on Instagram. 

Instagram To SMS checks for new Instagram posts from a list of people and when it finds new posts it sends the image and caption as a text message to my phone.

Interesting TED talk about quitting social media [here.](https://www.ted.com/talks/cal_newport_why_you_should_quit_social_media?language=en)


## Dependencies and repos that made this project possible
This project relies on the [intagram-scraper](https://github.com/rarcega/instagram-scraper) project by [rarcega](https://github.com/rarcega) to download all the images from someone's Instagram profile and I use [Twilio](http://twilio.com) to send text messages.

I also used [Flask](http://flask.pocoo.org/) and [Ngrok](https://ngrok.com/) to create a simple file server so that I could create a public URL for the downloaded images so that Twilio could send them.

## Usage
1. Update env variables 
2. Start up Image Server (export FLASK_APP=flaskImageServer.py and python -m flask run)
3. Run setupImageServer.sh to set up ngrok (CRON this as urls expire)
4. Run instagramToSMS.py script to check for images and send them (CRON)

You can run steps 3 and 4 in CRON everyday assuming the flask app is constantly running.
