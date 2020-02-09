import time
import pandas as pd
import numpy as np

CITY_DATA = {
    "chicago": "chicago.csv",
    "new york city": "new_york_city.csv",
    "washington": "washington.csv",
}

MONTHS = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
]
DAYS = [
    "sunday",
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
]
CITIES = ["chicago", "new york city", "washington"]


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("Hello! Let's explore some US bikeshare data!")
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input(
            "Which city would you like to see data for Chicago, New York City, or Washington? (Enter city to continue)]>>> "
        )
        city = city.lower()

        if city in CITIES:
            print()
            break
        else:
            print(
                "\n\nPlease choose from the list 'Chicago, New York City, or Washington'.\n\n"
            )

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:

        month = input(
            "Which month would you like to filter by?\n[Options: january, february, ... , june. (Enter month or press enter to select all)]>>> "
        )
        month = month.lower()

        if month in MONTHS:
            break
        else:
            month = "all"
            print("\nNote:Selected all months.\n")
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:

        day = input(
            "\nWould you like to filter by day of the week?[Options: monday, tuesday, ... sunday. (Enter day of the week or press enter to select all)]>>> "
        )
        day = day.lower()

        if day in DAYS:
            break
        else:
            day = "all"
            print("\nNote: Selected all days of the week.\n")
            break

    print("-" * 40)
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    # extract month and day of week from Start Time to create new columns
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.weekday_name

    # filter by month if applicable
    if month != "all":
        # use the index of the MONTHS list to get the corresponding int
        month = MONTHS.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df["month"] == month]

    # filter by day of week if applicable
    if day != "all":
        # filter by day of week to create the new dataframe
        df = df[df["day_of_week"] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df["month"].mode()[0]

    most_common_month = MONTHS[most_common_month]
    print("The most common month is {}".format(most_common_month.title()))

    # TO DO: display the most common day of week
    # find the most popular day of the week
    day_of_week = df["day_of_week"].mode()[0]
    print("Most common day of the week: {}".format(day_of_week.title()))

    # TO DO: display the most common start hour
    # convert the Start Time column to datetime
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    # extract hour from the Start Time column to create an hour column
    df["hour"] = df["Start Time"].dt.hour

    # find the most popular hour
    popular_hour = df["hour"].mode()[0]
    print("Most common start hour: {}".format(popular_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df["Start Station"].mode()[0]
    start_station_counts = max(df["Start Station"].value_counts())
    print(
        "Most popular start station: {} with counts: {}".format(
            start_station, start_station_counts
        )
    )
    # TO DO: display most commonly used end station
    end_station = df["End Station"].mode()[0]
    end_station_counts = max(df["End Station"].value_counts())
    print(
        "Most popular end station: {} with counts: {}".format(
            end_station, end_station_counts
        )
    )
    # TO DO: display most frequent combination of start station and end station trip
    freq_combination = df["Start Station"] + " to " + df["End Station"]
    freq_combination = freq_combination.describe()["top"]
    print(
        "Most frequent combination of start and end station trip: {}".format(
            freq_combination
        )
    )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print("\nCalculating Trip Duration...\n")
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("Total travelling time: {} hours.".format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("Total mean travelling time: {} hours.".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print("\nCalculating User Stats...\n")
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df["User Type"].value_counts()
    print("Number of user types:")
    print("\tSubscriber: {}\n\tCustomer: {}\n".format(user_types[0], user_types[1]))
    # TO DO: Display counts of gender
    try:
        gender = df["Gender"].value_counts()
        print(f"\nThe types of users by gender are given below:\n\n{gender}")
    except:
        print("\nThere is no 'Gender' column in this file.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        birth_year = df["Birth Year"]
    except KeyError:
        print(f"City does not have 'Birth Year'")
    else:
        most_common_byear = int(birth_year.mode()[0])
        print("The most common birth year is '{}'.".format(most_common_byear))
        most_recent_byear = int(birth_year.max())
        print("The most recent birth year is '{}'.".format(most_recent_byear))
        earliest_byear = int(birth_year.min())
        print("The earliest birth year is '{}'.".format(earliest_byear))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def display_data(df, current_line=0):
    """
    Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more.
    Continues asking until they say stop.
    Args:
        (pandas DataFram) df: dataframe of bikeshare data
    Returns:
        If the user says yes then this function returns the next five lines
            of the dataframe and then asks the question again by calling this
            function again (recursive)
        If the user says no then this function returns, but without any value
    """
    display = input(
        "\nWould you like to view individual trip data? Enter 'yes' or 'no'. >>>"
    ).lower()
    start, end = 0, 5

    while (display in ["yes", "y"]):
        print(df.iloc[start:end])
        start += 5
        end += 5
        display = input(
                "\nDo you want to see more 5 lines of raw data? "
                "Enter 'yes' or 'no'. >>> "
            ).strip().lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input("\nWould you like to restart? Enter 'yes' or 'no'. >>> ")
        if restart.lower() != "yes":
            break


if __name__ == "__main__":
    main()
