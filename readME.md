# Ethereum Wallet and Blockchain Explorer

A terminal application in Python which pulls data from the Ethereum Blockchain and etherscan.io API. Tracking any single wallet’s data history and the live/historical information of the entire blockchain presented in MatPlotLib.

## Description

As you might have guessed by looking at my other projects I am quite interested in the Crypto sphere. Not so much the currencies, more so the technology. So I set about making a nice little project to navigate the land of Ethereum. My inital plan was to download the entire Ethereum blockchain, throw it into a database and navigate it from there. Sadly, the Ethereum blockchain is almost 250gb in size and I don't really have that storage freely sitting about.

<p align="center">
  <img src="https://user-images.githubusercontent.com/70699565/122992854-82f01e00-d39e-11eb-8196-e84ead919a50.png">
</p>

So I found some APIs which allowed me to abstract me downloading the entire chain away.

<p align="center">
  <img src="https://user-images.githubusercontent.com/70699565/122992881-8b485900-d39e-11eb-8129-8e8d7f0b8730.png">
</p>

My application has way way way less functionality than the Etherscan.io and the like. But that doesn't matter, I learnt a fair bit about extracting and manipulating data from APIs etc.

<p align="center">
  <img src="https://user-images.githubusercontent.com/70699565/122992897-913e3a00-d39e-11eb-9478-d1cbc82bb4fb.png">
</p>

In future updates I might make it so you can save output data to a file. Yet to be decided.

<p align="center">
  <img src="https://user-images.githubusercontent.com/70699565/122992915-9602ee00-d39e-11eb-93f1-7147aef0c562.png">
</p>

## Getting Started

There's not much to the 'getting started' install and run

### Dependencies

* Python

### Installing

* The folder is small and can be simply downloaded and run as is

### Executing program

* Navigate to the Tracker folder
* key in:
```
python main.py
```

## Help

The etherscan API has a pro/paid tier which is needed for the program to fully run.. I'm too stingy at the moment to pay

## Authors

Contributors:

    * Me

## Version History

* 0.1
    * Initial Release

## License

I have no idea
