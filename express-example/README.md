# Express node webapp for devops candidate test

This is a bare bones express nodejs webapp that simply
responds with a Hello sentence when called with its url.

## How to get the application to run

* You need node version 12 or up
* Run `npm install`
* Run `node index`

That's literally it.  The application will then run and listen on port 3000 so you have to make sure your load balancer or api gateway or whatever you are using connects to that port.

## What to do (high level)

You need to create a 
pipeline that triggers when changes are pushed to git
and deploys this simple application to servers
that are auto-scaled to 3 instances during the day 8am - 6pm UTC,
and then auto-scaled down to 2 instances for the rest of the time.
You must also provide a single environment variable MYENVVAR
to the application, the value of which can be any arbitrary
string you like.

## What to do (the details)

We're looking for:

* Cloudformation to be used to create the auto-scaler and
any load balancers or api gateways etc
* The pipeline to be triggered when a push is made to the
master branch of the git repo
* The environment variable MYENVVAR must either be set in the 
environment before the application is started OR in a `.env`
file in the same folder as the application.  It *cannot* be stored in the git repo.
* A zip file of all the resources (scripts, cloudformation templates etc) you have created and any other documentation or screenshots you think we need to understand your solution.
* We do NOT need to see a demo or have access to the live version of your solution
* You do NOT need to use any custom domain names in the URL.  In other words we don't expect any domain registrations or DNS work to be done.
* You may use whatever git system you are familiar with, bitbucket or github etc, which obviously means you may copy this repo to anywhere you wish.  If your pipeline is built using the services of github or bitbucket, make sure you include screenshots of how you configured all of that.
* You should use your own AWS account whilst you develop all the resources for this test.  You may use whatever VPCs and other base resources you already have and we do NOT expect you to show us the
creation of all of those fundamental network resources in Cloudformation.



