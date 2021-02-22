# Find Me My Lab

Web application to find an available lab host with specific software<br/>

# Live Demo
https://find-me-my-lab.herokuapp.com/<br/>

# Usage

Create a .env file at root directory with your ENCS account info
```bash
ENCS_LOGIN_NAME=your_login_name
ENCS_PASSWORD=your_password
``` 

Then install required packages by running
```bash
pip3 install -r requirements.txt
```

Then run a local server
```bash
flask run # To start a local flask server
or
heroku local # To start a local heroku server
```

# Documents
[Full instruction](https://www.concordia.ca/ginacody/aits/support/faq/connect-from-home.html)<br/>
[Software availability](https://www.concordia.ca/it/services/comp-labs-encs/windows-software-public-labs.html)<br/>
[cURL data for request](https://curl.trillworks.com/)<br/>