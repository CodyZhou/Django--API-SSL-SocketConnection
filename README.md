Python Test Project
===================================
Description
---------------------------------
  This is a Python Project for Test. It is use Python + Django + RESTful framework to build a REST Api for clients. This is a client/server framework. When clients get some seriously problems, they can send a JSON error message to this master server through the REST Api, then the api could check the informaiton from clients and send the information (OR command) to the master server through socket connection, then the master server can write the error message to a file for checking. (It is means that you can sepreate the api and the master server, deploy them on different servers.) The communication between the master server and the api is encrypted by a pair of ssh key (Public Key / Private Key) with Python PyCryptodome library. 
  
  
Installation
-----------------------------------
  Because of the special functions in this projects, please install these major special libraies before you try this project. These major special libraies listed as below, also, you can find these major special libraies information in the ./requirements.txt file.
  * Django==1.10.5 : Django Framework.
  * djangorestframework==3.6.2 :  Django RESTful framework.
  * pycryptodomex==3.4.5 : RSA encrypt / decrypt library. 
  * python==3.4.4
  * other libraries.
  
  You can use the command as below to export these libraries.

    pip install -r requirements.txt
  
  OR, you can export the libraries you need by the commands as below.

    pip install Django==1.10.5
    pip install djangorestframework==3.6.2
    pip install pycryptodomex==3.4.5
    pip install python==3.4.4
  	
  	
How It Works
------------------------------------

### Step 1 - Check Settings
  Check the **./pythontest/settings.py** file to make sure the settings are correct. Make sure the public key and the private key are the correct positon, which the sofeware can find them. The section of ssh key files set up as below:

    PUBLIC_KEY = os.path.join(BASE_DIR, 'mypublickey.key')
    PRIVATE_KEY = os.path.join(BASE_DIR, 'myprivatekey.key')
    SECURITY_CODE = 'pythontest'

  **The 'SECURITY_CODE' is the passphrase for the ssh key files, please do not change it.**
	
### Step 2 - Set up for the master server
  Still in the **./pythontest/settings.py** file, set up the message file, the host and the port for the master server.

    SERVER_RECV_MESSAGE_FILE = os.path.join(BASE_DIR, 'master_server_recv_message.txt')
    SERVER_HOST = 'localhost'
    SERVER_PORT = '4444'
	
### Step 3 - Start the master server
  At the base dir of the project, use the command to execute the master server.

    python masterserver.py

  Then you will see the message on the screen as below:

    Master Server Started ... 
    Master Server is listen localhost:4444 ...

  **Do not stop the master server untill you finished all jobs.**
	
### Step 4 - Start the django framework
  At the base dir of the project, use the command to start the django framework.

    python manage.py runserver

  Then, you can go to your browser, and input the url as below:

    http://127.0.0.1:8000/api/master/
	
### Step 5 - Do Test
  At the browser, you can use the data as below to test the server. Copy the data and paste to the "Content" area, then click 'POST' button.

    {
        "command": "run",
        "message": "This is a test information from api!"
    }

  If anything is working well, you will see the result on the screen.

    HTTP 200 OK
    Allow: GET, POST, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept
    {
        "result": "successful"
    }
	

Contact Me
------------------------------------------------
  Email: codysbusiness050917@gmail.com
	
