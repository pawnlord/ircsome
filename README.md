```
----- ------ ------ ------ ------- --------- ------
-___- --__-- --___- --___- --___-- --__-__-- - ___-
--|-- -|__|- -/---- -|---- -|---|- -|--|--|- -|----
--|-- -|-\-- |----- -|__-- -|---|- -|--|--|- -|___-
--|-- -|--\- |----- ----|- -|---|- -|--|--|- -|----
-_|_- -|--|- -\___- -___|- -|___|- -|-----|- -|___-
----- -----  ------ ------ ------- --------- ------
```
# ircsome
A command-line IRC client made in python.  
This isn't meant to be overly good, just some fun with IRC because I have always been interested in it.  

## usage  
Just run ircsome.py with python3 in the top directory (for example, if it's stored in `/home/guest/ircsome`, run it there). 
The syntax is:  
```
python3 ircsome.py [-a <address>] [-p <port number>]
```
If the address or port number aren't provided, it goes to the default set in the config (see the config section for more details).  
You are prompted with all information you need to go to a server.  
Once in, syntax is as follows:  
- Join always acts as the command. This will change  
- When you put an exclimation point (or whatever you set in config), that message sends as it would be in normal IRC protocol  
    - For example, `!PRIVMSG guest hello!` would send a private message to guest containing the text `hello!`.  
    - For more commands, look at section 4 of (these docs)[https://tools.ietf.org/html/rfc1459#section-4.6.2]
    - If you set `CMD_STR` to `cmd` in the config, the equivalent would be `cmdPRIVMSG guest hello!`.  
- When you put an @ (or whatever you set in config) at the beginning, it PM's that person  
    - For example, `@guest hello!` will send guest a private message containing `hello!`.
    - If you set `PM_STR` to `pm` in the config, the equivalent would be `pmguest hello`.   
- Anything else will be sent as `PRIVMSG <channel> <msg>`  
    - For example, typing `hello!` in channel `#general` will send `PRIVMSG #general hello!`  

## config
The config can be used to customize ircsome. It is stored in `default.cfg`, so any changes should be done to that.  
The available config options go as follows:  
- **TITLE_COLOR:** color to be used for the introduction title, available colors are RED, YELLOW, BLUE, ORANGE, PURPLE, LIGHT_BLUE, and NONE  
- **BODY_COLOR:** color to be used for introduction paragraph  
- **INPUT_COLOR:** color to be used when asking for non-message related info (password, nickname, username, and real name)  
- **NAME_COLOR:** color to be used for names (your`s and others).  
- **TEXT_COLOR:** color to be used for message text.  
- **CHANNEL_COLOR:** color to indicate the channel next to your name.  
- **CMD_STR:** string to start writing a command instead of message  
- **PM_STR:** string to start writing a private message instead of message  
- **DEFAULT_IP:** default IP for server if none is provided (this is mainly for easier testing).  
- **DEFAULT_PORT:** default port for server if none is provided.  

For example, if you wanted to set `TITLE_COLOR` to `RED`, simply type `TITLE_COLOR RED` into the config file.  
If you had multiple things setting `TITLE_COLOR`, the last one in the file would be used.  

## bugs and future needs
Orderd in how quickly they will be done.  
 
### bugs:
- PING messages are only being returned when you send another message. This relates to the 2nd need.  

### needs:
- Separate channel messages from pm's   
- Asynchronous messages (messages while you're typing a message) would be nice, but `input` is still annoying so I'd have to rewrite it, or do some really wild asychronous programming by using 2 different processes.  
- Actual ssl encryption (hardest thing here).  

### unknowns:
- Colors might create errors on unsupported systems. Add this to the config.  