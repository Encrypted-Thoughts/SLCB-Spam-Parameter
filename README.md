========================================================================================
=======================================[ Credits ]=======================================
=========================================================================================

Script made by:         EncryptedThoughts
Twitch:                 http://www.twitch.tv/EncryptedThoughts

=========================================================================================
=======================================[ Script Changes ]================================
=========================================================================================

1.0.0 - Script made. Only tested with Twitch and Discord.

=========================================================================================
==================================[ Future implementations ]=============================
=========================================================================================

I dunno, whatcha want it to do?

=========================================================================================
=======================================[ About ]=========================================
=========================================================================================

The Spam Parameter allows for creating custom commands to take user input, duplicate it
a specified number of times, and then have the bot post it to chat a specified number
of times.

=========================================================================================
=======================================[ Instructions ]==================================
=========================================================================================

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
