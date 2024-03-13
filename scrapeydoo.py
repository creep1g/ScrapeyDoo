import os
import requests
import json

def get_top_repos(n):
    url = 'https://github.com/search?q=stars%3A%3E200+forks%3A%3E50&type=Repositories&ref=advsearch&l=&l=&p={}'
    repos = []

    for p in range(1, n + 1):
        # n = number of pages
        formated = url.format(p)
        res = requests.get(formated)
        if res.status_code == 200:
            data = json.loads(res.text)
            res = data.get('payload', {}).get('results',[])
            
            for r in res:
                repo = r.get('hl_name')
                if repo:
                    repos.append(repo)
        else:
            print(p, "Failed")

    return repos


def clone(repos):
    for repo in repos:
        print("Do you want to clone(y/n):", repo)
        a = input()
        if a.to_lower() == "y":
            clone = f"https://github.com/{repo}.git"
            print ("Cloning", repo, "..." )
            os.system(f"git clone {clone}")
        else:
            print("Skipping")

if __name__ == '__main__':
    n = 3  #Number of pages
    repos= get_top_repos(n)
    print("Found",n,"repositories")
    clone(repos)

