# Table of Content

* [Requirements](#Requirements)
* [Starting Bot](#Starting-the-Bot)
  * [Command](#Command)
  * [Example](#Example)
  * [Parameters](#Parameters)
# Requirements
twitter => [Detailed Information](https://pypi.org/project/twitter/)

Installing package: 
```
pip install python-twitter
```
# Starting the Bot

Start the bot by running 'driver.py'. 
## Command
```
python driver.py <[-l][-r]> <filename> <keyword> <prefix> <suffix>
```
## Example
```
python driver.py -l thor "Bruce Banner" The #Avengers
```
## Parameters

- **Model options**:
  - **-l** : Load model from file
  - **-r** : Read file to create model
- **Filename** : Name of pickle model file if load option set. Name of text file if read option set.  
- **Keywords** : Seedwords which are an intergral part of tweet. Keywords may be single or multiple. 
- **Prefix**   : Word/s to start the tweet with. Prefix may be single or multiple words. 
- **Suffix**   : Word/s to add at the end of tweet. Suffix may be single or multiple words. 