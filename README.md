# tableau-challenge

See vizualization story on Tableau Public at: https://public.tableau.com/app/profile/andre.shearer/viz/HW_20_Tableau/CitiReport


Service level for bikes: Should be serviced every 45 days. Source: Feb 2021 monthly report at https://d21xlh2maitm24.cloudfront.net/nyc/February-2021-Citi-Bike-Monthly-Report.pdf

Definition – Peak Hours: based on trip start time

Data cleaning:

File for 2021-04: Found three suspect columns, namely mode of birth year, tripduration, and gender. 
•	Mode of birth year had >95% of values as 1970, so it should be disregarded. It was not dropped to maintain union-ability with other files, but I am checking older files to see   if the same pattern recurs. 
•	Tripduration clustered around 5 minutes, which seems reasonable, but showed some very large outliers that moved the average well ahead of the median. The trips containing    tripduration outliers were dropped.  
    o	Possible reasons could be customers taking a long time to return a bike, e.g. holding on to a single bike for several hours or longer. 
•	Gender was unknown over most values, but when filtered on customer (short term) vs subscriber (longer term), the unknown values are mostly in the customer segment. I interpret this as meaning the data are probably okay for subscribers, but customers rarely supply this information. 

File for 2021-03:  Similar histogram profile of columns, meaning the same as above looked suspect. 
•	Mode of birth year: 1970, 95% of trips recorded
•	Tripduration: 5% outliers, these records were dropped
•	Gender: keeping because it looks like good data as long as it is filtered to customer


File for 2021-02:  Similar histogram profile of columns, meaning the same as above looked suspect. 
•	Mode of birth year: 1970, 95% of trips recorded
•	Tripduration: 5% outliers, these records were dropped
•	Gender: keeping because it looks like good data as long as it is filtered to customer


File for 2021-01:  Similar histogram profile of columns, but histogram for mode of birth year is less suspect. 
•	Mode of birth year: 1969, only 9% of trips recorded, which looks plausible, so keeping this field
•	Tripduration: 6% outliers, these records were dropped
•	Gender: keeping because it looks like good data as long as it is filtered to customer


File for 2020-12:  Similar histogram profile of columns, but histogram for mode of birth year is less suspect. 
•	Mode of birth year: 1969, only 9% of trips recorded, which looks plausible, so keeping this field
•	Tripduration: 5% outliers, these records were dropped
•	Gender: keeping because it looks like good data as long as it is filtered to customer


File for 2020-11:  Similar histogram profile of columns, but histogram for mode of birth year is less suspect. 
•	Mode of birth year: 1969, only 9% of trips recorded, which looks plausible, so keeping this field
•	Tripduration: 5% outliers, these records were dropped
•	Gender: keeping because it looks like good data as long as it is filtered to customer


File for 2020-10:  Similar histogram profile of columns, but histogram for mode of birth year is less suspect. 
•	Mode of birth year: 1969, 12% of trips recorded, which looks high. Keeping field but will probably filter such that ‘birth year’ excludes 1969, and any years earlier than 1940, which would mean accepted age range is 16-90 years old in 2020
•	Tripduration: 4% outliers, these records were dropped
•	Gender: keeping because it looks like good data as long as it is filtered to customer


### Brief summary of data quality issues:
•	Birth year appears to have quite a lot of dummy values. This becomes more pronounced between January and February of 2021, going from about 9% of records having a birth year equal to the mode, to about 95% of records. 
    o	The mode appears to be a dummy value because it switches from 1969 pre-2021-02, to 1970 from 2021 February through April. This may be due to a default in the data collection process; it would be a good idea to check how birth year is gathered to identify process improvements
•	Trip Duration: about 5% were outliers to the high side.  Outliers below lower bound were not checked because the IQR lower_bound would turn out to be less than zero.  Citi Bike only records trips at least 60 seconds in length. I suspect these were for trips where end station and end time are less than reliable, so all records with outlier trip times were excluded from analysis. 
