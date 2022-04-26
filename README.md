# Automated Build and Deployments of Docker Images to Docker Hub via a CircleCI pipeline.

[**Session Recording availabe here**](https://stdntpartners-my.sharepoint.com/personal/ondiek_ochieng_studentambassadors_com/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fondiek%5Fochieng%5Fstudentambassadors%5Fcom%2FDocuments%2FRecordings%2FIntroduction%20to%20CI%5FCD%20with%20CircleCI%20%26%20Docker%20Hub%2D20220420%5F194042%2DMeeting%20Recording%2Emp4&parent=%2Fpersonal%2Fondiek%5Fochieng%5Fstudentambassadors%5Fcom%2FDocuments%2FRecordings&ga=1)


### Set up & Installation

1. Navigate into your desired folder, then clone this repo as shown, remember the dot (.) so as to avoid duplicating this repo's name again.

   `git clone https://github.com/Dev-Elie/CircleCI-to-DockerHub-Deployments.git .`

2. Change to that specific directory

   `cd directory path`

3. Create a virtual environment & activate it

   **Windows**
          
   ```bash
   #create a venv
   py -3 -m venv venv
   # activate venv
   venv\Scripts\activate
   ```
          
   **macOS/Linux**
          
   ```bash
   #create a venv
   python3 -m venv venv
   # activate venv
   source venv/bin/activate
   ```
      
4. Install the requirements from the requirements.txt file.

   `pip install -r requirements.txt`


5. Start the server

   `uvicorn app.main:app --reload`
   
   
   
  

