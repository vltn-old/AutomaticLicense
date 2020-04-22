import os, sys;
from github import Github;

def getGithubLogin(arguments):
    try:
        file = open(arguments[0][:-len("Create License/createLicense.py")] + "githubLogin.txt", "r");
        fileData = file.readlines();

        return fileData;
    except:
        print('!!! You miss to set your github login data.');
        print('Call gitPush --setLoginInfos to fix this error');
        print('See "gitPush --help" for more infos.');
        print();

        return "False";



def createLicense(arguments):
    try:
        licenseType = arguments[2];
        path = arguments[1];

        try:
            file = open(arguments[0][:-len("Create License/createLicense.py")] + "Licenses/" + licenseType + ".txt", "r");
            fileData = file.read();
            file.close;

            print('Creating LICENSE file');
            file = open(path + "/LICENSE", "a+");
            print('test1');
            file.write(fileData);
            print('tets2')
            file.close();

            print();

            email = getGithubLogin(arguments)[0][:-len("\n")];
            mdp = getGithubLogin(arguments)[1][:-len("\n")];

            if email == "False" or mdp == "False":
                return False;

            print('Going to ' + path);
            os.chdir(path);

            print();

            print('Configurating user identification to github for the project.');
            os.system('git config user.email "' + email + '"');

            print();

            print('Do commit');
            os.system('git add .');
            os.system('git commit -m "Create LICENSE"');
            os.system('git push -u origin master');

        except:
            print("This LICENSE does not exist. Make sure that you have created '" + licenseType + ".txt' file in the correct folder");
    except:
        print("!!! You miss to refer the LICENSE type. For example MIT");


def setLoginInfos(arguments):
    print("What is your github account email adress ?");
    email = input();

    print();

    print("What is your github account password ?");
    password = input();

    file = open(arguments[0][:-len("Create License/createLicense.py")] + "githubLogin.txt","a+");
    file.write(email + "\n");
    file.write(password + "\n");
    file.close();



def help(): # function help that list all function and there utilisation
    print();

    print('How to use create license:');
    print("    _ createLicense <commit description>");
    print("    _ createLicense --setLoginInfos");
    print("    _ createLicense --help");

    print();

    print('createLicense <commit description>:');
    print('    your commit description need to be between quotation mark.');

    print();
    
    print('!!! *** !!!');
    print();
    print('Important: before using createLicense you NEED:');
    print('    to refers your github account email adress and github password');
    print();
    print('!!! *** !!!');



def main():
    arguments = sys.argv;

    if "--help" in arguments: # run the help function
        help();
    elif "--setLoginInfos" in arguments: # run setLoginInfos function
        setLoginInfos(arguments);
    else: # create the project
        createLicense(arguments);

main();