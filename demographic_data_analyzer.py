import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = None
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = None

    # What is the average age of men?
    average_age_men = None

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = None

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = None
    lower_education = None

    # percentage with salary >50K
    higher_education_rich = None
    lower_education_rich = None

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = None

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = None

    rich_percentage = None

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = None
    highest_earning_country_percentage = None

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = None

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


df = pd.read_csv('adult.data.csv')
print(df.head())
print(len(df))

#TASK 1
# race_count = df['race'].value_counts()
# race_unique = df['race'].unique()
# race_series = pd.Series(race_count, index = race_unique)
# print(race_series)

#TASK 2
# men = df[df['sex'] == 'Male']
# ave_men_age = df['age'].mean().round(decimals = 1)
# print(men)
# print(ave_men_age)

#TASK 3
# num_Bsc_degrees = len(df[df['education'] == 'Bachelors'])
# num_education = len(df['education'])
# Bsc_degree_percent = round((num_Bsc_degrees/num_education) * 100, 1)
# print(Bsc_degree_percent)

#TASK 4
# advanced_education = ['Bachelors', 'Masters', 'Doctorate']
# advanced_education_df = df[df['education'].isin(advanced_education)]
# num_advanced_education = len(advanced_education_df)
# advanced_education_with_high_salary_df = advanced_education_df[advanced_education_df['salary'] == '>50K']
# num_advanced_education_with_high_salary = len(advanced_education_with_high_salary_df)
# advanced_education_with_high_salary_percent = round((num_advanced_education_with_high_salary/num_advanced_education) * 100, 1)
# print(f"percentage of people with advanced education (Bachelors, Masters, or Doctorate) who make more than 50K:", advanced_education_with_high_salary_percent,"%")

#TASK 5
# num_rows = len(df)
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
# countries_salary_df= df.filter(['native-country', 'salary'])
# print(f"Filtered database with necessary columns:\n", countries_salary_df)
# country_salary_count = countries_salary_df.value_counts()
# print(f"Dataframe with count of each country with different salaries:\n", country_salary_count)
#     # total_countries_salary_counted = country_salary_count.sum()
#     # print(f"Checking if total adds up to ", len(df),":", total_countries_salary_counted)
#     # num_unique_countries = countries_salary_df['native-country'].nunique()
#     # print(f"Number of unique countries:", num_unique_countries)
# countries_high_sal_df = countries_salary_df[countries_salary_df['salary'] == '>50K']
# num_countries_high_sal = len(countries_high_sal_df)
# print(f"DataFrame of countries with ONLY salaries greater than 50K:\n", countries_high_sal_df.head())
# print(f"Total number of countries with salaries greater than 50K:", num_countries_high_sal)
# countries_high_sal_count = countries_high_sal_df.value_counts().reset_index(name = 'count')
# print(countries_high_sal_count)
#     # print(f"Checking if total number of countries with high salary =", len(countries_high_sal_df), ":", countries_high_sal_count.sum())
# country_with_highest_sal = countries_high_sal_count.iloc[countries_high_sal_count['count'].idxmax()]
# print(f"Country with the highest count of salary greater than 50K:", country_with_highest_sal['native-country'])
# country_with_highest_sal_percent = round((country_with_highest_sal['count']/num_countries_high_sal) * 100, 1)
# print(country_with_highest_sal['native-country'], f"occupies", country_with_highest_sal_percent, "%", "of the total people with salary >50K.")

#TASK 9
