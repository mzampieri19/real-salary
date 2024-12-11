# Group 12 - Team Real Salry

## Authors: 

1. Anh le
2. Cheyanne Atole
3. Hanh Pham 
4. Michelangelo Zampieri

## Teaching Assistant 

1. Caroline Cunningham 

## Challange Advisors

1. Amy Shratter 
2. Chad Woodrick 

-------------------------------

This repository contains all of our work for this project. The following folders and files are included.

- word_frequency_analysis
1. Preliminary_Analysis.ipynb - This notebook contains the code for our original word frequency analysis as well as some prelimiary analysis of the data 
2. sector_JSONs - Directory of JSON files which holds word frequencies for each sector. 
3. selected_words_analysis - Directory containing filed for selected words analysis. 

- datasets (hidden since they are too large to upload to github, can be provided on request)
4. job_descriptions - Our original data set
5. filtered_country_work_type- Data set filtered by country and work type, nulls removed and company profile split into industry and sector.
6. mapped_sectors - Mapped industry to real-salary sectors. 

- testing
7. api.py - This was a test for an API call to predict metro area, this was scrapped due to issues in the data 
8. llama_api.ipynb - Used for testing of the llamma3 API, disregarded later was we decided to use ollama instead
9. ollama.ipynb - Contains code for testing of the ollama API. 
10. ollama_output_10_26.txt - This was a test for the output of the ollama model, tested our first prompt. 

- JSON_dictionaries 
11. job_function.json - The JSON object containing mapping of roles to predicted job functions.
12. industry.json- The JSON object containing mapping of companies to predicted industires. 

- Other files 
13. accuracy-test-ollama.ipynb - Our first round of testing for accuracy using the ollama model. This was done with the the complete list of industry and sectors. 
14. Analysis.ipynb - This is where we did the analysis for the shorter list of industries. 
15. job_function.ipynb - Notebook we used to predict job function. 

-------------------------------

## Overview of Project

We started our project by trying to understand our data, we did an inital preview of the dataset to try and get more familiar with it. This can be seen in 1. 

Next we began a word frequency analysis on the sectors, at first our aim was to try to get some relationships between sectors and words, which altough we did find, we realized this relationship was not super useful to our overall project. This can be seen in 1, 2, and 3. 

While working on the word frequency analysis we also began to work on the API call for the metro area prediction. Unfortunatly we realized this would not be possible due to the synthetic nature of our data set. Our initial work is in 7. 

Next we began to work on the API, specifically with the LLAMA API, this was our first attempt at using an AI API and while it went fine at first we realized we would have to pay to continue using this specific API. We ended up scrapping the idea while retaining what we learned to be used in the next API. This was done in 8.

Finally, we get to our most recent work, which is with the OLLAMA API, this API worked much better, first its run localy so there is no internet issues and its free! With this API we were able to get significant progress done and achieve great results. Everything is in 9, 10, 13, 14 with 15 continaing our latest and best results. 

We also included the datasets we used for this project. Our intial datset is from kaggle, which is extrenly large and pretty well organized, 4. Next we filtered the original data set into US only and full time listings, this was our baseline datset we used, 5. Lastly, we created a mapping of all industry to real-salary sectors, we saved this dataset as well, 6, which was used when predicting industry. 

## Current Results 

As of right now we are getting an accuracy of 60% with a response time of 1:37 minutes for 50 entries. This was achieved with a condensed list of indstries based on the list of industries given by our challange advisors. 

## Improved Results 

We were able to improve our accuracy a little but by changing our method. In our new method, we choose our compnaies at random anf then compare them to test for accuracy with this we got an average of 65% accuracy. 

## Company Dictionary

After we were satisfied with our accuracy we began to construct a dictionary of correctly predicted industires. This dictionary is called "prediction_dictionary.json" which maps company names to predicted industry. This dictionary is our "final" product and what we will give to our challange advisors. We will probably do something similar for job function. 

## Job Function

We took a similar approach to industry for job function, we used the API to map roles to predicted job functions. To help the API we gave it job description, responsabilities, and skills. 

-------------------------------

## Expanding the dictionaries 

To exapand the industry and job function dictionary all that is needed to be done is run analysis.ipynb to predict more industries and job_function.ipynb to predict more job_functions. 

---------------------------------

## Disclaimer 

All of the code, results, and artifacts in this repository are public and may be shared out if needed. 

---------------------------------

Thank you everyone for all your help and deidication to this project, please feel free to reach out if any questions arise!!
