# Generator of the PDF containing exaustive infromation on all software products that are used for building an open source project

 - assign all words in `NameOfRepo/README.md` a scores of their specificality
 - for each word over a treshold, find a Github repo and link it 
   - see [WikipediaGithubExport](https://github.com/StandartTemplateConstruct/WikipediaGithubExport)
 - for each github repo found repeat the process
 - sort chapters of the book from less specific word definitions to more specific
 - put "NameOfRepo: Description" on cover and add `NameOfRepo/README.md` in front again
