# SLCB Spam Parameter

The Spam Parameter allows for creating custom commands to take user input, duplicate it
a specified number of times, and then have the bot post it to chat a specified number
of times.

## Installing

This script was built for use with Streamlabs Chatbot.
Follow instructions on how to install custom script packs at:
https://github.com/StreamlabsSupport/Streamlabs-Chatbot/wiki/Prepare-&-Import-Scripts

## Use

Once installed the below parameter can be inserted into custom commands created in SLCB.
Note: If the parameter is used everything else in the message outside of the first instance
of the parameters use will be ignore. 
```
$spam(
    (stream|discord),   # Chat Type: Specify whether to post the message to stream or to discord
                          Note: If set to stream and command called in discord. bot will post in 
                          stream and vice versa.
    number,             # Spam Count: Set the number of times for bot to post message
    number,             # Max Length: Set max character length of spam message. 
                          Limited to 400 for stream, 1795 for discord.
    (true,false),       # Allow Partial Message: Sets whether the duplicated user input will
                          truncate the final duplicate message or drop it entirely.
                          Ex: true: This is spam. This is spam. This is
                             false: This is spam. This is spam.
    string              # Message: The user input string to be duplicated and spammed.
)

Example Command: !command add !spam $spam(stream,1,400,false,THIS... IS... SPAM!!!)
Example Command: !command add !megaspam $spam(stream,5,400,false,PogChamp)
Example Command: !command add !megaspam $spam(stream,5,400,false,$msg)
```

Example in twitch chat:

![exspample](https://user-images.githubusercontent.com/50642352/72397338-357d7500-3705-11ea-907e-46b987052662.png)

## Author

EncryptedThoughts - [Twitch](https://www.twitch.tv/encryptedthoughts)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
