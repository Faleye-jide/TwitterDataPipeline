import tweepy 
import pandas as pd
import yaml
from yaml.loader import SafeLoader
import json
import os


class TwitterDataPipeline:
    """
    A class for twitter data pipeline
    """
    def __init__(self, config_file) -> None:
        self.config_file = config_file
        
    def load_config(self):
        """
        Function to load config file written in yaml file

        Returns:
            _type_: credential information
        """
        with open(self.config_file, 'r') as out_file:
            config = yaml.load(out_file, Loader=SafeLoader)

        return config
        # consumer_key, consumer_secret = config['Consumer Keys']['Key'], config['Consumer Keys']['Secret']
        # access_token, access_token_secret = config['Access Keys']['Token'], config['Access Keys']['Secret']

    def create_folder(self, folder_path):
        """Function to create a folder to store the extracted data

        Args:
            folder_path (_type_): _description_
        """
        try:
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)
                print("folder created")
        except FileExistsError:
            print("folder doesn't exist")
        
    def authenticate(self):
        """Function to connect and authenticate with the twitter api
        """
        # call the load_config function to retrieve credentials 
        config = self.load_config()
        # load bearer token from the ymal file
        consumer_key, consumer_secret = config['Consumer Keys']['Key'], config['Consumer Keys']['Secret']
        access_token, access_token_secret = config['Access Keys']['Token'], config['Access Keys']['Secret']

        # authenticate with twitter api
        auth = tweepy.OAuth1UserHandler(
            consumer_key, consumer_secret, access_token, access_token_secret
        )

        return auth 

    def extract(self):
        """
        Extracts data from the api and then creates a pandas dataframe
        """
        # call the authenticate function
        auth = self.authenticate()
        # create an api instance 
        api = tweepy.API(auth)

        item_list = []
        followers = api.get_friends(user_id="@iam_jeeday")

        # print(data)
        # print(followers[:1])
        for follower in followers:
            result = {
                "name":follower.name,
                "username":follower.screen_name,
                "Bio": follower.description,
                "location": follower.location,
                "date_created": follower.created_at,
                "number_of_friends":follower.friends_count,
                "number_of_followers": follower.followers_count,
                "background_image":follower.profile_background_image_url,
                "header":follower.profile_image_url

            }
            item_list.append(result)

        df = pd.DataFrame(item_list)
        
        return df
        
    def get_file_path(self):
        parent_path = os.path.abspath(os.getcwd())
        folder_name = "Extracted_data"
        # print("BASE_DIR:", parent_path)
        folder_path = os.path.join(parent_path, folder_name)
        # print("FOLDER_PATH:", folder_path)
        folder = self.create_folder(folder_path)
        file_name = "twitter.csv"
        file_path = os.path.join(folder_path, file_name)
        # print("FILE_PATH:", file_path)
        return file_path
    
    def load_to_csv(self, df, file_path):
        # print(df.head())
        # store data to csv
        # send data to csv format
        df.to_csv(file_path)
        
    def load_to_excel(self, df, file_path):
        df.to_excel(file_path)
        

