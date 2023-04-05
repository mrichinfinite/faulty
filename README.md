# faulty
Bot that sends a message to a Webex space when a new fault is detected in an ACI fabric.

*This is a work in progress and by no means a finished product. If you have any ideas or suggestions, please let me know by submitting an Issue.

Instructions on how to create your own bot:

1. Navigate to developer.webex.com and sign in.

2. Click on your icon in the top right corner of the page and select "My Webex Apps".

3. Click on "Create a New App".

4. Click on "Create a Bot".

5. Fill out the details for your bot and click on "Add Bot".

6. Copy your bot's access token.

7. Paste your bot's access token into the ACCESS_TOKEN variable in the access.py file (after "Bearer").

8. Navigate to the Webex app.

9. Create a new space or navigate to an existing space.

10. Add your newly created bot to the Webex space.

11. Obtain the Webex space ID by using the CTRL + SHIFT + K keyboard shortcut on Windows or Option + Command + K on Mac. After executing the keyboard shortcut, the space ID (along with some other information) is copied to your local machine's clipboard. Paste this information into a text file, then copy the space ID value only.

12. Navigate to developer.webex.com/docs/api/v1/rooms/get-room-details and paste your Webex space ID into the roomId parameter in the URI for the GET request.

13. Click on the Run button.

14. Copy the value of the id key in the JSON response and paste it into the ROOM_ID variable in the access.py file.

Your bot will now send you messages to the specified space each time a new fault is generated in the fabric! Please note that the bot will send messages for each transition of a fault and for every severity. The code can be altered to not send a message for each transtion and to only send messages for a specific severity, if needed.
