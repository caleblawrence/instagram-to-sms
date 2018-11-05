# instagram-to-sms
This is an application that sends select users Instagram posts to you as text messages (even if they are private). It's a way of receiving images/updates from someone without being on Instagram.

## Motivation
The reasoning for this project because is that I wanted to receive images (Instagram posts) from my family members but at the same time I'm not on social media. I wanted to have a way of "following" them but not being on Instagram. 

Instagram To SMS checks for new Instagram posts from a list of people and when it finds new posts it sends the image and caption as a text message to my phone.


## Dependencies and repos that made this project possible
This project relies on the [intagram-scraper](https://github.com/rarcega/instagram-scraper) project by [rarcega](https://github.com/rarcega) to download all the images from someone's Instagram profile and I use [Twilio](http://twilio.com) to send text messages.

I also used [Flask](http://flask.pocoo.org/) and [Ngrok](https://ngrok.com/) to create a simple file server so that I could create a public URL for the downloaded images so that Twilio could send them.

## Usage
//todo
