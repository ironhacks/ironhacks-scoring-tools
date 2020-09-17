# extract-and-download-links
Script to Extract and Download Links 

Step 0 

Put all the input files that you want to extract URLS and download URLS from in the same directory as the extract-url.sh script and download.py script

Step 1

Run "chmod +x extract-url.sh" to enable the execution of the bash script.

Step 2

When you execute "./extract-url.sh", you will see a list of URLS output on your screen. 

Step 3

Copy all the URLS output to the screen to a newly created text file named "to-be-downloaded.txt" in the same directory as the download.py script. 

Step 4

Do "module load anaconda/5.1.0-py36" to load the python3 modules in the environment. 


Step 5

Execute the python script by running "python3 download.py" to download the files from the URLS. 


