# Devops Test Solution - Express Web App

## How to get the application to run

### - Run the Cloudformation scripts:  Loadbalancer.yaml, and Autoscaling_Template.yaml

    1. The loadbalancer needs to be created first, as it exports some outputs used by the AutoScaling Group.

    2. To run these templates, the assumption is that you have a keypair, subnets. 
    
    3. Please take note of your ALB stack name when running the ASG template. It is a required parameter. 


### - Parameter Store in AWS System Manager - 
    It is required to create a parameter called ENVVAR. The value of which can be any arbitrary string you like.

### - AWS CodeDeploy  

    1. In CodeDeploy - Create an Application, e.g. Atheneum-CodeDeploy
    2. Create a Deployment Group - Atheneum-CodeDeploy-DG
    3. Ensure to have a CodeDeploy Service Role
    4. Choos In-place for the deployment type, as this is a test.
    5. You can select the Name Tag on your running EC2 instances -      ExpressApp. You should find 1 unique matched instance.
    6. Setup Pipeline as shown in the screenshots attached with this repo.
    7. Leave the remaining options as defaults. 
    8. Do not enable Load balancing in your code deploy settings

### - AWS CodePipeline - 
    1. Create a Pipeline - AtheneumCodePipeline
    2. Choose Source Provider as GithubV2, and connect to Github. The source provider can also be Bitbucket.
    3. Skip build stage
    4. Choose CodeDeploy as Deploy Provider, and choose the earlier configured application and Deployment Group settings

Once the Pipeline is created successfully. Check the ALB DNS URL.
 

### - Troubleshooting:
    See express-app.log in the root expressapp folder
    sudo service expressapp status - to check the state of the app
    


That's it. 

When all the prerequisites are running, you should be able to reach the application directly only via the Application Load balancer DNS URL. You can find that in the output section of the Loadbalancer Cloudformation stack.

Thank you.




