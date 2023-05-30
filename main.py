from twitter_etl import TwitterDataPipeline


"The entry point to the ETL pipeline"
if __name__ == "__main__":
    # an instance of twitter_etl
    config_file = "secrets.yml"
    twitter = TwitterDataPipeline(config_file)
    print(twitter)
    twitter.extract()