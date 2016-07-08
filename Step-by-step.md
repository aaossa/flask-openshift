# Step by step

This is a guide explaining the process to create this template.

- Create a Python application, as explained in [OpenShift's Getting Started guide](https://developers.openshift.com/languages/python/getting-started.html) (Step 1)

```bash
$ rhc app create <project> python-3.3
```

- If you are using a GitHub remote you may want to push to GitHub and OpenShift with different commands. [This answer](http://stackoverflow.com/a/12669112/3281097) in [this StackOverflow question](http://stackoverflow.com/q/12657168/3281097)could be helpful.

```bash
$ git push
$ git push openshift HEAD
``` 

- Add Flask dependency in `<project>/requirements.txt`

```
Flask==0.11
```

- Personalize `<project>/setup.py`

- wsgi

- fodlers

- Flask says "Hello World!"

- Environment variables