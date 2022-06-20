import requests

new_user = {
    "text":'We reject the certified results of the 2020 Presidential election, and we hold that acting President Joseph Robinette Biden Jr. was not legitimately elected by the people of the United States,” reads the resolution, passed by voice vote in Houston on Saturday. “We strongly urge all Republicans to work to ensure election integrity and to show up to vote in November of 2022, bring your friends and family, volunteer for your local Republicans, and overwhelm any possible fraud.'
}

r = requests.post("http://127.0.0.1:5000/news", json=new_user)
print(r.text)