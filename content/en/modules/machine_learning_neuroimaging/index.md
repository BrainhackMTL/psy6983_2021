---
type: "modules" # DON'T TOUCH THIS ! :)

# Title of your project (we like creative title)
title: "Machine learning for neuroimaging"

# Your project GitHub repository URL
github_repo:

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/PSY6983-2021/project_template), click `manage topics`.
# Please only lowercase letters
tags: [fMRI, machine learning, neuroimaging]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "An introduction to fMRI data: the captured signal, the main steps of preprocessing and how functional connectivity is calculated."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "fMRI_connectivity.png"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Information

The estimated time to complete this training module is 4h.

The prerequisites to take this module are:
 * the [installation](/modules/installation) module.
 * the [introduction to python for data analysis](/modules/python_data_analysis) module.

Contact François Paugam if you have questions on this module, or if you want to check that you completed successfully all the exercises.

## Resources
This module was presented by Pierre Bellec during the QLSC 612 course in 2020, the slides are available [here](https://docs.google.com/presentation/d/1mTJoOSRKtGzhWeNLa9PXyKUYA0p9733UHVWrmIyi4zs/edit#slide=id.p).

The video of the presentation is available below:
<iframe width="560" height="315" src="https://www.youtube.com/embed/RoKt_c08wx" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## Exercise

 * Download the jupyter notebook with the folowing command, follow it carefully and complete the 3 exercises at the end.
 ```
 wget https://raw.githubusercontent.com/BrainhackMTL/psy6983_2021/master/content/en/modules/fmri_connectivity/BHS_fMRI_connectivity.ipynb
 ```
 * Follow up with François Paugam to validate you completed the exercise correctly.
 * :tada: :tada: :tada: you completed this training module! :tada: :tada: :tada:

## More resources

[Here](https://pbellec.github.io/functional_parcellation/#/) are Pierre Bellec's slides for a course on brain parcellation. They contain snippets of examples of nilearn code to load datasets, plot brains, compute and plot connectomes...

The video on resting state mentionned by Pierre in his presentation :
<iframe width="560" height="315" src="https://www.youtube.com/embed/_Iph3WW9UOU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

If you want to know more about fMRIprep, Basile Pinsard made a presentation on this topic for BrainHack school 2019 :
<iframe width="560" height="315" src="https://www.youtube.com/embed/WTcucXAAVBU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

