# Deploying to Azure App Services

App created on Azure App Services as:

```
az webapp up --sku F1 --location "West US 2" --name rethinksmoking
```
To deploy updates, issue the same command as used to create the app.

Reference:
[Quickstart: Create a Python app in Azure App Service on Linux](
https://docs.microsoft.com/en-us/azure/app-service/containers/quickstart-python)

App is configured as:
```
az webapp config set --resource-group pnovak2_rg_Linux_westus2 --name rethinksmoking --startup-file "gunicorn --bind=0.0.0.0 --timeout 600 --log-level debug --capture-output \"rethinksmoking.flask_app:create_app()\""
```

The option `--log-level debug` means `gunicorn` logs more debugging output, including which end points or routes are queries, and with which methods. The option `--capture-output` means that any `print()` function calls will be logged, and not lost. The command at the end `"rethinksmoking.flask_app:create_app()"` specifies how the `gunicorn` WSGI server should start and run the Flask app in the rethinksmoking package.

Reference: [Configure a Linux Python app for Azure App Service](https://docs.microsoft.com/en-us/azure/app-service/containers/how-to-configure-python#flask-app)
