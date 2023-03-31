# Prolexa

#### A virtual assistant using ChatGPT.
---
## Quickstart
Insructions for Macos:

Installation:
```
pip3 install -U openai-whisper
pip3 install --upgrade openai
brew install ffmpeg
git clone git@github.com:the-real-finnventor/prolexa.git
cd prolexa
```

Edit:
```
ffmpeg -f avfoundation -list_devices true -i ""
```
Find out what number the audio divice you want to use is.
```
open prolexa.py
```

Paste in your OpenAI API key that you can get it [here](https://platform.openai.com/account/api-keys) to where it says sk-xxx

Also change `:4` to `:` then your audio devce number

Run:
```
python3 prolexa.py
```
