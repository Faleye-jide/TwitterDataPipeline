from twitter_etl import TwitterDataPipeline


# "The entry point to the ETL pipeline"
if __name__ == "__main__":
#     # an instance of twitter_etl
    config_file = "secrets.yml"
    twitter = TwitterDataPipeline(config_file)
    
    df = twitter.extract()
    file_path = twitter.get_file_path()
#   # save to csv
    twitter.load_to_csv(df, file_path)
    # save to excel
    twitter.load_to_excel(df, file_path)