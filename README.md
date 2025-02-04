# Python--Delivery-to-Mars
Interactive Python game

## Project Overview  
This project was inspired by "Interstellar Delivery," a DataCamp exercise aimed at mastering Python's built-in `datetime` module. However, I wanted to take the idea further and create a playful game set in a future where humanity lives on Mars.  

In this fictional scenario, you're the captain of a space delivery company tasked with delivering cargo from Earth to Mars. You'll face challenges like meteor showers, solar flares, and fuel leaks along the way.  

Your mission? Complete deliveries, manage your resources wisely, and avoid running out of rockets! Earn eight rockets to win the game, or lose them all and face failure.  

### Inspiration
As mentioned before, this game was inspired in a DataCamp exercise, which is designed to reinforce Python's datetime concepts and functionalities.

The exercise consists in defining three functions:

- format_date(): accepting "timestamp" and "datetime_format", and should return the date correctly formatted as a string
- calculate_landing_time(): accepting "rocket_launch_dt" and "travel_duration", and should return the estimated Mars landing time as a datetime string in the format DD-MM-YYYY
- days_until_delivery(): accepting "expected_delivery_date" and "current_dt", and should calculate the difference in days between the expected delivery datetime and the current datetime, then return the number of days remaining as an integer.

The exercise resolution code is the following:
```python
from datetime import datetime, timedelta

def format_date(timestamp, datetime_format):
    """
    Transforms unix timestamp int into desired datetime_format.
    """
    datetime_timestamp = datetime.fromtimestamp(timestamp)
    format_timestamp = datetime_timestamp.strftime(datetime_format)
    return format_timestamp

def calculate_landing_time(rocket_launch_dt, travel_duration):
    """
    Calculates estimated landing time on Mars as a str.
    Args:
    rocket_launch_dt: rocket launch datetime object.
    travel_duration: expected travel time in days as int.
    """
    dt_duration = timedelta(days=travel_duration)
    iso_landing_time = rocket_launch_dt + dt_duration
    str_landing_time = iso_landing_time.strftime("%d-%m-%Y")
    return str_landing_time

def days_until_delivery(expected_delivery_dt, current_dt):
    """
    Calculates days until a package arrives as int.
    Args:
    expected_delivery_dt: estimated delivery date as a datetime object.
    current_dt: current date as a datetime object.
    """
    total_days = (expected_delivery_dt - current_dt).days
    return total_days
```
The context of the exercise inspired me into creating a game where the objective is to send packages with rockets from the Earth to the Moon, simulating a delivery service.

## 🎮 How to Play  
1. **Start the Game:** Run the script and follow the on-screen prompts.  
2. **Choose Your Delivery Type:**  
    - `1`: Small Delivery (30 days)  
    - `2`: Medium Delivery (45 days)  
    - `3`: Large Delivery (60 days)  
3. **Navigate Space Hazards:**  
    - Random events may require fuel-depleting deviations.  
    - You can choose to proceed with or without deviation—both come with risks.  
4. **Manage Your Rockets:**  
    - Deliver successfully to earn rockets.  
    - Lose fuel and crash to lose them.  
5. **Winning and Losing:**  
    - Earn 8 rockets to win!  
    - Run out of rockets, and it's game over.  

## 🌟 Game Features  
- **Random Events:** Fuel loss and unexpected deviations keep the game dynamic.  
- **Strategic Choices:** Players must weigh risks and rewards.  
- **Victory and Failure:** Progress towards triumph or crash into disaster.  
- **Humorous and Engaging Gameplay:** Lighthearted messages guide players through victory and defeat.  

## 📚 Learning Objectives  
This game helps reinforce Python programming concepts such as:  
- Conditionals (`if`/`else`)  
- Loops (`while`)  
- Functions (`def`)  
- Random number generation with the `random` module  
- User input handling  

## 🔧 Installation  
To run this project, you need Python 3.x installed  

## 🎯 Example Output  
```python
Welcome to Delivery to Mars! 🚀  

It is the year 2156, and Elon Musk's idea came true...  
There are already colonies on Mars!!!  

Your mission is to complete deliveries from Earth to Mars.  
Rockets have enough fuel for 100 days, and you start with 3 rockets.  

Choose a delivery type:  
1 - Small (30 days)  
2 - Medium (45 days)  
3 - Large (60 days)  
Type: 1  

👀 ..it seems there is a meteor shower, or maybe a solar flare, or a fuel leak..  
🧐 Proceed without deviation (1) or with deviation (2)?  
Choose: 2  

😎 Delivery successful! You earned one rocket!  
Total rockets: 4
```


Enjoy your space delivery adventures! 🌌 


