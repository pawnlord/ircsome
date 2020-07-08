```
----- ------ ------ ------ ------- --------- ------
----- --__-- --___- --___- --___-- --__-__-- - ___-
--|-- -|__|- -/---- -|---- -|---|- -|--|--|- -|----
----- -|-\-- |----- -|__-- -|---|- -|--|--|- -|___-
--|-- -|--\- |----- ----|- -|---|- -|--|--|- -|----
--|-- -|--|- -\___- -___|- -|___|- -|-----|- -|___-
----- -----  ------ ------ ------- --------- ------
```
# ircsome
A command-line IRC client made in python.
This isn't meant to be overly good, just some fun with IRC because I have always been interested in it.
## usage
Just run ircsome.py with python3. You are prompted with all information you need to go to a server.
Once in, syntax is as follows:
- Join always acts as the command. This will change
- When you put an exclimation point, that message sends as it would be in normal IRC protocol
    - For example, `!PRIVMSG guest hello!` would send a private message to guest containing the text hello.
    - For more commands, look at section 4 of (these docs)[https://tools.ietf.org/html/rfc1459#section-4.6.2]
- Anything else will be sent as `PRIVMSG <channel> <msg>`
    - For example, typing `hello!` in channel `#general` will send `PRIVMSG #general hello!`

## bugs and future needs
Orderd in how quickly they will be done.

### bugs:
- Not all PING messages are being returned with a PONG, which disconnects you from a server.

### needs:
- Privmsg with a user should be easier than having to type `!PRIVMSG <recipient> <msg>`
- Asynchronous messages (messages while you're typing a message) would be nice, but `input` is still annoying so I'd have to rewrite it, or do some really wild asychronous programming by using 2 different processes.