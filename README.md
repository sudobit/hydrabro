# hydrabro
Hero Wars Hydra Optimizer

This is a python script, which helps to find the best possible solution to kill hydra heads in Hero Wars. It takes a CSV comma-formatted list as input parameter and calculates possible kill configurations. Right now it ignore common and elder hydra and only goes for Ancient, Dreadful and Legendary. The algorithm basically brute forces the best configuration, while trying to use the best player to file the gap. This is why creating a lot of configurations is necessary to achieve good results. In our guild it achieves like the 95% top result and can be improved with some handy work after. 

## Install

- Install Python3, I used Python3.6 and it was not tried with any other version.

## Usage

Before you can run the tool you have to provide your players attack numbers on the hydra heads. This data is read from an .csv file. Look at example.csv to understand the structure. Running the tool is quit easy, since only two parameters can be provided. 

```
usage: hydrabro.py [-h] [--players CSV_FILE] [--amount AMOUNT]

Run HydraBro to optimize your hydra gains.

optional arguments:
  -h, --help          show this help message and exit
  --players CSV_FILE  Path to csv file which holds player numbers
  --amount AMOUNT     Amount of configurations to create, default to 50.000
```
Increasing AMOUNT above 250.000 can slow down the tool a lot. From expierence the best results are normally found after 25.000 configurations.

## Output

The tool outputs the top three configurations after it ran. It sorts each player to the head it is suppost to attack with an @ before. This should make it easy to post in your discord. The output looks something like this:

```
----- Configuration created on 2022-07-15-----
--- Legendary Hydra ---
Darkness: 2x @Player22, 2x @Player10, 3x @Player17, 1x @Player11, 1x @Player16, 1x @Player01, 
Light: 3x @Player04, 2x @Player11, 1x @Player02, 
Water: 2x @Player09, 1x @Player19, 1x @Player14, 1x @Player07 , 1x @Player08, 2x @Player16, 3x @Player13, 2x @Player03, 
Wind: 2x @Player19, 1x @Player14, 3x @Player15, 2x @Player07 , 1x @Player01, 1x @Player02, 
Earth: 
Fire: 1x @Player10, 1x @Player09, 1x @Player14, 2x @Player08, 1x @Player01, 1x @Player03, 1x @Player02, 

--- Ancient Hydra ---
Darkness: 1x @Player22, 1x @Player05 , 
Light: 2x @Player05 , 3x @Player24, 
Water: 2x @Player12, 2x @Player25, 
Wind: 
Earth: 
Fire: 1x @Player12, 1x @Player20, 

--- Dreadful Hydra ---
Darkness: 
Light: 
Water: 
Wind: 
Earth: 
Fire: 
```

This one was created with the example.csv file.

## Roadmap

Right now I am happy with the results and do not see a need to improve. I am thinking to try a second approach which should result in better results but yeah. Maybe add Common and Elder, but we do not have a use-case for that right now.
