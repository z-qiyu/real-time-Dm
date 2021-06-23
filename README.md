# real-time-Dm


The data directory is the directory where the data files are stored; and data_temp directory is obtain data for comparison.

You need download a chromedriver, because one of the spider is automatic spider, so I used selenium model.

In spider_item directory , There are six spider files there, sp_6 used selenium, and other used requests,header.py is save request header and file comparison function ; and note.py is send mail and
read the configuration file and get real time and write to log file.

If the retrieved data file has changed, it's called a websiteupdate, and if website has been updated, email is used to prompt the user.

the config.txt is configuration file , You can configure the frequency inside and Some configuration about mail.

the csv file ,I need GBK encoding.
