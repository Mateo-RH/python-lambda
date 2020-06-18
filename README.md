
# Research about local test of aws lambda with python

## Links: 
* [lambda and python packaging](https://www.serverless.com/blog/serverless-python-packaging/)
* [Serverless framework](https://www.npmjs.com/package/serverless)
* [Plugin for python requeriments](https://www.npmjs.com/package/serverless-python-requirements)
* [Plugin for offline testing](https://www.npmjs.com/package/serverless-offline)

## Before start
You need to have installed the followings:
* Python, pip, etc... (All that python stuff)
* npm
* docker

### Steps

1. Install serverless: $npm install -g serverless

2. Create lambda aplication: $serverless create \
  --template aws-python3 \
  --name numpy-test \
  --path numpy-test

  * [Other examples](https://github.com/serverless/examples)

3. Create venv inside the project: $virtualenv venv --python=python3 or >python3 -m venv venv

3.3.1 Activate venv: $source venv/bin/activate or >.\venv\Scripts\activate

4. Install your python packages and write down in the __requirements.txt__:  $pip install numpy && pip freeze > requirements.txt

5. Create a __package.json__: $npm init

**6.** Install the plugins dependencies: $npm i serverless-python-requirements serverless-offline

**7.** Configure your handler and serverless: check handler.py and serverless.yml for the configuration details

**8.** (Optional) for deployments you need aws credentials and configure it on serverless: $ serverless config credentials --provider aws --key YOUR_KEY --secret YOUR_SECRET

### Commands

* **Offline test**

```
$serverless offline
```

* **AWS deploy**

```
$serverless deploy
```
