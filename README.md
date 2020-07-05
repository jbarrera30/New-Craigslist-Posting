# New-Craigslist-Posting

I found myself in the market for a new Fender Telecaster electric guitar, and most of the good deals are on Craigslist. The thing is, I just don't have time to be constantly checking to see if there has a new listing added, and the good deals go fast. I wrote this script to alert me immediately when a new listing has been posted, and send a text to my phone with the url. I can quickly click the link, and see if I should get in contact with the seller.

This script utlilzes BeautfulSoup to pull data from the html file when there is a new listing. I then sorted through the data to isolate the new postings and their links, and I utilized the Twilio API to send a text to my phone directly.
