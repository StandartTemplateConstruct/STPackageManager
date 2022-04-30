# GithubRepoGenerator
 - runs in the git repository containing some documenation files
 - extracts from it the terms that look like names of programs - `NAMES`
 - chooses a template for the project based of text of `README.md`, scaffolds it
   - *leverages cmake?*
   - Picks a template from a folder of templates
     - SwiftUI iOS app
     - RealityKit iOS app
     - Unity iOS AR project
     - Unreal iOS AR project
     - python package
     - ReactJS one page static app
     - Etherium Smart Contract
     - autotools C++ project
 - for each `NAME` generates `docs/NAME.md` filled with results of interference of [READMEToDocumentationDecomposer](https://github.com/StandartTemplateConstruct/GithubRepoGenerator/blob/main/READMEToDocumentationDecomposer.md) 
 - creates class/*other code entity* for each mentioned `NAME`
 - populates each class with prompts from `docs/NAME.md`

Uses OpenAI Codex or alternative 
