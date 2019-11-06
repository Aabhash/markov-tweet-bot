# Table of Content

* [Markov Chain](#Markov-Chain)
* [Requirements](#Requirements)
* [Starting Bot](#Starting-the-Bot)
  * [Command](#Command)
  * [Example](#Example)
  * [Parameters](#Parameters)

# Markov Chain
Markov Chains are mathematical systems that go from one state to another. A few rules associated with this broad statement are as follows: the next state is entirely dependent on the previous state. The next state is determined on a probabilistic basis. 
In python terms, you create a dictionary of every unique word in your corpus. From there, you make the values of your dictionary a list of words that appear after each unique word. The more often a word appears after another, the higher the probability that it will be selected in the text generator.

This is used as the core for this program to generate the twitter. Other scripts are to communicate with the user and the twitter API.

## Advantages
Using Markov Chain in text generator has following advantages:
* It has simple structure so you can easily understand the principle.
* It works well enough if the corpus has the similar context of data as the sentence you want to generate.
* You don't need any complex Neural networks to set this up.

## Disadvantages
Since it may be the simplest text generator after random generator. It has many limitations.
* The texts are random, the probability for using most used words is high but it is still random.
* If the corpus is unrelated, the text generated will be completely rubbish.
* If the corpus has small number of words, you'll see repetition of same words.


# Requirements
* [twitter](https://pypi.org/project/twitter/)
* [pandas](https://pypi.org/project/pandas/)

Installing required package: 
```
pip install -r requirements.txt
```
# Starting the Bot

Start the bot by running 'driver.py'. 
The module has following functionalities.:
* Load a saved model -L 
* Train a model from File -R
* Collect Tweets -C
* Load a number of tweets and amplify -A

More about the parameters are given in [Parameters](##Parameters)
## Command
```
python driver.py <[-l][-r]> <filename> <keyword> <prefix> <suffix> <num_tweets>
```
## Example
```
python driver.py -l thor "Bruce Banner" The "#Avengers" 5
```
If the parameters has python special characters like # in it, you have to enclose them in `""`.
## Parameters

* **Model options**:
  * **-l** : Load model from file. Use this if using an existing model. 
    * **Filename** : Name of pickle file to load markov model.  
    * **Keywords** : Seedwords which are an intergral part of tweet. Keywords may be single or multiple. 
    * **Prefix**   : Word/s to start the tweet with. Prefix may be single or multiple words. 
    * **Suffix**   : Word/s to add at the end of tweet. Suffix may be single or multiple words.
    * **num_tweets**   : Number of tweets to be written.
  * **-r** : Read file to create model. Use this if including your own text file.
    * **Filename** : Name of text file to construct markov model.  
    * **Keywords** : Seedwords which are an intergral part of tweet. Keywords may be single or multiple. 
    * **Prefix**   : Word/s to start the tweet with. Prefix may be single or multiple words. 
    * **Suffix**   : Word/s to add at the end of tweet. Suffix may be single or multiple words.
    * **num_tweets**   : Number of tweets to be written.
  * **-c** : Collect tweets from TwitterStream.
    * **no** : Number of tweets to collect.
  * **-a** : Amplify tweets i.e. Retweet tweets stored using -c.   
    * **no** : Number of tweets to amplify.
    * **timeout** : Time to wait in seconds before retweeting. 
