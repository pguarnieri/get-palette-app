The Get Palette App is a simple service that takes an input image and creates a new one with a colour palette at the bottom.

The service can be tried at: [getpalette.app](getpalette.app)

This is set up as serveless application hosted on AWS and written as a Python package.

The colour palette is created by applying the K-Means clustering algorithm on the RGB colour coordinates of the input image. The code runs on-demand using a Lambda Function triggered by a REST API. 

This is a side project by [Pierandrea Guarnieri](https://www.linkedin.com/in/pierandrea-guarnieri/) aimed at creating a demo end-to-end data science solution fully integrated with a cloud service. [Giuseppe Crinò](https://www.linkedin.com/in/giuseppe-crino-179bb071/) supported the AWS implementation and the integration with the GitHub CI/CD capabilities. [Marco Ontino](https://www.linkedin.com/in/marco-ontino/) developed and designed the website to make the service accessible by everyone.

*This project is not actively maintained, but feel free to get in touch if you have questions or suggestions.*

The main Python code is found in:
```
get_palette
```
The lambda function is found in:
```
lambda_function.py
```
The following script packages correctly all elements needed for the lambda function:
```
zip_lambda_function.sh
```
When the repo receives a new commit, the Lambda function is automatically updated using the GitHub CI/CD integration with file:
```
update_lambda.yml
```
