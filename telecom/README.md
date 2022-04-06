# Searching for an optimal tariff for telecom

The telecom operator suggests for clients two tariffs: "smart" and "ultra". The commercial department would like to know which tariff is more profitable. We have a data sampling with 500 users of the operator. This data shows where a client is from, how many messages and calls he has done, how many gigabytes he used, and what tariff he used. The main task: analyze the data and conclude what tariff is best for the company.

Description of tariffs:
 «smart»
- 550 rur per a month
- 500 minutes, 50 messages and 15 Gb of the internet
- extra tariffs:
  1-minute call: 3 rur; 
  SMS: 3 rur; 
  1 Gb: 200 rur; 
 
 «ultra»
- 1950 rur per a month
- 3000 minutes, 1000 messages and 30 Gb of the internet
- extra tariffs:
  1-minute call: 1 rur; 
  SMS: 1 rur; 
  1 Gb: 150 rur; 

*Important information: in the data, we will look at 0-minutes calls; it is missing calls*

Plan of analyzing:
1. Discovering the datasets
2. For every user, we should count:
 * how many calls he did and how many minutes he used per month;
 * quantity of sent SMS per month
 * how many Gb he used per month
 * month revenue from the user per a month
3. Count mean quantity, standard deviation and dispersion. Create histograms.
4. Check out 2 hypotheses:
 * mean revenue between tariffs "ultra" and "smart" has a difference
 * mean revenue between users from Moscow and other regions has a difference

We have 4 CSV files: 
1. users :
 * user_id
 * first_name 
 * last_name
 * age
 * reg_date — registration dare (day, month, year)
 * churn_date — user is quit from this tariff
 * city 
 * tariff — the name of the tariff
2. calls :
 * id — unique number of the call
 * call_date 
 * duration (minutes)
 * user_id 
3. messages:
 * id — unique number of the SMS
 * message_date 
 * user_id 
4. internet :
 * id — unique number of the session
 * mb_used 
 * session_date
 * user_id 
5. tariffs:
 * tariff_name 
 * rub_monthly_fee 
 * minutes_included  
 * messages_included 
 * mb_per_month_included (Mb)
 * rub_per_minute (extra tariff for calls)
 * rub_per_message (extra tariff for SMS)
 * rub_per_gb (extra tariff for the internet)

## Short conclusion
1. SMS is useless. Users prefer calls and the internet
2. The first hypothesis about the mean difference between "ultra" and "smart" was rejected. Mean count from "smart" gave us 1290 rur, "ultra" - 2070 rur
3. The Second hypothesis about mean revenue between users from Moscow and other regions wasn't rejected
4. The optimal tariff for the operator is "ultra"
