# purview-serverless

In this repo, you will find a sample project that showcases the use of the Python SDK of [Azure Purview](https://azure.microsoft.com/en-gb/services/purview/).

# Content

We cover the typical use-case of a company that owns a DataLake, and wants to scan its assets with Purview. 
We provide:

* A sample code that uses the [Azure Purview Scanning](https://azuresdkdocs.blob.core.windows.net/$web/python/azure-purview-scanning/1.0.0b2/index.html) and [Purview Catalog ](https://azuresdkdocs.blob.core.windows.net/$web/python/azure-purview-catalog/1.0.0b2/index.html) SDKs to do the most common operations in Python, namely:
    * Registering a datasource
    * Deleting a datasource
    * Creating a scan
    * Running a scan
    * Retrieving datasources
    * Retrieving scans and their runs histories
    * Searching the Purview catalog

* A basic serverless Architecture composed of:
    * Azure Storage 
    * Python Function App 
    * App Service Plan
    * Azure Purview instance
    * App Insights instance 
    
* An ARM Template to deploy the following architecture:

    <!-- [PUT DIAGRAM] -->

# How to use 
## Deploying the infrastructure
You have two options to deploy the infrastructure with the provided [ARM Template](https://docs.microsoft.com/en-us/azure/azure-resource-manager/templates/overview).

### Option 1: Deploy the ARM template via the portal
Click on the following button: 

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fatrao%2Fpurview-serverless%2Fdocumentation%2Finfra%2Fazuredeploy.json) 


You can choose an existing ressource group in the drop-down menu or a create a new one. Click on "Review + Create". Select "Create" once the validation succeeds.

### Option 2: Deploy the ARM via the Azure CLI
This option requires the [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli) to be installed.

1. Log in to you Azure account 

    ```
    az login
    ```

2. Create a Resource Group 

    ```
    $resourceGroup = "MyResourceGroupName"
    $location = "westeurope" 
    az group create -n $resourceGroup -l $location
    ```

    NB: You can find the list of all the Azure regions byentering the following command:
    ```
    az account list-locations -o table 
    ```

3. Deploy the resources 
    ```
    az deployment group create --resource-group $resourceGroup --template-file ./infra/azuredeploy.json
    ```



## Deploying the Function App 
You can deploy the Function App in various ways. Here we presentt two of them: via Visual Studio Code or the Azure CLI.

### Option 1: Deploy with VS Code
This option requires the installation of [Visual Studio Code](https://code.visualstudio.com/) and the [Azure Functions extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions).

Steps:
1. Open a new VS Code window

2. Manually clone this repo or click on "Clone Git Repository" in VS Code    

3. Create an environment and install the required packages
    ```
    python3.8 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

4. Go on the Azure Extension tab and roll out Functions. The Function App appears under the "Local Project" folder.
    <!-- Include image here  -->





### Option 2: Deploy with the Azure CLI



##  Running the functions
### Run the functions locally 
To run the functions locally, you need have the needed packages installed, as described above. 
<!-- [Insert link here to the descirption] -->


### Examples
<!-- Notes on choices (Storage Kind) -->
Examples of code 
