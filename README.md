Hi there! This readme is from my blog at https://rboyd.me and you should check it out if you find this tutorial helpful.

I will not be using a virtual environment for this tutorial, because the dependencies do not work properly. Instead, I would recommend using Oracle VM. This way, if your project gets too messy, which it did for me when I was figuring this out, you can just scrap everything and not have code all over your PC.

So let’s get started. First,  download a Linux OS and set it up in Oracle VM. I use Xubuntu, but any Ubuntu versions should be functionally the same for this. When you are in your desktop, run software updater, restart, press Ctrl + Alt + T to open up a terminal, and run the following commands:

sudo apt-get update

sudo apt-get upgrade

sudo apt install python-pip

sudo apt install python3-pip

sudo apt-get install npm

sudo apt-get install git

sudo apt-get install curl

curl -sl https://deb.nodesource.com/setup_8.x | sudo -E bash -

sudo apt-get install -y nodejs

npm install ngrok



OK! Now we can get started with my repo. Run this command:

git clone https://github.com/RonanBoyd/weatherbotRB

Okay. In terminal, navigate to the directory you cloned to by typing in 

cd weatherbotRB

and run

pip3 install -r requirements.txt

Now, we need to get spacy, and the spacy language models. Run

pip install -U spacy

We need the language model, for the sake of this tutorial we will use the small one, but for real world application, make sure you use at least the medium size, by replacing sm in this code with md. So now let’s run

sudo python3 -m spacy download en_core_web_sm

and this next command will link the model. Be aware, it almost NEVER works until you run the pip reinstall command I have posted below.

python3 -m spacy link en_core_web_sm en -f

If you run into issues here, try running

sudo python3 -m pip uninstall pip && sudo apt install python3-pip --reinstall

Now, run

sudo npm i -g rasa-nlu-trainer



This is the end of my tutorial for now. I will be updating it soon, with info on how to connect to a web API.
