# Home-Depot-Semantic-Segmentation

## Milestone 1

### CVAT Installation Instructions Followed

- Install WSL2 (Windows subsystem for Linux) refer to [this official guide][WSL2-Guide] 
WSL2 requires Windows 10, version 2004 or higher. Note: You may not have to install a Linux distribution unless needed.

- Download and install [Docker Desktop for Windows][Docker-Download] Double-click `Docker for Windows Installer` 
to run the installer. Note: Check that you are specifically using WSL2 backend for Docker.

- Download and install [Git for Windows][Git-Download]. When installing the package please keep all options 
by default. More information about the package can be found here.

- Download and install [Google Chrome][Chrome-Download]. It is the only browser which is supported by CVAT.

- Go to windows menu, find Git Bash application and run it. You should see a terminal window.

- Clone CVAT source code from the GitHub repository.

The following command will clone the latest develop branch:

```
git clone https://github.com/opencv/cvat
cd cvat
```

Run docker containers. It will take some time to download the latest CVAT release and other 
required images like postgres, redis, etc. from DockerHub and create containers.

```
docker-compose up -d
```

You can register a user but by default it will not have rights even to view list of tasks. 
Thus you should create a superuser. A superuser can use an admin panel to assign correct 
groups to other users. Please use the command below:

```
winpty docker exec -it cvat_server bash -ic 'python3 ~/manage.py createsuperuser'
```

Choose a username and a password for your admin account. For more information please read Django documentation.

Open the installed Google Chrome browser and go to localhost:8080.

![Screenshot of CVAT's Log-in Page][CVAT-LogIn-Screenshot]

[WSL2-Guide]: [https://docs.microsoft.com/windows/wsl/install-win10]
[Docker-Download]: [https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe?utm_source=docker&utm_medium=webreferral&utm_campaign=dd-smartbutton&utm_location=module]
[Git-Download]: [https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-64-bit.exe]
[Chrome-Download]: [https://www.google.com/chrome/]
[CVAT-LogIn-Screenshot]:./media/CVAT-LogIn-ScreenShot.png "CVAT LogIn Page Screenshot"

