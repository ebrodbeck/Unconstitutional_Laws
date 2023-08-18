# Unconstitutional_Laws
An Analysis of Laws Held Unconstitutional in Whole or in Part by the Supreme Court - https://constitution.congress.gov/resources/unconstitutional-laws/

First, I started with this website which has tabulated all unconstitutional laws and their associated details.
## Data Source
![Source Data](https://github.com/ebrodbeck/Unconstitutional_Laws/blob/main/Data%20Source.png)

## Total Unconstitutional Laws by State
![Total Unconstitutional Laws by State](https://github.com/ebrodbeck/Unconstitutional_Laws/blob/main/Total%20Unconstitutional%20Laws%20by%20State.JPG)
After formatting the data, here are the quick hits relating to the main question. Note that the Federal government has had more than 2x the amount of laws overturned as the highest state (NY). To keep the plots interesting, I'll omit the Federal government from the rest of the analysis.
One might see these plots and say "some states have existed longer, so the data is biased". Good point, lets examine that.
## Unconstitutional Laws per Decade by State
![Unconstitutional Laws per Decade by State](https://github.com/ebrodbeck/Unconstitutional_Laws/blob/main/Unconstitutional%20Laws%20per%20Decade%20by%20State.JPG)

Examining the scatter plot, there is a clear trend indicating that the amount of time a state has existed is correlated with the number of laws it has that were found unconstitutional. To normalize this, both plots show the average unconstitutional laws written per decade (total uncon. laws divided by state lifetime, x10 years). While states like Rhode Island, Delaware, Vermont, and New Hampshire have existed since the beginning of the dataset and had relatively few constitutional oversteps, the same can't be said for New York, Louisiana, and a handful of others.
## Unconstitutional Laws by State and Time
![Unconstitutional Laws by State and Time](https://github.com/ebrodbeck/Unconstitutional_Laws/blob/main/Unconstitutional%20Laws%20by%20State%20and%20Time.jpg)

The above visualization shows a heatmap of unconstitutional laws by year, filtered by the top offenders. There appears to be a noticeable uptick in Supreme Court activity during the civil rights movement and onward to the 1990s.
## Unconstitutional Laws by State and Subject Matter
![Unconstitutional Laws by State and Subject Matter](https://github.com/ebrodbeck/Unconstitutional_Laws/blob/main/Unconstitutional%20Laws%20by%20State%20and%20Subject%20Matter.png)

Heat map for the subject matter of overturned laws. Some of the most common include Civil Rights, Criminal Law, Elections, and Tax Law. These are filtered to show the most common categories (there are many more with only a few relevant cases)

## Constitutional Provision Invoked in Overturning of the Law
![](https://github.com/ebrodbeck/Unconstitutional_Laws/blob/main/Constitutional%20Provision%20Invoked.webp)

Constitutional Provision Invoked in the overturning of the respective law. 1A, 14A, and Article 1 are most common. It is worth noting that the Federal gov has had 30 cases overturned regarding the 1st amendment and another 30 cases regarding the 5th amendment. I had to remove those because they drown out the colors of everything else
## Further Discussion
- An interesting exercise would be to track which party held power in each state when the law in question was written, but the data on this is pretty scattered. Additionally, governor party affiliation is not as relevant to the political opinions of the population as the affiliations of the state legislature, and the affiliations of the state legislatures since 1803 when this data set starts will be difficullt to collect.
- Two resonable hypotheses to explain some of the trends (or confounding factors) observed in this analysis are that (1) States with divided political opinions will see higher counts of laws deemed unconstitutional because laws are more likely to be challenges in court by the side that doesn't support it. And (2) States with larger populations like NY, CA, and TX would be more likely to have laws challenged because even the minority dissenting party has a higher absolute count of citizens to present a challenge.
- Conversely, small and politically homogenous states would be less likely to have many laws found unconstitutional. Which is somewhat evident in those states in the bottom left corner of the Laws per Decade scatterplot.
- Another confounding factor that may be further examined by diving into the "Subject Matter" and "Provisions Invoked" data would be the impact of states who's laws were born of one era only for them to be later struck down by changing political ideals of more progressive eras, specifically post-civil war. There appears to be a mix of prior-confederate states (LA, TX, VA) and non-confederate states (NY, CA, OH, IL) in the top offenders. It would be interesting to analyze the how southern states clinging to their old ways during reconstruction bolstered their unconstitutional law count, compared to NY and CA who never had such a history, yet still remain the top offenders.
- All of these factors would make for interesting expansions of this dataset and analysis.
