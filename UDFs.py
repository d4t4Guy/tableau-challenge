import pandas as pd

def humanbytes(B):  #https://stackoverflow.com/questions/12523586/python-format-size-application-converting-b-to-kb-mb-gb-tb
   'Return the given bytes as a human friendly KB, MB, GB, or TB string'
   B = float(B)
   KB = float(1024)
   MB = float(KB ** 2) # 1,048,576
   GB = float(KB ** 3) # 1,073,741,824
   TB = float(KB ** 4) # 1,099,511,627,776

   if B < KB:
      return '{0} {1}'.format(B,'Bytes' if 0 == B > 1 else 'Byte')
   elif KB <= B < MB:
      return '{0:.2f} KB'.format(B/KB)
   elif MB <= B < GB:
      return '{0:.2f} MB'.format(B/MB)
   elif GB <= B < TB:
      return '{0:.2f} GB'.format(B/GB)
   elif TB <= B:
      return '{0:.2f} TB'.format(B/TB)

   





def df_memory_total (df):     #takes dataframe as input.
    s=df.memory_usage()       #generate series to call sum() next
    t=s.sum()                 #getting the total of all memory components
    return(humanbytes(t))     #format the total in terms of KB, MB, etc.





#borrowed from: https://towardsdatascience.com/exploring-bike-share-data-3e3b2f28760c 
def column_metadata(df):   #takes dataframe as input. Then calculates details on each column and returns a dataframe containing the result values. DEPENDENCY: Pandas as pd
    return pd.DataFrame.from_records([(col, df[col].nunique(), df[col].dtype, df[col].memory_usage(deep=True) )  for col in df.columns], columns=['Column Name', 'Unique', 'Data Type','Memory Usage'])


def greatest_frequency (df, column_name):
    s = df[column_name].value_counts(sort=True)
    check_year = df[column_name].value_counts().idxmax()
    numerator = s[check_year]
    denominator = s.sum()
    ratio = numerator/denominator
    return(f'The value {check_year} appears in the column {numerator:,} times, comprising {ratio:.0%} of all the records')
    
 




#designed to remove outliers from trip length.
# Takes dataframe and target column, calculates outlier boundary and 
# returns both a filtered df with no outliers in the target column (entire row deleted), and 
# a reporting string showing the ratio of outliers in data set. 
def strip_high_fliers(df, column_name):                    
    # Determine outliers using upper and lower bounds
    #     Perform necessary calculations to get outlier bounds
    quartiles = df[column_name].quantile([.25,.5,.75]) 
    lowerq = quartiles[0.25]                           
    upperq = quartiles[0.75]                           
    
    iqr = upperq-lowerq                                
    lower_bound = lowerq - (1.5*iqr)                   
    upper_bound = upperq + (1.5*iqr)                   
    
    #count the number of outliers in data set
    outliers_count = 0
    for value in df[column_name]:
        if (value > upper_bound):
            outliers_count += 1


    numerator   = outliers_count
    denominator = len(df[column_name])
    ratio = numerator/denominator
    
    out_string = f'There are {numerator:,} out of {denominator:,} outliers, or {ratio:.0%}. These records will be excluded from analysis'
    df1 = df[df[column_name]<upper_bound]

    return df1, out_string
    
    
    
    
    
    
def concat_csv_files(directory):
    import os
    import glob
    #set working directory
    os.chdir(directory)

    #find all csv files in the folder
    #use glob pattern matching -> extension = 'csv'
    #save result in list -> all_filenames
    extension = 'csv'
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
    #print(all_filenames)

    #combine all files in the list
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
    #export to csv
    combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')