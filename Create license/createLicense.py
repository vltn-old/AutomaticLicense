import os, sys;
from github import Github;



def main():
    arguments = sys.argv;

    if "--help" in arguments: # run the help function
        help();
    elif "--setLoginInfos" in arguments: # run setLoginInfos function
        setLoginInfos();
    else: # create the project
        gitCommit(arguments);

main();