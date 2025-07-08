import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')


    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_num = df['race'].value_counts()
    race_unique = df['race'].unique()
    race_count = pd.Series(race_num, index = race_unique)
    # race_count = None


    # What is the average age of men?
    men = df[df['sex'] == 'Male']
    average_age_men = men['age'].astype(float).mean().round(decimals = 1)
    # average_age_men = None


    # What is the percentage of people who have a Bachelor's degree?
    num_Bsc_degrees = len(df[df['education'] == 'Bachelors'])
    num_education = len(df['education'])
    percentage_bachelors = round((num_Bsc_degrees/num_education) * 100, 1)
    # percentage_bachelors = None


    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    advanced_education = ['Bachelors', 'Masters', 'Doctorate']
    advanced_education_df = df[df['education'].isin(advanced_education)]
    higher_education = len(advanced_education_df)
    # higher_education = None
    lower_education_df = df[~df['education'].isin(advanced_education)]
    lower_education = len(lower_education_df)
    # lower_education = None


    # percentage with salary >50K
    advanced_education_with_high_salary_df = advanced_education_df[advanced_education_df['salary'] == '>50K']
    num_advanced_education_with_high_salary = len(advanced_education_with_high_salary_df)
    higher_education_rich = round((num_advanced_education_with_high_salary/higher_education) * 100, 1)
    # higher_education_rich = None
    lower_education_with_high_salary_df = lower_education_df[lower_education_df['salary'] == '>50K']
    num_lower_education_with_high_salary = len(lower_education_with_high_salary_df)
    lower_education_rich = round((num_lower_education_with_high_salary/lower_education) * 100, 1)
    # lower_education_rich = None


    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    # min_work_hours = None


    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_hours_worked_df = df[df['hours-per-week'].isin([1])]
    num_people_with_min_hours = len(min_hours_worked_df)
    min_hours_worked_with_high_sal_df = min_hours_worked_df[min_hours_worked_df['salary'] == '>50K']
    num_min_workers = len(min_hours_worked_with_high_sal_df)
    # num_min_workers = None
    rich_percentage = round((num_min_workers/num_people_with_min_hours) * 100, 1)
    # rich_percentage = None


    # What country has the highest percentage of people that earn >50K?
    total_per_country = df['native-country'].value_counts()
    rich_per_country = df[df['salary'] == '>50K']['native-country'].value_counts()
    percentage_rich = (rich_per_country/total_per_country) * 100
    percentage_rich = percentage_rich.dropna().round(1)
    highest_earning_country = percentage_rich.idxmax()
    # # highest_earning_country = None
    highest_earning_country_percentage = percentage_rich.max()
    # highest_earning_country_percentage = None


    # Identify the most popular occupation for those who earn >50K in India.
    india_df = df[df['native-country'].isin(['India'])]
    india_high_sal_df = india_df[india_df['salary'] == '>50K']
    india_occupation_count_df = india_high_sal_df['occupation'].value_counts().reset_index(name = 'count').rename(columns={'index': 'occupation'})
    top_IN_occupation = india_occupation_count_df.iloc[india_occupation_count_df['count'].idxmax()]['occupation']
    # top_IN_occupation = None

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }


# df = pd.read_csv('adult.data.csv')
# print(df.head())
# # print(len(df))

# TASK 1
# race_num = df['race'].value_counts()
# race_unique = df['race'].unique()
# race_count = pd.Series(race_num, index = race_unique)
# print(race_count)

#TASK 2
# men = df[df['sex'] == 'Male']
# average_age_men = df['age'].mean().round(decimals = 1)
# print(men)
# print(average_age_men)

#TASK 3
# num_Bsc_degrees = len(df[df['education'] == 'Bachelors'])
# num_education = len(df['education'])
# percentage_bachelors = round((num_Bsc_degrees/num_education) * 100, 1)
# print(percentage_bachelors)

#TASK 4
# advanced_education = ['Bachelors', 'Masters', 'Doctorate']
# advanced_education_df = df[df['education'].isin(advanced_education)]
# num_advanced_education = len(advanced_education_df)
# advanced_education_with_high_salary_df = advanced_education_df[advanced_education_df['salary'] == '>50K']
# num_advanced_education_with_high_salary = len(advanced_education_with_high_salary_df)
# advanced_education_with_high_salary_percent = round((num_advanced_education_with_high_salary/num_advanced_education) * 100, 1)
# print(f"percentage of people with advanced education (Bachelors, Masters, or Doctorate) who make more than 50K:", advanced_education_with_high_salary_percent,"%")

#TASK 5
# lower_education_df = df[~df['education'].isin(advanced_education)]
# num_lower_education = len(lower_education_df)
# lower_education_with_high_salary_df = lower_education_df[lower_education_df['salary'] == '>50K']
# num_lower_education_with_high_salary = len(lower_education_with_high_salary_df)
# lower_education_with_high_salary_percent = round((num_lower_education_with_high_salary/num_lower_education) * 100, 1)
# print(f"percentage of people without advanced education who make more than 50K:", lower_education_with_high_salary_percent,"%")

#TASK 6
# min_hour_per_week = df['hours-per-week'].min()
# print(min_hour_per_week)

#TASK 7
# min_hours_worked_df = df[df['hours-per-week'].isin([1])]
# num_people_with_min_hours = len(df[df['hours-per-week'].isin([1])])
# print(num_people_with_min_hours)
# min_hours_worked_with_high_sal_df = min_hours_worked_df[min_hours_worked_df['salary'] == '>50K']
# print(min_hours_worked_with_high_sal_df)
# num_min_hours_worked_with_high_sal = len(min_hours_worked_with_high_sal_df)
# min_hours_worked_with_high_sal_percent = round((num_min_hours_worked_with_high_sal/num_people_with_min_hours) * 100, 1)
# print(f"percentage of people who work the minimum number of hours per week and have a salary of more than 50K:", min_hours_worked_with_high_sal_percent,"%")

#TASK 8
# total_per_country = df['native-country'].value_counts()
# rich_per_country = df[df['salary'] == '>50K']['native-country'].value_counts()
# percentage_rich = (rich_per_country/total_per_country) * 100
# percentage_rich = percentage_rich.dropna().round(1)
# highest_earning_country = percentage_rich.idxmax()
# highest_earning_percentage = percentage_rich.max()
# print(f"Country with highest percentage of >50K earners: {highest_earning_country}")
# print(f"Percentage: {highest_earning_percentage}%")

# #TASK 9
# india_df = df[df['native-country'].isin(['India'])]
# print(india_df)
# india_high_sal_df = india_df[india_df['salary'] == '>50K']
# print(india_high_sal_df)
# num_india_high_sal_df = len(india_high_sal_df)
# print(num_india_high_sal_df)
# print(f"Count of each occupation in India with salaries greater than 50K:\n", india_high_sal_df['occupation'].value_counts())
# india_occupation_count_df = india_high_sal_df['occupation'].value_counts().reset_index(name = 'count').rename(columns={'index': 'occupation'})
# print(india_occupation_count_df)
# india_most_popular_occupation = india_occupation_count_df.iloc[india_occupation_count_df['count'].idxmax()]['occupation']
# print(f"Most popular occupation in India where salary is greater than 50K:", india_most_popular_occupation['occupation'])