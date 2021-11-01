import time
import datetime as dt
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_NAMES = {'1':'January', '2':'February', '3':'March', '4':'April', '5':'May', '6':'June', '7':'July', '8':'August', '9':'September', '10':'October', '11':'November', '12':'December'}

DAY_OF_WEEK = {'0':'Monday', '1':'Tuesday', '2':'Wednesday', '3':'Thursday', '4':'Friday', '5':'Saturday', '6':'Sunday'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("What city are you interested in? Please enter 'Chicago', 'New York City', or 'Washington': ").lower()
        
    while city.title() not in ['Chicago', 'New York City', 'Washington']:
        city = input("What you entered was not a valid option. Please enter 'Chicago', 'New York City', or 'Washington': ")
            

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("What month are you interested in? Please spell out the full name of the month (all, january, february, ... , june): ")
        
    while month.title() not in ['All', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']:
        month = input("What you entered was not a valid option. Please enter 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', or 'All': ")        
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("What day of the week are you interested in? Please spell out the full name of the day (all, monday, tuesday, ... sunday): ")

    while day.title() not in ['All', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
        day = input("What you entered was not a valid option. Please enter 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', or 'All': ") 
        
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    #print(df.head())

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # convert the Start Time column to datetime and create other columns
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.dayofweek
    df['Hour'] = df['Start Time'].dt.hour
    #print(df.head())

    # TO DO: display the most common month
    common_month = df['Month'].mode()[0]
    common_month1 = df['Month'].value_counts().max() #should give you the max counts
    print("The most common month is {} with {} records.".format(MONTH_NAMES[str(common_month)],common_month1))

    # TO DO: display the most common day of week
    common_day = df['Day of Week'].mode()[0]
    common_day1 = df['Day of Week'].value_counts().max() #should give you the max counts
    print("The most common day of the week is {} with {} records.".format(DAY_OF_WEEK[str(common_day)],common_day1))

    # TO DO: display the most common start hour
    common_hour = df['Hour'].mode()[0]
    common_hour1 = df['Hour'].value_counts().max() #should give you the max counts
    print("The most common start hour is {} with {} records.".format(common_hour,common_hour1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most common start station is {} which occurs {} times.".format(df['Start Station'].mode()[0],df['Start Station'].value_counts().max()))

    # TO DO: display most commonly used end station
    print("The most common end station is {} which occurs {} times.".format(df['End Station'].mode()[0],df['End Station'].value_counts().max()))

    # TO DO: display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] +' as the start and ending at '+ df['End Station']
    print("The most common start and end station combination is {} which occurs {} times.".format(df['Trip'].mode()[0],df['Trip'].value_counts().max()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # convert the End Time column to datetime
    df['End Time'] = pd.to_datetime(df['End Time'])

    # TO DO: display total travel time
    df['Travel Time'] = df['End Time'] - df['Start Time']
    print("The total travel time is: {}".format(df['Travel Time'].sum()))

    # TO DO: display mean travel time
    print("The average travel time is: {}".format(df['Travel Time'].mean()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
    start_loc = 0
    if view_data == 'yes':
        while (start_loc < len(df)):
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
            view_display = input("Do you wish to continue? Enter yes or no.\n: ").lower()
            if view_display != 'yes':
                break
    
    
    # TO DO: Display counts of user types
    print("The counts of user types are:\n {}".format(df['User Type'].value_counts()))

    # TO DO: Display counts of gender
    if 'Gender' in df:
        print("\nThe counts of gender are:\n {}".format(df['Gender'].value_counts()))
    else:
        print("Sorry! There is no gender data available in the data")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print("\nThe earliest year of birth is: {}".format(int(df['Birth Year'].min())))
        print("The most recent year of birth is: {}".format(int(df['Birth Year'].max())))
        print("The most common year of birth is: {}".format(int(df['Birth Year'].mode()[0])))
    else:
        print("Sorry! The birth year of users is not available in the data") 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()