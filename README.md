# Flask OpenShift

This is a template to host in [OpenShift](https://openshift.redhat.com) a Python 3.x app using [Flask](http://flask.pocoo.org/). If you want to learn the process, you can read the [step by step](https://github.com/aaossa/flask-openshift/blob/master/Step-by-step.md) guide.

### Running on OpenShift

Create a Python application and move to your new folder

```bash
rhc app create <project> python-3.3
cd <project>
```

Add this upstream and pull

```bash
git remote add upstream -m master https://github.com/aaossa/flask-openshift.git
git pull -s recursive -X theirs upstream master
```

Now push the repo upstream

```bash
git push
```

Checkout the "hello world example" at

```
https://<project>-<namespace>.rhcloud.com
```

# License

Code licensed under [GNU General Public License v3](http://opensource.org/licenses/GPL-3.0).
