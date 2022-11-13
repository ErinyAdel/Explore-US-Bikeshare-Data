import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = str(input("Would you like to see data for Chicago, New York, or Washington?")).lower()
    print("Looks like you want to hear about " + city + "! If this is not true, restart the program now!")

    while city not in CITY_DATA.keys():
        print("Invalid city!")
        city = str(input("Would you like to see data for Chicago, New York, or Washington?")).lower()
        print("Looks like you want to hear about " + city + "! If this is not true, restart the program now!")

    while True:
        filter = str(input("Would you like to filter the data by month, day, or not at all? Type 'none' for no time filter."))
        if filter == "month" or filter == "day" or filter == "both" or filter == "none":
            months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
            days = ['all', 'm', 'tu', 'w', 'th', 'f', 'sa', 'su']

            if filter == "month":
                while True:
                    month = str(input("Which month? January, February, March, April, May, June, or All? Please type out the full month name.")).lower()
                    day = None
                    if month in months:
                        break
                    else:
                        print("Invalid input!")

            elif filter == "day":
                while True:
                    day = str(input("Which day? Please type a M, Tu, W, Th, F, Sa, Su, or All.")).lower()
                    month = None
                    if day in days:
                        break
                    else:
                        print("Invalid input!")

            elif filter == "both":
                while True:
                    month = str(input("Which month? January, February, March, April, May, June, or All? Please type out the full month name.")).lower()
                    if month in months:
                        break
                    else:
                        print("Invalid input!")
                while True:
                    day = str(input("Which day? Please type a M, Tu, W, Th, F, Sa, Su, or All.")).lower()
                    if day in days:
                        break
                    else:
                        print("Invalid input!")

            elif filter == "none":
                month = None
                day = None

            break

        else:
            print("Invalid input!")

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

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all' and day is None and month is not None:
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all' and month is None and day is not None:
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("The most common month: {}".format(df['month'].mode()[0]))

    # display the most common day of week
    print("The most common day of week: {}".format(df['day_of_week'].mode()[0]))

    # display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    print("The most common start hour: {}".format(df['start_hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most commonly used start station: ".format(df['Start Station'].mode()[0]))

    # display most commonly used end station
    print("The most commonly used start station: ".format(df['End Station'].mode()[0]))

    # display most frequent combination of start station and end station trip
    df['comb_start_end'] = df['Start Station'] + "," + df['End Station']
    print("The most commonly used start station: ".format(df['comb_start_end'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("The total travel time: {}".format(df['Trip Duration'].sum()))

    # display mean travel time
    print("The mean travel time: {}".format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Counts of user types: {}".format(df['User Type'].value_counts()))

    # Display counts of gender
    print("Counts of user types: {}".format(df['Gender'].value_counts()))

    # Display earliest, most recent, and most common year of birth
    print("The earliest year of birth: {}".format(df['Birth Year'].min()))
    print("The most recent year of birth: {}".format(df['Birth Year'].max()))
    print("The most common year of birth: {}".format(df['Birth Year'].mode()[0]))

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
