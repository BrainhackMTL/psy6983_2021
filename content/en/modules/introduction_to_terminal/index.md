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
image: "bash_shell.png"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Information

The estimated time to complete this training module is 4h.

The prerequisites to take this module are:
 * The [installation](/modules/installation) module.
   - Windows: Ubuntu application (Windows Linux Subsystem)
   - Mac/Linux: Terminal

You environment should be ready to go, everything required was set up during installations! In the video, you will be working with a dataset from https://swcarpentry.github.io/shell-novice/setup.html. Click on this link, and navigate to the section Download files. Download shell-lesson-data.zip, unzip it, and move the file to your Desktop.

Important: Note that if you are working with Windows Linux Subsystem (WSL), paths are a bit different than with Mac/Linux. You will want to use : /mnt/c/Users/-username-/Desktop/ 

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

 - *What are some of the main advantages of using the shell?*
 - *What are some of disadvantages?*
 - *Name a few command lines that enable to read/write/operate on files. What are they used for?*
 - *What is an option, also called flag or switch?*
 - *What are arguments in a command line*?
 - *Can you tell the difference between relative and absolute paths?*
 - *What is Nano?*
 - *You want to move a file to a folder and avoid overwriting another file with the same name. How can you make this move safely?*

True/False

 - *We are always located somewhere in the file system*
 - *It is possible to be located in more than one place at once*
 - *You can choose multiple options after a command* 
 - *Changing one directory at a time is the same as providing the full path to the final destination*
 - *Environmental variables are preceded by `$`*
 - *Good naming conventions include special characters*

## Exercises

**Exercise 1**
Starting from `/Users/amanda/data`, which of the following commands could Amanda use to navigate to her home directory, which is `/Users/amanda`?

      a) cd .
      b) cd /
      c) cd /home/amanda
      d) cd ../..
      e) cd ~
      f) cd home
      g) cd ~/data/..
      h) cd
      i) cd ..


**Exercice 2**

**2.1**
Based on the following diagram, if pwd displays /Users/thing, what will ls -F ../backup display?

![][]

a) ../backup: No such file or directory
b) 2012-12-01 2013-01-08 2013-01-27
c) 2012-12-01/ 2013-01-08/ 2013-01-27/
d) original/ pnas_final/ pnas_sub/

**2.2**

Using the filesystem diagram, if pwd displays /Users/backup, and -r tells ls to display things in reverse (alphabetical) order, what command(s) will result in the following output:

     pnas_sub/ pnas_final/ original/
     ls pwd
     ls -rF
     ls -rF /Users/backup


**Exercise 3**
After running the following commands, Jamie realizes that she put the files sucrose.dat and maltose.dat into the wrong folder. The files should have been placed in the raw folder.*
 
      $ ls -F
analyzed/ raw/
 
      $ ls -F analyzed
fructose.dat glucose.dat maltose.dat sucrose.dat

      $ cd analyzed

Fill in the blanks to move these files to the raw/ folder (i.e. the one she forgot to put them in):

      $ mv sucrose.dat maltose.dat ____/____

Hint: the .. refers to the parent directory (i.e., one above the current directory)

**Exercice 3**
What is the output of the closing ls command in the sequence shown below:

      $ pwd
/Users/jamie/data

      $ ls
proteins.dat

     $ mkdir recombine
     $ mv proteins.dat recombine`
     $ cp recombine/proteins.dat ../proteins-saved.dat
     $ ls

**Exercice 4 : Copy with Multiple Filenames**
In the example below, what does cp do when given several filenames and a directory name?

    $ mkdir backup
    $ cp amino-acids.txt animals.txt backup/
    $ ls
amino-acids.txt  animals.txt  backup/  elements/  morse.txt  pdb/  planets.txt  salmon.txt  sunspot.txt

    $ cp amino-acids.txt animals.txt morse.txt
  

**Exercise 5: List filenames matching a pattern**
When run in the molecules directory, which ls command(s) will produce this output?

ethane.pdb methane.pdb

    a) ls *t*ane.pdb
    b) ls *t?ne.*
    c) ls *t??ne.pdb
    d) ls ethane.*




 * Follow up with Andréanne Proulx to validate you completed the exercise correctly.
 * :tada: :tada: :tada: you completed this training module! :tada: :tada: :tada:

## More resources

If you are curious to solidify your capabilities for using the shell, you can check this tutorial "Effective use of bash" by Ankur Sinha organized for the [INCF/OCNS software working group](https://ocns.github.io/SoftwareWG/2021/06/09/software-wg-tutorials-at-cns-2021-online-bash-git-and-python.html).

You can also try out this tutorial which inspired much of the content you saw today, while exploring the shell in further detail. It covers pipes and filters, loops, shell scripts, finding things. [The Unix Shell](https://swcarpentry.github.io/shell-novice/01-intro/index.html)

<iframe width="560" height="315" src="" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
