# Griffin- a AI Powered Privacy Shield Against UI Deception and Product Info Mislead

Griffin, a Chrome extension, detects and highlights dark patterns on shopping websites by analyzing product page text. It owes its success to the research paper "Dark Patterns at Scale" by Mathur et al., leveraging their dataset and page segmentation algorithm. The extension exposes and categorizes dark patterns, empowering users with insights into deceptive practices in the online shopping landscape. The collaboration with Mathur et al. has been instrumental in enhancing awareness and promoting responsible design.




![newui_after](https://github.com/Harris2621/griffin/assets/144410689/753673c8-92cd-4e95-b921-4db5fb822d41)

WHAT IS DARK PATTERNS?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Dark patterns refer to deceptive design techniques employed in user interfaces to manipulate users into taking actions they may not otherwise choose to do. These patterns are often used to trick, coerce, or mislead users, typically for the benefit of a website or service, at the expense of user experience and autonomy.To know more about dark patterns and its approach refer the site https://en.wikipedia.org/wiki/Dark_pattern

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
TECH STACK:
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The Chrome Extension front-end that scrapes the active web page is written in Javascript. For the back-end, a Python server running Flask interfaces RCNN models to classify tokens of text sent to it. To train these algorithms, datasets from Princeton University researchers along with manually annotated datasets were used.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

INSTALLATION:
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
To begin installation, first clone this repository, or download and unzip it.

Install and run the Flask app backend by navigating to api, installing required libraries, and running app.py with Python

Install the Chrome extension:

Navigate to chrome://extensions
Enable "Developer mode" by toggling the switch at the top right of the page
Click the "Load unpacked" button.
Navigate to the repository directory, and select the folder app for installation
Ensure that the extension is enabled, and if so, the extension has been successfully installed!

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## REFERENCE:

Mathur, A., Acar, G., Friedman, M. J., Lucherini, E., Mayer, J., Chetty, M., & Narayanan, A. (2019). Dark Patterns at Scale: Findings from a Crawl of 11K Shopping Websites. Proceedings of the ACM on Human-Computer Interaction, 3(CSCW), 81.
