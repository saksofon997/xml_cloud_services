# Cloud Services

Extension of Cloud Services from XML WS course project. Email and Vehicle Location FaaS Lambdas hosted on AWS.

## Requirements

- [Install serverless][sls-install] framework. 
- [Configure AWS][sls-config] account.
- [Install Docker][docker-desktop].
- [Install Python 3.8][python-3.8].

## Configuration

The application uses the serverless framework to deploy backend API. 
To run the application you need to provide environment variables listed below.

| Variable       |      Description      | AWS SSM Path                         |
|----------------|:---------------------:|--------------------------------------|
| MAIL_LOGIN     | Email login           | /xmlws/[stage]/email/login           |
| MAIL_PASSWORD  | Email password        | /xmlws/[stage]/email/password        |


Required variables should be stored on the AWS System Management Parameter Store for the deployed application.
Retrieval of variables should be described using a [serverless.yml][sls-config] file.

For the local running of the application, they should be stored in `.env` (place it in `root` folder) file in the form `AWS SSM Path = value`, for example:
```markdown
/xmlws/dev/version=0.0.1
```

## Plugins

To install all required plugins type the command ```npm install```.
Note that you need to update [package.json][npm-pckg] file anytime you add new plugin. 

## Dependencies

Python libraries are managed using [serverless-python-requirements][sls-python-req] plugin. 
This plugin automatically bundles dependencies from [requirements.txt][pip-req] and makes them available in your `PYTHONPATH`.
So, if you want to add a new python library, just add it to the [requirements.txt][pip-req] file.

## Running

To run the application locally you should use [serverless offline][sls-offline] plugin.
Python is needed for local running.

Type command:
```bash
sls offline
```
The server will be started on `localhost:3000`. 

Do not forget, that every route has a stage as a prefix.
For example route defined in `serverless.yml` as `/status` should be available at `localhost:3000/dev/status`. 

## Deployment

To deploy the server type command below. Docker is needed for server deployment.

```bash
sls deploy
```

## Testing

To run the test do next steps. Python is needed for running tests.

Activate Python virtual environment:
```bash
source ./venv/Scripts/activate
```

Next run tests with command:
```bash
python -m pytest
```

[sls-install]: https://serverless.com/framework/docs/getting-started
[sls-config]: https://serverless.com/framework/docs/providers/aws/cli-reference/config-credentials
[sls-offline]: https://github.com/dherault/serverless-offline
[sls-python-req]: https://serverless.com/plugins/serverless-python-requirements
[pip-req]: requirements.txt
[sls-conf]: serverless.yml
[npm-pckg]: package.json
[docker-desktop]: https://www.docker.com/products/docker-desktop
[python-3.8]: https://www.python.org/downloads/
