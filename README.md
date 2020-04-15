# Predicting the artist from the artwork webapp
This project was performed for my course CSYE 7374 - Parallel Machine Learning and AI. The main goal of the course was to understand
parallel processing and hardware abilities while training machine learning model. The main results along with the project report
can be found at [Hardware Comparisons for ML - CPU vs GPU](https://github.com/akmenon1996/Harware_Comparison-GPUvsCPU-/blob/master/instructions.md)

In this repository, I take you through the ML side of the project via a web application. 

## Getting started with deploying this application. 

- Clone this repository to your workstation. 
```shell
$ git clone https://github.com/akmenon1996/Artwork-artist-prediction-webapp.git
```
- Move into repo directory. 
```shell
 $ cd Arwork-artist-prediction-webapp
 ```
- Install requirements by running 
 ```shell
 $ pip install requirements.txt
 ```
- Download the trained model file and place it in the /models directory with the name 'trained_model' by 
following Instructions under [this repository](https://github.com/akmenon1996/Harware_Comparison-GPUvsCPU-/blob/master/instructions.md)
- Run the script by running app.py
 ```shell
 $ python app.py
 ```

- Go to http://localhost:5000 (Preferebly on a Safari/Mozilla browser)

- Upload a picture of a painting. (There are a few sample images that you can use in the /uploads folder. 

:point_down: Screenshot:

<p align="center">
  <img src="https://github.com/akmenon1996/Artwork-artist-prediction-webapp/blob/master/display_outputs/home_page.png" height="480px" alt="">
</p>

## Run with Docker

Using the **[Docker](https://www.docker.com)** image you should be able to set up the instance pretty easily as well. :whale:


1. First, clone the repo
```shell
$ git clone https://github.com/akmenon1996/Artwork-artist-prediction-webapp.git
$ cd keras-flask-deploy-webapp
```
2. - Download the trained model file and place it in the /models directory with the name 'trained_model' by 
following Instructions under [this repository](https://github.com/akmenon1996/Harware_Comparison-GPUvsCPU-/blob/master/instructions.md)

3. Build Docker image
```shell
$ docker build -t artist-pred-app .
```

4. Run!
```shell
$ docker run -it --rm -p 5000:5000 artist-pred-app
```



Open http://localhost:5000 and wait till the webpage is loaded.

<p align="center">
  <img src="https://github.com/akmenon1996/Artwork-artist-prediction-webapp/blob/master/display_outputs/output_image.png" height="480px" alt="">
</p>


Shout out to [Supratim Haldar](https://supratimh.github.io/) for the baseline machine learning model code on top of which I built for comparisons across hardware.
