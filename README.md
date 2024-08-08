


Industries, companies, cities, households, etc., all consume energy. Both consumers and producers can benefit greatly from accurate estimates of 
future consumption. Therefore, the forecasts are also a key input of the decision-making process.
This particular project is about a Norweigien Manufacturing company where they want to predict their electricity load for the given hour. If the predicted load is higher than a decided threshold they will activate solar powered electricity as well for the continiuos operations.





Steps of creating API with FastAPI, containerizing it with Docker and Deploying in Azure Container registry and Azure container Instance

Create API  

1. Create main_api.py file
2. create test.py file

Testing on Local
1. run following commands on 2 seperate terminals

    uvicorn main_api:app in one terminal
    python test.py in another terminal
paste http://127.0.0.1:8000/docs

Creating docker image  - 

 1. create Dockerfile as done
 2. run the command

    docker build -t load-pred-api .      
    docker run -d -p 8000:8000 load-pred-api       

Deploying in Azure
 1. make resource group
 2. make container registry attached to resource group
 3. install Azure CLI on local
 4. Login to Azure:
        az login

5. Login to Azure Container Registry:
    az acr login --name <AzureContainerRegistryName>

        Use this command to authenticate with your Azure Container Registry. Check the "access keys" tab on ACR page. tick admin

6. List Docker Images:
    docker images

        This command lists all the Docker images available on your machine.

7. Tag Docker Image for ACR:
    docker tag <ImageName> <AzureContainerRegistryName>.azurecr.io/<ImageName>

        Tag your Docker image for upload to Azure Container Registry.

8. List Docker Images (Verification):
    docker images

        Verify the tagged Docker image.

9. Push Docker Image to ACR:
    docker push <AzureContainerRegistryName>.azurecr.io/<ImageName>

        Upload your Docker image to Azure Container Registry.check by going to repositories

10. Create Azure Container Instance:
    az container create --resource-group <ResourceGroupName> --name <ContainerName(giveAsYouWish)> --image <RegistryName>.azurecr.io/   <your-image-name>:v1 --dns-name-label <DnsNameLabel(GiveAsYouWish)> --ports 80

          Deploy your containerized application on Azure Container Instance.

11. Check Container Deployment Status:
        Go to container instance service . get FQDN 

