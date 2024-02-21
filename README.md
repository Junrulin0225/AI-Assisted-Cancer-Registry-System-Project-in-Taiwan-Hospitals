#### Introduction
Welcome to the **AI-Assisted Cancer Registry System Project in Taiwan's Hospitals**🏥!

During my previous job working as a medical report analyst at IASL, Taiwan, I helped my team analyze our medical reports more efficiently with the help of Python and Excel.

In this project, we trained the AI-Assisted Cancer Registry System to fill up the correct medical codes for each feature (e.g. Primary Site, Histology, Pathological Grade, pT, ICD-10, ICD-O-3...) so cancer registers don't have to spend a lot of time filling up the columns manually. 

#### Workflow
- Step 1: We have to understand the meaning of each medical feature and code and how to decide which code to apply for each feature.




- Step 2: The data scientist will run the performance for each feature first based on the pre-build/pre-trained model which contains a lot of rules.




- Step 3: We utilize Excel to do the error analysis so we understand why AI filled up incorrectly. For the details of the error analysis and brief introduction/workflow please check 👉https://docs.google.com/presentation/d/1Crrhc7DIUsnR9lTOaAMdMKDzy6O2XHWxUdgXICo_418/edit#slide=id.p



- Step 4: Clean Data from

**Answer for Cancer.csv** 👉 **CountValues for Each Columns (Data_Cleaning).ipynb** 👉 **Col Counts.csv**

to see how many cases are correlated to each code of each column (e.g. feature). Turning the result into DataFrame makes it easier to read. 
ex: We see that for Pathological Grade (Grade_P), many cases are grade 1, 2, 3, 9, then we check the pathological report to see what keywords or contents determine grade 2 or grade 9.



- Step 5: (take uteri cancer for example) Calculate the AI score from

True data  **(True) Uteri Cancer.csv**
Predict data **(Predict) Uteri Cancer.csv**
👉 **Score for Each Column.py** 👉 **Uteri Score.csv**   



- Step 6: Compare AI scores between colleagues
  
**Score Comparison.csv**  👉 **Score Comparison.py**  👉 **Merge Compared.csv**

