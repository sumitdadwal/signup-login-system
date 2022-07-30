Instructions:

Use the following commands to run the code:

- git clone https://github.com/sumitdadwal/signup-login-system.git

- pip install -r requirements.txt

- cd backend

- uvicorn main:app --reload

Once the program is up and running:

- Go to http://localhost:8000/docs through your web browser

- Click on Cretae User
- Then click "Try it out" to create a user.
- Then you can go to login to login through that user.


Functioning:
- Once the user is created, user will be stored in SQLlite database under user table.
- Password will be hashed for security purposes.