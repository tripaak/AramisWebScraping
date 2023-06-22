@author : tripaak.akash@gmail.com

Project structure: 

AramisWebScraping
        |
      Spiders
        |
        |---clicars
        |
        |---Brumbrum (yet to devlop)
        |
        |
      runner.py (to run the project)






Project: Clicars 

    Prerequistes: 
        1. clicars.csv --> name of file should be maintained 
        2. Header name in clicars.csv should be maintained (i.e  "vin", "URL" )
        3. requirement.txt file has all dependencis 
        
        prepare: 
        1. git clone <repo>
        2. cd <repo>
        2. pip install virtualenv (if you don't already have virtualenv installed)
        3. virtualenv venv to create your new environment (called 'venv' here)
        4. source venv/bin/activate to enter the virtual environment
        5. pip install -r requirements.txt to install the requirements in the current environment

    Execution: 
        python ./ clicars_runner.py
        OR
        python3 ./ clicars_runner.py


    Output: 
        output is produced in folder ./output_folder/DDMMYY/(Todays Date)
        output file in format clicras_status_HHMMSS.CSV
        