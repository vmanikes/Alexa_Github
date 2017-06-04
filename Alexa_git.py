from flask_ask import statement,Ask,question
from flask import Flask
from github import Github

app = Flask(__name__)
ask = Ask(app,"/")
g = Github("", "")


watched = []
subscriptions = []
starred = []
Repos = []
orgs = []
followers = []
following = []


#Number of repositories watching
for i in g.get_user().get_watched():
    watched.append(i)

#Number of subscriptions
for i in g.get_user().get_subscriptions():
    subscriptions.append(i)

#Number of Starred
for i in g.get_user().get_starred():
    starred.append(i)

#Number of Repos
for repo in g.get_user().get_repos():
    Repos.append(repo)

#Number of Orgs
for i in g.get_user().get_orgs():
    orgs.append(i)

#Number of Followers
for i in g.get_user().get_followers():
    followers.append(i)
#Number following
for i in g.get_user().get_following():
    following.append(i)

@ask.launch
def launch():
    return question("Hello KC! Do you want me to list your Github information").reprompt("Say yes or no. Don't waste my time sir")

@ask.intent("YesIntent")
def yes():
    msg = "You have {} Repositories. You have subscribed to {} Repositories. You are following {} Users. You are followed by {} Users".format(len(Repos),len(subscriptions),len(following),len(followers))
    return statement(msg)

if __name__ == '__main__':
    app.run(debug=True)

