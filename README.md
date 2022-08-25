# slack2discord
A python3 CLI program to migrate a full Slack workspace to Discord. 

# How to 

After forking/cloning/downloading the repository:

## Exporting the Slack workspace

On the Slack workspace you administer, go to Workspace Settings  and click on "Import/Export data":
![image](https://user-images.githubusercontent.com/7917951/186669908-c2179578-a45e-418d-b05b-14abc974ad83.png)

Choose a date range and export the files:

![image](https://user-images.githubusercontent.com/7917951/186670106-2ebd0abb-2a49-48d7-8f67-92c7afcb0d47.png)


Note that private channels are __not__ exported. 

Slack says that "Workspace Owners on the Free and Standard plans must contact Slack and apply to export content from private channels and direct/group messages."
Paid workspaces can be exported in full (see https://slack.com/help/articles/201658943 for details)


Now that you have exported the public channels, you may download and unzip them .

In [migrate.py](https://github.com/lubianat/slack2discord/blob/master/src/slack2discord/migrate.py), change the MAIN variable to the path of the folder. 

## Creating a Discord bot

To migrate this export to Discord, first create a discord bot.  You will need to create a bot account: https://discordpy.readthedocs.io/en/stable/discord.html 

![image](https://user-images.githubusercontent.com/7917951/186671829-af735879-42fd-413a-9c71-46f85ea2ac7e.png)

After the bot is created, set up Oauth2 to authorize the bot on your channel:

![image](https://user-images.githubusercontent.com/7917951/186672932-b0b69f29-9201-4c46-ab45-53d17a0a1094.png)

Go to the URL Generator and generate an authentication URL:

![image](https://user-images.githubusercontent.com/7917951/186673472-0e60b916-25d3-4ddc-94de-5f8e7e5b43e9.png)

With the generated URL, you will be able to add the bot to your channel.  

Now on the bot page, get a token for your bot:

![image](https://user-images.githubusercontent.com/7917951/186673832-c8d5c75a-afc0-4a8e-988b-05a82fd71711.png)

On slack2discord add this token in a new file called "TOKENS.py" to a variable called "bot_token". 
This file shouldn't be committed to github and is automatically on gitignore. 

![image](https://user-images.githubusercontent.com/7917951/186673883-a6922fc4-9f58-403c-a02f-bada34aaffb0.png)

## Running the script

Now run the script on the command line ("python3 migrate.py"). 

The bot will now be active and listening. To effectively migrate, go on any discord channel and post the message "!slack2discord". The bot will start creating new channels and adding the information from the Slack workspace.


