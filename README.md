# purview-serverless

In this repo, you will find a sample project that showcases the use of the Python SDK of Azure Purview [LINK] 

# Content

In this repo, we cover the typical use-case of a company that owns a DataLake, and wants to scans its assets with Purview. 
We provide:

* A sample code that uses the Azure purview Scanning [PUT LINK] and Catalog [PUT LINK] SDKs to do the most common operations in Python, namely:
    * Registering a datasource
    * Deleting a datasource
    * Creating a scan
    * Running a scan
    * Retrieving datasources
    * Retrieving scans and their runs histories
    * Search the Purview catalog
    
* A basic serverless Architecture composed of:
    * Azure Storage 
    * Python Function App 
    * App Service Plan
    * Azure Purview instance
    * App Insights instance 
    
    [PUT DIAGRAM]
    
* An ARM Template to deploy the architecture
    
[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://raw.githubusercontent.com/atrao/purview-serverless/documentation/infra/azuredeploy.json?token=AUMPCYFDZFR6OHDUUHUIK6TB2M7SK)