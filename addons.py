def install_addons():
  print("Addons already installed!")

new_responses = {"Install addons":install_addons, "Install addons beta":install_addons}

responses = dict(responses, **new_responses)
