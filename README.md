# Disease Prediction API
---

## General Info

### About this Project
<p align="justify">
Nowadays, even with the fast development of technology, it is still hard to know what disease we have from the symptoms that we know without consulting directly to a doctor. We could search for the answer on the internet, but sometimes the result is inaccurate because of the limitation of what we could do on a search engine. What could we do to make disease prediction easier? With that problem in mind, we want to make it easier for everyone to gain information about their disease by using the help of machine learning. 
</p>

### Our Team Member
<center>

|          Nama         | Bangkit-ID |       Path       |
|:---------------------:|:----------:|:----------------:|
|  Daniel Syahputra Purba  |  M2010F1071  | Machine Learning |
|   Mardianto  |  M7010F1029  | Machine Learning |
|    Larasati   |  M7271F2361  | Machine Learning |

</center>

  
### Tech Stack
<p align="center">
  <img align="center" src="https://i.ibb.co/f0k1VN5/README-1.png" alt="tech-stack"/>
</p>

### Machine Learning Process
<p align="center">
  <img align="center" src="https://i.ibb.co/GHGGNvn/Bangkit-Capstone-Page-2.png" alt="ml-process"/>
</p>

### Project Repository
- [Android](https://github.com/KristiantoD/disease-prediction-app)
- [Cloud Computing](https://github.com/MatthewBrandon21/Disease-Prediction-API-Capstone)

## Online API
We also provide you an online API thay you can access through the link given: [API Documentation](https://ml.matthewbd.my.id/docs)

### How to Use This API
You can try how this API works via CURL command, API testing tools such as Postman, or directly via API documentation. If you want to try via CURL, We give you an example of CURL command below:

```
curl -X 'POST' \
  'https://ml.matthewbd.my.id/predict/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "desc": "my son is aggressive and violent does not listen, easily distracted"
}'
```

## Setup API in Local Environment
Before you go to the next step, I recommend to you to create your virtual environment for this project.
- Clone this repo using this command `git clone https://github.com/danielsyahputra13/ml_capstone.git`
- Run this: `cd ml_capstone`
- Install requirements or dependencies using `pip install -r requirements.txt`
- Run service using `uvicorn main:app --reload`

## Project Demo
[Project Demo](https://drive.google.com/file/d/1qUKOZaJ25uH5O0SklWD_agC6fS2ybLbn/view?usp=sharing)
