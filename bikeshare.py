#file to insert in branch refactoring 
#Use Python to understand U.S. bikeshare data. 

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    
    print('Hello! Let\'s explore some US bikeshare data!')
    
    while True:
 
       city = input('Which city would you like to explore? chicago, new york city, or washington? ')
       city.lower()

       if (city in['chicago', 'new york city', 'washington']):
          break
       else:
          print('Ooops! Not a valid city, please enter either .chicago, new york city, or washington')


    while True:
    
       month = input('Which month would you like to explore for? january, february, march, april, may, june or all?: ')
       month.lower()
 
       if (month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']):
          break
       else: 
          print('Ooops! Please Enter a valid month, january, february, march, april, may, june or all.')

           
    while True:
    
       day = input('Enter the day of the week you would like to explore: monday, tuesday, wednesday, thursday, friday, saturday, sunday or all? ')
       day.lower()
 
       if (day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']):
            break
       else:
            print('Ooops!, that is not a valid day, please enter either monday, tuesday, wednesday, thursday, friday, saturday, sunday or all')
    
    print('-'*40)
    return city, month, day

get_filters()



def load_data(city, month, day):

    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day
    print(df['day_of_week'])

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
  
  print('\nCalculating The Most Frequent Times of Travel...\n')
  start_time = time.time()

  df['Start Time'] = pd.to_datetime(df['Start Time'])

  # the most common month
  df['month'] = df['Start Time'].dt.month
  popular_month = df['month'].mode()[0]
  print("The most common month: ", popular_month)  

  # the most common day of week
  df['day_of_week'] = df['Start Time'].dt.day
  popular_day = df['day_of_week'].mode()[0]
  print("The most common day of week", popular_day) 

  # the most common start hour
  df['hour'] = df['Start Time'].dt.hour
  popular_hour = df['hour'].mode()[0]
  print('The most common start hour', popular_hour)

  
  print("\nThis took %s seconds." % (time.time() - start_time))
  print('-'*40)
  

def station_stats(df):
  """Displays statistics on the most popular stations and trip."""

  print('\nCalculating The Most Popular Stations and Trip...\n')
  start_time = time.time()

  # display most commonly used start station
  common_start = df['Start Station'].mode()[0]
  print("Common start station: ", common_start)
   
  # display most commonly used end station
  common_end = df['End Station'].mode()[0]
  print("Common end station: ", common_end)
   
  # display most frequent combination of start station and end station trip
  df['combination'] = df['Start Station'] + ' to ' + df['End Station']
  common_combination = df['combination'].mode()[0]
  print("most frequent combination of start station and end station trip", common_combination)

  print("\nThis took %s seconds." % (time.time() - start_time))
  print('-'*40)


def trip_duration_stats(df):
  """Displays statistics on the total and average trip duration."""

  print('\nCalculating Trip Duration...\n')
  start_time = time.time()

  # display total travel time
  total_travel = df['Trip Duration'].sum()
  print("Total travel time: ", total_travel)
  
  # display mean travel time
  mean_travel = df['Trip Duration'].mean()
  print("Mean travel time: ", mean_travel)


  print("\nThis took %s seconds." % (time.time() - start_time))
  print('-'*40)

    
def user_stats(df):
  """Displays statistics on bikeshare users."""

  print('\nCalculating User Stats...\n')
  start_time = time.time()

  # counts of user types
  user_types = df['User Type'].value_counts()
  print("counts of user types: ", user_types)

  # counts of gender
  if 'Gender' in df:
      gender = df['Gender'].value_counts()
      print("Gender: ", gender)
  else:
      print("There is no gender information in this city.")
  
  # earliest, most recent, and most common year of birth
  if 'Birth_Year' in df:
      earliest = df['Birth_Year'].min()
      print("earliest year of birth: ", earliest)
      recent = df['Birth_Year'].max()
      print("recent year of birth: ", recent)
      common_birth = df['Birth Year'].mode()[0]
      print("common year of birth: ", common_birth)
  else:
      print("There is no birth year information in this city.")

  print("\nThis took %s seconds." % (time.time() - start_time))
  print('-'*40)


def data(df):
    """Asking 5 lines of the raw data and more, if they want"""
    raw_data = 0
    while True:
        answer = input("Do you want to see the raw data? Yes or No: ").lower()
        if answer not in ['yes', 'no']:
            answer = input("You wrote the wrong word. Please type Yes or No: ").lower()
        elif answer == 'yes':
            raw_data += 5
            print(df.iloc[raw_data : raw_data + 5])
            again = input("Do you want to see more? Yes or No? ").lower()
            if again == 'no':
                break
        elif answer == 'no':
            return


def main():
   while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
