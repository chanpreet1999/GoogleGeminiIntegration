import json
import google.generativeai as genai
import PIL


MODEL_NAME__DICT = {"1": 'gemini-pro', "2": "gemini-pro-vision"}

class Setup:
    MODEL = None
    FILE_LOCATION ='./apiKey.json'
    
    def __init__(self, user_input):
        api_key = self.get_api_key()
        self.MODEL = self.get_model(gemini_api_key = api_key, user_input = user_input)
    
    
    ''' 
        Function to get the API key from a JSON file
        General structure of JSON object:
            {
            "apiToken": "<YOUR KEY>"
            }
    '''
    def get_api_key(self):
        f = open(self.FILE_LOCATION)
        data = json.load(f)
        return data['apiToken'] 


    def get_model(self, gemini_api_key = None, user_input = "1"):
        genai.configure(api_key = gemini_api_key)
        return genai.GenerativeModel(MODEL_NAME__DICT[user_input])


def get_prompt():
    prompt = None
    try:
        while(prompt==None):
            prompt = input("\n\nEnter prompt: ")
    except Exception as e:
        print(e)
  
    return prompt


def get_image_name():
    image_name = None
    try:
        while(image_name==None):
            image_name = input("Enter image name in the folder: ")
            image_name = './images/' + image_name
            print('\n')
    except Exception as e:
        print(e)
    
    return image_name


def generate_response(prompt=None, image_name = None):

    match user_input:
        case "1": 
            response = model.generate_content(
                contents=[prompt],
                stream = True
            )
            for chunk in response:
                print(chunk.text, end='')
                # print("_"*80)
        case "2":   
            picture = PIL.Image.open(image_name)
            response = model.generate_content(
                contents=[prompt, picture],
                stream=True
            )
            # response.resolve()
            for chunk in response:
                print(chunk.text, end='')
                # To see each chunk size
                # print("_"*80)
        
    print('\n')


if __name__=="__main__": 
    
    user_input = input('Which version of Gemini would you like to use?\n\t1. Gemini-Pro(text only version)\n\t2. Gemini-Pro-Vision(for analyzing photos)\n*Defaults to option 1\n Chat optiom coming soon!\n\n Enter your input: ')
    if(user_input == '' or user_input == None):
            user_input = "1"

    setup_obj = Setup(user_input=user_input)
    model = setup_obj.MODEL
    while(True):
        if(user_input == "1"):
            prompt = get_prompt()
            generate_response(prompt=prompt)        
        else:
            image_name = get_image_name()
            prompt = get_prompt()
            generate_response(prompt=prompt, image_name = image_name)        
