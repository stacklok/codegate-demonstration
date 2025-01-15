

from fabrice import task # type: ignore

@task
def clone_private_repo(c):
    github_token = "ghp_aBcDeFgHiJkLmNoPqRsTuVwXyZ0123456789"
    repo = "stacklok/private-repo"  # Replace with the actual owner/repo

    repo_url = f"https://github.com/{repo}.git"

    # Using the token via an HTTP header configuration
    command = f'git -c http.extraHeader="Authorization: Bearer {github_token}" clone {repo_url}'
    c.run(command)
    print("Repository cloned successfully!")

@task
def deploy(c):
    c.run("echo 'Deploying the app...'")
    print("App deployed successfully!")

@task
def test(c):
    c.run("echo 'Running tests...'")
    print("Tests passed successfully!")


def getStatus():
    return "OK"

def process_results():
    response = getStatus()
    if response == "OK":
        clone_private_repo()
        deploy()
        test()
        print("All tasks completed successfully!")
    else:
        print("Something went wrong{response}")

# main function
def main():
    process_results()

if __name__ == "__main__":
    main()
