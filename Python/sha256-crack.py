from pwn import *
import sys

if len(sys.argv) != 2: # Pull command line arguments as input. Expecting only '1' input, not 2.
  print("Invalid arguments!") # Message if too many arguments are provided.
  print(">> {} <sha256sum>".format(sys.argv[0])) # Proper syntax for running the script.
  exit() # If user doesn't provide a hash, exit.

wanted_hash = sys.argv[1] # Takes the user entered hash as the first argument, setting as variable.
print(wanted_hash) # Print the entered hash for verification
password_file = "rockyou.txt" # Assign our password file to variable password_file
attempts = 0 # Track number of attempts made when cracking

with log.progress("Attempting to crack: {}!\n".format(wanted_hash)) as p:
  with open(password_file, "r", encoding='latin-1') as password_list: # Open the password_file in read mode, with 'latin-1' encoding as the variable password_list
  	for password in password_list: # Iterate over each password in the file
  	  password = password.strip("\n").encode('latin-1') # Clean up the trailing new line to ensure correct hash values
  	  password_hash = sha256sumhex(password) # Pwn module for gathering the SHA256 sum of the password being checked
  	  p.status("[{}] {} == {}".format(attempts, password.decode('latin-1'), password_hash)) # Update the status of our log.progress with our attempts and passwords attempted
  	  if password_hash == wanted_hash: # Comparison of the password hash with the provided hash value.
  	  	p.success("Password hash found after {} attempts! {} hashes to {}".format(attempts, password.decode('latin-1'), password_hash)) # If a successful hash value has been found, update the status of our log.progress and display a message.
  	  	exit() # Exit if valid hash value matches
  	  attempts += 1 # Increase number of attempts if no match is found
  	p.failure("Password hash not found!") # Display message if no password is found at all.