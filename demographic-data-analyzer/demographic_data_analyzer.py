import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    menAge = df[df['sex'] == 'Male']
    menAgeCol = menAge['age']
    average_age_men = round(pd.to_numeric(menAgeCol, errors='coerce').mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    numBach = df[df['education'] == 'Bachelors'].size
    percentage_bachelors = round((numBach/df.size)*100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    excludeHirEd = ['Bachelors', 'Masters', 'Doctorate']
    hirEd = df[df['education'].isin(excludeHirEd)] # create another dataframe and select only the education that is Bachelors, Master, Doctorate
    lowEd = df[~df['education'].isin(excludeHirEd)] # create another dataframe and select only the education that is NOT Bachelors, Master, Doctorate
    higher_education = round((hirEd['salary'] == '>50K').mean() * 100, 1)
    lower_education = round((lowEd['salary'] == '>50K').mean() * 100, 1)

    # percentage with salary >50K
    higher_education_rich = higher_education
    lower_education_rich = lower_education

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    minRich = (num_min_workers['salary'] == '>50K').mean() * 100
    rich_percentage = minRich

    # What country has the highest percentage of people that earn >50K?
    avgSalary = df.groupby('native-country')['salary'].apply(lambda x: (x == '>50K').mean())
    highest_earning_country = avgSalary.idxmax()
    highCountry = df[df['native-country'] == highest_earning_country]
    highest_earning_country_percentage = round((highCountry['salary'] == '>50K').mean() * 100, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    occup = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    highEarn = occup['occupation'].mode()[0]
    top_IN_occupation = highEarn

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
