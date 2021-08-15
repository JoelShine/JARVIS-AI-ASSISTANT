# JARVIS-AI-ASSISTANT

<p align='center'>
  <img src = "https://github.com/JoelShine/JARVIS-AI-ASSISTANT/blob/main/jarvis-assets/J.A.R.V.I.S.png" height='300' width='300'>
  </p>

A true Artificial Intelligent Assistant with ALICE as backend and offline speech recognition with vosk engine and pyttsx3 as text to speech engine

Unlike other assistants, this **JARVIS** is truly an ai written with ALICE files which uses Lisp as background.

Any issues on downloading and using this assistant, feel free to raise an [issue](https://github.com/JoelShine/JARVIS-AI-ASSISTANT/issues) so I can look into the problem code. Please follow the below installation process to get it done nicely for your needs.

## About JARVIS

Jarvis is actually an ai which was introduced in the first Iron Man movie. A very spohisticated AI for Tony Stark made programmers think about making their on AI Assistants. This JARVIS also got it's inspiration fro Iron Man movies.

JARVIS - **JOEL'S ARTIFICIAL REALISTIC VIRTUAL INTERNET SERVICE"**

There had been many different versions of my Jarvis in the past few months. First, it had been a text assistnat, then speech came and this version is my first every fully artificially intelligent jarvis program with AIML. This is completely written in Python and it is compatible with almost all systems (Mac OS, Linux and Windows(Recommended)). Being written in Windows, it is more suitable to be used in Windows. Some minor changes will be needed to run on other os.

See my first JARVIS project (text to speech only) - https://github.com/JoelShine/JARVIS-The-Ultimate-Project

See my second JARVIS initiative (speech recognition) - https://github.com/JoelShine/Jarvis-v2.0

## Specialty of JARVIS

<ul>
  <li>Fully autonomous with <b>AIML</b> and <b>Lisp</b> as the brain of JARVIS.</li>
  <li>Support with offline speech recognition with the help of <b>vosk</b> models.</li>
  <li>Offline Text to Speech service with <b>pyttsx3</b>.</li>
  <li>More surer program launching mechanism.</li>
  <li>Very powerful chat mode with ALICE files.</li>
</ul>

## Setup Procedures
For getting JARVIS up and running, the instructions are given below :

### Environment setup
<ul>
  <li> <h4> You need to have Python 3.7 or later versions top run Jarvis. Jarvis is initially developed in Python 3.8.9, so getting the same version will be nice to avoid any other issues but 3.7 or later is also okay</h4> <b>Please note : Make sure to download Python 64 bit only ! Some modules are compatible only with 64 bit version. Also add Python to your system PATH.</b> <br><br> Download your python version from https://www.python.org/ <br> For getting Python 3.8.9, just click this link and download python for your os - https://www.python.org/downloads/release/python-389/ <br> Python 3.8.9 download for windows - https://www.python.org/ftp/python/3.8.9/python-3.8.9-amd64.exe <br></li>
  
  <li> <h4> After installing python correctly, make sure you have pip installed on your machine. Open command prompt or powershelll and type <i>pip</i> or <i>pip3</i> if something shows up, it's fine but if it says "It is not recognised as an internal or external command", just google it on how to install pip.<br><br>How to fix pip - https://www.youtube.com/resultssearch_query=how+to+fix+pip+is+not+recognized+as+an+internal+or+external+command</h4></li>
  
  <li><h4>Finally, once you install Python 64-bit version and pip, we can go on with installing the key dependencies. <br></h4></li>
</ul>

### Installing the required modules

<ul>
  <li><h4> First, navigate to this cloned repository and open cmd and then type : </h4></li>
</ul>

```
pip install -r requirements.txt
```
<ul>
  <li>Most of the times, you may run into an error saying <b>'no module named pyaudio'</b>. If there is any error on installing SpeechRecognition, do check out this website. Please download the ".whl" file of pyaudio of your python version. Link to website - https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio . After downloading that, pip install that .whl file. For Eg:</li>
  </ul>
  
 ```
 pip install PyAudio‑0.2.11‑cp38‑cp38‑win_amd64.whl
 ```
 <ul>
  <li>The above wheel is suitable for Python 3.8 version. amd64 means 64 bit and win32 means 32-bit. First pip install the wheel and then again run pip install -r requirements.txt . After all these procedures, we are ready to start testing out JARVIS. <br></li>
  </ul>

### Getting the models for our Speech Engine

<ul>
  <li><h4>Now, the next step is to download the models for our vosk speech Engine. Go to this website for downloading the model of your choice - https://alphacephei.com/vosk/models</h4></li>
  <li>There are models available for several accents of English and I am currently using the Indian Model. If you are in USA, you could download the usa-english model. The model is not uploaded on github as it will take up large space.<br></li>
  <li>Once you have downloaded the Vosk speech engine model, then extract all the files inside the downloaded folder and copy the files inside the <b>'vosk_speech_engine/model'</b> folder. Make sure to place this in the model folder inside vosk_speech_engine.<br></li>
  <li>Once you have placed that, we can successfully run our JARVIS program<br><br></li>
  </ul>

## Running the Python script

Now we can run our python script. Just navigate to the cloned directory and open cmd and then type :
```python
python jarvis.py
```
This will initialize the python program. If you run into any problems during the installation of any modules, feel free to open an [issue](https://github.com/JoelShine/JARVIS-AI-ASSISTANT/issues). Thanks for supporting this project and happy coding !!
