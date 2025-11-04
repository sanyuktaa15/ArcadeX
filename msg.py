"""We’ve all sent a message we knew we shouldn’t. 🫣

Thankfully, technology is here to save the day! 🌟

Let's use .seek() and .truncate() to simulate unsending a message within a text file.

First, create a new sent_message.txt file and write a secret message to it:

sent_message = 'Hey there! This is a secret message.'

with open('sent_message.txt', 'w') as file:
  file.write(sent_message)

Read the message and use .seek() to move the cursor to the beginning (0):

with open('sent_message.txt', 'r+') as file:
  # Read the sent message from the file
  original_message = file.read()
      
  # Move the cursor to the beginning of the file
  file.seek(0)

Note: r+ in the open() function is used to indicate both reading and writing are allowed in the file.

# Modify the message to simulate unsending
unsent_message = 'This message has been unsent.'

Use .truncate() to reset the content to the length of the unsend message.
Save the new message to the file.
Print your messages!
Note: seek(0) is used to move the cursor to the beginning of the file before modifying the message.

Then, truncate() is used to adjust the file size to match the length of the new message. This simulates the act of unsending the message within the file.)"""

# Step 1: Write the original secret message
sent_message = 'Hey there! This is a secret message.'

with open('sent_message.txt', 'w') as file:
    file.write(sent_message)

# Step 2: Read and modify the message to "unsend" it
with open('sent_message.txt', 'r+') as file:
    # Read the original message
    original_message = file.read()
    
    # Move the cursor to the beginning of the file
    file.seek(0)
    
    # Define the new "unsent" message
    unsent_message = 'This message has been unsent.'
    
    # Overwrite the file with the new message
    file.write(unsent_message)
    
    # Use truncate() to cut off any remaining old text
    file.truncate(len(unsent_message))

# Step 3: Print both messages
print("Original Message:", original_message)
print("Updated Message:", unsent_message)
 