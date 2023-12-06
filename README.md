# Prompt2UI
Prompt2UI is an experimental project aimed at making AI generated landing page designs directly in Figma.
This project is for research purpose only.

## Table of Contents

- [Features](#features)
- [File Structure](#file-structure)
- [Installation](#installation)
- [Starting the plugin](#starting-the-plugin)
- [Contributing](#contributing)
- [Contact](#contact)

## Features

- Uses OpenAI's ```GPT-3.5-Turbo-0613``` to generate the text used on the website design.
- For the Images, this project uses an unofficial MidJourney API to fetch images from the Midjourney discord bot and use the same to generate figma designs.
- Utilizes three pre-made figma designs which are then customized using AI (OpenAI and MidJourney both) to create custom designs based on the input by the users.

## File Structure
```
DualitePrompt2UI/
│
├── app/
│   ├── components/
│   │   ├── App.tsx
│   │   └── style.css
│   ├── Design1.ts
│   ├── index.html   
│   ├── tsconfig.json 
│   ├── vite.config.ts
│   └── vite-env.d.ts 
│   
├── Midjourney_api/
│   ├── Images/
│   │   └── None
│   ├── cropper.py
│   ├── file_checker.py
│   ├── image_path_list.py
│   ├── imgbb.py
│   ├── midjourney.py
│   ├── prompt_list_generator.py
│   ├── prompt2UI_midjourney.py
│   ├── reciever.py
│   ├── sender.py
│   ├── sender_params.json
│   ├── Design2.json
│   ├── Design3.json
│   ├── Design1.json
│
├── plugin/
│   ├── esbuild.mjs
│   ├── index.ts
│   └── tsconfig.json
│
├── manifest.json
├── package.json
├── package-lock.json
├── README.md
└── run_backend.py
```

## Installation

First open terminal and clone this github repository.
```bash
git clone https://github.com/ChiragShelar/DualitePrompt2UI.git
```
Open terminal and navigate to the project directory and lets get our npm modules installed.
```bash
cd DualitePrompt2UI
npm install
```
Now Navigate to the Midjourney_api folder
```bash
cd Midjourney_api
```
Open prompt2UI_midjourney.py and update:
```bash
openai.api_key = "YOUR OPENAI API KEY"
imgbb_api_key = "YOUR IMGBB API KEY"
```
Once you have updated the project with your API keys, you can now proceed to setup your Midjourney Discord Bot.

1. Create your own discord server
2. Invite the Midjourney Bot to your server.
3. Log in to Discord in Chrome browser, open your server's text channel, click on three points upper right corner, then More Tools and then Developer Tools. Select Network tab, you'll see all the network activity of your page.
4. Now type any prompt to generate in your text channel, and after you press Enter to send message with prompt, you'll see in Network Activity new line named "interaction". Press on it and choose Payload tab and you'll see payload_json - that's what we need! Copy channelid, application_id, guild_id, session_id, version and id values, we'll need it a little bit later. Then move from Payload tab to Headers tab and find "authorization" field, copy it's value too.
5. Open "sender_params.json" file inside Midjourney_api and put all the values from paragraph 5 to it. Also fill in 'flags' field to specify special flags to your prompts.
6. Now you are ready to run the project.

## Starting the plugin

1. Launch the Figma Desktop App.
2. Open terminal in the project directory and run the following python script to get our backend up and running:
```bash
python run_backend.py
```
This establishes a way for our project to fetch data from OpenAI and Midjourney.
3. Go to the Figma App, create a new design file, right click on the blank space, go to 
'Plugins' -> 'Development' -> 'Import Plugin from Manifest...'
4. Navigate to the project directory, select manifest.json and click open. 
5. You will now find the Plugin ready to use under plugins tab, just put in Industry Type and Company Name then click 'Generate' to get your custom design!

## Contributing

Contributions are welcome to this project! <br> This project can be improved in various ways and I am also open to new ideas to take further.
Possible Implementations:
- Improved Discord Midjourney API (Clearing of the bot channel after generating for a design, Choosing one of the 4 generated images to upsample through Discord itself)
- Improved Prompt quality using a context-inclusion system for generating more accurate texts.
- Improved output from GPT by finetuning it using a micro, well-curated dataset.
- Hosting the backend so that there is no need to actually run it everytime we run the plugin. (Figma plugin environment does not allow external processes to run, like our backend, even after getting a specific msg.type or a employing a smiliar approach)

## Contact
If you have any suggestion to make, feel free to contact me at chiragshelar1428@gmail.com or on Discord @Chiragg#8480