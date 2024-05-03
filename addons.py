del install_addons
del install_addonsbeta


# Standard I/O for addons; use instead of input() and print()
def addon_print(string=""):
  print(string)

def addon_input(prompt=""):
  return input(prompt)

def addon_chatbot(prompt):
  chatbot(prompt)

def complete_install():
  print("Addons installed successfully!")

def newinstall_addons():
  print("Addons already installed!")

new_responses = {"Install addons":newinstall_addons, "Install addons beta":newinstall_addons}

responses = dict(responses, **new_responses)

complete_install()
