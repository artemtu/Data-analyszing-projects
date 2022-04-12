# Analyze for games store. Popular platforms and genres in different regions

Our client is a game store. We have some historical information about sales, rating from users and experts, genres and platforms from open-source data. We need to identify the patterns that determine the success of the game. This will allow you to bid on a potentially popular product and plan advertising campaigns.

We must:
1. Prepare the data (fill the gaps, change types of the data)
2. Count summary sales on the regions and add them to another column
3. Investigate the data:
 * How many games were released in other years? Is it significant to save all data?
 * Choose the platforms which gave more revenue. Create graphics
 * Create box plots for global sales games on the platform
 * How impact reviews of users and experts for the most popular platform? Create a scatterplot and correlation between reviews and sales
 * What genres are most popular and unpopular?
4. Create a users portrait for every region (NA, EU, JP)
 * TOP-5 popular platforms
 * TOP-5 genres
 * How are ESRB ratios impacting sales?
5. Check out hypotheses
 * The mean user ratio between Xbox One and PC is the same
 * The mean user ratio between 'Action' and 'Sports' isn't the same

Description of the data
 * Name — the name of the game
 * Platform 
 * Year_of_Release 
 * Genre 
 * NA_sales — sales in North America (millions)
 * EU_sales — sales in Europe (millions)
 * JP_sales — sales in Japan (millions)
 * Other_sales — sales in other regions (millions)
 * Critic_Score (max 100)
 * User_Score  (max 10)
 * Rating —  ESRB (англ. Entertainment Software Rating Board). Censure ratio for ages categories

## Conclusion

1. We found out that platforms live for four-six years, but user's behaviour doesn't match with trends
2. The most popular platforms are PS4 and Xbox one, especially in the USA. However, the store can order games for PS3 because this platform is popular in Europe, Japan and other counties
3. The most popular genres are 'action', 'shooter' and 'sport'. The censure ratio correlates with sales, but the user's ratio does not
4. We checked out two hypotheses, and as a result, the mean user's ratio between PC and Xbox one matched. But the mean user's ratio between 'action' and 'sport' doesn't do the same.

