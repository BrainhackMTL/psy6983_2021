---
type: "modules" # DON'T TOUCH THIS ! :)

# Title of your project (we like creative title)
title: "A brief introduction to the bash shell"

# Your project GitHub repository URL
github_repo:

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/PSY6983-2021/project_template), click `manage topics`.
# Please only lowercase letters
tags: [bash shell, terminal]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "This tutorial aims at introducing students to the use of command line terminal which offers more flexibility than build-in graphical user interfaces. We hope to provide students with an understanding of the basic command lines and advantages of working with the bash shell."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "git_github.png"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Information

The estimated time to complete this training module is 4h.

The prerequisites to take this module are:
 * The [installation](/modules/installation) module.
   - Windows: Ubuntu application (Windows Linux Subsystem)
   - Mac/Linux: Terminal

You environment should be ready to go, everything required was set up during installations!

Contact Andréanne Proulx if you have questions on this module, or if you want to check that you completed successfully all the exercises.

## Resources
This module was presented by [Ross Markello](https://rossmarkello.com/) during the QLSC 612 course in 2020.

All the tutorial notes related to the video below are available [here](https://github.com/neurodatascience/course-materials-2020/blob/master/lectures/11-may/03-intro-to-shell/introduction-to-shell.ipynb). 

The video of the presentation is available below (duration 1h13) :
<iframe width="560" height="315" src="https://www.youtube.com/watch?v=N6soV0dlB-k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Follow along with the video of the presentation, typing the command line into your terminal.

## Exercises

### Test your knowledge

Once you've completed the tutorial, try testing your understanding by answering the following questions. 

Short answers

 - *What are some of the main advantages in using the shell?*
 - *What are some of its disadvantages?*
 - *Name a few command lines that enable to read/write/operate on files. What are they used for?*
 - *What is an option, also called flag or switch?*
 - *What are arguments in a command line*?
 - *Can you tell the difference between relative and absolute paths?*

True/False

 - *We are always located somewhere in the file system*
 - *It is possible to be located in more than one place at once*
 - *You can’t choose multiple options after a command* 
 - *Changing one directory at a time is the same as providing the full path to the final destination
 - *Environmental variables are preceded by `$`*

Multiple choice answer

 - *Starting from `/Users/amanda/data`, which of the following commands could Amanda use to navigate to her home directory, which is `/Users/amanda`?*
     - a) cd .
     - b) cd /
     - c) cd /home/amanda
     - d) cd ../..
     - e) cd ~
     - f) cd home
     - g) cd ~/data/..
     - h) cd
     - i) cd ..
   
 - *After running the following commands, Jamie realizes that she put the files sucrose.dat and maltose.dat into the wrong folder. The files should have been placed in the raw folder.*
> `$ ls -F`
 analyzed/ raw/
 
> `$ ls -F analyzed`
fructose.dat glucose.dat maltose.dat sucrose.dat

> `$ cd analyzed`
Fill in the blanks to move these files to the raw/ folder (i.e. the one she forgot to put them in):
`$ mv sucrose.dat maltose.dat ____/____`
mv sucrose.dat maltose.dat ../raw

Suppose that you created a plain-text file in your current directory to contain a list of the statistical tests you will need to do to analyze your data, and named it: statstics.txt

After creating and saving this file you realize you misspelled the filename! You want to correct the mistake and remove the incorrectly named file. Which of the following commands could you use to do so?

cp statstics.txt statistics.txt
mv statstics.txt statistics.txt
mv statstics.txt .
cp statstics.txt .

Remember, the .. refers to the parent directory (i.e., one above the current directory)

 * Practice makes perfect! Complete the following exercices using the shell. 
 
 # Exercice 1 







 - True/False
 - 
 

 * Practice makes perfect! Complete the following exercices using the shell. 

 - Now, let’s open the terminal and start typing some commands!
 - Figure out where you are in the file system using the command `pwd`
 - 






## More resources

If you are curious to solidify your capabilities for using the shell, you can check this tutorial "Effective use of bash" by Ankur Sinha organized for the [INCF/OCNS software working group](https://ocns.github.io/SoftwareWG/2021/06/09/software-wg-tutorials-at-cns-2021-online-bash-git-and-python.html).

You can also try out this tutorial which inspired much of the content you saw today, while exploring the shell in further detail. It covers pipes and filters, loops, shell scripts, finding things) [The Unix Shell](https://swcarpentry.github.io/shell-novice/01-intro/index.html)

<iframe width="560" height="315" src="" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
