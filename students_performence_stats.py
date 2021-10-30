import csv
import pandas as pd
import statistics as st

df=pd.read_csv("StudentsPerformance.csv")
readScore_list=df["reading score"].to_list()
writeScore_list=df["writing score"].to_list()

#average of height & weight
readScore_mean=st.mean(readScore_list)
writeScore_mean=st.mean(writeScore_list)

#median of height&weight
readScore_median=st.median(readScore_list) 
writeScore_median=st.median(writeScore_list)

#mode of height&weight
readScore_mode=st.mode(readScore_list)
writeScore_mode=st.mode(writeScore_list)

print("Mean, Median and Mode of the reading scores of children is {}, {} and {} respectively".format(readScore_mean,readScore_mode,readScore_median))
print("Mean, Median and Mode of the written scores of children is {}, {} and {} respectively".format(writeScore_mean,writeScore_median,writeScore_mode))

#standard deviation of height&weight
readScore_standard_deviation=st.stdev(readScore_list)
writeScore_standard_deviation=st.stdev(writeScore_list)

#1,2,3 standard deviation of height&weight
height_first_std_deviation_start, readScore_first_std_deviation_end = readScore_mean-readScore_standard_deviation, readScore_mean+readScore_standard_deviation
height_second_std_deviation_start, readScore_second_std_deviation_end = readScore_mean-(2*readScore_standard_deviation), readScore_mean+(2*readScore_standard_deviation)
height_third_std_deviation_start, readScore_third_std_deviation_end = readScore_mean-(3*readScore_standard_deviation), readScore_mean+(3*readScore_standard_deviation)

readScore_list_of_data_within_1_std_deviation = [result for result in readScore_list if result > height_first_std_deviation_start and result < readScore_first_std_deviation_end]
readScore_list_of_data_within_2_std_deviation = [result for result in readScore_list if result > height_second_std_deviation_start and result < readScore_second_std_deviation_end]
readScore_list_of_data_within_3_std_deviation = [result for result in readScore_list if result > height_third_std_deviation_start and result < readScore_third_std_deviation_end]

print("{}% of data for height lies within 1 standard deviation".format(len(readScore_list_of_data_within_1_std_deviation)*100.0/len(readScore_list)))
print("{}% of data for height lies within 2 standard deviation".format(len(readScore_list_of_data_within_2_std_deviation)*100.0/len(readScore_list)))
print("{}% of data for height lies within 3 standard deviation".format(len(readScore_list_of_data_within_3_std_deviation)*100.0/len(readScore_list)))