# About
**pdfsplit** is simple, open-sourced and privacy-aware tool to split PDF files into their multiple pages. The web application allows users to upload a PDF file and in turn download a .zip file with all the pages that the original file contains.

For example, if I upload a file called `notes.pdf` and this file has 3 pages, the user will be able to download a `notes.pdf.zip` file with the following files inside:

```
1.pdf
2.pdf
3.pdf
```

# Privacy
**pdfsplit** is designed with privacy in mind. All uploaded and processed files are automatically deleted after the download is completed to ensure user data is not stored on the server unnecessarily. The only information we'll eventually track is the number of pages of each PDF and their size for analytics purposes.

# PDF page splitter CLI
To use the CLI, clone the repository and run the commands
```
pip3 install -r requirements
python3 cli/run.py <pdf_filename>
```

The command will create multiple PDF files in the `output/` folder and rename them in the format `<page-number>.pdf`.
