# slack2discord
A python3 CLI program to migrate a full Slack workspace to Discord. 

# How to 

On the Slack workspace you administer, go to Workspace Settings  and click on "Import/Export data":
![image](https://user-images.githubusercontent.com/7917951/186669908-c2179578-a45e-418d-b05b-14abc974ad83.png)

Choose a date range and export the files:

![image](https://user-images.githubusercontent.com/7917951/186670106-2ebd0abb-2a49-48d7-8f67-92c7afcb0d47.png)


Note that private channels are __not__ exported. 

Slack says that "Workspace Owners on the Free and Standard plans must contact Slack and apply to export content from private channels and direct/group messages."
Paid workspaces can be exported in full (see https://slack.com/help/articles/201658943 for details)


Now that you have exported the public channels, you may download and unzip them .

In [migrate.py](https://github.com/lubianat/slack2discord/blob/master/src/slack2discord/migrate.py), change the MAIN variable to the path of the folder. 

To migrate this export to Discord, first create a discord bot.  You will need to create a bot account: https://discordpy.readthedocs.io/en/stable/discord.html 

![image](https://user-images.githubusercontent.com/7917951/186671829-af735879-42fd-413a-9c71-46f85ea2ac7e.png)
