import pandas as pd 

class handle_inputs:

    @staticmethod
    def read_csv_to_dict(file: str): 
        df = pd.read_csv(file)

        return df.to_dict(orient="records")
    
    @staticmethod
    def read_text_to_list(file:str):
        data = list()
        with open(file, "r") as f:
            for line in f:
                data.append(line.strip())
        
        return data

