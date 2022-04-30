# GithubReadmePDFBookGenerator
Generate a PDF book out of Github README.md


 - receives Github repo, generates a PDF file out it's README.md
 - wide fields, page numbers
 - on the page fields:
   - a visually connected to the place of origin with a light grey comicbook flyout to the hyperlinks
     - QRCode
     - Thumbnail of the page where this hyperlink is leading
     - `see page XX.` - if hyperlink is leading onto Github markdown file that is included into the book
 - Contents of the book:
   -  `README.md` of the first project
   -  All internal to this project Markdown documents in separate chapters
   -  All source code listings to which links from Markdown documents are made
     -  In literate programming format: two columns one is comments another is code
   -  Per section for each project that first project references, processed in the same way as first project
 -  Wrapped with text AI generated illustrations one per page, for inferred with "consise that" model text as the prompt to DALL-E AI
   
