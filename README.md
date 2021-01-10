# The Quantified Self 
### Optimizing health by learning from the past

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](../../)

## Basic Overview <br />
The Quantified Self is a holistic health program that seeks to optimize personal well-being by continually aquiring data of key trackers that contribute to one's overall health. Importantly, the data is analyzed daily using deep learning algorithms in order to make recommendations by which the user's health will be optimized. These recommendations pertain directly to the daily choices that each individual makes. The central idea of this program is that it is not enough to simply tracking one's own data; rather, self-improvement can only be obtained by learning from the past. The concepts behind The Quantified Self are in essence the foundation of preventive health care. 

The code is still early in its beta phase (which is also true for the movement at large), and it will become increasingly impactful the more user-friendly it becomes. A major limiting factor for this is the user input. The code should seek to track desired quantities in an automated way, with as little user interaction as possible. To this end, one key development may come from voice command applications. Specifically, there are currently a number of trackers that can only be input by hand (e.g. mindfulness time, nutrition, etc.), although a simple voice command (recorded by a smart watch or similar devive) would make tracking such quantities much more efficient. 

## Interfacing with Apple Health Data <br />

The current version of the code is only compatible with **Apple Health** and the **Health Auto Export to CSV** app (available [here](https://apps.apple.com/us/app/health-auto-export-to-csv/id1115567069)). In general, there are many different apps that one may use to track different quantities. However, these are all integrated via Apple Health into a single user interface that contains everything, i.e. one doesn't need to monitor the data over the numerous tracking apps. The Health Auto Export app synces the data in real time with a user's iCloud Drive. Likewise, The Qunatified Self connects with the user's health data through their iCloud drive, which is direclty accesible on their laptop/desktop. Note that since the program is ran from the user's computer, and interfaces entirely through Apple applications, the software does not introduce any increased risk to thier data privacy. In summary, to synce the code with your health data, the following steps must be taken:


<pre>
 1. Download the Health Auto Export to CSV app, available on Apple iPhone and Apple Watch
    - Allow the app to access Apple Health data
    - Synce the app with iCloud Drive
  
 2. Find the path to iCloud Drive on your laptop/desktop:
    - Should look something like this: "/Users/chriskarwin/Library/Mobile Documents/iCloud~com~ifunography~HealthExport/Documents/"
  
 3. Upon first using the code you will be prompted to enter the above path 
</pre>

## Input Data <br />

In general, there is a broad range of quantities a user may be interested in tracking. Some of these may include

* heart rate
* blood pressure
* o2 levels
* weight
* sleep
* steps
* mindfullness
* nutrition

Additionally, there are other quantities that will be more specific to each user. The Quantified Self allows the user to define their own set of values they wish to track, allowing the code to be specialized to each user's health needs/goals. As mentioned above, the code will become increasingly impactful the more automated the inputs become. This will surely be made possible via devices such as Apple Watch (more info [here](https://www.apple.com/watch/)).

## Health Evaluation <br />

There are four values that quantify a user's health: 

* Physical Health: the body
* Mental Health: the brain
* Spiritual Health: the soul (there are many synonyms for this)
* Happiness: one's overall state of content, security, joy, etc. In part, a wieghted sum of the first three evaluation variables.

These parameters should range from 0-10, and they are the subjective evaluations to be determined by the user. Ideally, health evaluations should be made daily. These are the parameters that the will be optimized over time, according to the input data. As the algorithm learns the input values that maximize the health parameters, is will begin to make recommendations as to future behavours that should be taken. 

The four health parameters listed above are in essence the most general components that comprize one's holistic self. In future versions of the code, these inputs should be developed further. Specifically, users will have specific health evaluation parameters that will best quantify thier overall well-being, e.g. they may be focused towards certain diseases such as diabetes, obesity, heart disease, etc. 

Note: the learning algorithm has not yet been applied to the code. 

## Quickstart Guide <br />

The code requires Python3. Currently, the user interacts with the code via the python API. The code can be envoked either from the terminal or the desktop (after specifying in the file info that it should be opened with Python3 as default). Upon first starting the code, the registration GUI will appear, as shown below. If defining values that will be synced with Apple Health, the value names must match exactly with the names from Health Auto Export.

<p align="center">
<img width="600"  src="Images/registration.png">
</p>

The main GUI is shown below. The "Input Data" tab allows the user to input thier daily data. The synced values will automatically update each day. The "Evaluate Self" tab allow the user to input thier own daily health assesment. Finaly, the self-reflection tab allows the user to see thier data. When a tracker is clicked a plot will appear showing the data. The user can specify the time range as either day (D), week (W), month (M), year (Y), or all data (A).

<p align="center">
<img width="600"  src="Images/main_overview.png">
</p>


