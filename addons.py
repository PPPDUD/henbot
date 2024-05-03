del install_addons
del install_addonsbeta


def complete_install():
  print("Addons installed successfully!")

def newinstall_addons():
  print("Addons already installed!")

new_responses = {"Install addons":newinstall_addons, "Install addons beta":newinstall_addons}

responses = dict(responses, **new_responses)

complete_install()
