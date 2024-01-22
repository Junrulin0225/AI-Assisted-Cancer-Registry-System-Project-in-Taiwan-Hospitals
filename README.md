#### Introduction
Welcome to the **AI-Assisted Cancer Registry System Project in Taiwan's Hospitals**🏥!

During my previous job working as a medical report analyst at IASL, Taiwan, I am grateful for the chance to help my team analyze our medical reports more efficiently with the help of Python and Excel.

In this project, we trained the AI-Assisted Cancer Registry System to fill up the correct codes for each feature (e.g. Primary Site, Histology, Pathological Grade, pT,...) so the cancer registers don't have to spend a lot of time on filling up the columns manually. 

#### Workflow
- Step 1: Clean Data from

**Answer for Cancer.csv** 👉 **CountValues for Each Columns (Data_Cleaning).ipynb** 👉

in order to see how many cases are correlated to each code of each column (e.g. feature). Turning the result into DataFrame makes it easier to read. 
ex: We see that for Pathological Grade (Grade_P), many cases are grade 1, 2, 3, 9, then we check the pathological report to see what keywords or contents determine grade 2 or grade 9.

- Step 2: (take uteri cancer for example) Calculate the AI score from

True data  **(True) Uteri Cancer.xlsx**
Predict data **(Predict) Uteri Cancer.xlsx**
👉 **Score for Each Column.py** 👉 **Uteri Score.xlsx**   

- Step 3: Compare AI scores between colleagues
  
**Score Comparison.xlsx**  👉 **Score Comparison.py**  👉 **merge compared.xlsx**




#### Brief Introduction and Workflow click here 👉https://docs.google.com/presentation/d/1Crrhc7DIUsnR9lTOaAMdMKDzy6O2XHWxUdgXICo_418/edit#slide=id.p
