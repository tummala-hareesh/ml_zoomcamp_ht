# Import user-defined modules
import utilities_midterm_project as utils_mtp
import warnings

warnings.filterwarnings("ignore")


if __name__ == "__main__":

    dict_input = {'reportedyear': 2014,
          'geodivision': "D12",
          'category': "Crimes Against the Person", 
          'subtype': "Attempt Murder"
         }
    print(" >>> Input for the model:")
    print(" \t - ",dict_input)
    
    # Load trained model
    model_loaded = utils_mtp.load_model_pickle('./model_total_crime_count_final.pkl')
    
    # Prepare features for prediction
    df_input, target_max = utils_mtp.prepare_for_prediction(dict_input)
    
    # Prediction on input
    prediction = utils_mtp.predict_reg("RandomForestRegressor", model_loaded, df_input)

    # Prediction
    print(" >>> Predicted no. of total crimes are:",prediction*target_max)