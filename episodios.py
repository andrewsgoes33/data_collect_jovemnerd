
# %%
import requests
import datetime
import pandas as pd
import json

class Collector:
    
    def __init__(self, url, instance_name):
        self.url = url
        self.instance_name = instance_name
        
    def get_content(self,**kwargs):
        url = "https://api.jovemnerd.com.br/wp-json/jovemnerd/v1/nerdcasts/"
        resp = requests.get(self.url, params=kwargs)
        return resp

    def save_data(self, data, format = 'json'):
        
        now = datetime.datetime.now(). strftime("%Y-%m-%d_%H-%M%S.%f")
        

        if format == 'json':
            with open(f"data/episodios/json/{now}.json", "w") as open_file:
                json.dump(data,open_file)
                
        if format == "parquet":
            df = pd.Dataframe(data)
            pd.to_parquet(f"data/episodios/parquet/{now}.parquet", index = False)
            
#%%
resp = get_content(per_page=1000, page = 1)
resp.json()

# %%
