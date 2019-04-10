# Note 1 - The following should be connected to a real database (using MySQL via the SQLite interface for example),
#         however the challenge states not to use a database, so I have used a fictional txt file with a list of customers and their numbers which is obviously not best practice. 

# Note 2 - I've applied for a business analyst position, not software development.
#         Therefore programming is not my greatest strength, so I have had to make some assumptions in the following code which I realise may not practically work when run.

# Note 3 - Thanks for taking the time to review my code.


#First API to "Get all phone numbers":
# Note 4 - As a business analyse I would question the endpoint required of getting all phone numbers,
# specifically the verb "get" as this implies to simply store in memory, but without displaying. Therefore I have displayed just incase this is the requirement.
def GetAllPhoneNumbers():
    usefile = open("fictionaldb.txt", "r") # Open fictionaldb.txt for reading text from the file.
    contents = use.read()                  # Read the file into a string.
    print contents                         # Display the contents of the file to the user.
    usefile.close()                        # Closes the file.

#Second API to "Get all phone numbers of a single customer":
# Note 5 - Again, the challenge uses the verb "get", which once in memory could be ambiguose and lead to data entry errors
#          if the no customer details are also retreived / displayed, so again as a business analyst I would be clarifying the aim of the endpoint.
def SingleCustomerAllNumbers():
    usefile = open("fictionaldb.txt", "r") # Open fictionaldb.txt for reading text from the file.
    contents = use.read()                  # Read the file into a string.
    lines = list(contents)                 # Store the contents of the file into a list format.
    loopgate=int(1)                        # Create a variable to be used in a loop.
    While loopgate==1                      # Initiate a While loop.
    customername=("Please enter the name of the customer to return all of their associated phone numbers") # Ask the user to enter the name of the customer whose phone numbers are to be displayed.
    if customername in lines:              # Check if the user response exists, if it does then run the following code...
        print item                         # print the line from the list which contains all of the phone numbers for the customer.
        usefile.close()                    # Closes the file.
        loopgate=(2)                       # Closes the loop.
    else:                                  # If the user respones does not exist the run the following code instead...
        print("That customer name does not exist, please try again.") # Display this response if the user entered a customer that does not exist.

#Third API to activate a phone number:
# Note 6 - I think this section should also contain a check to see if the number that is attempting to be activated is already activated, as this may identify a discrepency somewhere in a previous process that should be investigated.
def ActivatePhoneNumber():
    usefile = open("fictionaldb.txt", "r+") # Open fictionaldb.txt for reading and writing text.
    contents = use.read()                   # Read the file into a string.
    lines = list(contents)                  # Store the contents of the file into a list format.
    loopgate=int(1)                         # Create a variable to be used in a loop.
    While loopgate==1                       # Initiate a While loop.
    phonenumber=("Please enter the phone number to activate") # Ask the user which phone number they want to activate.
    if phonenumber in lines:                # Check if the phone number exists, if it does then run the following code...
        phonenumber.activate                # Activate the phone number, this assumers that the phone number has a property that can be activated.
        print("The phone number "+phonenumber+" is now activated") # Display a confirmation message. 
        usefile.close()                     # Closes the file.
        loopgate=(2)                        # Closes the loop.
    else:                                   # If it does not then run the following code...
        print("That phone number does not exist, please try again.") # Display this response if the user entered a phone number that does not exist.
        
        
    

