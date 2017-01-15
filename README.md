# Flask OpenShift

This is a template to host in [OpenShift](https://openshift.redhat.com) a Python 3.x app using [Flask](http://flask.pocoo.org/). If you want to learn the process, you can read the [step by step](https://github.com/aaossa/flask-openshift/blob/master/Step-by-step.md) guide.

### Running on OpenShift

Create a Python application with this command

```bash
rhc app-create <project> python-3.3 --from-code https://github.com/aaossa/flask-openshift.git
```

Checkout the "hello world example" at

```
https://<project>-<namespace>.rhcloud.com
```

### More

You can use a different cartridge:

```bash
rhc app create <project> <cartridge> --from-code https://github.com/aaossa/flask-openshift.git
```

If you want to use Python 3.5, I recommend [this custom cartridge](https://github.com/Grief/openshift-cartridge-python-3.5). You can create your app with this command

```bash
rhc app create <project> https://raw.githubusercontent.com/Grief/openshift-cartridge-python-3.5/master/metadata/manifest.yml diy-0.1 --from-code https://github.com/aaossa/flask-openshift.git
```

If you're interested in Telegram bots, you can use [my template](https://github.com/aaossa/Telegram-bot-in-OpenShift) to create your own just using 3 console commands, 3 Telegram messages and 1 url.

# License

Code licensed under [GNU General Public License v3](http://opensource.org/licenses/GPL-3.0).
