# Discovering the reliability of borrowers 

Our client is a credit department of a bank. We should discover how humans factor impact returns credits. The factors: married/unmarried, has children or no.

Tasks:
1. Check out the data and decide what should we do with gaps and duplicates.
2. Do we have anomalies in the data?
3. Add a column with the purpose of the credit.
4. Add a column with characteristics of the salary.
5. Give answers for the credit departments:
 * How do children impact returning of the credit?
 * How does marital status impact returning of the credit?
 * How does the grade of the salary impact return of the credit?
 * How do different purposes impact return of the credit?

## Description of the data
* children — quantity of childen in family
* days_employed 
* dob_years 
* education 
* education_id 
* family_status 
* family_status_id 
* gender 
* income_type 
* debt 
* total_income 
* purpose 

## Short conclusion
The most preferred borrowers are owners of flats. I guess these humans pay for the credit both and have a more stable job. Guys who had a wedding are also good creditors because they didn't take extensive credit and relatives present money. As a result, students and car owners aren't good clients for the bank. Obviously, students don't have a stable and good grade salary. Who bought a car can spend a lot of money on insurance and repair the car.
- The difference between those who have children and who haven't children is 2%
- Unmarried people have back payments of 10,1%, but married have 7,6%. Widows more preferable for the bank because, unlike different categories, they have back payments of 6,5%
- We separated people into different categories and saw that lower-class have more back payments (9,1%)
- Weddings and flats are the best categories for the bank. Worst - cars (9,3%) and education (9,1%)
