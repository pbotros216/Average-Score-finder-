"""
Peter Botros
lab3.py
9/16/2024
"""
# This program will average test scores to determine if a student passes or not.

# Minimum passing score (global variable)
passing_score = 50

# Function to calculate the average of two scores
def calculate_average(score1, score2):
    """
    Calculate the average of two scores.
    Parameters:
        score1 (int or float): The first score
        score2 (int or float): The second score
    Returns:
        float: The average of the two scores
    """
    average = (score1 + score2) / 2  # Add the two scores and divide by 2 to get the average
    return average  # Return the calculated average

# Function to check if the score passes the minimum threshold
def check_passing_status(average):
    """
    Check if the average score is above the passing score.
    Parameters:
        average (float): The average score
    Returns:
        bool: True if the average is above the passing_score, False otherwise
    """
    if average >= passing_score:
        return True
    else:
        return False

# Function to provide feedback based on scores
def provide_feedback(score1, score2):
    """
    Provides feedback based on the scores by calling other functions.
    Parameters:
        score1 (int or float): The first score.
        score2 (int or float): The second score.
    """
    # Calculate the average score by calling calculate_average function
    average = calculate_average(score1, score2)
    
    # Check if student passes by calling check_passing_status function
    if check_passing_status(average):
        print(f"Your average score is {average}. Congratulations! You passed.")
    else:
        print(f"Your average score is {average}. Sorry, you did not pass.")

# Main block to run the program
if __name__ == "__main__":
    # Example: Test case with two scores
    score1 = float(input("Enter the first score: "))
    score2 = float(input("Enter the second score: "))
    
    # Call the provide_feedback function to give the student feedback
    provide_feedback(score1, score2)

