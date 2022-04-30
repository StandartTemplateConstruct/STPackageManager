
A static website that displays all Readme.md s of all GitHub/GitLab repos from the twits marked with `#ProjectFinancier` hashtag with a MetaMask enabled link to donate them money/buy into their ICOs


## Project list

last 200 twits with #ProjectFinancier are fetched. The pattern of github repos is found in them. For each github repo, following is listed:

 - link to the project page
 - link to the github repo
 - *optional* github activity graph
 - last commit
 - amount of commits
 - github description

## Project page

 - link to the GitHub repo
 - button to contribute via metamask/qr code popup, to the address listed in `README.md` file
 - contents of Readme.md, formatted
 - *optional* translation to languages of choice (based on the LANGUAGES: EN, ES statement in `.finpresent` file in the repo)
 - *optional* navigation through all `.md` files of github repo tree in-site 



#### old


GithubDonationPortfolio.com
A web portfolio of GitHub projects of the user with metamask enabled donation links per project.

Fetches from the README.md of the project:

ETH wallet for donation
How much is needed to project completion
Fetches from Eth network:

how much total have been sent to this wallet
