import openai
import json
from flask import Flask, request, jsonify
import random
from flask_cors import CORS
import time
import logging

# Configure OpenAI API key
openai.api_key = "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"

# Set default values for company type and name
company_type = "Company Type"
company_name = "Company Name"

# Configure logging
logging.basicConfig(level=logging.INFO)

def return1():
    design1_button_list = [
        "Company Name text",
        "Creative Headline for Section 1",
        # ... (other button names)
        "Creative CTA button text for Section 4"
    ]
    design1_image_list = ["Section 1 Image"]
    return design1_button_list, design1_image_list
def return2():
    design2_button_list = [
    "Company Name text",
    "Creative Headline for Section 1",
    "Creative Tagline for Section 1",
    "CTA button title for Section 1",
    "Creative Headline for Section 2",
    "Creative Headline for Section 3",
    "Creative Description for Section 3",
    "Creative CTA Tagline for Section 4",
    "Creative CTA description for Section 4",
    "CTA button title for Section 4"
    ]
    design2_image_list = [
    "Section 2 Image",
    "Section 3 Image",
    "Section 4 Image"
    ]

    return design2_button_list, design2_image_list
def return3():
    design3_button_list = [
    "Company Name text",
    "Creative Headline for Section 1",
    "Creative Tagline for Section 1",
    "Creative CTA button text for Section 1",
    "2 Words Creative Headline for Section 2",
    "Creative Description for Section 2",
    "2 Words Creative Headline for Section 3",
    "Creative Description for Section 3",
    "Main Creative CTA Tagline for Section 4",
    "Creative CTA button title for Section 4"
    ]
    design3_image_list = [
    "Aesthetic Background Image",
    "Section 2 Image",
    "Section 3 Image"
    ]

    return design3_button_list, design3_image_list

# ... (similar functions for return2 and return3)

def returnText(button_name):
    completion = None  # Initialize completion variable

    if button_name == 'Company Name text':
        return company_name
    else:
        for delay_secs in (2**x for x in range(0, 6)):
            try:
                print(f"Generating for {button_name}")
                completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo-0613",
                    messages=[
                        {"role": "system", "content": f"You are a UI content writer who writes content to be included in the website for {company_name} company that has been divided into Sections and also creates names for companies."},
                        {"role": "user", "content": f"""I want to make a {company_type} company landing page. Write me a {button_name} of Website.

                            I want this data so that I can add it to the figma structure JSON and generate the design on figma.

                            Example is enclosed below in three backticks:
                            ``` 
                            XYZ-characters

                            Here, 
                            XYZ-characters should actually be the {button_name}.
                            ```

                            The output format I am looking for is just plain text with nothing else and only the requested text, The generated text will directly go into the website so do not use any extra words in it. Each output should be less than 20 words and if the output is to be generated for 'CTA button title' output should be less than 3 words. Do not include quotation marks anywhere in the output. Also, do not include things that specify what section of the website it is.
                            """}
                    ]
                )
                print(f"Done for {button_name}")
                break

            except openai.OpenAIError as e:
                randomness_collision_avoidance = random.randint(0, 1000) / 1000.0
                sleep_dur = delay_secs + randomness_collision_avoidance
                print(f"Error: {e}. Retrying in {round(sleep_dur, 2)} seconds.")
                time.sleep(sleep_dur)
                continue

    if completion:
        elements = completion.choices[0].message.content
        clean_element = elements.replace("'", "").replace('"', '').replace("\n", " ")
        return clean_element
    else:
        return f"Error generating text for {button_name}"

        elements = completion.choices[0].message.content
        clean_element = elements.replace("'", "").replace('"', '').replace("\n", " ")
        return clean_element
def update_json(file_path, name_to_match, new_characters_value):
    with open(file_path, 'r') as file:
        data = json.load(file)

    for element in data:
        if 'name' in element and element['name'] == name_to_match:
            element['characters'] = new_characters_value

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)
def returnImage(image_name):
    PROMPT = f"""Generate me a {image_name} for a {company_type} company that is relevant for the company's website. Make sure the generated image is light overall
    and not dark. Also ensure that image does not have any type of text in it and try to keep it as modern as possible and as relevant as possible."""

    response = openai.Image.create(
      prompt=PROMPT,
      n=1,
      size="1024x1024",
    )

    link = response["data"][0]["url"]

    return link


# ... (similar functions for update_json and returnImage)

app = Flask(__name__)
CORS(app)

@app.route('/post', methods=['POST'])
def get_data():
    data = request.get_json()
    if 'variable1' in data and 'variable2' in data:
        global company_name
        global company_type
        company_type = data['variable1']
        company_name = data['variable2']
        return jsonify("Works"), 200
    else:
        error_result = {'error': 'Missing variables in the request'}
        return jsonify(error_result), 400
@app.route('/')
def index():
    return 'Welcome to my website!'
@app.route('/get_data', methods=['GET'])
def send_data():
    design_number = 2  # You can change this logic if needed
    if design_number == 1:
        button_list, image_list = return1()
        file_path = 'Design1.json'
    elif design_number == 2:
        button_list, image_list = return2()
        file_path = 'Design2.json'
    elif design_number == 3:
        button_list, image_list = return3()
        file_path = 'Design3.json'

    for element in button_list:
        text = returnText(element)
        update_json(file_path, element, text)

    link_list = []
    for element in image_list:
        link = returnImage(element)
        link_list.append(link)

    with open(file_path, 'r') as file:
        data = json.load(file)

    response_data = {'data': data, 'image_list': link_list}
    return jsonify(response_data)

@app.after_request
def after_request(response):
    response.headers.set('Access-Control-Allow-Origin', '*')
    response.headers.set('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.set('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

if __name__ == '__main__':
    app.run(debug=True)
