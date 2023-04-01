# Prolexa

#### A virtual assistant using ChatGPT.
---
## Quickstart
Instructions for Macos:

Installation:
```
pip3 install -U openai-whisper
pip3 install --upgrade openai
brew install ffmpeg
git clone git@github.com:the-real-finnventor/prolexa.git
cd prolexa
```

If you get errors like:
```
Cloning into 'prolexa'...
git@github.com: Permission denied (publickey).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```

Then try:
```
git clone git@github.com:the-real-finnventor/prolexa.git
cd prolexa
```

Edit:
```
ffmpeg -f avfoundation -list_devices true -i ""
```
Find the number of the audio device you want to use to record. I use `Built-in Microphone`.
```
open prolexa.py
```

Paste in your OpenAI API key that you can get it [here](https://platform.openai.com/account/api-keys) to where it says `sk-xxx`.

Also change `:4` to `:` then your audio devce number

Run:
```
python3 prolexa.py
```
