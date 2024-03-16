
def calculate_prediction(user, movie_id, prediction_function):
    print(movie_id)
    return movie_id, prediction_function(user, movie_id)