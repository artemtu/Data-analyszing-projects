## Searching profitable marketing sources for "Yandex afisha"

We should find profitable advertisement sources.


The data from June 2017 to May 2018 :
- Log with visitors
- File with orders
- Advertisement statistic 

Tasks:
1. Product metrics
 * DAU, WAU, MAU, and create histograms
 * How many times do users visit a website? 
 * How many hours/minutes do users are looking at the website
 * Count the retention rate with cohorts
2. E-commerce metrics:
 * Analyze how much time (average count) is spent from the first visit to the order
 * Count mean quantity of orders per one user
 * Count AOV
 * Count average LTV in cohorts for six month
3. Marketing metrics:
 * Count sum on the marketing costs per sources. Create histograms
 * CAC
 * Count ROMI of cohorts per sources

Description of the data:
- visits_log.csv
 * Uid — unique ID of the user,
 * Device — the type of the device,
 * Start Ts — date and time when the user started a session,
 * End Ts — date and time when the user finished a session,
- Source Id 
 * orders_log.csv
 * Uid — unique ID of the user,
 * Buy Ts — date and time of the order,
 * Revenue — the sum of the order
- costs.csv
 * source_id — unique ID of advertisement source,
 * dt — date of the advertisement campaign,
 * costs — costs of advertisement campaign

# Short conclusion

Product metrics

1. Thankfully WAU & MAU could notice a peak of user's activity. It was between forty-two and fifty-two weeks of 2017
2. Users visit the website not more than one time per a day
3. The median time at the website = 643 seconds; as we could see on the histogram, it is unnormal. Mode = 60 seconds
4. Retention rate not perfect, in the second-month average count is 6.5%

E-commerce metrics

1. Users decided to buy less than one day
2. Average orders per user were in the first (2.19) and third (1.6) cohorts
3. AOV = 4.96, on the median = 4.5, peak were in last month 2017
4. The best result on LTV is the first and fourth cohorts


Marketing metrics

1. The summary cost of an advertising campaign is 329 thousand. Source #3 is a leader (141 thousand), sources #4(61 thousand) and #5 (51 thousand) 
2. The average CAC per user is 9 с.u. But in some sources average count is more than usual (like 14, 15, 16 c.u.)
3. The best profitable source is #1, but #5 has a prospect
