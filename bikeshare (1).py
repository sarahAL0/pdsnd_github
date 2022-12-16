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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
   city=['chicago','new york city', 'washington']
   while True:
        try:
            city = input(' city name? : \n').lower()
            if city in ['chicago','new york city', 'washington']:
                break
            else:
                print("wrong city,city must be chicago,new york city, or washington")
        except:
            print("wrong city")
        
         
     
    # TO DO: get user input for month (all, january, february, ... , june)
   month=['all','january','february','march','april','may','june']
   while True:
        try:
            month=input('month of year?:\n').lower()
            if month in ['all','january','february','march','april','may','june']:
                break
            else:
                print('wrong month')
        except:
            print("wrong month")
            
            
         
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
   day = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
   while True:
        try:
             day = input('day of week ? : \n').lower()
             if day in ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
                break
             else:
                print('wrong day')
        except:
            print("wrong day")
        
        
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
  df=pd.read_csv(CITY_DATA[city])
  df['Start Time']=pd.to_datetime(df['Start Time']) 

  df['month']=df['Start Time'].dt.month
  df['day_of_week']=df['Start Time'].dt.weekday_name
  df['hour']=df['Start Time'].dt.hour

  if month != 'all':
     months=['january','february','march','april','may','june']
     month=months.index(month)+1 
     df=df[df['month'] == month]
  if day!='all':
     df=df[df['day_of_week']==day.title()]
    
  return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('most common month:', common_month)

    # TO DO: display the most common day of week
    common_day=df['day_of_week'].mode()[0]
    print('most common day:',common_day)

    # TO DO: display the most common start hour
    common_start_hour=df['hour'].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('common start station:', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('common end station:',common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combined_station=df.groupby(['Start Station','End Station'])
    common_combined_station=combined_station.size().sort_values(ascending=False).head(1)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:',total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print("mean travel time:",mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('User Type Stats:')
    print(df['User Type'].value_counts())
    while True:
        try:
            if city != 'washington':
                # TO DO: Display counts of gender
                print ('Gender Stats:')
                print(df['Gender'].value_counts())
                # TO DO: Display earliest, most recent, and most common year of birth
                print('Year Of Birth Stats:')
                earliest_year=df['Birth Year'].min()
                print('Eaeliest Year:',earliest_year)
                most_recent_year=df['Birth Year'].max()
                print('most recent year:', most_recent_year)
                most_common_year=df['Birth Year'].mode()[0]
                print('most commomn year:',most_common_year)
                break 
        except:
            print("end of data")
            break
            
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while view_data != 'no':
        print(df.iloc[0:5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()

def main():
    while True:
        city, month, day =get_filters()
        df = load_data (city,month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
            
if __name__=="__main__":
    main()
