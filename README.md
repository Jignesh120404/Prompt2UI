# Prompt2UI
Prompt2UI is an experimental project aimed at making AI generated landing page designs directly in Figma.
This project is for research purpose only.

## Features

- Uses OpenAI's ```GPT-3.5-Turbo-0613``` to generate the text used on the website design.
- Utilizes three pre-made figma designs which are then customized using AI  to create custom designs based on the input by the users.



## Starting the plugin

1. Launch the Figma Desktop App.
2. Open terminal in the project directory and run the following python script to get our backend up and running:
```bash
python prompt2UI.py
```
This establishes a way for our project to fetch data from OpenAI and Midjourney.
3. Go to the Figma App, create a new design file, right click on the blank space, go to 
'Plugins' -> 'Development' -> 'Import Plugin from Manifest...'
4. Navigate to the project directory, select manifest.json and click open. 
5. You will now find the Plugin ready to use under plugins tab, just put in Industry Type and Company Name then click 'Generate' to get your custom design!
