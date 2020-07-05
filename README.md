# New-Craigslist-Posting

I found myself in the market for a new Fender Telecaster electric guitar, and most of the good deals are on Craigslist. The thing is, I just don't have time to be constantly checking to see if there has a new listing added, and the good deals go fast. I wrote this script to alert me immediately when a new listing has been posted for a certain keyword, and send a text to my phone with the url. I can quickly click the link, and see if the post is what I'm looking for.

This script utlilzes Beautful Soup library to pull data from the html file when there is a new listing. I sorted through the data to isolate the new postings and then their links, and I utilized the Twilio REST API to send a text to my phone directly.

The code is flexible, all you have to do is input the url of the listing page with the keyword already in the search bar, so you can get as specific with your search as you'd like. Also add your Twilio data and phone number, and that's all you need to get started.
