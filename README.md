# Brainhack School
[![Netlify Status](https://api.netlify.com/api/v1/badges/4bc0bac4-8f69-4d6e-b214-8c7b7ebfa1d5/deploy-status)](https://app.netlify.com/sites/suspicious-golick-ab329b/deploys)

This is the website of the brainhack school, built with [hugo](https://gohugo.io/), and deployed with [netlify](https://www.netlify.com/). 

To test it locally, you will need to:
1. Clone/fork this GitHub repo: `git clone https://github.com/BrainhackMTL/school.git`
1. Make sure you're inside the **school/** dir (`cd psy6983_2021`), then **clone the submodule for themes:** `git submodule update --init --recursive --remote`
1. If [Hugo](https://gohugo.io/) is not installed, follow the steps in their documentation to install it on your machine: https://gohugo.io/getting-started/installing/
1. To run the website locally, make sure you are still in `school/` dir and type `hugo serve -D`.
   - The -D option is to serve the website including the draft .md files.
