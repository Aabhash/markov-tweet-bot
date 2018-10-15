# Table of Content

* [Requirements](#Requirements)
* [Starting Bot](#Starting-the-Bot)
  * [Command](#Command)
  * [Example](#Example)
  * [Parameters](#Parameters)
# Requirements
twitter => 1.18.0 - [Detailed Info](https://pypi.org/project/twitter/)
pandas 
Installing package: 
```
pip install twitter
```
```
pip install pandas
```
# Starting the Bot

Start the bot by running 'driver.py'. 
## Command
```
python driver.py <[-l][-r]> <filename> <keyword> <prefix> <suffix> <num_tweets>
```
## Example
```
python driver.py -l thor "Bruce Banner" The #Avengers 5
```
## Parameters

- **Model options**:
  - **-l** : Load model from file. Use this if using an existing model. 
  - **-r** : Read file to create model. Use this if including your own text file.
  - **Filename** : Name of pickle model file if load option set. Name of text file if read option set.  
  - **Keywords** : Seedwords which are an intergral part of tweet. Keywords may be single or multiple. 
  - **Prefix**   : Word/s to start the tweet with. Prefix may be single or multiple words. 
  - **Suffix**   : Word/s to add at the end of tweet. Suffix may be single or multiple words.
  - **num_tweets**   : Number of tweets to be written.
  - **-c** : Collect tweets from TwitterStream.
  - **no** : Number of tweets to collect.
  - **-a** : Amplify tweets i.e. Retweet tweets stored using -c.   
  - **no** : Number of tweets to amplify.
  - **timeout** : Time to wait in seconds before retweeting. 