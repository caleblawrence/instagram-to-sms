# instagramToSms
This is a application that sends select users Instagram posts to you as text messages. It's a way of receiving images/updates from someone without being on Instagram.

## Movativation
The reasoning for this project because is that I wanted to recieve images (Instagram posts) from my family members but at the same time I'm not on social media. I wantked to have a way of "following" them but not being on Intagram. 

Instagram To SMS checks for new Instagram posts from a list of people and when it finds new posts it sends the image and caption as a text message to my phone.


## Dependencies and repos that made this project possible
This project relies on the [Intagram Scraper](https://github.com/rarcega/instagram-scraper) project by [rarcega](https://github.com/rarcega) to download all the images from someone's Instagram profile and I use [Twillio](www.twillio.com) to send text messages.

I also used [Flask](http://flask.pocoo.org/) and [Ngrok](https://ngrok.com/) to create a simple file server so that I could create a public URL for the downloaded images so that Twillio could send them.
