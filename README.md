# URL shortener

### Notes for interviewers
I am a slow person, so as you can see I didn't accomplish to fully finish the project.

Backend is built using Django, Django Rest Framework.
Frontend is build using React.js.

Some integrations tests were done. 
Couldn't pay too much attention to frontend (especially error messages etc.). But form validation both on frontend 
and backend was done. 

### Installation

In order to run the application in local environment follow instructions below.


  ```bash
  # clone
  git clone https://github.com/r-aliev/url_shortener.git
  
  ## For frontend
  cd url-shortener/frontend
  npm install
  npm start
  
  ### For backend
  cd url-shortener/backend
  source venv/bin/activate
  pip install -r requirements.txt
  pip install -r requirements_dev.txt
  + Create .env and put your postgres db credentials inside
  
  LOAD_DOT_ENV=1 python manage.py runserver
  
  