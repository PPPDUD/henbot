del install_addons
del install_addonsbeta


# Standard I/O for addons; use instead of input() and print()
def addon_print(string=""):
  print(string)

def addon_input(prompt=""):
  return input(prompt)

def addon_chatbot(prompt):
  chatbot(prompt)

# User-generated functions

def complete_install():
  addon_print("Addons installed successfully!")

def newinstall_addons():
  addon_print("Addons already installed!")

new_responses = {"Install addons":newinstall_addons, "Install addons beta":newinstall_addons}

responses = dict(responses, **new_responses)

complete_install()
